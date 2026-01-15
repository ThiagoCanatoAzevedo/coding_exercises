def get_dict_value(dct, path):
    keys = path.split(".")
    current = dct
    
    for k in keys:
        if not isinstance(current, dict) or k not in current:
            return None
        current = current[k]
    
    return current


dct = {"a": {"b": {"c": 42}}}
print(get_dict_value(dct, "a.b.c"))