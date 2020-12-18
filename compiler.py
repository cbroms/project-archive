import os
import glob

from PIL import Image, ImageSequence
from config import * 

Image.MAX_IMAGE_PIXELS = 933120000


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
    size_mid =  400, 400
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
            im.convert('RGB').save(filename.split('.')[0] + "-mid.jpg", "JPEG", quality=75, optimize=True, progressive=True)
            im=Image.open(filename)
            im.thumbnail(size_small)
            print("Saved Thumbnail Small: " + filename.split('.')[0] + "-thumb.jpg")
            im.convert('RGB').save(filename.split('.')[0] + "-thumb.jpg", "JPEG", quality=90, optimize=True, progressive=True)
            


    gifs = glob.glob(PATH_TO_STATIC_FILES + 'images/**/*.gif')

    for index, filename in enumerate(gifs):

        if "-mid" not in filename:
            # make sure the thumbnails haven't already been generated 
            im = Image.open(filename)
            frames = ImageSequence.Iterator(im)

            # save small preview image
            sm = frames[0]
            sm.thumbnail(size_mid)
            print("Saved Gif Thumbnail Mid: " + filename.split('.')[0] + "-gif-mid.jpg")
            sm.convert('RGB').save(filename.split('.')[0] + "-gif-mid.jpg", "JPEG",  quality=75, optimize=True, progressive=True)

                # # save small gif
                # frames = create_gif_thumbnails(frames, size_mid)
                # om = next(frames)
                # om.info = im.info
                # print("Saved Gif Mid: " + filename.split('.')[0] + "-mid.gif")
                # om.save(filename.split('.')[0] + "-mid.gif", save_all=True, append_images=list(frames))




"""
Generate the thumbnails 
"""
if __name__ == "__main__":

    print("generating thumbnails...")
    create_all_thumbnails()


