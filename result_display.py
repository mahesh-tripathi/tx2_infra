# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:32:06 2019

@author: mahesh_tripathi
"""


# init_dir:
text_file = 'output.txt'

# total number of classes:
flc_class = ['2LB','Coarse','3LB','1LB' ]
# flc_class = ['Coarse','1LB' ]

# reading file:
f = open(text_file, 'r')
x = f.readlines()
f.close()

# getting the values:

try:
    i = 0
    while i < len(flc_class):
        j = 1
        while j <= len(x):
            # print(j)
        # for j in range(1,len(x)):
            if x[-j].find(flc_class[i])==0:
                # flc_class.remove(i)
                i += 1
                count = x[-j].split(',')[0].split('=')[-1].strip()
                print(f'{flc_class[i]} : {count}')
                # print(x[-j])

                # print(flc_class[i], ' : ', count)
                # print(flc_class[i])
                # print(count)

                break

            j+=1
except:
    pass