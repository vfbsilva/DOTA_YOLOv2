#!/usr/bin/python
from PIL import Image
import sys
import re


def compare(title, image, colour_tuple):
    image.show(title=title)
    image = Image.new("RGB", (200, 200,), colour_tuple)
    return image


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    #compare("Most Common", image, most_frequent_pixel[1])

    return most_frequent_pixel

image_in=Image.open(sys.argv[1])
with open(sys.argv[2],'r') as report:
    for line in report:
        print(line)
        points=re.findall("[0-9]+",line)
	name=re.search("(?<=Type: )[a-zA-Z-]+",line)
        if points is not None:
	    print(name.group(0))
            print(points)
            box=[int(x) for x in points]
            area = image_in.crop(box)
	    print(str((box[3]-box[1])*(box[2]-box[0])))
	    print(most_frequent_colour(area))
            area.save(sys.argv[3]+"_"+str(name.group(0))+"_"+points[0]+"_"+points[1]+"_"+points[2]+"_"+points[3]+".png", 'png')
            area.close()
image_in.close()
