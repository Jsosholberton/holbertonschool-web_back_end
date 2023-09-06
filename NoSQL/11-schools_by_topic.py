#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME = 11-schools_by_topic
-------------------------------------------------------------------------------
DESCRIPTION:
-------------------------------------------------------------------------------
Write a Python function that returns the list of school having a specific topic
    -Prototype: def schools_by_topic(mongo_collection, topic):
    -mongo_collection will be the pymongo collection object
    -topic (string) will be topic searched
'''


def schools_by_topic(mongo_collection, topic) -> list:
    ''' that retunrs the list that having a specific topic '''
    return [document for document in mongo_collection.find({'topics': topic})]
