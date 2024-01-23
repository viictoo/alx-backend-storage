#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs stored in MongoDB
    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the number of docs in this collection
        second line: Methods:
        5 lines with the number of documents with the method =
        ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
        one line with the number of documents with:
            method=GET
            path=/status
 """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method, collection.count_documents({"method": method})))
    print("{} status check".format(
        collection.count_documents({"path": "/status"})))

    print("IPs:")
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
