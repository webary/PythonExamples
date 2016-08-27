#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

"""
@author webary(http://www.cnblogs.com/webary/)
@date 2016-08-27 20:00
@brief 利用palab包对数据进行绘图
"""

import sys
import math
import random
import numpy as np
import pylab as pl


def get_relative(x, y):
    """返回两个list数据的相关系数r"""
    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)
    xy_pair = zip(x, y)
    sum_xy, sum_x2, sum_y2 = 0, 0, 0
    for x_, y_ in xy_pair:
        sum_xy += (x_ - x_avg) * (y_ - y_avg)
        sum_x2 += (x_ - x_avg) ** 2
        sum_y2 += (y_ - y_avg) ** 2
    r = sum_xy / math.sqrt(sum_x2 * sum_y2 + 0.000001)
    return r


def x_y_feature(x, y):
    """返回两个list的数据进行拟合后的线性回归方程"""
    params = np.polyfit(x, y, 1)
    poly1 = np.poly1d(params)
    return poly1


def draw_pic(x, y, x_label, y_label):
    # type: (list, list, str, str) -> None
    """显示x和y的曲线以及线性拟合曲线"""
    x, y = zip(*sorted(zip(x, y)))  # 根据x的值进行排序,并维持对应的y的顺序
    r = get_relative(x, y)
    poly1 = x_y_feature(x, y)
    pred_y = [poly1(i) for i in x]  # 计算线性拟合后的值序列

    # 通过接收命令行参数设置横轴和纵轴要显示的最大值,示例: py plot.py 5 10
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        pl.xlim(0.0, float(sys.argv[1]))  # set x axis limits
    if len(sys.argv) > 2 and sys.argv[2].isdigit():
        pl.ylim(min(y), float(sys.argv[2]))  # set y axis limits
    else:
        pl.ylim(min(y), max(y))
    pl.plot(x, y, 'ob-', label=u"%s/%s趋势图\n相关性系数R=%.3f" % (x_label, y_label, r))  # 画数据曲线
    pl.plot(x, pred_y, 'or--', label=u'线性回归拟合曲线')  # 画拟合线
    pl.xlabel(x_label)
    pl.ylabel(y_label)
    pl.legend()  # make legend
    pl.show()


def demo():
    x = range(10)+[100]
    y = [i*i for i in x]
    pl.xlim(-1, 11)  # 限定横轴的范围
    pl.ylim(-1, 110)  # 限定纵轴的范围
    pl.title(u'图像标题')
    pl.plot(x, y, 'ob-', label=u'y=x^2曲线图')  # 加上label参数添加图例
    pl.legend()  # 让图例生效
    pl.xlabel(u"我是横轴")
    pl.ylabel(u"我是纵轴")
    pl.show()  # 显示绘制出的图


if __name__ == "__main__":
    demo()
    x = range(10) + [1.5 * i for i in range(5)]
    y = [1.7 * i + 4 * random.random() for i in x]
    print 'x:', x
    print 'y:', y
    draw_pic(x, y, u'横轴', u'纵轴')
