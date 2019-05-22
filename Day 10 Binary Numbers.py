#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary=[]
 
    while n > 0:
        binary.append(n%2)
        n = n//2
    
    current = 0
    longest = 0
    for number in binary:
        if number == 1:
            current += 1
        else:
            longest = max(current,longest)
            current = 0
    
    print(max(current,longest))