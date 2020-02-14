# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:42:59 2020

@author: VIET
"""

import os
import shutil
import glob

options = input(
    'Type 0 to copy and make treeseg directories hierachy from *.rxp files in registered scan directory or\nType 1 to rename *.DAT files:\n')
if options == '0':
    print('-'*30 + '\n' + 'This will copy and make treeseg directories hierachy from *.rxp files in registered scan directory' + '\n' + '-'*30 + '\n')
    from_directory = input('From directory (like G:/k34-sapflow-2019-09-28.RiSCAN):\n')
    to_directory = input(
        '\n' + '*'*30 + '\nTo directory (like G:/TREESEG-k34-sapflow-2019-09-28.RiSCAN), this will create the folder if not existed:\n')

    # Calculate number of folders
    n_folders = sum(os.path.isdir(os.path.join(from_directory + '/SCANS', ii))
                    for ii in os.listdir(from_directory + '/SCANS'))

    print('*'*30)
    if not os.path.exists(to_directory):
        os.makedirs(to_directory)

    for i in range(n_folders):
        os.makedirs(to_directory + '/Scanpos' + str(i+1).zfill(3), exist_ok=True)
        for file in glob.glob(from_directory + '/SCANS/ScanPos'+str(i+1).zfill(3)+'/SINGLESCANS/*[!residual].rxp'):
            shutil.copy2(file,
                         to_directory + '/Scanpos' + str(i+1).zfill(3) + '/' + str(i+1).zfill(3) + '.rpx')
            print('copying............' + file)
    print('Done')
elif options == '1':
    print('-'*30 + '\n' + 'This will rename all the *.DAT files in a selected directory' + '\n' + '-'*30 + '\n')
    from_directory = input(
        'From directory (like G:/k34-sapflow-2019-09-28.RiSCAN/matrix) which contains all the *.DAT files:\n')
    for i in range(60):
        os.rename(from_directory + '/Scanpos' + str(i+1).zfill(3)+'.DAT',
                  from_directory + '/' + str(i+1).zfill(3)+'.dat')
