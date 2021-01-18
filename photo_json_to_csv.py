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
              
                
if not os.path.isfile("data/photo_header.csv"):
    with open("dataset/photo.json", encoding="utf-8") as photo_json, \
            open("data/photo.csv", 'w', encoding="utf-8") as photo_csv, \
            open("data/business_HAS_PHOTO_photo.csv", 'w', encoding="utf-8") as business_photo_csv:

        write_header("data/photo_header.csv", ['id:ID(Photo)', 'caption', 'label'])
        write_header("data/business_HAS_PHOTO_photo_header.csv", [':START_ID(Business)', ':END_ID(Photo)'])
        

        photo_writer = csv.writer(photo_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        business_photo_writer = csv.writer(business_photo_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        
        for line in photo_json.readlines():
            item = json.loads(line)
            photo_writer.writerow([item["photo_id"], item["caption"], item["label"]])
            business_photo_writer.writerow([item["business_id"], item["photo_id"]])
            
