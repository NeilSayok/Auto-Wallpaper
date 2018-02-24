# Imports #
import json
import urllib.request


###############################################################################################
# pinterest                                                                                   #
# Uses pinterest api to get the pinned images from the users board                            #
# https://api.pinterest.com/v3/pidgets/boards/<username>/<board>/pins/                        #
# The api returns a json array                                                                #
# From which only the image url is picked up                                                  #
# The image url is of a small image of something size '273x'                                  #
# By replacing the text '273x' with 'originals' gives the image links of the larger image     #
###############################################################################################


def pinterest():
    try:
        fr = open("E:\\Wallpaper\\Links.txt", 'r')
        alllinks = fr.readlines()
        fr.close()
        fh = open("E:\\Wallpaper\\Links.txt", 'a')
        with urllib.request.urlopen(
                "https://api.pinterest.com/v3/pidgets/boards/sayokdeymajumder1998/wallpapers/pins/") as url:
            data = json.loads(url.read().decode())

        for i in data['data']['pins']:
            stri = i['images']['237x']['url']
            stri = stri.replace('/237x/', "/originals/")
            if not stri + '\n' in alllinks:
                fh.write(stri + '\n')

        fh.close()
    except FileNotFoundError:
        fr = open("E:\\Wallpaper\\Links.txt", 'w')
        fr.close()
        pinterest()


########################################################################################################################


###############################################################################################
# bing                                                                                        #
# Uses bing api to get the bing daily wallpapers from the bing.com                            #
# http://www.bing.com/HPImageArchive.aspx?format=js&n=10&mkt=en-US                            #
# 'format' defines request type (js = json , xml = XML , rss = RSS)                           #
# 'n' defines number of images to be returned(but only returns 8)                             #
# 'mkt' defines the location( It can be ommited too)                                          #
# Here the api returns a json array                                                           #
# From which only the image url is picked up                                                  #
###############################################################################################

def bing():
    try:
        fr = open("E:\\Wallpaper\\Links.txt", 'r')
        alllinks = fr.readlines()
        fr.close()
        fh = open("E:\\Wallpaper\\Links.txt", 'a')
        with urllib.request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&n=10&mkt=en-us") as url:
            data = json.loads(url.read().decode())

        for i in data['images']:
            stri = 'https://www.bing.com' + i['url']
            if not stri + '\n' in alllinks:
                fh.write(stri + '\n')

        fh.close()
    except FileNotFoundError:
        fr = open("E:\\Wallpaper\\Links.txt", 'w')
        fr.close()
        bing()

########################################################################################################################
