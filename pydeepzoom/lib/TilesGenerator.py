import pudb
import pyvips
from tempfile import NamedTemporaryFile

from configparser import ConfigParser
config = ConfigParser()
config.read('./pydeepzoom/config.ini')


class TilesGenerator():
	def __init__(self, cachedimage, dzipath):
		self.cachedimage = cachedimage
		self.dzipath = dzipath
		
		self.loadImage()
		self.writeTiles()
		del self.img
	
	def loadImage(self):
		self.img = pyvips.Image.new_from_file(self.cachedimage.getFilePath())
	
	def writeTiles(self):
		uchar_img = self.img.scaleimage().cast('uchar')
		uchar_img.dzsave(self.dzipath)

	def getImageWidth(self):
		return self.img.width

	def getImageHeight(self):
		return self.img.height

