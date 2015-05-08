#!/usr/bin/python

__author__ = 'Bryce Ogden'

import Queue
import threading

# ref. spider.py
from spider import Spider


exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q, spider):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = str(name)
        self.q = q
        self.spider = spider

    def run(self):
        print "%s starting " % self.name

        process_data(self.name, self.q, self.spider)

        print "%s exiting " % self.name


def process_data(threadName, q, crawlerObj):
    """ Callback for initializing/"run" new thread """
    try:
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                url = q.get()

                queueLock.release()
                print "Processing %s" % threadName

                crawlerObj.crawl(url, threadName)

            else:
                queueLock.release()

    except Exception as e:
        print "Error processing data: %s" % e



def load_queue(data):
    """ Load up queue with links """

    # Force threads to run synchronously
    queueLock.acquire()

    editFlag = 0

    # Iterate through URL array
    for link in urls:
        # toss the URL into the queue
        workQueue.put(link)

    # Release lock since it is no longer required
    queueLock.release()



threadList = ["T-1", "T-2", "T-3", "T-4", "T-5"]
queueLock = threading.Lock()
workQueue = Queue.Queue()
threads = []
threadID = 1

# Create new threads with Spider object
spider = Spider()
for tName in threadList:
    thread = myThread(threadID, tName, workQueue, spider)
    thread.start()
    threads.append(thread)
    threadID += 1


load_queue(records)


# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"
