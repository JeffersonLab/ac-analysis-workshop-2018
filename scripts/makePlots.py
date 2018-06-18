#!/usr/bin/python

# Import various modules
import pickle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ROOT as R
from matplotlib import rc

rc('text', usetex = True)
rc('font', family = 'serif')
mpl.rcParams.update({'font.size': 18})
mpl.rcParams.update({'errorbar.capsize': 10})

# Open data dictionary produced via calcQNY.py
dd = pickle.load(open('../dicts/dataDictXbj.pkl', 'rb'))

# Make simple overlay plot of E' yield for the c12 target, recall there are 2 momentum settings
# plt.figure()
# plt.title('Charge Normalized Yields for 12C')
# plt.xlim(3.5, 6.1) 
# plt.ylim(0.0, np.max(dd['c12']['eprime_qny'][0]) + np.max(dd['c12']['eprime_qny'][0])*0.10)
# plt.xlabel('E\' / 0.100 GeV')
# plt.ylabel('Yield')
# plt.errorbar(dd['c12']['eprime_val'][0], dd['c12']['eprime_qny'][0],
#             yerr = dd['c12']['eprime_qny_err'][0], fmt = 'bd', 
#             markersize = 10.0, label = '4.0 GeV')
# plt.errorbar(dd['c12']['eprime_val'][1], dd['c12']['eprime_qny'][1],
#             yerr = dd['c12']['eprime_qny_err'][1], fmt = 'gs', 
#             markersize = 10.0, label = '5.1 GeV')
# plt.legend(loc = 'best', numpoints = 1, fancybox = True)
# plt.savefig('../plots/c12-qny-simple.png')


# Make overlay plot of xbj yields with data points
# tarfont = {'family' : 'serif',
#            'color'  : 'darkred',
#            'weight' : 'normal',
#            'size'   : 32 }
# mkrs = ['bd', 'gs', 'ko']
# fig, axs = plt.subplots(nrows = 2, sharex = True)
# fig.suptitle(r'$\mathrm{Charge\ Normalized\ Yields}$')
# fig.text(0.01, 0.5, r'$\mathbf{\mathrm{Y / \epsilon Q}}$', va = 'center', rotation = 'vertical')
# for tar, tar_dict in dd.items():
#    for index, mom_list in enumerate(dd[tar]['pcent_list']):
#        if (tar == 'c12') :
#            ax = axs[0]
#            ax.errorbar(dd[tar]['xbj_calc_val'][index], dd[tar]['xbj_calc_qny'][index], 
#                        yerr = dd[tar]['xbj_calc_qny_err'][index], fmt = mkrs[index], 
#                        label = str(dd[tar]['pcent_list'][index]) + ' GeV')
#            ax.set_xlim(0.2, 1.01)
#            ax.set_ylim(0.0, np.amax(dd[tar]['xbj_calc_qny'][0]) + np.amax(dd[tar]['xbj_calc_qny'][0])*0.10)
#            ax.text(0.1, 0.2, r'${}^{12}\mathrm{{C}}$', ha = 'center', va = 'center', transform = ax.transAxes, fontdict = tarfont)
#            ax.legend(loc = 'best', numpoints = 1, fancybox = True)
#        if (tar == 'be9') :
#            ax = axs[1]
#            if (dd[tar]['pcent_list'][index] == 3.3) : tmpfmt = mkrs[2]
#            else : tmpfmt = mkrs[index]
#            ax.errorbar(dd[tar]['xbj_calc_val'][index], dd[tar]['xbj_calc_qny'][index], 
#                        yerr = dd[tar]['xbj_calc_qny_err'][index], fmt = tmpfmt, 
#                        label = str(dd[tar]['pcent_list'][index]) + ' GeV')
#            ax.set_ylim(0.0, np.amax(dd[tar]['xbj_calc_qny'][0]) + np.amax(dd[tar]['xbj_calc_qny'][0])*5.0)
#            ax.set_yscale('log')
#            ax.set_xlabel(r'$\mathrm{x_{Bj}}$')
#            ax.text(0.1, 0.2, r'${}^{9}\mathrm{{Be}}$', ha = 'center', va = 'center', transform = ax.transAxes, fontdict = tarfont)
#            ax.legend(loc = 'best', numpoints = 1, fancybox = True)
# plt.savefig('../plots/multi-tar-qny-xbj.png')

# # Make stacked histogram overlay plot of x yields
# carr = ['b', 'g']
# fig, axs = plt.subplots(nrows = 2, ncols = 2)
# # Unpack the axs array into its individual components
# ax0, ax1, ax2, ax3 = axs.flatten()
# for tar, tar_dict in dd.items():
#    for index, mom_list in enumerate(dd[tar]['pcent_list']):
#       if (tar == 'c12') :
#          ax0.bar(dd[tar]['eprime_val'][index], dd[tar]['eprime_ry'][index], yerr = dd[tar]['eprime_ry_err'][index],
#                  width = 0.100, align = 'center', color = carr[index], alpha = 0.5)
#          ax0.set_xlim(3.5, 6.1)
#       if (tar == 'be9') :
#          ax1.bar(dd[tar]['eprime_val'][index], dd[tar]['eprime_ry'][index], yerr = dd[tar]['eprime_ry_err'][index],
#                  width = 0.100, align = 'center', color = carr[index], alpha = 0.5)
#          ax1.set_xlim(2.9, 6.2)

plt.show()
