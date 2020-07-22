#-*-coding:utf-8 -*

from os import system

from database import Database
from substitute import Substitute
from tests import Tests
import menu

class Substitutes:
    def __init__(self, database, products):
        # system("cls")
        self.database = database
        self.products = products
        self.substitutes_proposed_list = []
        self.sorted_substitutes = []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
        self.selected_substitute = None
        self.register_input_valid = False
        self.registration = False
        self.substitutes_registered_list = []

    def create_table(self):
        statement = "CREATE TABLE IF NOT EXISTS substitute(\
            product_product_id SMALLINT UNSIGNED NOT NULL,\
            substitute_product_id SMALLINT UNSIGNED NOT NULL,\
            FOREIGN KEY (product_product_id) REFERENCES product(id_product),\
            FOREIGN KEY (substitute_product_id) REFERENCES product(id_product)\
            )ENGINE=INNODB;"
        return statement
  
    def instanciate(self):
        self.database.open_cursor()
        self.database.cursor.execute ("SELECT * FROM substitute")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            product_product_id= elt[0]
            substitute_product_id = elt[1]
            substitute = Substitute(product_product_id,\
            substitute_product_id)
            self.substitutes_registered_list.append(substitute)
        self.database.close_cursor()

    def nominal_scenario(self):
        self.find()
        self.organize()
        self.show()
        self.select()
        self.execute_selection()
        self.register()
        self.execute_registration()
        self.insert_substitute()

    def exception_scenario_one(self):
        self.show()
        self.select()
        self.execute_selection()
        self.register()
        self.execute_registration()
        self.insert_substitute()

    def exception_scenario_two(self):
        self.register()
        self.execute_registration()
        self.insert_substitute()

    def find(self):
        for elt in self.products.selected_products:
            if elt.id_product != self.products.selected_product.id_product and\
            elt.nutriscore_grade < self.products.selected_product.nutriscore_grade:
                self.substitutes_proposed_list.append(elt)

    def organize(self):
        if self.substitutes_proposed_list:
            self.sorted_substitutes = sorted(self.substitutes_proposed_list,\
            key = lambda product : product.nutriscore_grade)
        else:
            system("cls")
            print("There is no healthier substitute for that product")
            menu.Menu(self.database)     

    def show(self):
        print ("SUBSTITUTES:")
        rank = 1
        for elt in self.sorted_substitutes:
            elt.temp_substitute_rank = rank
            print (elt.temp_substitute_rank ," - ",elt.product_name,\
            " - ", elt.nutriscore_grade)
            rank += 1

    def select(self):
        self.question= input("Which substitute you want to choose?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute_selection(self):
        if self.select_input_valid:
            system("cls")
            self.question = int(self.question)
            if self.question <= len(self.substitutes_proposed_list):
                for elt in self.substitutes_proposed_list:
                    if elt.temp_substitute_rank == self.question:
                        print ("You\'ve choosen the following substitute:",\
                        "\n   - Product name:", elt.product_name,\
                        "\n   - Nutriscore value:", elt.nutriscore_grade,\
                        "\n   - Check product at:", elt.url,\
                        "\n   - Sold in:", elt.stores) 
                        self.selected_substitute = elt
            else:
                system("cls")
                print ("Only numbers included in above list can be used. Retry")
                self.exception_scenario_one()

        else:
            system("cls")
            print ("Only numbers can be used. Retry")
            self.exception_scenario_one()

    def register(self):
        self.question= input("Do you want to register that choice(y/n)?\n")
        self.tests.test_string(self.question)
        if self.tests.valid:
            self.register_input_valid = True

    def execute_registration(self):
        if self.register_input_valid:
            self.question = str(self.question)
            if self.question in "yY":
                self.registration = True
                print("Substitute product has been registered !") 
            elif self.question in "nN":
                menu.Menu(self.database) 
            else: 
                system("cls")
                print ("Only letter y/n can be used. Retry ")
                self.exception_scenario_two()
        else:
            system("cls")
            print ("Only letter y/n can be used. Retry ")
            self.exception_scenario_two()

    def insert_substitute(self):
        if self.registration:
            self.database.open_cursor()
            statement = "INSERT INTO substitute (product_product_id,\
            substitute_product_id) VALUES (%s, %s)"
            value = [self.products.selected_product.id_product,\
            self.selected_substitute.id_product]
            self.database.cursor.execute(statement, value)
            self.database.connection.commit()
            self.database.close_cursor()
            menu.Menu(self.database)





