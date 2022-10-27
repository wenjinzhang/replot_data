# -*- coding:utf-8 -*-
# 
# Author: Yang Sui
# Time: 10/26/22 16:14


from matplotlib.pylab import datestr2num
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import rcParams
# font = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
# print(font)
# color: https://zhuanlan.zhihu.com/p/65220518


rcParams['font.family']='sans-serif'
rcParams['font.sans-serif']=['Times New Roman']
rcParams['font.weight']='bold'

fig = plt.figure(figsize=(12, 10))
# x_jpeg = [1.3, 2.1, 2.5, 3.0, 3.6, 4.1, 4.8, 5.15, 5.7, 6.3]
# x_minnen2018 = [1.3, 2.1, 2.5, 3.0, 3.57, 4.1, 4.8, 5.13, 5.8, 6.45]
# x_cheng2020 = []

# y_jpeg = [5.08, 5.25, 5.36, 5.51, 5.68, 5.78, 5.84, 5.91, 5.99, 6.11]
# y_minnen2018 = [4.4, 4.61, 4.88, 5.21, 5.45, 5.51, 5.69, 5.75, 5.86, 5.95]
# y_cheng2020 = []
Cheng_2020_1M_steps_x= [0.058782498414711476, 0.09701965757767914, 0.16493341788205454, 0.2933417882054533, 0.4434369055168041, 0.6494610019023463, 0.785859226379201]
Cheng_2020_1M_steps_y= [26.249999999999947, 27.833333333333286, 29.458333333333293, 31.718749999999968, 33.78124999999998, 35.69791666666665, 36.90624999999999]
Minnen2018_reproduction_x= [0.10329740012682306, 0.1786303107165504, 0.3213062777425491, 0.4845275840202918]
Minnen2018_reproduction_y= [27.333333333333286, 29.177083333333293, 31.541666666666636, 33.65624999999998]


fontsize = 20
font={'weight':'bold',
      'color':'black',
      'size':fontsize
}
plt.grid(linestyle = '--', linewidth =1)
linewidth = 1
markeredgewidth = 1
markersize = '10'
plt.plot(Cheng_2020_1M_steps_x, Cheng_2020_1M_steps_y, 'orange', label = 'jpeg', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(Minnen2018_reproduction_x, Minnen2018_reproduction_y, 'orange', label = 'jpeg', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)



plt.xlabel('Bits Per Pixel (BPP)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize)
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
# plt.ylim((0.3, 1.5))
plt.tight_layout()
plt.savefig("kodak_mse.pdf")


















