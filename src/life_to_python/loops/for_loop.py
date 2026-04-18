

table_of = int(input("table of :"))
table_range = int(input("till range : ")) + 1

for i in range(1,table_range):
    print(f"{table_of} x {i} = {table_of*i}")

## loop through a list

list_of_names = ["George","Christian","Marago","Mandla", "Maggi"]

for i in list_of_names:
    print(i)

## loop through characters
for character in list_of_names[0]:
    print(character)
    
text="something went wrong"

for i in text:
    print(i)
    

list_of_tupples =[(2,4),(4,4)]

for i in list_of_tupples:
    print(i[0])



