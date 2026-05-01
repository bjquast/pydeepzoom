from setuptools import setup
import sys

# check for python version and define the right requirements
if sys.version_info < (3, 0):
	raise Exception ('python version must be >= 3.0')
else:
	pass

requires = [
	'configparser',
	'pyramid',
	'pyramid_chameleon',
	'pyramid_debugtoolbar',
	'waitress',
	'requests',
	'Pillow',
	'pyvips',
	'pudb'
]

setup(name='pydeepzoom',
	author='Börn Quast',
	author_email='b.quast@leibniz-lib.de',
	license='CCBy 4.0',
	packages=['pydeepzoom'],
	install_requires=requires,
	entry_points="""\
	[paste.app_factory]
	main = pydeepzoom:main
	""",
)
