import webapp2

routes = [
    webapp2.Route(
        r'/crawl', handler='handlers.CrawlHandler', name='crawl'),
]

config = {}

app = webapp2.WSGIApplication(routes=routes, config=config, debug=True)
