import pudb
import re

from urllib.parse import urlparse

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')

import logging.config
logging.config.fileConfig('pydeepzoom/logging.conf')
log = logging.getLogger('pydeepzoom')
errorlog = logging.getLogger('error')


class DomainCheck():
	def __init__(self, url):
		
		urldict = urlparse(url)
		self.domain = urldict.netloc
		
		self.whitelist = []
		self.blacklist = []
		
		wl = config.get('allowed_domains', 'whitelist', fallback = '')
		bl = config.get('allowed_domains', 'blacklist', fallback = '')
		
		if wl != '':
			self.whitelist = [wl.strip() for wl in config.get('allowed_domains', 'whitelist', fallback = '').split(',')]
		if bl != '':
			self.blacklist = [bl.strip() for bl in config.get('allowed_domains', 'blacklist', fallback = '').split(',')]
		
		log.debug('whitelist {0}'.format(', '.join(self.whitelist)))
		log.debug('blacklist {0}'.format(', '.join(self.blacklist)))
		log.debug('url domain {0}'.format(self.domain))


	def isAllowedDomain(self):
		allowed = True
		if len(self.whitelist) > 0:
			allowed = False
			if self.domain in self.whitelist:
				allowed = True
		if len(self.blacklist) > 0:
			if self.domain in self.blacklist:
				allowed = False
		return allowed








