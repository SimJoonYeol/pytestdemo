# -*- coding: utf-8 -*-

def demo_method(num):
    num += 1
    return num

def demo_raise():
    import rospy

class demo_class(object):

    def demo_plus_10(self, num):
        num += 10
        return num

    def demo_minus_10(self, num):
        num -= 10
        return num

def get_collections():
    from demopytest import demomock
    collections = demomock.get_mongodb()
    result = ''
    for collection in collections:
        result += collection
    return result
