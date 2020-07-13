#-*-coding:utf-8 -*

import substitute
import database
import research
import menu

class Substitutes:
    def __init__(self):
        self.substitutes_proposed_list=[]
        self.substitutes_proposed_with_rank=[]
        self.selected_substitute = 0
        self.registration = False
        self.substitutes_registered_list=[]

    def instanciate_substitute(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM p5.substitute")
        selection = database_instance.cursor.fetchall()
        for elt in selection:
            product_product_id= elt[0]
            substitute_product_id = elt[1]
            substitute_instance = substitute.Substitute(product_product_id,\
            substitute_product_id)
            self.substitutes_registered_list.append(substitute_instance)


    def filter(self, products_instance):
        selected_product_nutriscore = [elt.nutriscore_grade for elt in\
        products_instance.selected_products if elt.id_product ==\
        products_instance.selected_product]
        selected_product_nutriscore = selected_product_nutriscore [0]
        for elt in products_instance.selected_products:
            if elt.id_product != products_instance.selected_product and\
            elt.nutriscore_grade < selected_product_nutriscore:
                self.substitutes_proposed_list.append(elt)

    def show(self):
        if self.substitutes_proposed_list:
            print ("SUBSTITUTES:")
            sorted_substitutes = sorted(self.substitutes_proposed_list, key = lambda \
            product : product.nutriscore_grade)
            rank = 1
            for elt in sorted_substitutes:
                print (rank ," - ",elt.product_name, " - ", elt.nutriscore_grade)
                substitutes_proposed_with_rank=(elt.id_product,\
                elt.product_name, elt.nutriscore_grade, rank)
                self.substitutes_proposed_with_rank.append(substitutes_proposed_with_rank)
                rank += 1
        else: 
            print("There is no healthier substitute for that product")
            database_instance= database.Database()
            menu.Menu.show(database_instance)

    def select(self):
        question= input("Which substitute you want to choose ?")
        try:
            question = int(question)
            if question <= len(self.substitutes_proposed_with_rank):
                for elt in self.substitutes_proposed_with_rank:
                    if elt[3] == question:
                        print ("You\'ve choosen the ", elt[1], "product as a substitute") 
                        self.selected_substitute = elt[0]
            else:
                print ("Only numbers included in above list can be used. Retry ")
                Substitutes.select(self)
        except:
            print ("Only numbers can be used. Retry ")
            Substitutes.select(self)

    def register(self):
        question= input("Do you want to register that choice (y/n)?")
        question = str(question)
        if question in "yY":
            self.registration = True
            print("Substitute product has been registered !") 
        elif question in "nN":
            database_instance= database.Database()
            menu.Menu.show(database_instance)
        else:
            print ("Only letter y/n can be used. Retry ")
            Substitutes.register(self)



