# -*- coding: utf-8 -*-
# @File  : mydodule.py
# @Author: Yikun Gong
# @Date  : 2019/8/3
# python3.7 & tensorflow 1.13.1 & pytorch1.0.1 & keras2.2.4


class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)


p = Person('gongyk')
p.sayHi()
