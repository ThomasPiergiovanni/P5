#-*-coding:utf-8 -*
"""Engin module.
"""
from programm.admin.database import Database
from programm.admin.tests import Tests
from programm.loop.loops.abandon import Abandon
from programm.loop.loops.categories import Categories
from programm.loop.loops.records import Records
from programm.loop.loops.products import Products
from programm.loop.loops.substitutes import Substitutes
from programm.loop.menu import Menu

class Engin:
    """Engin class.
    """
    def __init__(self):
        self.database = Database()
        self.tests = Tests()
        self.menu = Menu()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.records = Records()
        self.abandon = Abandon()

    def initialize_database(self):
        """Method that initialize the database. It checks if
        the DB exists and if its tables categories
        and products are populated.
        - If it does, the programm "datas" are strored into a list and the
        Menu programm is started.
        - If it don't, the database and its componnents are created.
        """
        if self.database.verify(self.database.exists()):
            self.database.execute_one(self.database.use())
            if self.database.verify(self.categories.exists()) and\
            self.database.verify(self.products.exists()):
                self.set_datas()
                self.start_loop()
            else:
                self.database.reset(self)
        else:
            self.database.reset(self)

    def set_datas(self):
        """Method that sets datas them into their
        respective list.
        """
        self.categories.set_categories_list(self.database)
        self.products.set_products_list(self.database)
        self.substitutes.set_substitutes_list(self.database)
        self.records.set_records_list(self)

    def start_loop(self):
        """Method that start the Menu loop(i.e. the main loop).
        """
        self.menu.start(self)
       