from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import views.root
import views.stop

views = [
    ('/', views.root.View),
    ('/stop', views.stop.View),
]

application = webapp.WSGIApplication(views, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()