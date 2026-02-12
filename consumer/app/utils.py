def make_doc_to_row(doc):
    keys = doc.keys()
    columns = ", ".join(keys)
    placeholders = ", ".join(["%s"] * len(keys))
    values = tuple(k[v] for k, v in doc.items())
    return columns, values, placeholders