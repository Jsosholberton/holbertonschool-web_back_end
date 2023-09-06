#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME = 8-all
-------------------------------------------------------------------------------
DESCRIPTION:
-------------------------------------------------------------------------------
Write a Python function that lists all documents in a collection:
    -Prototype: def list_all(mongo_collection):
    -Return an empty list if no document in the collection
    -mongo_collection will be the pymongo collection object
'''


def list_all(mongo_collection) -> list:
    """ That list all documentes in a collection """
    return [document for document in mongo_collection.find()]
