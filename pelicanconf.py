#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Wladislaw Merezhko"
SITENAME = u"Infinity's space!"
SITEURL = 'http://infinitylx.org'
PDF_GENERATOR = False  # FIXME: fix links workaround in rst2pdf
# PDF_STYLE = 'test_greek'  # Name of style wich rst2pdf will use
# PDF_STYLE_PATH = '/home/infinitylx/tmp/infinitylx-s-space/'
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
TIMEZONE = 'Europe/Kiev'

PLUGINS = [ 'pelican.plugins.sitemap', 'pelican.plugins.gzip_cache' ]

DEFAULT_LANG = 'en'

ARTICLE_DIR = 'blog'
DEFAULT_METADATA = (('yeah', 'it is'),)  # ???
DIPLAY_PAGES_ON_MENU = True
THEME = "theme"
# Blogroll
# for now no links... my be later add some usefull links
# LINKS = (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#           ('Python.org', 'http://python.org'),
#           ('Jinja2', 'http://jinja.pocoo.org'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('FB', '#'),
#           ('Twit me', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["pictures", "images"]
DEFAULT_CATEGORY = 'blog'
TYPOGRIFY = True
RELATIVE_URLS = True  # False - only for prod mode
TWITTER_USERNAME = "infinitylX"

GOOGLE_ANALYTICS = "UA-34537389-1"
YANDEX_METRYKA = "16922653"

GITHUB_URL = 'https://github.com/infinitylx'
GITHUB_POSITION = 'right'

DISQUS_SITENAME = "infinitylxsspace"

SHORT_MAIL = 'infinitylX@shortmail.com'

SITEMAP = {
    'format': 'xml', 
    'priorities': {'articles': 0.8, 'pages': 0.6, 'indexes': 1}, 
    'changefreqs': {'articles': 'monthly', 'pages': 'monthly', 'indexes': 'weekly'}
}
