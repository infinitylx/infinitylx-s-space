#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Wladislaw Merezhko"
SITENAME = u"Infinity's space!"
SITEURL = 'http://blog.infinitylx.org.ua'
PDF_GENERATOR = False  # FIXME: found why this is doesn work
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
TIMEZONE = 'Europe/Kiev'

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
RELATIVE_URLS = False  # False - only for prod mode
TWITTER_USERNAME = "infinitylX"
GOOGLE_ANALYTICS = "UA-34537389-1"
