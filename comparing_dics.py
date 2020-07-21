#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  comparing_dics.py
#  
#  




def dict_compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	shared_keys = d1_keys.intersection(d2_keys)
	added = d1_keys - d2_keys
	removed = d2_keys - d1_keys
	modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
	same = set(o for o in shared_keys if d1[o] == d2[o])
	return added, removed, modified, same

x = {2:1, 3:3, 5:1, 7:1}
y = {2:2, 3:2, 5:2, 11:1}
added, removed, modified, same = dict_compare(x, y)
print(added, removed, modified, same)
