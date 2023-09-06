#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME = 12-log_stats
-------------------------------------------------------------------------------
DESCRIPTION:
-------------------------------------------------------------------------------
Write a Python script that provides some stats about Nginx logs stored in
MongoDB:

    -Database: logs
    -Collection: nginx
    -Display (same as the example):
    -first line: x logs where x is the number of documents in this collection
    -second line: Methods:
    -5 lines with the number of documents with the method = ["GET", "POST", "PU
    T", "PATCH", "DELETE"] in this order (see example below - warning: it's a t
    abulation before each line)
    -one line with the number of documents with:
        * method=GET
        * path=/status

You can use this dump as data sample: dump.zip
The output of your script must be exactly the same as the example
'''
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    count = nginx.count_documents({})
    print(f'{count} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")

    for method in methods:
        count = nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status_check} status check')
