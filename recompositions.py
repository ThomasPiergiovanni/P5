#-*-coding:utf-8 -*

import recomposition

class Recompositions:
    def __init__(self):
        self.recompositions_list=[]

    def recompose(self,substitutes_instance, categories_instance, products_instance):
        for substitute in substitutes_instance.substitutes_registered_list:
            recomposed_object = {}

            product  = [(product.id_product, product.product_name,\
            product.nutriscore_grade, product.url, product.stores, product.category_id)\
            for product in\
            products_instance.products_list if product.id_product ==\
            substitute.product_product_id]

            substitute = [(product.id_product, product.product_name,\
            product.nutriscore_grade, product.url, product.stores) for product in\
            products_instance.products_list if product.id_product ==\
            substitute.substitute_product_id]

            category = [category.name for category in\
            categories_instance.categories_list if category.id_category ==\
            product[0][5]]


            recomposition_instance = recomposition.Recomposition(\
            product[0][0],\
            product[0][1],\
            product[0][2],\
            product[0][3],\
            product[0][4],\
            product[0][5],\
            category[0],\
            substitute[0][0],\
            substitute[0][1],\
            substitute[0][2],\
            substitute[0][3],\
            substitute[0][4])

            self.recompositions_list.append(recomposition_instance)

        for elt in self.recompositions_list:
            print(elt.product_product_name, "-", elt.substitute_product_name, "-", elt.category_name)

            


            # for product in products_instance.products_list:


            #     if product.id_product == substitute.product_product_id:
            #         recomposed_object["product_product_id"] = product.id_product
            #         recomposed_object["product_product_name"] = product.product_name
            #         recomposed_object["product_nutriscore_grade"] = product.nutriscore_grade
            #         recomposed_object["product_url"] = product.url
            #         recomposed_object["product_stores"] = product.stores
            #         # print ("initial :", recompose_product_name)

            #     elif product.id_product == substitute.substitute_product_id:
            #         recomposed_object["substitute_product_id"] = product.id_product
            #         recomposed_object["substitute_product_name"] = product.product_name
            #         recomposed_object["substitute_nutriscore_grade"] = product.nutriscore_grade
            #         recomposed_object["substitute_url"] = product.url
            #         recomposed_object["substitute_stores"] = product.stores  
            #         # print ("substitute :", recompose_product_name)

            # for key, value in recomposed_object.items():
            #     product_category_id = 
            #     if key == "initial_name":
            #         print ("initial_name: ", value,)
            #     elif key == "substitute_name":
            #         print ("substitute_name: ", value)