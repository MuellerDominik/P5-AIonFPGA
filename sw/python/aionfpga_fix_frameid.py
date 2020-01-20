#!/usr/bin/env python3

'''aionfpga ~ fix frameid
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import os
import re
import shutil

import modules.daa as daa

directory = daa.dir_frames

# Functions for unit-testing

test_ext = '.txt'

test_ts = 1574937102
test_tid = 1
test_object = 'spiky-ball'
test_name = lambda i : f'{test_ts}_{test_tid}_{i}_{test_object}'

def unit_test():
    for i in range(100):
        create_unordered_files(i+1)
        fix_frameid(test_ts, test_tid, i+1, test_object, test_ext)
        res = check_files()
        if res:
            if res is not True:
                print(f"Fixing {i+1} didn't work.")
                break
            else:
                pass    # no error
        else:
            print(f'Error in {i+1} (RegEx).')
            break

def create_unordered_files(amount):
    # remove everything in the frames directory
    for f in os.listdir(directory):
        os.unlink(f'{directory}\\{f}')

    for i in range(amount):
        with open(f'{directory}\\{i}', 'w') as f:
            f.write(str(i))

    for (i, f) in enumerate(os.listdir(directory)):
        shutil.move(f'{directory}\\{f}', f'{directory}\\{test_name(i+1)}{test_ext}')

def check_files():
    for file in os.listdir(directory):
        with open(f'{directory}\\{file}', 'r') as f:
            frameid_search = re.search("^[\\d]*_[\\d]*_([\\d]*)_[a-z-]*.[a-z]*$", file)
            if frameid_search:
                frameid = int(frameid_search.group(1))
            else:
                return None
            text = f.read()
            if int(frameid) != int(text)+1:
                return False
    return True

# Functions to fix the frameid

def move_file(name_1, name_2):
    shutil.move(f'{directory}\\{name_1}', f'{directory}\\{name_2}')

# fix up to 100 frames
def fix_frameid(timestamp, throwid, frames, object_safe, file_ext='.png'):
    nof = frames
    rest_list_shift = [0 for x in range(nof) if x < 2]
    rest_list = [x+1 for x in range(nof) if x < 2]

    tmp_ext = '.tmp'
    name = lambda i : f'{timestamp}_{throwid}_{i}_{object_safe}'

    # add '.tmp' to all files
    for i in range(frames):
        move_file(f'{name(i+1)}{file_ext}', f'{name(i+1)}{file_ext}{tmp_ext}')

    if nof > 10:
        packets = [(p*11 + 3) for p in range(int((nof-10)/10))]   # start of full packet
        rest_list_shift.extend([10*(i+1) for (i, p) in enumerate(packets) if p+10 < 100])
        rest_list.extend([p+10 for p in packets if p+10 < 100])

        shift = 8
        for i in packets:   # handle full packets
            for j in range(10):
                move_file(f'{name(i+j)}{file_ext}{tmp_ext}', f'{name(i+j+shift)}{file_ext}')
            shift = shift - 1

        nof_left = nof - len(packets)*10 - 10   # len(packets)*10: handled by full packages / 10: 1-10
        if nof_left > 0:
            index = len(packets)*11 + 3
            rest_list_shift.extend([rest_list_shift[len(rest_list_shift)-1]+nof_left]*(10-len(rest_list_shift)))
            rest_list.extend(range(index+nof_left, nof+1))
            for i in range(nof_left):    # handle not full packets
                move_file(f'{name(index)}{file_ext}{tmp_ext}', f'{name(index+shift)}{file_ext}')
                index = index + 1
        else:
            rest_list_shift.extend([rest_list_shift[len(rest_list_shift)-1]]*(10-len(rest_list_shift)))
            rest_list.extend(range(len(packets)*10+len(rest_list)+1, nof+1))
    else:
        rest_list_shift.extend([0 for x in range(nof-len(rest_list))])
        rest_list.extend([x+3 for x in range(nof-len(rest_list))])

    for (i, r) in enumerate(rest_list):     # handle the lowest
        move_file(f'{name(r)}{file_ext}{tmp_ext}', f'{name(r-rest_list_shift[i])}{file_ext}')

def main():
    num_of_frames = 0
    try:
        throws = daa.fetch_field(daa.tab_settings, 0, 'throwid')
    except Exception as e:
        print(e)
        input()
        raise e
    for i in range(throws):
        try:
            throw = daa.fetch_rows(daa.tab_frames, 'throwid', i+1, '*')
        except Exception as e:
            print(e)
            input()
            raise e
        rowcount = len(throw)
        ts = throw[0][1]
        obj = throw[0][5]
        obj_san = daa.objects_san[daa.objects.index(obj)]
        fix_frameid(ts, i+1, rowcount, obj_san)
        num_of_frames += rowcount
        print(f'{i+1}: {ts} {obj_san} {rowcount}')
    print(f'#Frames = {num_of_frames}')

if __name__ == '__main__':
    # unit_test()
    main()
