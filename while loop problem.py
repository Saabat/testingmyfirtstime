#
# 01. Take 3 integers from keyboard using loop and print their average value on the screen.

number = int(input("Enter number: "))
i = 5
sum = 0
temp = 0

while i>0:
    sum = sum + number
    i = i - 1

    temp2 = temp + sum
    temp = sum
    print(temp2)
    # print(sum)

avg = temp2 / 5
print(avg)

# has not solved
