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
