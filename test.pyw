import schedule
import threading
import time
import urllib.request
import os
import imageLinks, imageLinkUpdater
import ctypes


# c = 0
# for url in open('E:\\Wallpaper\\Links.txt').readlines():
#     url = url.strip()
#     t = threading.Thread(target=urllib.request.urlretrieve(url, 'E:\\Wallpaper\\Images\\'+str(c)+'.jpg'))
#     t.start()
#     c +=


def imgDown(link_arrs):
    c = 0
    if not os.path.exists('E:\\Wallpaper\\Images\\'):
        os.mkdir('E:\\Wallpaper\\Images\\')
    for url in link_arrs:
        url = url.strip()
        t = threading.Thread(target=urllib.request.urlretrieve(url, 'E:\\Wallpaper\\Images\\' + str(c) + '.jpg'))
        t.start()
        c += 1


def func():
    with open('E:\\Wallpaper\\Settings.txt') as f:
        count = int(f.readline())
        f.close()

        try:
            link_arr = open("E:\\Wallpaper\\Links.txt").readlines()
        except:
            imageLinks.pinterest()
            imageLinks.bing()
            link_arr = open("E:\\Wallpaper\\Links.txt").readlines()
        t_links = len(link_arr) - 1
        if count <= t_links - 5:
            link_arr = link_arr[count:count + 5]
            count += 5
            with open('E:\\Wallpaper\\Settings.txt', 'w') as f:
                f.write(str(count))
                f.close()
            imgDown(link_arr)


        else:
            link_arr = link_arr[count:]
            count = 0
            with open('E:\\Wallpaper\\Settings.txt', 'w') as f:
                f.write(str(count))
                f.close()
            imgDown(link_arr)


def imgDownload():
    if os.path.isfile('E:\\Wallpaper\\Settings.txt'):
        func()

    else:
        with open('E:\\Wallpaper\\Settings.txt', 'w') as f:
            f.write('0')
            f.close()
            func()


min = 1

i = 0


def setWallPaper():
    global i
    stri = "E:\\Wallpaper\\Images\\" + str(i) + ".jpg"
    print('setWallpaper')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, stri, 0)
    if i == 4:
        i = 0
    else:
        i += 1


c = threading.Thread(target=imageLinkUpdater.calligFunc)
c.start()
schedule.every(min).minutes.do(setWallPaper)
schedule.every(min * 5).minutes.do(imgDownload)
while 1:
    schedule.run_pending()
    time.sleep(1)
