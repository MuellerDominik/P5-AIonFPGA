#!/usr/bin/env python3

'''aionfpga ~ data acquisition and alteration (daa)
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

from modules.definitions import *

rep = [(' ', '-'), ('(', ''), (')', '')]
objects_san = [repl(obj.lower(), rep) for obj in objects]
