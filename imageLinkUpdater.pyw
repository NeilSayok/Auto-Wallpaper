import schedule
import time
import threading


def fCall():
    import imageLinks
    a = threading.Thread(target=imageLinks.pinterest)
    b = threading.Thread(target=imageLinks.bing)

    a.start()
    b.start()


def job():
    t = threading.Thread(target=fCall())
    t.start()


def calligFunc():
    schedule.every(6).hours.do(job)
    schedule.every().day.at("00:30").do(job)
    schedule.every().day.at("06:30").do(job)
    schedule.every().day.at("12:30").do(job)
    schedule.every().day.at("18:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)
fCall()

