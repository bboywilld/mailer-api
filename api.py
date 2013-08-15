# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import taskqueue
from google.appengine.api import mail

class TaskQueueHandler(webapp2.RequestHandler):
  """ Вызывается тасками. Шлет email на указанный адрес.
  """
  def post(self):
    email = self.request.get('email')
    subject = self.request.get('subject')
    body = self.request.get('body')
    html = self.request.get('html')
    sender = 'Social-Leads.ru <noreply@social-leads.ru>'
    message = mail.EmailMessage(sender=sender, subject=subject)
    message.to = '<%s>' % email
    message.body = body
    message.html = html
    message.send()


class MailerAPI(webapp2.RequestHandler):
 """ Генерирует отдельный таск для каждого мыла.
 """
 def send(self):
    emails = self.request.get('emails')
    subject = self.request.get('subject')
    body = self.request.get('body')
    html = self.request.get('html')
    emailsArray = emails.split(',')
    for email in emailsArray:
      # таск будет пытаться выполниться пока не получит ответ 200 - ОК
      # очередь должна существовать в файле queue.yaml
      taskqueue.add(queue_name='emails', url='/api/send', params={
        'email': email,
        'subject': subject,
        'body': body,
        'html': html})
