#!/usr/bin/env python3

'''aionfpga ~ settings
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

from enum import Enum
from pathlib import Path

# Database -------------------------------------------------------------------

# Connection
host = '<host>'
port = 3306
user = '<user>'
passwd = '<password>'
database = 'aionfpga' # default to this database

# Tables
tab_frames = 'frames'
tab_settings = 'settings'

# Objects --------------------------------------------------------------------

# special chars: only spaces and round brackets (i.e. `(` and `)`)
objects = [
    'Nerf Dart', 'American Football', 'Table Tennis Ball',
    'Shuttlecock', 'Sporf', 'Arrow', 'Hand Featherball', 'Floorball',
    'Spiky Ball', 'Tesafilm', 'Sponge', 'Lego Duplo Brick (Red)',
    'Lego Duplo Brick (Green)', 'Lego Duplo Figure', 'Foam Dice',
    'Infant Shoe', 'Stuffed Bunny', 'Goalkeeper Glove', 'Hemp Cord',
    'Paper Ball', 'Beer Cap', 'Water Bottle'
]

# list `objects_san` is dynamically created in `daa.py`
# objects_san = ['nerf-dart', 'american-football', 'table-tennis-ball',
#     'shuttlecock', 'sporf', 'arrow', 'hand-featherball', 'floorball',
#     'spiky-ball', 'tesafilm', 'sponge', 'lego-duplo-brick-red',
#     'lego-duplo-brick-green', 'lego-duplo-figure', 'foam-dice',
#     'infant-shoe', 'stuffed-bunny', 'goalkeeper-glove', 'hemp-cord',
#     'paper-ball', 'beer-cap', 'water-bottle'
# ]

# Directories ----------------------------------------------------------------

dir_frames = Path(r'B:\aionfpga\frames')
dir_temp = Path(r'B:\aionfpga\temporary')

# Users ----------------------------------------------------------------------

class User(Enum):
    DOMINIK = 1
    NICO = 2
