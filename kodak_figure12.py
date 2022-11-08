# -*- coding:utf-8 -*-
# 
# Author: Yang Sui
# Time: 10/26/22 16:14


from cgitb import handler
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

Entroformer_x= [0.09932279909706548, 0.1550037622272385, 0.1956358164033108, 0.22573363431151244, 0.326561324303988, 0.471030850263356, 0.6681715575620769, 0.9209932279909705, 1.0203160270880363]
Entroformer_y= [12.55254237288138, 14.261016949152566, 15.277966101694933, 16.020338983050863, 17.7084745762712, 19.488135593220345, 21.328813559322036, 23.199999999999996, 23.769491525423724]

fontsize = 20
font={'weight':'bold',
      'color':'black',
      'size':fontsize
}
plt.grid(linestyle = '--', linewidth =1)
linewidth = 1
markeredgewidth = 1
markersize = '10'
colors = ["#00a8e1", "#99cc00", "#e30039", "#fcd300", "#800080", "#00994e", "#ff6600", "#808000", "#db00c2", "#008080", "#0000ff ", "#c8cc00"]
l0, =plt.plot(Entroformer_x, Entroformer_y, color=colors[0], label = 'Entroformer', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)






plt.xlabel('Bits Per Pixel (Minnen2018_opt_mse)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize-3, handles=[l0,], loc='best')
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
# plt.ylim((26, 40))
plt.tight_layout()
plt.savefig("kodak_mse_figure12.pdf")
# plt.show()

