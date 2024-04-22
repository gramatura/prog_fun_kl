def remove_duplicates(duplikaty):
    seen = set()
    result = []
    for item in duplikaty:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

duplikaty = [1,1,2,2,"nwm","nwm"]

print (remove_duplicates(duplikaty))