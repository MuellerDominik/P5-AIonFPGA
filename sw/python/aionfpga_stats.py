#!/usr/bin/env python3

'''aionfpga ~ stats
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import matplotlib.pyplot as plt

import modules.daa as daa

objects_plot = [
    'Dart', 'Football', 'Ping Pong', 'Shuttle', 'Sporf', 'Arrow',
    'Featherball', 'Floorball', 'Spiky', 'Tesafilm', 'Sponge', 'Duplo (Red)',
    'Duplo (Green)', 'Duplo Figure', 'Dice', 'Shoe', 'Bunny', 'Glove', 'Cord',
    'Paper', 'Beer Cap', 'Bottle'
]

def main():
    noo, *_ = daa.objects_list_info()

    frames = [0]*noo
    frames_partial = [0]*noo

    rows = daa.fetch_all_rows(daa.tab_frames)
    for row in rows:
        if row[6] == 1: # valid
            if row[7] == 0: # not partial
                frames[daa.objects.index(row[5])] += 1
            else:
                frames_partial[daa.objects.index(row[5])] += 1

    frames_valid = sum(frames) + sum(frames_partial)
    frames_invalid = len(rows) - frames_valid

    print(f'frames_valid {frames_valid}')
    print(f'frames_invalid {frames_invalid}')

    for idx, o in enumerate(daa.objects):
        if frames[idx] < 500:
            print(f'{o}: {frames[idx]}')

    plt.figure(figsize=[12, 6], tight_layout=True)
    p1 = plt.bar(objects_plot, frames, color=(0, 0.4470, 0.7410))
    p2 = plt.bar(objects_plot, frames_partial, bottom=frames, color=(0.8500, 0.3250, 0.0980))
    plt.legend((p1[0], p2[0]), ('Object fully visible', 'Object partially visible'))
    plt.xticks(rotation=45)
    plt.savefig('statistics.pdf', transparent=True)
    plt.show()

if __name__ == '__main__':
    main()
