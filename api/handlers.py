import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb
from model import Site


class SitesHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        """Returns a Jinja2 renderer cached in the app registry"""
        return jinja2.get_jinja2(app=self.app)

    def get(self):
        sites_data = Site.query().fetch(keys_only=True)
        sites_data = ndb.get_multi(sites_data)
        context = {'data': sites_data}
        content = self.jinja2.render_template('sites.html', **context)
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.write(content)
