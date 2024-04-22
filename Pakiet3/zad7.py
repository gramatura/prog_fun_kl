def flatten_list(nested_list):
    flattened = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened.extend(flatten_list(sublist))
        else:
            flattened.append(sublist)
    return flattened

nested_list=[[1,2,3],[4,5,6],[7,8,9]]

print (flatten_list(nested_list))