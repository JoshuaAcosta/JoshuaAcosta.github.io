#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joshua Acosta'
SITENAME = u"Joshua's Blog"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = "Graduate CS Student"

SITELOGO = '/images/photo.png'

STATIC_PATHS = ['images']

PATH = 'content'

TIMEZONE = 'America/New_York'

THEME = "pelican-themes/Flex"

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/joshuaacosta/'),
          ('github', 'https://github.com/joshuaacosta'),
          ('twitter', 'https://twitter.com/Josh_Acosta'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
