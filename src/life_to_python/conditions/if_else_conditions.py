

a = 3
b = 5
c = "hello world"
print(type(c))


if a<b:
    print(f"{b} is greater than {a}")
    

input_first = input("enter a number: ")
input_second = input("enter another number: ")

if input_first > input_second:
    print(f"{input_first} is greater than {input_second}")
        
elif input_first < input_second:
    print(f"{input_second} is greater than {input_first}")

else:
    print("both numbers are equal")

