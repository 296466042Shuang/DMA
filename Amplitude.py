# Author: Zhi Kai
# Time:  14:23
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pylab as pl
from matplotlib.pylab import mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

# 通过文件读取数据
data = pd.read_csv('sample1_dma/matrix_scan01/sample1_dma S-1 X-1 Y-1 I-1.txt',sep="/")
#选取某一列数据
x = data['Piezo (nm) ']
#开始求数据振幅
sampling_rate = 10 #取样频率(来自传感器说明书)
fft_size = 35798 #FFT处理的数据样本数

# 用linspace计算每个数据点的时间标，时间标的单位为s,总时长为35.8s(35798个数据点)：
# linspace在指定的间隔内返回均匀间隔的数字
tstemp = np.linspace(0,int(1e6/sampling_rate * fft_size),fft_size)/1e3

# 绘制图形
#绘制原始数据趋势图
pl.figure(figsize=(14,8))
pl.title("data")
pl.ylabel("sample value")
pl.xlabel("time(ms)")
pl.plot(tstemp,x[:fft_size])
#绘制原始数据分布直方图
pl.figure(figsize=(14,8))
pl.title("data")
pl.ylabel("spot")
pl.xlabel("sample value")
pl.hist(x[:fft_size],bins=100)
pl.show()

#进行傅里叶变换
rf = abs(np.fft.rfft(x))

#绘制前后对比图
plt.figure(figsize=(14,8))
a = plt.subplot(211)
a.set_xlabel('time [s]')
a.set_ylabel('sample value')
n = np.arange(35798)/35798
plt.plot(n, x)
b = plt.subplot(212)
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(rf)
plt.savefig('sample-graph.png')
