#!/usr/bin/python
# -*- coding: utf-8 -*-


import re

newpat='这里是中文内容'.decode("utf8")
news=re.sub(pat,newpat,s)
print news