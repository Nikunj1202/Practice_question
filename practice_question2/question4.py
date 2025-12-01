# Merge two dictionaries.
di1 = {
    "name" : "nikunj",
    "age" : 20,
    "hobby" : {"python","treding"}
    }
di2 = {
    "city" : "baroda",
    "natue" : "calm"
}

di3 = di1 | di2
print(di3)