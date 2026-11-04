import json

from SaleApp.models import Category, Product


def load_categories():
    return Category.query

def load_products(q=None, cate_id=None):
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.cate_id.__eq__(int(cate_id)))

    return query

def get_product_by_id(id):
    return Product.query.get(id)

if __name__=="__main__":
    print(load_categories())