chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    merge=[]
    for i in chunk_one:
        merge.append(i)
    for j in chunk_two:
        merge.append(j)
    print(merge) 

merge_list(chunk_one, chunk_two)
