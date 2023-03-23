# -*- coding: utf-8 -*-
"""
Hex to character converter
Created on Fri Sep 30 17:23:26 2022

@author: AL-AMIN
"""

import codecs

hexadecimal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
hexs = ''.join(hexadecimal.split(' '))
bin_str = codecs.decode(hexs, 'hex')


print(hex((0xc4115 ^ 0x4cf8)))  #hextroordinary
print(str(bin_str, 'utf-8'))