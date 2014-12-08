import webapp2

routes = [
    webapp2.Route(r'/', handler='app.handlers.MainHandler', name='main'),
    webapp2.Route(r'/run', handler='app.handlers.RunHandler', name='run'),
]

config = {
    'webapp2_extras.jinja2': {'template_path': 'app/views'}
}

app = webapp2.WSGIApplication(routes=routes, config=config, debug=True)
