#!/usr/bin/env python
"""

GIMP Plugin for Export psd layers to distinct images with 
xml map of coordinates

plugin should have execute "permission" on UNIX system
"""


from gimpfu import *
import plistlib 
import os




def process_image(image,dirpath):
    layers = [{'name':layer.name,
               'x':layer.offsets[0],
               'y':layer.offsets[1],
               'width':layer.width,
               'heigh':layer.height} 
              for layer in image.layers]

   

    for layer in image.layers:
        layer_path = "%s%s%s.png" % (dirpath,os.sep,layer.name)
        print layer_path
        pdb.file_png_save_defaults(image,layer,layer_path,layer_path)


    path = "%s%s%s.plist" % (dirpath, os.sep, image.name)
    plistlib.writePlist(layers, path)
    

def plug_fun(*arg):
    process_image(**dict(
            image = arg[0],
            dirpath = arg[2])
                  )

register(
    "export-from-psd",
    "666",
    "help",
    "nero hellier",
    "fuck copyright",
    "1488",
    "<Image>/PSD",
    "*",
    [(PF_DIRNAME, "x_blur", "Folder", "")],#ask for dir
    [],
    plug_fun,
    )

main()
