# -*- coding: utf-8 -*-

import webapp2
import logging

logging.getLogger().setLevel(logging.DEBUG)
application = webapp2.WSGIApplication([
  webapp2.Route(r'/api', 'api.MailerAPI:send', methods=['POST']),
  webapp2.Route(r'/api/send', 'api.TaskQueueHandler:post')
], debug=True)