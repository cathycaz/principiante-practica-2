sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []   

for i in range(len(sample_list)-1,-1,-1):
    new_list.append(sample_list[i])
print(new_list)

"""TAMBIEN PUEDE SER...
for i in reversed(sample_list):
    new_list.append(i)  
print(new_list)"""
