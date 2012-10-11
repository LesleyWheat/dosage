# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..util import tagre
from ..scraper import _BasicScraper


class NineteenNinetySeven(_BasicScraper):
    name = '1997'
    latestUrl = 'http://www.1977thecomic.com/'
    imageUrl = 'http://www.1977thecomic.com/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.1977thecomic\.com/comics-1977/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"Previous")
    help = 'Index format: yyyy/mm/dd/strip-name'
