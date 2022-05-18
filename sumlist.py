# Reversing a list using reverse()
def Reverse(lst):
    lst.reverse()
    return lst

# Take 2 lists as input 
input1 = [7, 1, 6]
input2 = [5, 9, 2]

# Reverse the lists taken as input
reverse1 = Reverse(input1)
reverse2 = Reverse(input2)

# Join all the elements in each reversed list into a string, then convert them to an int
num1 = int(''.join(str(e) for e in reverse1))
num2 = int(''.join(str(e) for e in reverse2))

# Add the 2 ints together, put them into a list, reverse the list
print(num1 + num2)
out = [int(a) for a in str(num1 + num2)]
Reverse(out)



