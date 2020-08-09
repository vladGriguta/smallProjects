#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:40:05 2020

@author: vladgriguta
"""

import pandas as pd

data = pd.read_excel('DT-229_vlad.xlsx',sheet_name=None)



newData = pd.DataFrame(data['PI firms'],index=None)

newData['matchingCol'] = data['SalesForce List']['Account Name']

