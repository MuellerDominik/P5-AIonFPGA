#!/usr/bin/env python3

'''aionfpga ~ db backup
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import csv
from time import time

import modules.daa as daa

def backup_db():
    columns = daa.fetch_rows_and('COLUMNS', ['TABLE_SCHEMA', 'TABLE_NAME'],
                                 [daa.database, daa.tab_frames], 'COLUMN_NAME',
                                 database='INFORMATION_SCHEMA')
    columns = [column[0] for column in columns]
    rows = daa.fetch_all_rows(daa.tab_frames)
    timestamp = int(time())
    with open(f'aionfpga_db_{timestamp}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(columns)
        csv_writer.writerows(rows)
    return timestamp

def print_db(timestamp):
    with open(f'aionfpga_db_{timestamp}.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)

def main():
    ts = backup_db()
    print_db(ts)

if __name__ == '__main__':
    main()
