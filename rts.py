#Author - Rishabh Ostawal
#RTS lab coding test

print("Which question do you want to test?")
print("1. Print the number of elements in an array grater than or less than the input")
print("2. Rotate the charachters in a given input")

which_one = input("Input the number\n")
which_one = int(which_one)

if which_one == 1:

    arr = []

    n = int(input("Enter number of elements : "))

    for i in range(0, n):
        num = int(input())
  
        arr.append(num)
      
    check_input = int(input("Enter the input number you want to compare the arrays number with : "))

    greater = 0
    lesser = 0
    eqs = 0

    for nums in arr:
        if nums > check_input:
            greater += 1
        elif nums < check_input:
            lesser += 1 
        else:
            eqs += 1
    print("There are", greater, "numbers in the array above", check_input)
    print("There are", lesser, "numbers in the array below", check_input)

elif which_one == 2:
    stri = input("Enter the string : ")
    rot = int(input("Enter the number of letters to perform rotation with : "))
    len_of_string = len(stri)
    print(stri[len_of_string - rot: len_of_string] + stri[0:len_of_string - rot])


'''
Question 3 : One thing that I can change in my languge and framework?
Solution : There's a lot I can talk on this topic. But since, I used Python for this exercise, I would like to talk about it. Although, my favorite language
is C, I use python alot. Python is trivial and quick. It has many pros. But I miss pointers a lot. I feel like pointers give me more control of a program and
therefore they make my life easier. If I could change one thing about Python, that would be adding pointers functionality to it.
(I get that there are some languages like golang that is trivial and also uses python, but they have limited applications compared to python)


'''