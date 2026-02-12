from mysql_connection import get_connection



cnx = get_connection()




def insert_doc(docs):
    keys = docs[0].keys()
    columns = ", ".join(keys)
    placeholders = ", ".join(["%s"] * len(keys))
    values = [tuple(item[k] for k in keys) for item in docs]
    customers_values = []
    orders_values = []
    for row in values:
        if 'customer' in row:
            customers_values.append(row)
        else:
            orders_values.append(row)
    query = f"INSERT INTO customers ({columns}) VALUES ({placeholders})"
    cursor = cnx.exeutemany(query, values)
    query = f"INSERT INTO orders ({columns}) VALUES ({placeholders})"
    cursor.commit()
    cnx.close()


