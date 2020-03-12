
def flatten(iterable):
    flatten_array = []
    for i in iterable:
        if isinstance(i,list) and i :
            flatten_array.extend(flatten(i))
        elif i == None:
            break  
        else:
            flatten_array.append(i)
 
    return flatten_array