# -*- coding: utf-8 -*-
# @File  : input_output_13.py
# @Author: Yikun Gong
# @Date  : 2019/8/4
# python3.7 & tensorflow 1.13.1 & pytorch1.0.1 & keras2.2.4


# def reverse(text):
#     return text[::-1]
#
#
# def is_palindrome(text):
#     return text == reverse(text)
#
#
# somthing = input('Enter tet:')
# if (is_palindrome(somthing)):
#     print("yes")
# else:
#     print("no")


import pickle


shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)