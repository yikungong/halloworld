# -*- coding: utf-8 -*-
# @File  : exception.py
# @Author: Yikun Gong
# @Date  : 2019/8/4
# python3.7 & tensorflow 1.13.1 & pytorch1.0.1 & keras2.2.4


try:
    text = input('Enter something -->')
except EOFError:
    print("Why did you do an EOF in me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print('You entered {0}'.format(text))

