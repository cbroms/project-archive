import markdown
import frontmatter
import codecs
import os
import sys
import shutil, errno

import http.server
import socketserver

from config import * 

# all the output paths, to use for links on the index page
new_paths = []

"""
Get the file names in the source directory 
"""
def get_source_file_paths():
    files = [f for f in os.listdir(PATH_TO_SOURCE_FILES) if os.path.isfile(os.path.join(PATH_TO_SOURCE_FILES, f))]
    return filter(lambda x: ".md" in x, files)

"""
Convert a markdown file to html, given the name of the file
"""
def decode_source_file(rel_path):
    input_file = frontmatter.load(PATH_TO_SOURCE_FILES + rel_path)
    text = input_file.content
    return (markdown.markdown(text), input_file)

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
    print("Compiled file '{}' to '{}'".format(PATH_TO_SOURCE_FILES + rel_path, new_path))
    return link_path

"""
Add the source html to the template
"""
def add_source_to_template(html, meta):
    with open(PATH_TO_TEMPLATE, 'r') as template:
        text = template.read()
    return text.replace("[[ content ]]", html).replace("[[ title ]]", meta["title"] + " - " + SITE_NAME)

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
        html_link = '<div><a href="{}">{}</a></div>'.format(link_path, meta["title"])
        html_links += html_link

    # insert the generated html into the tempate
    with open(PATH_TO_TEMPLATE, 'r') as template:
        html = template.read()
    html = html.replace("[[ content ]]", html_links).replace("[[ title ]]", SITE_NAME)

    # save the new html as the index 
    output_file = codecs.open(PATH_TO_BUILD + "index.html", "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
    )
    output_file.write(html)
    print("Created index file '{}'".format(PATH_TO_BUILD + "index.html"))

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
def compile():
    print("Compiling files from '{}' to '{}'...".format(PATH_TO_SOURCE_FILES, PATH_TO_BUILD + PATH_TO_OUTPUT_FILES))
    decode_all_source_files()
    create_index()
    print("Copying static files from '{}' to '{}'...".format(PATH_TO_STATIC_FILES, PATH_TO_BUILD + PATH_TO_STATIC_FILES))
    copy_static_files()
    print("Build complete!")



if __name__ == "__main__":

    compile()

    for arg in sys.argv:
        if (arg == "serve"):
            os.chdir(PATH_TO_BUILD)
            Handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", DEV_PORT), Handler)
            print("Serving from '{}' at port {}".format(PATH_TO_BUILD, DEV_PORT))
            httpd.serve_forever() 
            
