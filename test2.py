#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:21:54 2020

@author: emilyspencer
"""


# %%

import boto3 

# %% 

data = 'hello'
print(data)

s3 = boto3.resource('s3')
object = s3.Object('webscrape-output-emily', 'data')
object.put(Body=data)
# %%

