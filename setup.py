try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ontrack',
      version='1.0',
      py_modules=['cosine_matcher', 'text_cleaners', 'string_searcher'],
      install_requires=['numpy', 'pandas', 'nltk', 'sklearn'],
      scripts=['scripts/download_nltk'])
