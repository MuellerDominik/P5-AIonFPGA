#!/usr/bin/env python3

'''aionfpga ~ definitions
Copyright (C) 2019 Dominik Müller and Nico Canzani
'''

import os
import re
import math

import MySQLdb

from modules.settings import *

# Functions ------------------------------------------------------------------

# replace 'o_n' with 'n_n' (rep=[(o_0, n_0), ..., (o_n, n_n)]), if in 'string'
def repl(string, rep):
    for o, n in rep:
        if o in string:
            string = string.replace(o, n)
    return string

# input single number [min, max]
def input_integer_range(text, min, max):
    while True:
        raw_inp = input(f'{text} ')
        try:
            inp = int(raw_inp)
        except Exception as e:
            pass
        else:
            if inp >= min and inp <= max:
                return inp

# input space separated list of integers
def input_integer_list(text, max):
    inp = None
    while inp is None:
        print()
        inp = input(f'{text} ').strip().split()
        if inp == []:
            break
        elif inp[0] == 'all':
            inp = [i+1 for i in range(max)]
            break
        inp_tmp = inp.copy()
        inp_ext = []
        popped = 0
        for idx, i in enumerate(inp):
            search = re.search("^([\\d]+)-([\\d]+)$", i)
            if search:
                inp_tmp.pop(idx-popped)
                inp_ext.extend(list(range(int(search.group(1)),
                                          int(search.group(2))+1)))
                popped += 1
        inp_tmp.extend(inp_ext)
        inp = inp_tmp
        try:
            inp = map(int, inp)
            inp = list(inp)
        except Exception as e:
            print(f'Error: only numbers allowed')
            inp = None
        else:
            inp = list(set(inp))

            if len(inp) > max:
                print(f'Error: input > frames ({len(inp)} > {max})')
                inp = None
            else:
                for i in inp:
                    if i < 1 or i > max:
                        if i < 1:
                            print(f'Error: input < 1 ({i} < 1)')
                        else:
                            print(f'Error: input > max(input) ({i} > {max})')
                        inp = None
                        break
    return inp

# return infos about the `objects` list
def objects_list_info():
    noo = len(objects) # number of objects
    max_length = max([len(e) for e in objects])
    nos = int(1.1 * max_length) + 1 # number of spaces
    if nos < 25: # at least 25 whitespace characters
        nos = 25
    nod = len(str(noo - 1)) # number of digits
    return noo, nos, nod # number of objects / spaces / digits

# print choice
def choice(text, choice_false, choice_true):
    noo, nos, nod = objects_list_info()
    space = nos
    string = f'0 {choice_false}'
    string += ' ' * (space - len(choice_false) + nod - 1)
    string += f'1 {choice_true} (Enter)\n'
    print(string)
    inp = input_integer_range(text, 0, 1)
    if inp == 0:
        return False
    else:
        return True

# print the objects list and request a valid input
def print_objects_list():
    noo, nos, nod = objects_list_info()
    even = (noo%2 == 0)
    if not even:
        offset = 1
    else:
        offset = 0
    string = ''
    for i in range(int(noo/2)):
        i2 = int(noo/2 + i + offset)
        len_object = len(objects[i])
        nos_before = nod - len(str(i))
        nos_after = nos - len_object + nod - len(str(i2))
        string += ' ' * nos_before
        string += f'{i} {objects[i]}'
        string += ' ' * nos_after
        string += f'{i2} {objects[i2]}\n'
    if not even:
        string += f'{int(noo/2)} {objects[int(noo/2)]}\n'
    print(string)
    return input_integer_range('Identify the object:', 0, len(objects)-1)

# Lambda Functions -----------------------------------------------------------

# Clear Screen (CLS) on Windows
clear = lambda: os.system('cls')

# Database Functions ---------------------------------------------------------

# execute query
def db_write(queries, database):
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cursor = db.cursor()
    for query in queries:
        cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()

# return the first match
def db_fetch_field(query, database):
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    field = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return field

# return the matching rows
def db_fetch_rows(query, database):
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows

# fetch specific field from specific row
def fetch_field(table, row, field, database=database):
    query = f"SELECT {field} FROM {table} WHERE id = '{row}'"
    return db_fetch_field(query, database)

# fetch 'fields' from rows where 'column' equals 'value' in 'table'
def fetch_rows(table, column, value, fields, database = database):
    query = f"SELECT {fields} FROM {table} WHERE {column} = '{value}'"
    return db_fetch_rows(query, database)

# returns all rows from 'table'
def fetch_all_rows(table, database = database):
    query = f"SELECT * FROM {table}"
    return db_fetch_rows(query, database)

def fetch_rows_and(table, columns, values, fields, database=database):
    query = f"SELECT {fields} FROM {table} WHERE {columns[0]} = '{values[0]}'"
    columns.pop(0); values.pop(0)
    for c, v in zip(columns, values):
        query += f" AND {c} = '{values[0]}'"
    return db_fetch_rows(query, database)

# set 'field' of 'row' to 'value' in 'table'
def update_field(table, row, field, value, database=database):
    update_fields(table, [row], field, [value])

# set 'field' of 'rows' to 'values' in 'table'
# 'rows' and 'values' need to be lists of same size
def update_fields(table, rows, field, values, database=database):
    queries = []
    for row, value in zip(rows, values):
        queries.append((f"UPDATE {table} SET {field} = '{value}' "
                        f"WHERE id = '{row}'"))
    db_write(queries, database)

# insert single 'row' into 'table'
def insert_row(table, row, database=database):
    insert_rows(table, [row])

# insert multiple 'rows' into 'table'
def insert_rows(table, rows, database=database):
    queries = []
    for row in rows:
        query = f'INSERT INTO {table} VALUES (NULL, '
        for val in row:
            query += f'{val}, '
        queries.append(f'{query[:-2]})')
    db_write(queries, database)
