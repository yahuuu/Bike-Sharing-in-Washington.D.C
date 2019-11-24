# coding:utf-8

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

def read(path):
    data = pd.read_csv(path, header=None, skiprows=1, index_col=None, usecols=[2])
    data = data.values.tolist()
    print([float(i[0]) for i in data])
    return [float(i[0]) for i in data]

def plot(y1:list, y2:list):

    x1 = [i for i in range(100)]
    y1 = y1
    x2 = [i for i in range(100)]
    y2 = y2

    # 绘制图形并设置要显示的图例文本

    plt.plot(x1, y1, label='train_acc1')
    plt.plot(x2, y2, label='val_acc1')

    # 绘制图形的x轴和y轴的轴名称
    plt.xlabel('epoch number')
    plt.ylabel('acc1')

    # 绘制图形的标题
    plt.title(u'')

    # 显示图形的图例
    plt.legend()
    # 显示图形

    plt.show()


y1 =read("/home/alex/传到我本地/train_acc1.csv")
y2 =read("/home/alex/传到我本地/val_acc1.csv")
plot(y1, y2)
