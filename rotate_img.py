#!/usr/bin/env python3

import os
from os import listdir
from PIL import Image

folder_dir = "/home/student-01-11267922e70c/images"
new_path = "/opt/icons"
#Get file from directory
for image_file in os.listdir(folder_dir): 
    if image_file.endswith("48dp"):
      #Get name without extension
        new_name = os.path.splitext(image_file)[0]
        im = Image.open(f"/home/student-01-11267922e70c/images/{image_file}")
        new_im = im.rotate(-90).resize((128, 128)).convert('RGB')
        #Save new image in required directory
        new_im.save(f"{new_path}/{new_name}", format="jpeg")
