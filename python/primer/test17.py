# -*- coding: UTF-8 -*-

# Filename : test17.py
# author by : www.snzigod.com

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()
