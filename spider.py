__author__ = 'Bryce Ogden'

from bs4 import BeautifulSoup as BS
import requests


class Spider(object):
    def _init_(self):
        """
        Initilize Spider object
        """

    def crawl(self, url, processName="Crawler"):
        print "%s - crawling: %s" % (processName, url)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'}
        info = "%s - " % processName

        try:
            r = requests.get(url, timeout=(8), headers=headers)

            if r.status_code == 200:
                soup = BS(r.text)
                info += "crawled %s" % url
                # do something with the page

            else:
                info += "%s - %s ERROR" % (url, r.status_code)

        except Exception as e:
            info += "ERROR crawling: %s" % e

        finally:
            print info

            