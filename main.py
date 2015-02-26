from google.appengine.ext.webapp import template
from google.appengine.api import mail,namespace_manager
import os,webapp2
from datetime import date

class Utility():
    @staticmethod
    def email(subject,content):     
		#email
		message = mail.EmailMessage(sender="Website <arman.fatahi@gmail.com>") 
		message.subject = subject
		message.to = "{0} <{1}>".format("Arman Fatahi", "arman.fatahi@gmail.com")
		message.html = content
		message.send() 
class BaseHandler(webapp2.RequestHandler):
    def show_page(self,page,param=None):
        if param:
            path = os.path.join(os.path.dirname(__file__),page + '.html')
            self.response.out.write(template.render(path,param))
        else:
            path = os.path.join(os.path.dirname(__file__),page + '.html')
            self.response.out.write(template.render(path,{}))
    def render(self,page,param):
        path = os.path.join(os.path.dirname(__file__),page + '.html')
        return template.render(path,param)

class MainHandler(BaseHandler):
    def get(self):
		content = self.render("index", {})
		self.response.write(content)

            
app = webapp2.WSGIApplication([
           ('/', MainHandler)
], debug=True)
