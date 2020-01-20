#!/usr/bin/env python3

'''aionfpga ~ data acquisition application (daa)
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import os
import shutil
import subprocess
from time import time

import modules.daa as daa

# location of the camera interface binary
cam_interface = r'..\cam-interface\cam-interface.exe'

def main():
    try:
        throwid = daa.fetch_field(daa.tab_settings, 0, 'throwid')
    except Exception as e:
        print(e)
        input()
        raise e

    session_throwid = 1

    for f in os.listdir(daa.dir_temp):
        os.unlink(daa.dir_temp / f)

    while True:
        daa.clear()

        print(f'Throw #{session_throwid} ({throwid} in total)\n')
        print(r'''
          _____                _       
         |  __ \              | |      
         | |__) |___  __ _  __| |_   _ 
         |  _  // _ \/ _` |/ _` | | | |
         | | \ \  __/ (_| | (_| | |_| |
         |_|  \_\___|\__,_|\__,_|\__, |
                                  __/ |
                                 |___/ 
        ''')

        subp = [cam_interface]
        res = subprocess.run(subp, stdout=subprocess.PIPE)
        # stdout = res.stdout.decode('utf-8')

        daa.clear()

        print(f'Throw #{session_throwid} ({throwid} in total)\n')

        valid = daa.choice('Throw valid?', 'No', 'Yes')
        print('\n')

        if valid:
            inp = daa.print_objects_list()
            print('\n')

            throwid += 1
            session_throwid += 1

            ts = int(time())
            obj = daa.objects[inp]
            obj_san = daa.objects_san[inp]
            framegood = True
            partial = False

            img_name = lambda i : f'{i}.png'
            frame = lambda i : f'{ts}_{throwid}_{i}_{obj_san}.png'

            rows = []
            for idx in range(1, len(os.listdir(daa.dir_temp))+1):
                row = [ts, throwid, idx, f"'{frame(idx)}'", f"'{obj}'", framegood, partial]
                rows.append(row)

            daa.insert_rows(daa.tab_frames, rows)

            for idx, f in enumerate(os.listdir(daa.dir_temp)):
                shutil.move(daa.dir_temp / img_name(idx),
                            daa.dir_frames / frame(idx+1))

            try:
                daa.update_field(daa.tab_settings, 0, 'throwid', throwid)
            except Exception as e:
                print(e)
                input()
                raise e
        else:
            for f in os.listdir(daa.dir_temp):
                os.unlink(daa.dir_temp / f)

if __name__ == '__main__':
    main()
