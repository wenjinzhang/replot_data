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

BPG_4_4_4_x= [0.024118070554355636, 0.06551475881929447, 0.18250539956803458, 0.33189344852411795, 0.517278617710583, 0.7026637868970481, 0.8628509719222461, 1.1274298056155507]
BPG_4_4_4_y= [6.644958996623206, 8.767486734201597, 11.710082006753463, 14.001447178002866, 15.93101784852868, 17.450554751567758, 18.584177520501672, 19.983116256632886]
Cheng2020_optms_ssim_x= [0.1177105831533477, 0.26979841612670985, 0.4839812814974802, 0.8412526997840171]
Cheng2020_optms_ssim_y= [13.326097443318831, 16.883743367100802, 19.814278822961878, 22.672455378678237]
Cheng2020_opt_mse_x= [0.09791216702663785, 0.17350611951043915, 0.29949604031677457, 0.4578833693304535, 0.6792656587473002, 0.8295536357091431]
Cheng2020_opt_mse_y= [10.697057404727412, 12.361312108055923, 14.58031837916061, 16.497829232995635, 18.222383019778082, 19.18716835504099]

Cheng2020_with_checkboard_6M_Steps_opt_ms_ssim_x= [0.026817854571634242, 0.06551475881929447, 0.18340532757379407, 0.351691864650828, 0.6045716342692585, 1.0320374370050396]
Cheng2020_with_checkboard_6M_Steps_opt_ms_ssim_y= [7.091172214182297, 10.697057404727412, 14.833574529667121, 17.643511818620336, 20.59816690786299, 23.794018330921368]

Cheng2020_with_checkboard_6M_steps_opt_mse_x= [0.09881209503239735, 0.16360691144708422, 0.2976961843052554, 0.43718502519798397, 0.6504679625629949, 0.7935565154787615]
Cheng2020_with_checkboard_6M_steps_opt_mse_y= [10.5282199710564, 12.337192474674351, 14.700916546068473, 16.449589966232487, 18.463579353593808, 19.51278340569222]
JPEG_x= [0.1771058315334773, 0.25629949604031677, 0.3552915766738661, 0.45068394528437716, 0.5892728581713462, 0.7152627789776818, 0.8538516918646506, 0.9618430525557953, 1.071634269258459, 1.1436285097192223]
JPEG_y= [5.656054027978726, 8.381572600096437, 10.479980704293258, 12.095996140858626, 13.784370477568713, 15.014471780028918, 16.148094548962835, 16.87168355041001, 17.450554751567758, 17.86058851905449]
Minnen2018_opt_mse_x= [0.07271418286537076, 0.1537077033837293, 0.2652987760979121, 0.42818574514038865, 0.6351691864650827, 0.9033477321814254]
Minnen2018_opt_mse_y= [9.647853352629, 11.95127834056919, 13.904968644476575, 15.955137481910256, 17.812349252291348, 19.657501205981653]
Minnen2018_withcheckboard_opt_ms_ssim_x= [0.018718502519798452, 0.05471562275018002, 0.18430525557955363, 0.3426925845932324, 0.6117710583153348, 1.0770338372930164]
Minnen2018_withcheckboard_opt_ms_ssim_y= [6.512301013024555, 9.225759768451478, 14.242643511818594, 17.064640617462594, 20.17607332368547, 23.540762180414855]
Minnen2018_with_checkerboard_opt_mse_x= [0.10961123110151189, 0.18430525557955357, 0.32649388048956063, 0.4911807055435564, 0.7116630669546433, 0.8781497480201585]
Minnen2018_with_checkerboard_opt_mse_y= [10.612638687891907, 12.337192474674351, 14.532079112397465, 16.449589966232494, 18.258562469850443, 19.51278340569222]

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
l0, =plt.plot(BPG_4_4_4_x, BPG_4_4_4_y, color=colors[0], label = 'BPG_4_4_4', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l1, =plt.plot(Cheng2020_optms_ssim_x, Cheng2020_optms_ssim_y, color=colors[1], label = 'Cheng2020_optms_ssim', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l2, =plt.plot(Cheng2020_opt_mse_x, Cheng2020_opt_mse_y, color=colors[2], label = 'Cheng2020_opt_mse', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
        ,markeredgewidth=markeredgewidth, markersize=markersize)

l3, =plt.plot(Cheng2020_with_checkboard_6M_Steps_opt_ms_ssim_x, Cheng2020_with_checkboard_6M_Steps_opt_ms_ssim_y, color=colors[3], label = 'Cheng2020_with_checkboard_6M_Steps_opt_ms_ssim', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l4, =plt.plot(Cheng2020_with_checkboard_6M_steps_opt_mse_x, Cheng2020_with_checkboard_6M_steps_opt_mse_y, color=colors[4], label = 'Cheng2020_with_checkboard_6M_steps_opt_mse', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l5, =plt.plot(JPEG_x, JPEG_y, color=colors[5], label = 'JPEG', linewidth=linewidth, linestyle = '-', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l6, =plt.plot(Minnen2018_opt_mse_x, Minnen2018_opt_mse_y, color=colors[6], label = 'Minnen2018_opt_mse', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l7, =plt.plot(Minnen2018_withcheckboard_opt_ms_ssim_x, Minnen2018_withcheckboard_opt_ms_ssim_y, color=colors[7], label = 'Minnen2018_withcheckboard_opt_ms_ssim', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

l8, = plt.plot(Minnen2018_with_checkerboard_opt_mse_x, Minnen2018_with_checkerboard_opt_mse_y, color=colors[8], label = 'Minnen2018_with_checkerboard_opt_mse', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

# l9, =plt.plot(Minnen_20_x, Minnen_20_y, color=colors[9], label = 'Minnen_20', linewidth=linewidth, linestyle = '-' , markerfacecolor='none'
#          ,markeredgewidth=markeredgewidth, markersize=markersize)


plt.xlabel('Bits Per Pixel (Minnen2018_opt_mse)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize-3, handles=[l0, l1, l2, l3, l4, l5, l6, l7, l8], loc='best')
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
# plt.ylim((26, 40))
plt.tight_layout()
plt.savefig("kodak_mse_figure5_ssim.pdf")
# plt.show()

