from mysql_connection import get_connection



cnx = get_connection()




def insert_doc(doc):
    keys = doc.keys()
    columns = ", ".join(keys)
    placeholders = ", ".join(["%s"] * len(keys))
    values = [tuple(item[k] for k in keys) for item in doc]
    if 'customer' in values:
        table_name = 'customers'
    else:
        table_name = 'orders'
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor = cnx.exeute(query, values)
    cursor.commit()
    cnx.close()


