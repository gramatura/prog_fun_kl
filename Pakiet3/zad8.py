def partition (list,size):
    for i in range(0,len(list) // size):
        yield list[i :: size]

O_list=[1,2,3,4,5,6,7,8,9]
n=2
p_list= list(partition(O_list,n))

print(O_list)
print(p_list)