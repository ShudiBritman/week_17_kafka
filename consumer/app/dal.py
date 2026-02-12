from mysql_connection import DBConnection
from utils import make_doc_to_row



cnx = DBConnection().get_connection()




def insert_doc(docs):
    order_values = []
    customer_values = []
    for doc in docs:
        if doc['type'] == "orders":
            result = make_doc_to_row(doc)
            orders_columns_keys = result[0]
            order_values.append(result[1])
            orders_placeholders = ", ".join(["%s"] * len(result[2]))
        else:
            result = make_doc_to_row(doc)
            customers_columns_keys = result[0]
            customer_values.append(result[1])
            customer_placeholders = ", ".join(["%s"] * len(result[2]))
    query = f"INSERT INTO customers ({customers_columns_keys}) VALUES ({customer_placeholders})"
    cursor = cnx.exeutemany(query, customer_values)
    query = f"INSERT INTO orders ({orders_columns_keys}) VALUES ({orders_placeholders})"
    cursor = cnx.exeutemany(query, order_values)
    cursor.commit()
    cnx.close()


