
def reverse_lookup(d:dict, v):
    for key in d:
        if d[key] == v:
            return key
    raise LookupError()



d = {1:"Afton", 2:"Alliyah", 3:"Matt", 4:"Piotr"}
print(reverse_lookup(d, "Matt"))

