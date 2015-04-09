import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

# Every hello leads to a goodbye...
class ByePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Goodbye, Cruel World!')

class YoPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Yo.')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bye', ByePage),
    ('/yo', YoPage),
], debug=True)
