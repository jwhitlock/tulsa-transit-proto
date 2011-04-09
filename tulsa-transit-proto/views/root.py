'''View for the / resource'''

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class View(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates', 'root.html')
        self.response.out.write(template.render(path, locals()))