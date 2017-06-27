#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joshua Acosta'
COPYRIGHT_NAME = AUTHOR
SITENAME = "Joshua Acosta's Blog"
SITEURL = 'https://joshuaacosta.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = "Graduate CS Student"
TIMEZONE = 'America/New_York'


SITELOGO = '/images/photo.png'
STATIC_PATHS = ['images']
PATH = 'content'
THEME = "pelican-themes/Flex"

DEFAULT_LANG = u'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = 2017


DEFAULT_LANG = u'en'

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),
             ('Categories', '/categories'),
             ('Tags', '/tags'),)

DISPLAY_PAGES_ON_MENU = True

#GOOGLE_ANALYTICS = ''
#GOOGLE_TAG_MANAGER = ''
#DISQUS_SITENAME = ''

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
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
