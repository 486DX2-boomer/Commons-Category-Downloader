# Download all images in a category from Wikimedia Commons

# How it works:
# Accept a Category: page from Wikimedia Commons as command line argument. For example, https://commons.wikimedia.org/wiki/Category:Costumes_of_All_Nations_(1882) or https://commons.wikimedia.org/wiki/Category:Quality_images_of_sculptures_in_Berlin
# Iterate through every element of class="gallerybox"
# Follow the link to the File: page, and then from there, grab the original file and download to cwd

from bs4 import BeautifulSoup
import html5lib
from urllib.request import urlopen, urlretrieve
import os
import sys

category_page = sys.argv[1]
with urlopen(category_page) as f:
    soup = BeautifulSoup(f, features="html5lib")

thumbnails = soup.find_all(class_="gallerybox")
# print(thumbnails)

# Convert the beautifulsoup tags to a list, so I can work with them easier
convert_to_list = []
for i in thumbnails:
    convert_to_list.append(str(i))
thumbnails = convert_to_list

for i in range(len(thumbnails)):
    image_url_start = thumbnails[i].find("File:") # Find where File: starts
    image_url_end = thumbnails[i][image_url_start:].find("\">") + image_url_start # Since it's sliced from a image_url_start, it's indexed off of that, and not zero indexed. So to get the right ending index we have to add the start index value to it
    this_image_page = thumbnails[i][image_url_start:image_url_end]
    # this_image_page is a string that reads File:_______.JPG which we will use to navigate through each thumbnail and get its real source image URL
    with urlopen("https://commons.wikimedia.org/wiki/" + this_image_page) as g:
        soup = BeautifulSoup(g, features="html5lib")
        # We have to find the href that is labelled "Original file" and download that jpg
        this_image = str(soup.find(text="Original file").find_parent().attrs['href'])
        print("Downloading " + this_image)
        filename = this_image.split('/')[-1] # a lot of these URLs have multiple / in them, this splits them apart and then grabs the last one, which will always be the filename
        urlretrieve(this_image, os.getcwd() + "\\" + filename) # This script always downloads to the current working directory






