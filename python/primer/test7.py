# -*- coding: UTF-8 -*-

# Filename : test7.py
# author by : www.snzigod.com

# 用户输入摄氏温度

# 接收用户收入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))