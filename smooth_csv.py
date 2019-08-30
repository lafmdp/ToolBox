#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  A tool for smooth csv data downloaded from tensorboard.

  It's originally copy from https://blog.csdn.net/charel_chen/article/details/80364841.

  @author: Charel_CHEN, pangjc
  @file: smooth_csv.py
  @time: 2019-08
'''

import pandas as pd
import numpy as np
import os
import glob


def smooth(csv_path, weight=0.9):
    data = pd.read_csv(filepath_or_buffer=csv_path, header=0, names=['Step', 'Value'],
                       dtype={'Step': np.int, 'Value': np.float})
    scalar = data['Value'].values
    last = scalar[0]
    smoothed = []
    for point in scalar:
        smoothed_val = last * weight + (1 - weight) * point
        smoothed.append(smoothed_val)
        last = smoothed_val

    save = pd.DataFrame({'Step': data['Step'].values, 'Value': smoothed})
    save.to_csv(csv_path[:-4]+'_smooth'+'.csv')


if __name__ == '__main__':
    file_name = 'file_name.csv'
    path_list = glob.glob(os.path.join(os.getcwd(), file_name))

    for i in path_list:
        path = i.split('\\')[-1]
        smooth(path)