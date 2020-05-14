import markdown
import frontmatter
import codecs
import os, sys, re
import shutil, errno
import glob
import http.server
import socketserver

from PIL import Image, ImageSequence
from config import * 

Image.MAX_IMAGE_PIXELS = 933120000

# all the output paths, to use for links on the index page
new_paths = []

footer_html = "<div><em>This is an archived page. Find recent projects <a href='https://christianbroms.com'>on my website</a></em></div>"
header_html = "<h1>All Projects</h1><p>All of the projects that I've worked on, from small to large. Photography, video, physical fabrication, installations, websites, graphic design, renderings, browser extensions, generative text, experimental media, and plenty of others.</p>"

"""
Get the file names in the source directory 
"""
def get_source_file_paths():
    files = [f for f in os.listdir(PATH_TO_SOURCE_FILES) if os.path.isfile(os.path.join(PATH_TO_SOURCE_FILES, f))]
    return filter(lambda x: ".md" in x, files)

"""
Convert a markdown file to html, given the name of the file. 
Add a link around every img tag to the src of the image. 
"""
def decode_source_file(rel_path):
    input_file = frontmatter.load(PATH_TO_SOURCE_FILES + rel_path)
    text = input_file.content
    html = markdown.markdown(text)
    imgs = re.findall(r'<img([\w\W]+?)>', html)
    for img in imgs:
        img_big = img
        img_small = img.split(".")[0] + "-thumb.jpg\""
       
        src_small = re.search(r'"\/([\w\W]+?)\"', img_small).group(0).replace("\"", "")
        src_big = re.search(r'"\/([\w\W]+?)\"', img_big).group(0)

        img_small = "<img style='background-image: url({})' data-src={} {}>".format(src_small, src_big, img_small)
        a_tag = "<a href={}>{}</a>".format(src_big, img_small)
        html = html.replace("<img{}>".format(img), a_tag)
    return (html, input_file)

"""
Create the output file given a path and the compiled html
"""
def create_final_file(rel_path, html):
    if (DISPLAY_FILE_EXTENSIONS):
        new_path = PATH_TO_OUTPUT_FILES + rel_path.replace('.md', '.html')
        link_path = new_path
        new_path = PATH_TO_BUILD + new_path
    else:
        clean_path = PATH_TO_OUTPUT_FILES + rel_path.replace('.md', '')
        link_path = clean_path
        clean_path = PATH_TO_BUILD + clean_path
        if not os.path.exists(clean_path):
            os.makedirs(clean_path)
        new_path = clean_path + "/index.html"

    output_file = codecs.open(new_path, "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
    )
    output_file.write(html)
    print("Compiled file '{}'".format(PATH_TO_SOURCE_FILES + rel_path))
    return link_path

"""
Crate the meta html tags for the page 
"""
def create_page_meta(meta):
    try:
        desc = meta["description"]
    except:
        desc = SITE_DESCRIPTION
    desc_html = "<meta name='desription' content='{}'>".format(desc)
    return desc_html

"""
Add the source html to the template
"""
def add_source_to_template(html, meta):
    with open(PATH_TO_TEMPLATE, 'r') as template:
        text = template.read()
    date = meta["date"].strftime("%b %d, %Y")
    dateHtml = "<div id='date'>" + date + "</div>"
    html = "<div id='content'>" + dateHtml + html + footer_html + "</div>"
    return text.replace("[[ content ]]", html).replace("[[ title ]]", meta["title"] + " - " + SITE_NAME).replace("[[ meta ]]", create_page_meta(meta))

"""
Convert all markdown files in the source directory to html
"""
def decode_all_source_files():
    # get the paths to the source files
    rel_paths = get_source_file_paths()

    # decode each file and put generated html in template, then save it
    for rel_path in rel_paths:
        html, meta = decode_source_file(rel_path)
        html = add_source_to_template(html, meta)
        link_path = create_final_file(rel_path, html)
        new_paths.append((link_path, meta))


"""
Create an index with a list of all files
"""
def create_index():
    # sort the pages by date
    new_paths.sort(key = lambda x: x[1]["date"], reverse=True)
    # generate the html link for each of the pages
    html_links = ""
    for link_path, meta in new_paths:
        formattedTime = '\'' + str(meta["date"]) + '\''
        date = meta["date"].strftime("%b %d, %Y")

        img = ""
        if "image" in meta:
            img = meta["image"]
            if ".gif" not in img:
                # get the mid size thumbnail 
                img = img.split('.')[0] + "-mid.jpg"
            else:
                img = img.split('.')[0] + "-gif-mid.jpg"

        if img != "":
            html_link = '<div class="list-link"><a onmouseenter="showImg({}, this)" onmouseout="hideImg({}, this)" href="{}" >{} <sup>{}</sup></a></div><img class="feature-img" id="{}" data-src="{}">'.format(formattedTime, formattedTime, link_path, date + " — " + meta["title"], '(' + meta["category"].lower() + ')', str(meta["date"]), img)
        else:
            html_link = '<div class="list-link"><a href="{}" >{} <sup>{}</sup></a></div>'.format( link_path, date + " — " + meta["title"], '(' + meta["category"].lower() + ')')
        html_links += html_link
    html_links = "<div id='content'>" + header_html + html_links + "</div>"

    # insert the generated html into the tempate
    with open(PATH_TO_TEMPLATE, 'r') as template:
        html = template.read()
    html = html.replace("[[ content ]]", html_links).replace("[[ title ]]", SITE_NAME).replace("[[ meta ]]", create_page_meta({}))

    # save the new html as the index 
    output_file = codecs.open(PATH_TO_BUILD + "index.html", "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
    )
    output_file.write(html)
    print("Created index file '{}'".format(PATH_TO_BUILD + "index.html"))

def create_gif_thumbnails(frames, size_gif):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size_gif, Image.ANTIALIAS)
        yield thumbnail

def create_all_thumbnails():

    # make thumbnails 
    image_list = []
    images = glob.glob(PATH_TO_STATIC_FILES + 'images/**/*.jpg')
    images.extend(glob.glob(PATH_TO_STATIC_FILES + 'images/**/*.jpeg'))
    images.extend(glob.glob(PATH_TO_STATIC_FILES + 'images/**/*.png'))

    size_small = 128, 128
    size_mid =  350, 350
    size_gif = 320, 240

    for index, filename in enumerate(images):
        if "-thumb" in filename or "-mid" in filename:
            os.remove(filename)

        if "-thumb" not in filename and "-mid" not in filename:
            # make sure the thumbnails haven't already been generated 
          #  if (index < len(images) - 1 and "-thumb" not in images[index + 1] and "-mid" not in images[index + 1]) or (index == len(images) - 1):
            im=Image.open(filename)
            im.thumbnail(size_mid)
            print("Saved Thumbnail Mid: " + filename.split('.')[0] + "-mid.jpg")
            im.convert('RGB').save(filename.split('.')[0] + "-mid.jpg", "JPEG", quality=30, optimize=True, progressive=True)
            im=Image.open(filename)
            im.thumbnail(size_small)
            print("Saved Thumbnail Small: " + filename.split('.')[0] + "-thumb.jpg")
            im.convert('RGB').save(filename.split('.')[0] + "-thumb.jpg", "JPEG", quality=90, optimize=True, progressive=True)
            


    gifs = glob.glob(PATH_TO_STATIC_FILES + 'images/**/*.gif')

    for index, filename in enumerate(gifs):

        if "-mid" not in filename:
            # make sure the thumbnails haven't already been generated 
            if (index < len(images) - 1 and "-mid" not in images[index + 1]) or (index == len(images) - 1):
                im = Image.open(filename)
                frames = ImageSequence.Iterator(im)

                # save small preview image
                sm = frames[0]
                sm.thumbnail(size_mid)
                print("Saved Gif Thumbnail Mid: " + filename.split('.')[0] + "-gif-mid.jpg")
                sm.convert('RGB').save(filename.split('.')[0] + "-gif-mid.jpg", "JPEG",  quality=30, optimize=True, progressive=True)

                # save small gif
                frames = create_gif_thumbnails(frames, size_mid)
                om = next(frames)
                om.info = im.info
                print("Saved Gif Mid: " + filename.split('.')[0] + "-mid.gif")
                om.save(filename.split('.')[0] + "-mid.gif", save_all=True, append_images=list(frames))


"""
Copy the static files to the build directory 
"""
def copy_static_files():
    dest = PATH_TO_BUILD + PATH_TO_STATIC_FILES
    try:
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        shutil.copytree(PATH_TO_STATIC_FILES, dest)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(PATH_TO_STATIC_FILES, dest)
        else: raise


"""
Prepare the build directory: compile the source files to html, 
create an index file, and copy the static files
"""
if __name__ == "__main__":

    if "compile-pages" in sys.argv:
        print("Compiling files from '{}' to '{}'...".format(PATH_TO_SOURCE_FILES, PATH_TO_BUILD + PATH_TO_OUTPUT_FILES))
        decode_all_source_files()
        create_index()

        if "compile-images" in sys.argv:
            print("Creating image thumbnails")
            create_all_thumbnails()

        print("Copying static files from '{}' to '{}'...".format(PATH_TO_STATIC_FILES, PATH_TO_BUILD + PATH_TO_STATIC_FILES))
        copy_static_files()
        print("Build complete!")

    if "serve" in sys.argv:
        os.chdir(PATH_TO_BUILD)
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", DEV_PORT), Handler)
        print("\n\nServing from '{}' at port {}\n\n".format(PATH_TO_BUILD, DEV_PORT))
        httpd.serve_forever() 


