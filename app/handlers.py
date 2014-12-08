import webapp2
from webapp2_extras import jinja2
from google.appengine.api import modules
from google.appengine.api import taskqueue


class MainHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        """Returns a Jinja2 renderer cached in the app registry"""
        return jinja2.get_jinja2(app=self.app)

    def get(self):
        context = {'api_base_url': modules.get_hostname(module='api')}
        content = self.jinja2.render_template('main.html', **context)
        self.response.write(content)


class RunHandler(webapp2.RequestHandler):

    def get(self):
        taskqueue.add(url='/crawl', params={'url': 'http://wp.pl'})
        self.redirect_to('main')
