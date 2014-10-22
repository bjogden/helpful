#!/usr/bin/python

import urllib

# file names extensions list
fname = "text-file-example.txt"

# open filename in variable 'f'
with open(fname) as f:
	# read contents of file and save in 'content' variable
    content = f.readlines()

for elements in content:
	# remove '\n' from elements and save as image variable
    image = elements.rstrip()
    # use string formatting to format URL based on element in list
    link = "http://example-url.com/images/%s" % image
    # open element-specific link
    resource = urllib.urlopen(link)
    # open new file to write in binary
    output = open(image, "wb")
    # write image to current working directory
    output.write(resource.read())
    # close new image
    output.close()

# close file
f.close()
