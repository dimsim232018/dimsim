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


if not os.path.isfile("data/city_header.csv"):
    with open("business.json", encoding="utf-8") as business_json, \
            open("data/city.csv", "w", encoding="utf-8") as city_csv, \
            open("data/business_IN_CITY_city.csv", "w", encoding="utf-8") as business_city_csv:

        write_header("data/city_header.csv", ['name:ID(City)'])
        write_header("data/business_IN_CITY_city_header.csv", [':START_ID(Business)', ':END_ID(City)'])

        business_city_writer = csv.writer(business_city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        city_writer = csv.writer(city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_cities = set()
        for line in business_json.readlines():
            item = json.loads(line)

            if item["city"].strip():
                unique_cities.add(item["city"])
                business_city_writer.writerow([item["business_id"], item["city"]])

        for city in unique_cities:
            city_writer.writerow([city])
            
        
                
                
                
