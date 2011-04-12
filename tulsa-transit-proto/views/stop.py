'''View for the /stop resource'''

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class View(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates', 'stop.html')
        submission = False
        self.response.out.write(template.render(path, locals()))
        
    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'templates', 'stop.html')
        submission = True
        self.response.out.write(template.render(path, locals()))