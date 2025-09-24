names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1]= "Steven"
names[len(names)-1]= "Pepe" # tambien puede ser names[-1]="Pepe"
names[0]= names[2]+names[4]


for name in range(len(names)-1,-1,-1): # tambien puede ser for name in reversed(names): 
   print(names[name])

    

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.reverse() # tambien puede ser my_list = my_list[::-1]
print(my_list)