#!/usr/bin/python
from nltk.stem.snowball import SnowballStemmer
import string
import re
import sys
from nltk.corpus import stopwords

def parseOutText(f):

    f.seek(0)
    all_text = f.read()
    content = all_text
    #content = list(filter(None, content))
    #print(content)
    #sorted(content)
    words = ''
    breakout_list = []
    if len(content) > 1:
        text_string = content.translate(string.maketrans("", ""), string.punctuation)
        words = text_string.lower()
        sw = stopwords.words("english")
        regValue = re.sub(r"[^a-zA-Z]+", ' ',words)
        breakout_list = regValue.split(" ")
        breakout_list = list(filter(None, breakout_list))

        #print(breakout_list)
        return breakout_list



"""def main():
    ff = open("resume_text.txt", "r")
    text = parseOutText(ff)
    #print text

if __name__ == '__main__':
    main()

"""
