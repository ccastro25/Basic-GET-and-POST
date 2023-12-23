import pickle
from insert_data_to_mysql import insert_data
from scrape_cvs_products import get_cvs_products
from scrape_acme_products import get_acme_products
from scrape_rite_aid import get_riteaid_products
from scrape_shoprite_products import get_shoprite_products
from scrape_walmart_products import get_walmart_products


stores_info2 = {'cvsproducts.pickle':get_cvs_products,'acmeproducts.pickle':get_acme_products
        ,'riteaidproducts.pickle':get_riteaid_products,'shopriteproducts.pickle':get_shoprite_products
        ,'walmartproducts.pickle':get_walmart_products}
        
stores_info = {
        'walmartproducts.pickle':get_walmart_products}

def pickle_dumps():
    for filename , func in stores_info.items():
        with open(f'../pickles/{filename}','wb') as f:
            pickle.dump(func(),f)
            print("created: " , filename)

def load_pickled_to_db():
    for file in stores_info:
        print(file)
        with open(f'../pickles/{file}','rb') as f:
            data = pickle.load(f)
            insert_data(data,file.split('.')[0])

pickle_dumps()
load_pickled_to_db()