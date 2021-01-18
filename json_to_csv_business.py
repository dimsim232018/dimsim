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
                     

if not os.path.isfile("data/user_header.csv"):
    with open("dataset/user.json", encoding="utf-8") as user_json, \
            open("data/user.csv", 'w', encoding="utf-8") as user_csv, \
            open("data/user_FRIENDS_user.csv", 'w', encoding="utf-8") as user_user_csv:

        write_header("data/user_header.csv", ['id:ID(User)', 'name'])
        write_header("data/user_FRIENDS_user_header.csv", [':START_ID(User)', ':END_ID(User)'])

        user_writer = csv.writer(user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_user_writer = csv.writer(user_user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in user_json.readlines():
            item = json.loads(line)
            user_writer.writerow([item["user_id"], item["name"]])

            if item["friends"] is not None:
                for friend_id in item["friends"].split(','):
                    user_user_writer.writerow([item["user_id"], friend_id.strip()])

                
                


        for line in review_json.readlines():
            item = json.loads(line)
            review_writer.writerow([item["review_id"], item["text"], item["stars"], item["date"]])
            user_review_writer.writerow([item["user_id"], item["review_id"]])
            review_business_writer.writerow([item["review_id"], item["business_id"]])
