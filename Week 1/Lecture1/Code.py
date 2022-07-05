# Date: 20-6-22
# Chapter 1: 1.1
#===============================================================================
from urllib.request import urlopen

#python built-in functions
shakespeare = urlopen("http://composingprograms.com/shakespeare.txt")
words       = set(shakespeare.read().decode().split())

# Compound expression
special_words = {w for w in words if len(w)==6 and w[::-1] in words}
