from google.appengine.ext import ndb


class Site(ndb.Model):
    url = ndb.StringProperty()
    count = ndb.IntegerProperty()
