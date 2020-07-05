#-*-coding:utf-8 -*

import database
import categories
import products


database_instance = database.Database()
database.Database.create(database_instance) 

categories_instance = categories.Categories()
categories.Categories.get_data(categories_instance)
categories.Categories.insert(categories_instance, database_instance)
categories.Categories.instanciate_category(categories_instance, database_instance)

# products_instance = products.Products()
# products.Products.get_data(products_instance, category_instance)
# products.Products.test(products_instance)



#products.Product.initialize(database_instance.selected_categories)
