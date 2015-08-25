try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Gothon Web Game',
    'author': 'Frank He',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'fshewl@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'pacakges': ['gothonweb'],
    'scripts': [],
    'name' : 'gothonweb'
}

setup(**config)
