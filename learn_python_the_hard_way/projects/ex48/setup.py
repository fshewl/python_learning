try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'exercise 48',
    'author': 'Frank He',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'fshewl@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'pacakges': ['ex48'],
    'scripts': [],
    'name' : 'projectname'
}

setup(**config)
