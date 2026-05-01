import logging.config
logging.config.fileConfig('pydeepzoom/logging.conf')
log = logging.getLogger('pydeepzoom')
errorlog = logging.getLogger('error')

from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import (view_config, view_defaults)
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPSeeOther

import pudb
import json

class helpView():
	def __init__(self, request):
		self.request = request
		pass
	
	
	@view_config(route_name='help', accept='text/html', renderer="templates/help.pt")
	def helpPage(self):
		pagecontent = {
			'pagetitle': 'API for image processing service',
			'applicationurl': self.request.application_url
			
		}
		return pagecontent
