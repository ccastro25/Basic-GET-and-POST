import pickle
from insert_data_to_mysql import insert_data
from scrape_cvs_products import get_cvs_products
from scrape_acme_products import get_acme_products
from scrape_rite_aid import get_riteaid_products
from scrape_shoprite_products import get_shoprite_products
from scrape_walmart_products import get_walmart_products


stores_info = {'acmeproducts.pickle':get_cvs_products(),'cvsproducts.pickle':get_acme_products()
        ,'riteaidproducts.pickle':get_riteaid_products(),'shopriteproducts.pickle':get_shoprite_products()
        ,'walmartproducts.pickle':get_walmart_products()}


def pickle_dumps():
    for filename , products in enumerate(stores_info):
        with open(f'../pickles/{file}','wb') as f:
            pickle.dump(products,f)

def load_pickled_to_db():
    for file in files:
        print(file)
        with open(f'../pickles/{file}','rb') as f:
            data = pickle.load(f)
            insert_data(data,file)

pickle_dumps()
load_pickled_to_db()