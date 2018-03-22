#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Theme
THEME = "themes/MinimalXY"
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = datetime.now().year

# Author
AUTHOR = 'David Roeca'

SITENAME = "David's Personal Site"
SITEURL = ''
PATH = 'content'

TIMEZONE = 'EST'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/davidroeca'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
