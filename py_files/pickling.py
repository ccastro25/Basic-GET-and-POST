import pickle
from insert_data_to_mysql import insert_data

files = ['acmeproducts','cvsproducts','riteaidproducts','shopriteproducts','walmartproducts']

def pickle_dumps(filename,products):
    with open(filename,'wb') as f:
        pickle.dump(products,f)

def load_pickled_to_db():
    for file in files:
        print(file)
        with open(f'../pickles/{file}.pickle','rb') as f:
            data = pickle.load(f)
            insert_data(data,file)

load_pickled_to_db()