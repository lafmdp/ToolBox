'''
  A tool for recording RL data.
  Usage:
    pm = PlotManager(["return", "loss"])
    pm.set_interval(10)

    while Training:
        pm.add_data("return", return)
        pm.add_data("loss", loss)

  @python version : 3.6.8
  @author : pangjc
  @time : 2019/8/26
'''

import os
from matplotlib import pyplot as plt
from multiprocessing import Process

class PlotManager():

    def __init__(self, attr_list):

        self.attr_list = attr_list
        self.plot_interval = 1

        self.database = {}

        if not os.path.exists('./figure'):
            os.mkdir('./figure')

        self.process = self.start_plot()

    def init_data(self):

        for v in self.attr_list:
            self.database[v] = []

    def start_plot(self):
        p = Process(target=self.plt_worker)
        p.start()

        return p

    def stop_plt(self):
        self.process.close()

    def add_data(self, key, value):

        self.database[key].append(value)

    def plt_worker(self):

        while True:
            figure_index = 1
            for key in self.attr_list:

                data_list = self.database[key]

                if len(data_list) <= 0:
                    continue

                plt.figure(figure_index)
                figure_index += 1

                x = range(len(data_list))
                x = [a * self.plot_interval for a in x]
                plt.plot(x, data_list, label=key, marker='.', linestyle='-')

                plt.xlabel('Episodes')
                plt.ylabel(key)
                plt.title('%s while training'%key)

                plt.legend()
                plt.show()

                plt.savefig('./figure/%s.jpg'%key)

    def set_interval(self, value):
        self.plot_interval = value
