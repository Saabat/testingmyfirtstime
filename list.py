#List Making , Accessing List Element and Implement to make sentences
#
#
# temp = int(input('Enter your input: '))
# temp = input('Enter your input: ')
# temp_2 = ('ashiq', 'rahman')
# print(temp[-1])
# print(temp_2[0])
# print(len(temp))

# print(type(temp[0]))

######
# user_one = ['john doe', 26 , True, 'dhaka bd']
# print(type(user_one))    #it shows, it is a list
# print(user_one[0], user_one[4])  #shows error, cause user_one[4] does not exist.
# print(user_one[0])  # positive way index start from 0
# print(user_one[-1])  # negative way index start from -1

# partial_list = user_one [1:3]
# partial_list1 = user_one [1:]
# partial_list2 = user_one [ :-1]

# print(partial_list) # the result will show 1 & 2 no position
# print(partial_list1) # the result will show 1 to last no position
# print(partial_list2) # the result will show -2 to last no position

# john doe is a man of 26 years old. he lives in dhaka bd.

# name = user_one [0]
# age = user_one[1]
# is_male = user_one[2]
# living_place = user_one[3]
# if is_male:
#     pronoun = 'He'
#     gender = 'man'
# else:
#     pronoun = 'she'
#     gender = 'woman'
#
# sentence = f'{name} is a {gender} of {age} years old. {pronoun} lives in {living_place}.'
# print(sentence)

####### Change the Element of List ###

# movie = ['Avatar', 'inception', 'Terminal', 'Spider man']
# movie.append('din the day')   # din the day will be add th the end of list
# print(movie)
#
# # we can replace anything from list. Example
# movie[0] = 'kites'  # it will replace avatar by kites
# movie[-1] = 'gravity'  # it will replace last element of list
# print(movie)
# movie[1:3] = ['tum', 'bin']
# print(movie)
# movie[0:2] = ['Rain the barsha']
# print(movie)
# movie[:-1] = ['hello']
# print(movie)
# movie[0: ] = ['hi']
# print(movie)

#### Adding Element to the List###
# append. it will add element at the end of list. Example

# movie = []
# movie.append('Nayok the hero')   # it will add Nayok the hero
# print(movie)
# movie.append('priyotoma')   # it will add priyotoma after nayok the hero
# print(movie)
# movie.append('ami bongshi')   # it will add ami bongshi after priyotoma
# print(movie)

###another way of adding element is insert. example

# movie.insert(0, 'hehe')   #added hehe at 0 position
# print(movie)

### extend. it will add list to the end of list

# list1 = ['hello', 'python']
# list2 = ['learning', 'batch']
# list1.extend(list2)
# print(list1)
# list2.extend(list1)
# print(list2)

#### 35 Remove Eleement from list ##
##remove
# heroin = ['mousumi',
#           'shabnur',
#           'shabana',
#           'popi',
#           'purnima']
# heroin.remove('purnima')   #it will remove purnima from list
# print(heroin)
# heroin.remove('shabnur')
# print(heroin)

##pop
# heroin.pop()   #it will pop last of the element from list
# print(heroin)
# heroin.pop()   #it will pop last of the element from list
# print(heroin)

# heroin.pop(2)       # it will remove 2 no position shabana from list

# del heroin[1]    # it will delete 1 no position value
#
# heroin.clear()     # it will clear whole list
# print(heroin)


###### 36 List Sorting and Joining ####

word_list = ['i', 'love', 'you']

## we can join by adding
# print(f'{word_list[0]}, {word_list[1]}, {word_list[2]}')
# print(f'{word_list[0]} {word_list[1]} {word_list[2]}')
# print(f'{word_list[0]} {word_list[1]} {word_list[2]}')

# sentence = ' '.join(word_list)      #we can add by join command and use separator first
# print(sentence)
#
# sentence = '***'.join(word_list)
# print(sentence)

number = [21, 4, 5, 55, 67, 344, 122, 897]

## we can do sorting by command sort
number.sort()
print(number)
number.sort(reverse=True)
print(number)