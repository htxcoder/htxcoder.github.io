#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown
import codecs


AUTHOR = u'hxtcoder team <hxtcoder@ggooglegroups.com>'
SITETITLE = u'HTX Coder - OutSource Developer, System Administrator, DevOps'
SITENAME = 'HTX Coder'
SITEURL = ''
SITEDISCRIPTION = 'IT OutSourcing Service, Web/Mobile App development, \
                  System Administrator, DevOps'

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
# RELATIVE_URLS = True


def markdown_file_to_html(path):
    """Converting markdown file to HTML string.

     :param path:   string    Path to makrdown file.

    """

    input_file = codecs.open(path, mode="r", encoding="utf-8")
    text = input_file.read()
    return markdown.markdown(text)


JINJA_FILTERS = {'markdown': markdown_file_to_html}

PROJECTS = [
    {'name': 'congtacvien', 'url': 'http://congtacvien.com.vn'},
    {'name': 'tab-player', 'url': 'http://tab-player.com/'},
    {'name': 'iseller', 'url': 'http://iseller.vn'},
    {'name': 'zikathemes', 'url': 'https://themeforest.net/user/aztemplates'},
    {'name': 'shipit', 'url': 'http://shipit.vn'},
]

DEVELOPERS = [
    {'name': 'Đặng Tùng Lâm', 'short_name': 'lamdt',
        'title': 'Backend Developer'},
    {'name': 'Vũ Thế Dũng', 'short_name': 'dungvt',
        'title': 'Frontend Developer'},
    {'name': 'Trần Mạnh Đồng', 'short_name': 'dongtm',
        'title': 'Designer'},
    {'name': 'Vũ Đình Cường', 'short_name': 'cuongvd',
        'title': 'Android Developer'},
    {'name': 'Nguyễn Việt Hưng', 'short_name': 'hungnv',
        'title': 'SysAdmin/DevOps'},
    {'name': 'Đặng Nam Hùng', 'short_name': 'hungdn',
        'title': 'PHP/Prestashop Developer'},
]
