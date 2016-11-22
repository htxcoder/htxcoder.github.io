#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown
import codecs


AUTHOR = u'hxtcoder team <hxtcoder@ggooglegroups.com>'
SITETITLE = u'HTX Coder - OutSource Web Developer, App Developer, System Administrator, DevOps'
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

STATIC_PATHS = ['img', 'CNAME', 'README.md', 'robots.txt', 'sitemap.xml']

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


TECH = [
    'ruby', 'python', 'golang', 'php', 'saltstack', 'bash',
    'css3', 'html5', 'javascript',
    'mongo', 'mysql', 'postgresql', 'redis',
    'android', 'ios', 'nginx', 'apache2', 'docker', 'git', 'jenkins',
    'travis', 'letsencrypt', 'newrelic', 'sentry', 'rabbitmq', 'bootstrap'
]


JINJA_FILTERS = {'markdown': markdown_file_to_html}

PROJECTS = [
    {'name': 'congtacvien', 'url': 'http://congtacvien.com.vn'},
    {'name': 'pyjobs', 'url': 'http://pyjobs.vn/'},
    {'name': 'tab-player', 'url': 'http://tab-player.com/'},
    {'name': 'aztemplates', 'url': 'https://themeforest.net/user/aztemplates'},
    {'name': 'miamor', 'url': 'http://miamor.vn'},
    {'name': 'remember', 'url': 'https://goo.gl/a7E78i'},
    {'name': 'iseller', 'url': 'http://iseller.vn'},
    {'name': 'chuanamkhoa', 'url': 'http://chuanamkhoa.com'},
    {'name': 'shipit', 'url': 'http://shop.shipit.vn'},
    {'name': 'your', 'url': '#contact'},
]

DEVELOPERS = [
    {'name': 'Đặng Tùng Lâm', 'short_name': 'lamdt',
        'title': 'Backend Developer',
        'linkedin': 'https://vn.linkedin.com/in/dangtunglam'},
    {'name': 'Vũ Thế Dũng', 'short_name': 'dungvt',
        'title': 'Frontend Developer',
        'linkedin': 'https://www.linkedin.com/in/vu-the-dung-57b060108'},
    {'name': 'Trần Mạnh Đồng', 'short_name': 'dongtm',
        'title': 'Designer',
        'linkedin': 'https://vn.linkedin.com/in/dong-tran-125652b4'},
    {'name': 'Vũ Đình Cường', 'short_name': 'cuongvd',
        'title': 'Android Developer',
        'linkedin': 'https://vn.linkedin.com/in/cuongvd'},
    {'name': 'Nguyễn Việt Hưng', 'short_name': 'hungnv',
        'title': 'SysAdmin/DevOps',
        'linkedin': 'https://www.linkedin.com/in/hvnsweeting'},
    {'name': 'Đặng Nam Hùng', 'short_name': 'hungdn',
        'title': 'PHP/Prestashop Developer',
        'linkedin': 'https://vn.linkedin.com/in/hungdn19'},
    {'name': 'Nguyễn Văn Hiệp', 'short_name': 'hiepnv',
        'title': 'Python/Golang/C Dev',
        'linkedin': 'https://www.linkedin.com/in/hiepnv90'},
    {'name': 'Bùi Đức Chung', 'short_name': 'chungbd',
        'title': 'iOS Developer',
        'linkedin': 'https://www.linkedin.com/in/bui-chung-8666aba3'},
    {'name': 'Lưu Tuấn Hải', 'short_name': 'hailt',
        'title': 'Ruby/Scala/Python Developer',
        'linkedin': 'https://www.linkedin.com/in/hải-lưu-tuấn-0b7909105'},
]
