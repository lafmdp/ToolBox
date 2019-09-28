'''
  A toolboox to recording return for reinforcement learning.
  @python version : 3.6.8
  @author : pangjc
  @time : 2019/9/27
'''

import os
import numpy as np

class ret_worker():
    def __init__(self, name, gap, save_path='./return/'):
        self.name = name
        self.gap = gap
        self.save_path = save_path

        self.record = {
            'return':[],
            'gap':gap
        }

    def append(self, data):
        self.record['return'].append(data)

    def reset(self):
        self.record = {
            'return': [],
            'gap': self.gap
        }

    def get_record(self):
        return  self.record

    def save(self):
        np.save(os.path.join(self.save_path, self.name,'.npy'), self.record)

    def load(self):
        self.record = np.load(os.path.join(self.save_path, self.name,'.npy'), allow_pickle=True).item()
        self.gap = self.record['gap']

class ret_manager():

    def __init__(self, save_path):
        self.worker_list = {}
        self.save_path = save_path

    def append(self, name, value):
        self.worker_list[name].append(value)

    def add_worker(self, name, gap):
        if name in self.worker_list.keys():
            pass
        else:
            self.worker_list[name] = ret_worker(name, gap, self.save_path)

    def save(self):
        for key in self.worker_list.keys():
            self.worker_list[key].save()

    def load(self, name):
        self.worker_list[name] = ret_worker(name, gap=None)
        self.worker_list[name].load()
