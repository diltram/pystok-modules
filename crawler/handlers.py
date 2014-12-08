import urllib2
import webapp2
from google.appengine.api import taskqueue
from model import Site
from BeautifulSoup import BeautifulSoup


class CrawlHandler(webapp2.RequestHandler):

    def post(self):
        url = self.request.POST.get('url')

        try:
            result = urllib2.urlopen(url)
            content = result.read()

            site = Site()
            site.url = url
            site.count = self.__count_imgs(content)
            site.put()
            self.__grab_urls(content)
        except:
            pass

    @staticmethod
    def __count_imgs(result):
        return result.count('<img')

    @staticmethod
    def __grab_urls(result):
        soup = BeautifulSoup(result)
        for tag in soup.findAll('a', href=True):
            # if not Site.query().filter(Site.url == tag['href']).count():
            taskqueue.add(url='/crawl', params={'url': tag['href']})
