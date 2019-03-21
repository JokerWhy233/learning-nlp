# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:30:50 2019
2.2.1
@author: Administrator
"""

import re
text_string = '不过在开始前我需要强调下，下面的步骤你要亲自跟着敲一遍并在自己的电脑上实践。虽然下面你会遇到很多命令，给了谁都记不住的。但是别怕，也别中途放弃，因为你没必要记住命令，因为当你在后面学习数据分析用的多了，自然就记住了。记不住也没关系，学会在哪查找就可以了。你只需要跟着上面步骤操作下，并理解了每一步是干什么的就可以了。后面遇到要做的事情，忘记了回头查这个文档就可以了。'
regex = '你'
p_string = text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)
    else:
            print('not match')
print('=============')
print(p_string)
##  if re.search(regex,line) is not None:  可以找到 目标中 含有regex的list


