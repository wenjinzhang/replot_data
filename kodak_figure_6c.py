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

Proposed_x= [0.09954128440366969, 0.15840978593272168, 0.24510703363914368, 0.35107033639143725, 0.5019877675840979, 0.7053516819571864, 0.987920489296636, 1.3721712538226296]
Proposed_y= [31.016326530612254, 32.51020408163266, 33.930612244897965, 35.44897959183674, 36.96734693877551, 38.52244897959184, 40.08979591836735, 41.68163265306123]
Xie_21_x= [0.07599388379204891, 0.1230886850152905, 0.218348623853211, 0.332874617737003, 0.4795107033639142, 0.589755351681957, 0.8102446483180422]
Xie_21_y= [29.595918367346947, 31.37142857142858, 33.50204081632654, 35.204081632653065, 36.74693877551021, 37.66530612244899, 38.98775510204082]
Cheng_20_x= [0.09097859327217125, 0.13486238532110087, 0.2044342507645259, 0.3221712538226299, 0.44633027522935764, 0.610091743119266]
Cheng_20_y= [30.183673469387763, 31.530612244897966, 32.96326530612245, 34.68979591836735, 35.96326530612245, 37.38367346938776]
Hu_21_x= [0.16055045871559628, 0.23547400611620792, 0.30825688073394497, 0.6036697247706423, 0.8166666666666665, 0.953669724770642, 1.144189602446483]
Hu_21_y= [31.885714285714293, 33.269387755102045, 34.34693877551021, 37.187755102040825, 38.693877551020414, 39.465306122448986, 40.46938775510205]
BPG_x= [0.08883792048929665, 0.08669724770642198, 0.12737003058103977, 0.2793577981651375, 0.551223241590214, 1.0114678899082568, 1.3946483180428133]
BPG_y= [29.057142857142864, 29.057142857142864, 30.47755102040817, 33.07346938775511, 35.84081632653062, 38.75510204081633, 40.395918367346944]
Balle_18_x= [0.1123853211009174, 0.16911314984709477, 0.25152905198776754, 0.36712538226299696, 0.5148318042813455, 0.7374617737003059, 1.0264525993883789, 1.3957186544342506]
Balle_18_y= [29.448979591836743, 30.979591836734702, 32.58367346938776, 34.212244897959195, 35.64489795918368, 37.49387755102041, 38.98775510204082, 40.81224489795919]
VVC_Intra_x= [0.0856269113149847, 0.1862385321100917, 0.36712538226299696, 0.6711009174311925, 1.2009174311926605, 1.3957186544342506]
VVC_Intra_y= [30.3061224489796, 32.81632653061225, 35.448979591836746, 38.057142857142864, 40.78775510204082, 41.424489795918376]
Minnen_18_x= [0.08669724770642198, 0.14128440366972475, 0.21513761467889905, 0.32431192660550456, 0.4848623853211008, 0.6828746177370032, 0.9590214067278287, 1.3133027522935776]
Minnen_18_y= [30.061224489795926, 31.493877551020418, 33.0, 34.45714285714286, 36.122448979591844, 37.7265306122449, 39.3795918367347, 40.81224489795919]

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
l0, =plt.plot(Proposed_x, Proposed_y, color=colors[0], label = 'Proposed', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l1, =plt.plot(BPG_x, BPG_y, color=colors[1], label = 'BPG', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l2, =plt.plot(Xie_21_x, Xie_21_y, color=colors[2], label = 'Xie_21', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
        ,markeredgewidth=markeredgewidth, markersize=markersize)

l3, =plt.plot(Hu_21_x, Hu_21_y, color=colors[3], label = 'Hu_21', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l4, =plt.plot(Cheng_20_x, Cheng_20_y, color=colors[4], label = 'Cheng_20', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l5, =plt.plot(VVC_Intra_x, VVC_Intra_y, color=colors[5], label = 'VVC_Intra', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l6, =plt.plot(BPG_x, BPG_y, color=colors[6], label = 'BPG', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l7, =plt.plot(Balle_18_x, Balle_18_y, color=colors[7], label = 'Balle_18', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)



plt.xlabel('Bits Per Pixel (BPP)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize-3, handles=[l0, l1, l2, l3, l4, l5, l6, l7], loc='best')
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
plt.ylim((26, 40))
plt.tight_layout()
plt.savefig("kodak_mse_figure6c.pdf")
# plt.show()


















