
# number = int(input('Enter number: '))
# i = 1
#
# while i <= 10:
#     number2 = number * i
#     print(number2)
#     i = i + 1

# age = int(input('Enter age: '))
#
# while age<=100:
#     print('your age is: ', age)
#     age = age + 1
# else:
#     print('you are expired')

##another example

# singer = ['Ayub bacchu', 'games', 'hasan', 'nandita']
# i = 0

# while i < len(singer):
#     print(singer[i])
#     i = i + 1

## anpther example of while loop

years = [1988, 3422, 1922, 1944]
i = 0
while i<len(years):
    if years[i] % 4 == 0:
        print(years[i], 'is a leap year')
    else:
        print(years[i], 'is not leap year')
    i = i + 1