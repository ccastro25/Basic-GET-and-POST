from insert_data_to_mysql import insert_data
from grocery_list import grocery_list
import pickle
import time

def get_save_items(store_product,get_product):

    products = []
    for item in grocery_list:
        print(f"current item: {item}")
        products.extend( get_product(item))
        print("starting")
        time.sleep(20)
        print("waiting 1 ") 
        time.sleep(20)
        print("waiting 2")
        time.sleep(20)
        print("waiting 3")
        time.sleep(20)
        print("done")
    

    with open(f'{store_product}.pickle','wb') as f:
        pickle.dump(final_list,f) 
    insert_data(final_list,store_product)

    
   
 