#!/usr/bin/env python3

import string

with open("message.txt") as filp:
	contents = filp.read()[29:]

print(contents)
print("---------")

up_key = 'EKSZJTCMXOQUDYLFABGPHNRVIW'
low_key = up_key.lower()

up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase

for char in contents:
	if char.isupper():
		# uppercase letters
		print(up_letters[up_key.index(char)],end="")
	elif char.islower():
		# lowercase letters
		print(low_letters[low_key.index(char)],end="")
	else:
		print(char,end="")