#!/usr/bin/env python
# -*- coding: utf-8 -*-
# module:
# author:

import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name,'w', encoding="utf-8") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)



if not os.path.isfile("data/category_header.csv"):
    with open("business.json", encoding="utf-8") as business_json, \
            open("data/category.csv", 'w', encoding="utf-8") as categories_csv, \
            open("data/business_IN_CATEGORY_category.csv", 'w', encoding="utf-8") as business_category_csv:

        write_header("data/category_header.csv", ['name:ID(Category)'])
        write_header("data/business_IN_CATEGORY_category_header.csv", [':START_ID(Business)', ':END_ID(Category)'])

        business_category_writer = csv.writer(business_category_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        category_writer = csv.writer(categories_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_categories = set()
        for line in business_json.readlines():
            item = json.loads(line)
            
            if item["categories"] is not None:
                for category in item["categories"].split(','):
                    unique_categories.add(category.strip())
                    business_category_writer.writerow([item["business_id"], category])
                
        for category in unique_categories:
            try:
                category_writer.writerow([category])
            except Exception as e:
                print(category)
                raise e     
                
                
                
