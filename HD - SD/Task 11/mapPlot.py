#!/usr/bin/env python
# LatitudePlot.py
# Created 30 July 2013
# Created by snowdonjames@googlemail.com

import os, time, math
from datetime import datetime
from time import mktime
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw


def get_kml_files():
    """Locates and reads local .kml files, returns a list of kml dictionary data"""
    kml_data = []
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            sp = filename.split('.')
            if sp[len(sp)-1] == "kml":  # locate kml files
                print("Reading kml file " + filename)
                kml_data.append(read_kml_file(dirname, filename))
    return kml_data


def read_kml_file(dirname, filename):
    """Parses a single kml file, returns a dict of format {time: [lat, long]}"""
    kml_data = {}
    kmltime = datetime.time
    latlist = []
    longlist = []
    timelist = []
    cnt = 0
    f = open(filename)
    line = f.readline()
    while line:
        if 'when' in line:
            timelist.append(time.strptime(ET.fromstring(line)[0].text, "%Y-%m-%dT%H:%M:%SZ"))
        if 'coordinates' in line:
            latlist.append(float(ET.fromstring(line)[0].text.split(',')[0]))
            longlist.append(float(ET.fromstring(line)[0].text.split(',')[1]))
            cnt += 1
            if cnt % 5000 == 0:
                print("Parsing " + filename + ": points found: " + str(cnt))
        line = f.readline()
    f.close()
    return [latlist, longlist, timelist]


def draw_map_data(kml_data, input_image, output_image, itop, ibottom, ileft, iright, xnudge, ynudge):
    """Draws kml line data on top of the specified image"""
    im = Image.open(input_image)
    draw = ImageDraw.Draw(im)
    cnt = 0
    for KmlD in kml_data:
        for d in range(len(KmlD[0])-1):
            # Get points x and y coordinates and draw line
            x1 = (long_to_x(KmlD[0][d], ileft, iright, im.size[0])) + xnudge
            y1 = (lat_to_y(KmlD[1][d], itop, ibottom, im.size[1])) + ynudge
            x2 = (long_to_x(KmlD[0][d+1], ileft, iright, im.size[0])) + xnudge
            y2 = (lat_to_y(KmlD[1][d+1], itop, ibottom, im.size[1])) + ynudge
            if euclid_distance(x1, y1, x2, y2) < 10000:
                # setting this around 80 works okay. Attempts to remove some noise
                draw.line((x1, y1, x2, y2), fill=10)
            cnt += 1
            if cnt % 10000 == 0:
                print("Drawing point number " + str(cnt))
    im.save(output_image)


def long_to_x(input_long, left_long, right_long, im_width):
    """Converts a longitude value in to an x coordinate"""
    return scaling_func(input_long + 360, left_long + 360, right_long + 360, im_width)


def lat_to_y(input_lat, top_lat, bottom_lat, im_height):
    """Converts a latitude value in to a y coordinate"""
    return scaling_func(input_lat + 360, top_lat + 360, bottom_lat + 360, im_height)


def euclid_distance(x1, y1, x2, y2):
    """Calculates the euclidean distance between two points"""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def scaling_func(inputv, minv, maxv, size):
    """Helps convert latitudes and longitudes to x and y"""
    if (float(maxv) - float(minv)) == 0:
        return 0
    return ((float(inputv) - float(minv)) / (float(maxv) - float(minv))) * float(size)


def parse_image_file():
    """Reads SatelliteImageData.csv containing:
<File name of image to draw data on>,
<image top latitude>,
<image bottom latitude>,
<image left longitude>,
<image right longitude>,
(optional) <x value nudge>,
(optional) <y value nudge>"""
    with open('image_data.csv', 'r') as f:
        read_data = f.read().split(',')
    while 5 <= len(read_data) < 7:
        read_data.append(0)
    return_data = [0] * 7
    return_data[0] = read_data[0]
    for i in range(1, 7):
        return_data[i] = float(read_data[i])
    return return_data


if __name__ == "__main__":
    image_data = parse_image_file()
    draw_map_data(get_kml_files(), image_data[0], "Location History.png", image_data[1], image_data[2], image_data[
        3], image_data[4], image_data[5], image_data[6])
