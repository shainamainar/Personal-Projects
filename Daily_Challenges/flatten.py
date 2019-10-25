# Shaina Mainar 2019.
# Python3
# source: https://www.geeksforgeeks.org/python-convert-nested-dictionary-into-flattened-dictionary/
# Write a function to flatten a nested dictionary. Namespace the keys with a period.

import collections

def flatten(d, parent_key = '', sep='.'):
	items = []
	for k, v in d.items():
		new_key = parent_key + sep + k if parent_key else k
		try:
			items.extend(flatten(v, new_key, sep=sep).items())
		except:
		    items.append((new_key, v))
	return dict(items)

def main():
	d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        	   }
           }
        }
	print(flatten(d))

main()