#!/usr/bin/python

import os
import pickle
import re
import sys

from stemmer import parseOutText

ff = open("resume_text.txt", "r")

breakout_list = parseOutText(ff)
for value in breakout_list:
    print(value)
