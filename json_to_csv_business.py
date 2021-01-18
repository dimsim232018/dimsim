#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name,'w', encoding="utf-8") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)

if not os.path.isfile("data/business_header.csv"):
    with open("dataset/business.json",encoding="utf-8") as business_json, \
            open("data/business.csv", 'w',encoding="utf-8") as business_csv:

        write_header("data/business_header.csv", ['id:ID(Business)', 'name', 'address', 'city', 'state'])

        business_writer = csv.writer(business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in business_json.readlines():
            item = json.loads(line)
            try:
                business_writer.writerow([item['business_id'], item['name'], item['address'], item['city'], item['state']])
            except Exception as e:
                print(item)
                raise e

