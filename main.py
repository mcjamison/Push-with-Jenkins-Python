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

# Every hello leads to a goodbye...
class UpDogPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Nothing much, what's up with you?")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bye', ByePage),
    ('/updog', UpDogPage),
], debug=True)
