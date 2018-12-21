# -*- coding:utf-8 -*-

import json
import requests
import re
import time
from lxml import etree
import json
import xlwt

from urllib import parse
a= '1545288555TR_title?__id=qtdpPmmBihsnD5n7GTBk.jpg'



new_url=parse.quote_plus(a)
print(new_url)