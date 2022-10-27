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
BPG_x= [0.11509229098805646, 0.1612377850162866, 0.22638436482084695, 0.35396308360477735, 0.5331161780673181, 0.7774158523344191, 1.0841476655808902, 1.3175895765472316, 1.5985342019543975, 1.9432681867535293]
BPG_y= [27.652062516013313, 28.574429925698176, 29.886241352805527, 31.628490904432482, 33.5142198308993, 35.56392518575454, 37.57263643351268, 38.88444786062003, 40.18601076095311, 41.50807071483474]
Entroformer_x= [0.08794788273615634, 0.1449511400651466, 0.26574375678610207, 0.4082519001085775, 0.5955483170466884, 0.9402823018458196, 1.268729641693811, 1.6867535287730728, 1.970412595005429]  
Entroformer_y= [27.71355367665897, 29.230335639251848, 31.41327184217268, 33.24775813476812, 35.133487061234945, 37.71611580835254, 39.68383294901358, 41.6105559825775, 42.71739687419933]
JPEG_x= [0.2901737242128123, 0.39603691639522265, 0.48832790445168317, 0.6416938110749186, 0.9457111834961996, 1.268729641693811, 1.6813246471226928, 1.952768729641694]
JPEG_y= [25.786830643095048, 27.631565462464764, 28.8203945682808, 30.224442736356643, 32.28439661798616, 33.92416090187035, 35.60491929285165, 36.52728670253651]
JPEG2000_x= [0.16395222584147662, 0.234527687296417, 0.3051031487513569, 0.4068946796959826, 0.599619978284473, 0.9511400651465799, 1.2782301845819757, 1.6976112920738329, 1.963626492942454]       
JPEG2000_y= [27.44709198052779, 28.63592108634383, 29.60953112990007, 30.76761465539328, 32.53036126056878, 34.94901357929797, 36.67076607737637, 38.46425826287471, 39.43786830643095]
Lee_x= [0.09880564603691638, 0.16395222584147662, 0.2779587404994571, 0.44625407166123787, 0.6932681867535287, 0.9945711183496199, 1.268729641693811, 1.5944625407166124]
Lee_y= [27.67255956956187, 29.168844478606193, 30.972585190878803, 32.960799385088386, 35.17448116833205, 37.3061747373815, 38.925441967717134, 40.3602357161158]
Minnen_x= [0.07166123778501626, 0.15852334419109665, 0.2698154180238871, 0.4272529858849078, 0.6389793702497286, 0.9077090119435397, 1.257871878393051, 1.993485342019544]
Minnen_y= [26.791186266974115, 28.96387394312067, 30.993082244427356, 33.022290545734045, 35.01050473994363, 37.06021009479887, 39.08941839610556, 42.18447348193697]
Qian_x= [0.0906623235613464, 0.15852334419109665, 0.2752442996742671, 0.42182410423452765, 0.6064060803474485, 0.9457111834961996, 1.290445168295331, 1.7057546145494031, 1.9989142236699244]        
Qian_y= [27.488086087624897, 29.2508326928004, 31.259543940558537, 33.145272867025355, 35.01050473994363, 37.60338201383551, 39.58134768127081, 41.487573661286184, 42.676402767102225]


fontsize = 20
font={'weight':'bold',
      'color':'black',
      'size':fontsize
}
plt.grid(linestyle = '--', linewidth =1)
linewidth = 1
markeredgewidth = 1
markersize = '10'
plt.plot(BPG_x, BPG_y, 'orange', label = 'BPG (4:4:4)', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(Entroformer_x, Entroformer_y, 'orange', label = 'Entroformer: Context+Hyperprior', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(JPEG_x, JPEG_y, 'orange', label = 'JPEG (4:2:0)', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(JPEG2000_x, JPEG2000_y, 'orange', label = 'JPEG2000 (OpenJPEG)', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(Lee_x, Lee_y, 'orange', label = 'Lee (2019) Context-Adaptive', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(Minnen_x, Minnen_y, 'orange', label = 'Minnen (2018) Context+Hyperprior', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)

plt.plot(Qian_x, Qian_y, 'orange', label = 'Qian (2021) Reference', linewidth=linewidth, linestyle = '-', marker='^', markerfacecolor='none'
         ,markeredgewidth=markeredgewidth, markersize=markersize)



plt.xlabel('Bits Per Pixel (BPP)', fontdict=font)
plt.ylabel('PSNR', fontdict=font)
plt.xticks(fontsize=fontsize, fontweight='bold')
plt.yticks(fontsize=fontsize, fontweight='bold')
plt.legend(fontsize=fontsize)
plt.tick_params(top=False,bottom=True,left=True,right=False, width=2)
# plt.ylim((0.3, 1.5))
plt.tight_layout()
plt.savefig("kodak_mse_5.pdf")


















