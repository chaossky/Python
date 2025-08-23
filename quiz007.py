try:    
    d = {"a": 1}    
    print(d["b"])
except KeyError:
    print("missing key")