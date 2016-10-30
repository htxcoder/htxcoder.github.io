#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LamDT <dangtunglam14@gmail.com>'
SITENAME = u'HTX Coder - OutSource Developer, System Administrator, DevOps'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'vi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

THEME = 'themes/htx'

STATIC_PATHS = ['img', 'CNAME', 'README.md']

EXTRA_PATH_METADATA = {
    'img': {'path': 'img'},
    'CNAME': {'path': 'CNAME'}
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
