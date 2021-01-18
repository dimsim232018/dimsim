#!/usr/bin/env python
# -*- coding: utf-8 -*-
# module:
# author:

import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name,'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)
        
if not os.path.isfile("review_header.csv"):
    with open("review.json",encoding="utf-8") as review_json, \
            open("review.csv", 'w', encoding="utf-8") as review_csv:

        write_header("review_header.csv", ['id:ID(Review)', 'text', 'stars:int', 'date'])
       

        review_writer = csv.writer(review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        

        for line in review_json.readlines():
            item = json.loads(line)
            review_writer.writerow([item["review_id"], item["text"], int(item["stars"]), item["date"]])
            
            
            
            