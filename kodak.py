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

Balle2018_x= [0.11515031645569625, 0.18503428270042205, 0.30139767932489464, 0.46819620253164573, 0.6864187763713082, 0.8881592827004222]
Balle2018_y= [27.065572250046372, 28.71763123724726, 30.75227230569467, 32.781116675941384, 34.92589501020219, 36.54317380819885]
BPG_x= [0.0821861814345992, 0.19393459915611821, 0.3040348101265824, 0.47347046413502125, 0.6831223628691986, 0.867721518987342]
BPG_y= [26.694583565201256, 29.453811908736782, 31.227601558152475, 33.31441291040623, 35.2968836950473, 36.75765164162493]
Cheng_2020_with_checkerboard_x= [0.09778481012658231, 0.16329113924050637, 0.2981012658227849, 0.438607594936709, 0.6503164556962027, 0.7946202531645572]
Cheng_2020_with_checkerboard_y= [27.81636060100167, 29.619365609348915, 31.95659432387312, 33.959933222036724, 36.046744574290486, 37.18196994991653]
Cheng2020_with_checkboard_1M_x= [0.1013053797468355, 0.17020042194092833, 0.2981012658227849, 0.45171413502109714, 0.6649920886075953, 0.8073971518987345]
Cheng2020_with_checkboard_1M_y= [27.929280281951396, 29.62191615655722, 31.760897792617325, 33.8708959376739, 35.78960304210722, 36.93734928584678]
Cheng2020_x= [0.0976793248945148, 0.17349683544303807, 0.29941983122362875, 0.4566587552742617, 0.6791666666666669, 0.8288238396624475]
Cheng2020_y= [28.00463735856056, 29.923344462993875, 32.05073270265257, 34.183917640511964, 36.038861064737524, 37.10545353366722]

JPEG_x= [0.31722046413502103, 0.40952004219409294, 0.49522679324894525, 0.6000527426160339, 0.7088343881856541, 0.8367352320675108]
JPEG_y= [26.619226488592098,  28.15535151177889, 29.198757187905766, 30.265349656835465, 31.146447783342605, 32.073919495455385]

Minnen_2018_with_checkerboard_x= [0.10822784810126586, 0.18305643459915616, 0.32645042194092844, 0.4892932489451478, 0.7118011603375528, 0.8759625527426167]
Minnen_2018_with_checkerboard_y= [27.616258579113335, 29.442218512335373, 31.7377109998145, 33.85350584307179, 35.91133370432202, 37.26196438508625]
Minnen_2020_cc10_x= [0.11284282700421945, 0.1596518987341773, 0.29941983122362875, 0.4536919831223617, 0.6508175105485233, 0.7978375527426163]
Minnen_2020_cc10_y= [28.653867557039504, 29.708866629567794, 32.166666666666664, 34.039000185494345, 35.98089408273048, 37.14023372287145]
Minnen2018_w_o_context_x= [0.11646888185654013, 0.19063818565400853, 0.30139767932489464, 0.4550105485232069, 0.66664029535865, 0.8769514767932493]
Minnen2018_w_o_context_y= [27.871313299944347, 29.245130773511406, 31.331942125765163, 33.31441291040623, 35.36644407345576, 37.012706362455944]
Minnen2018_x= [0.07196729957805913, 0.15338871308016883, 0.26414820675105494, 0.4283095991561182, 0.6353243670886075, 0.8278349156118145]
Minnen2018_y= [26.746753849007604, 28.93210907067334, 31.076887404934148, 33.29702281580412, 35.36644407345576, 36.91416249304396]


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
l0, =plt.plot(Balle2018_x, Balle2018_y, color=colors[0], label = 'Ballé2018', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l1, =plt.plot(BPG_x, BPG_y, color=colors[1], label = 'BPG (4:4:4)', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l2, =plt.plot(Cheng_2020_with_checkerboard_x, Cheng_2020_with_checkerboard_y, color=colors[2], label = 'Cheng2020 with checkerboard, 6M steps', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
        ,markeredgewidth=markeredgewidth, markersize=markersize)

l3, =plt.plot(Cheng2020_with_checkboard_1M_x, Cheng2020_with_checkboard_1M_y, color=colors[3], label = 'Cheng2020 with checkerboard, 1M steps', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l4, =plt.plot(Cheng2020_x, Cheng2020_y, color=colors[4], label = 'Cheng2020', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l5, =plt.plot(JPEG_x, JPEG_y, color=colors[5], label = 'JPEG', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l6, =plt.plot(Minnen_2018_with_checkerboard_x, Minnen_2018_with_checkerboard_y, color=colors[6], label = 'Minnen2018 with checkerboard', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l7, =plt.plot(Minnen_2020_cc10_x, Minnen_2020_cc10_y, color=colors[7], label = 'Minnen2020, cc10', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l8, = plt.plot(Minnen2018_w_o_context_x, Minnen2018_w_o_context_y, color=colors[8], label = 'Minnen2018 w/o context', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l9, =plt.plot(Minnen2018_x, Minnen2018_y, color=colors[9], label = 'Minnen2018', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)


plt.xlabel('Bits Per Pixel (BPP)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize-2, handles=[l0, l1, l2, l3, l4, l5, l6, l7, l8, l9,], loc='best')
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
plt.ylim((26, 40))
plt.tight_layout()
plt.savefig("kodak_mse.pdf")
# plt.show()


















