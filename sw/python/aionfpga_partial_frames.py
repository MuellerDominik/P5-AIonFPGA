#!/usr/bin/env python3

'''aionfpga ~ partial frames
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import os
import shutil

import modules.daa as daa

# daa.Users.DOMINIK or daa.Users.NICO
user = daa.User.DOMINIK

def main():
    try:
        throwid = daa.fetch_field(daa.tab_settings, 0, user.name.lower())
    except Exception as e:
        print(e)
        input()
        raise e

    while True:
        daa.clear()

        for f in os.listdir(daa.dir_temp):
            os.unlink(daa.dir_temp / f)

        print(f'Throw #{throwid}\n')

        try:
            throw = daa.fetch_rows(daa.tab_frames, 'throwid', throwid, '*')
        except Exception as e:
            print(e)
            input()
            raise e

        id = throw[0][0]
        rowcount = len(throw)

        ts = throw[0][1]
        frame = throw[0][4]
        obj = throw[0][5]
        obj_san = daa.objects_san[daa.objects.index(obj)]

        name = lambda i : f'{ts}_{throwid}_{i}_{obj_san}.png'

        for idx in range(1, rowcount+1):
            shutil.copy(daa.dir_frames / name(idx),
                        daa.dir_temp / name(idx))

        inp = daa.input_integer_list("Enter frameid's (partial frames):", rowcount)
        inp = sorted(inp)

        input(f'\nHit enter to commit `{inp}` ')

        ids = inp.copy()
        values = [1]*len(ids)
        for idx in range(rowcount):
            if idx+1 not in inp:
                ids.append(idx+1)
                values.append(0)
            ids[idx] += id - 1

        try:
            daa.update_fields(daa.tab_frames, ids, 'partial', values)
        except Exception as e:
            print(e)
            input()
            raise e

        if user == daa.User.DOMINIK:
            throwid -= 1
        else:
            throwid += 1

        try:
            daa.update_field(daa.tab_settings, 0, user.name.lower(), throwid)
        except Exception as e:
            print(e)
            input()
            raise e

if __name__ == '__main__':
    main()
