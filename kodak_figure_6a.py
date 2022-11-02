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

Proposed_x= [0.1267097966728281, 0.2041127541589649, 0.31039741219963035, 0.4675138632162662, 0.6523567467652499, 0.8972735674676526, 1.2230591497227359, 1.6297134935304995]
Proposed_y= [29.145571278825997, 30.739190251572328, 32.32134433962264, 34.12133123689728, 35.90985324947589, 37.744234800838576, 39.55568658280922, 41.30981394129979]
Xie_21_x= [0.09782809611829946, 0.13364140480591502, 0.16367837338262475, 0.29306839186691314, 0.4513401109057301, 0.6512014787430683, 0.7909889094269873, 1.061321626617375]
Xie_21_y= [27.884433962264154, 28.950668238993714, 29.70735062893082, 31.920073375262056, 33.94935796645703, 35.84106394129979, 36.918763102725364, 38.477987421383645]
Qian_22_x= [0.08627541589648802, 0.14519408502772646, 0.26303142329020335, 0.40512939001848436, 0.5934380776340112, 0.9319316081330871, 1.2565619223659892, 1.6747689463955642]
Qian_22_y= [27.620741614255763, 29.157036163522015, 31.381223794549264, 33.16974580712788, 35.13024109014675, 37.72130503144654, 39.693265199161424, 41.57350628930817]
Cheng_20_x= [0.12093345656192239, 0.18331792975970423, 0.2711182994454713, 0.41783733826247693, 0.5957486136783734, 0.806007393715342]
Cheng_20_y= [28.572327044025158, 29.971042976939202, 31.3353642557652, 33.39904350104822, 35.11877620545073, 36.71239517819706]
VVC_Intra_x= [0.08627541589648802, 0.11169131238447322, 0.2480129390018485, 0.4906192236598895, 0.8753234750462107, 1.431007393715342, 1.7960720887245847]
VVC_Intra_y= [27.540487421383645, 28.480607966457022, 31.209250524109017, 34.25890985324948, 37.411753144654085, 40.4270178197065, 41.68815513626834]
BPG_x= [0.11746765249537894, 0.16136783733826254, 0.3519870609981517, 0.6847042513863214, 1.199953789279113, 1.794916820702403]
BPG_y= [27.56341719077568, 28.67551100628931, 31.599056603773583, 34.85508385744235, 38.260154612159326, 40.885613207547166]
Balle_18_x= [0.1313308687615527, 0.20988909426987057, 0.3196395563770795, 0.47791127541589673, 0.669685767097967, 0.9388632162661743, 1.2600277264325326, 1.6609057301293906]
Balle_18_y= [27.586346960167717, 29.191430817610062, 30.968487945492665, 32.8372641509434, 34.53406708595388, 36.74678983228511, 38.59263626834382, 40.5645964360587]
Minne_18_x= [0.11053604436229214, 0.18678373382624763, 0.28729205175600736, 0.4328558225508319, 0.6396487985212572, 0.8857208872458413, 1.2011090573012941, 1.588123844731978]
Minne_18_y= [28.090801886792452, 29.638561320754715, 31.358294025157228, 33.08949161425576, 35.0958464360587, 36.99901729559748, 38.93658280922432, 40.64485062893082]
Minnen_20_x= [0.11284658040665435, 0.18909426987061007, 0.30000000000000004, 0.45942698706099827, 0.6685304990757858, 0.9423290203327173, 1.279667282809612, 1.705961182994455]
Minnen_20_y= [28.60672169811321, 30.246200209643604, 31.943003144654092, 33.8003144654088, 35.760809748427675, 37.72130503144654, 39.613011006289305, 41.458857442348005]


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

l3, =plt.plot(Qian_22_x, Qian_22_y, color=colors[3], label = 'Qian_22', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l4, =plt.plot(Cheng_20_x, Cheng_20_y, color=colors[4], label = 'Cheng_20', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l5, =plt.plot(VVC_Intra_x, VVC_Intra_y, color=colors[5], label = 'VVC_Intra', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l6, =plt.plot(BPG_x, BPG_y, color=colors[6], label = 'BPG', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l7, =plt.plot(Balle_18_x, Balle_18_y, color=colors[7], label = 'Balle_18', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l8, = plt.plot(Minne_18_x, Minne_18_y, color=colors[8], label = 'Minne_18', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l9, =plt.plot(Minnen_20_x, Minnen_20_y, color=colors[9], label = 'Minnen_20', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)


plt.xlabel('Bits Per Pixel (BPP)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize-3, handles=[l0, l1, l2, l3, l4, l5, l6, l7, l8, l9,], loc='best')
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
plt.ylim((26, 40))
plt.tight_layout()
plt.savefig("kodak_mse_figure6a.pdf")
# plt.show()


















