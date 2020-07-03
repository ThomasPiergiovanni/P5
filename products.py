#-*-coding:utf-8 -*
import urllib.request
import json
import operator

import config


class Products():
    def __init__(self):
        self.source_data = []
        self.products_list = []

    def get_data(self,categories_instance):
        for elt in categories_instance.wanted_categories:
            url = config.PRODUCTS_ENDPOINT_BEGINNING + elt.id + config.PRODUCTS_ENDPOINT_END
            request = urllib.request.Request(url, headers = config.HEADER, method = 'GET')
            response = urllib.request.urlopen(request)
            self.source_data = json.load(response)
            print (self.source_data)

        # def initialize(self):
        # for elt in self.source_data["tags"]:
        #     id = elt["id"]
        #     name = elt["name"]
        #     url = elt["url"]
        #     products = elt["products"]
        #     category_instance = category.Category(id, name, url, products)
        #     self.categories_list.append(category_instance)
