import webapp2

routes = [
    webapp2.Route(
        r'/get_sites', handler='handlers.SitesHandler', name='sites'),
]

config = {
    'webapp2_extras.jinja2': {'template_path': 'views'}
}

app = webapp2.WSGIApplication(routes=routes, config=config, debug=True)
