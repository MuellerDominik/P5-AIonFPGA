#!/usr/bin/env python3

'''aionfpga ~ review labels
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
        obj_old = throw[0][5]
        obj_san_old = daa.objects_san[daa.objects.index(obj_old)]

        frame_old = lambda i : f'{ts}_{throwid}_{i}_{obj_san_old}.png'

        for idx in range(1, rowcount+1):
            shutil.copy(daa.dir_frames / frame_old(idx),
                        daa.dir_temp / frame_old(idx))

        print(f'Current throw is labeled as: `{obj_old}`\n\n')

        correct = daa.choice('Correct?', 'No', 'Yes')
        print('\n')

        if not correct:
            inp = daa.print_objects_list()
            print('\n')

            obj_new = daa.objects[inp]
            obj_new_san = daa.objects_san[inp]

            changed = (obj_new != obj_old)

            if not changed:
                input(f'Hit enter to abort without changing the label (`{obj_old}` stays `{obj_new}`) ')
            else:
                name_new = lambda i : f'{ts}_{throwid}_{i}_{obj_new_san}.png'

                # option to abort before committing
                input(f'Hit enter to commit `{obj_new}` ')

                ids = [id + idx for idx in range(rowcount)]
                frames = [name_new(idx) for idx in range(1, rowcount+1)]

                try:
                    daa.update_fields(daa.tab_frames, ids, 'frame', frames)
                    daa.update_fields(daa.tab_frames, ids, 'object', [obj_new]*rowcount)
                except Exception as e:
                    print(e)
                    input()
                    raise e

                for idx in range(1, rowcount+1):
                    shutil.move(daa.dir_frames / frame_old(idx),
                                daa.dir_frames / name_new(idx))

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
