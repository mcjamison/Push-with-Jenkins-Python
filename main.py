import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class ByePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Goodbye, Cruel World!')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bye', ByePage),
], debug=True)
