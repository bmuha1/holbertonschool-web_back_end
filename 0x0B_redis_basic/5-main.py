#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page
url = 'http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com'

print(get_page(url))
print(get_page(url))
