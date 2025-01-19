from database.db import get_connection
from .entities.Product import Product


class ProductModel():

    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, title, price, description, category, images FROM products")
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(
                        row[0], row[1], row[2], row[3], row[4], row[5])
                    products.append(product.to_JSON())

            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_product(self, id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM products WHERE id = %s", (id,))
                row = cursor.fetchone()
                single_product = None
                if row is not None:
                    single_product = Product(
                            row[0], row[1], row[2], row[3], row[4], row[5])
                 

            connection.close()
            if single_product is not None:
                return single_product.to_JSON()
            else: return single_product
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def create_product(self, product):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (title, price, description, category, images) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                    (product['title'], product['price'], product['description'], product['categoryId'], product['images'])
                )
                new_product_id = cursor.fetchone()[0]
                connection.commit()
                
            connection.close()
            return new_product_id
        except Exception as ex:
            raise Exception(ex)