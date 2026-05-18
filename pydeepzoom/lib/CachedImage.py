import pudb
import requests
from pyramid.httpexceptions import exception_response
import os
import time
from PIL import Image
from tempfile import NamedTemporaryFile 

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')


# from https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un

class CachedImage():
	def __init__(self, imageurl):
		self.imageurl = imageurl
		self.cachedir = config.get('tiles_cache', 'dir', fallback = './tilescache')
		self.tempdir = config.get('tiles_cache', 'tempdir', fallback = './temp')
		
		self.known_formats = [fm.strip() for fm in config.get('images', 'known_formats').split(',')]
		
		self.sslverify = config.getboolean('ssl_requests', 'sslverify')
		self.user_agent = config.get('request_headers', 'user-agent')
		self.request_headers = {'User-Agent': self.user_agent}


	def createTempFile(self):
		
		self.cachedfile = NamedTemporaryFile(dir=self.tempdir, delete=True)
		self.filepath = self.cachedfile.name
		self.readFileFormat()
		self.fetchImageFromURL()
		self.readImage()
		self.setImageInfo()
		#self.image.close()
		return self.filepath

	
	def fetchImageFromURL(self):
		r = requests.get(self.imageurl, allow_redirects=True, verify=self.sslverify, headers=self.request_headers, timeout = 60)
		if r.status_code == 200:
			self.cachedfile.write(r.content)
			return
		raise exception_response(r.status_code, detail=r.reason)
	
	def readFileFormat(self):
		h = requests.head(self.imageurl, allow_redirects=True, verify=self.sslverify, headers=self.request_headers, timeout = 10)
		header = h.headers
		contenttype = header.get('content-type')
		if h.status_code == 200:
			for fileformat in self.known_formats:
				if fileformat in contenttype.lower():
					self.fileformat = fileformat
					return
			raise exception_response(400, detail='file format {0} not supported'.format(contenttype))
		raise exception_response(h.status_code, detail=h.reason)
	
	def readImage(self):
		self.image = Image.open(self.cachedfile.name)
	
	def setImageInfo(self):
		self.height = self.image.height
		self.width = self.image.width
		#self.palette = image.palette
		
	
	def getFileFormat(self):
		return self.fileformat
	
	
	def getFilePath(self):
		return self.filepath


	def closeTempFile(self):
		self.cachedfile.close()



