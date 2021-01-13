
import string
import random as r


"""
print(string.punctuation)

special = r.choice(string.punctuation)
number = random.randrange(0, 100)

print('%s' % special)

print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.ascii_lowercase)

"""


def shuffle_string(var_string):
    length = len(var_string)
    new_string = ''.join(r.sample(var_string, length))
    return new_string
    #print('%s' % (new_string))

def shuffle_and_print_string(var_string):
    length = len(var_string)
    new_string = ''.join(r.sample(var_string, length))
    #return new_string
    print('%s' % (new_string))

def create_random(i, end, pass_1):

    i=0
    while (i < end):


        random_list = [r.choice(string.punctuation), r.choice(string.ascii_lowercase)]
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        upp_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        punc = '!#$%&()*+,-/:;<=>?@[\]^_{}~.'
        numbers = '0123456789abcdef'

        list(lower_letters)
        list(upp_letters)
        list(punc)
        list(numbers)

        if i == 0:
            my_word = r.choice(punc)
        elif i == 1:
            my_word = r.choice(lower_letters)
        elif i == 2:
            my_word = r.choice(numbers)
        elif i == 3:
            my_word = r.choice(upp_letters)
        elif i == 4:
            my_word = r.choice(numbers)
        elif i == 5:
            my_word = r.choice(lower_letters)
        else:
            my_word = r.choice(random_list)
            
        
        
        
        list(my_word)
        list(pass_1)
        pass_1.append(my_word)

        i += 1


print('Welcome to password creator')
print('')
print('*******************************************************************************')
print('*******************************************************************************')
print('*******************************************************************************')

print('')
print('')



sp_1 = r.choice(string.ascii_uppercase)

pass_1 = [sp_1]
#print('%s' % password)




print('')


create_random(0,20, pass_1)

new_string = ''.join(pass_1)
shuffle_string(new_string)


print("")
print('Here is your password: %s' % new_string)
print('')
print('')


shuffle_or_not = input("Do you want shuffle it? yes or no: ")
print('***********************************************')
print('')
print('')

while shuffle_or_not != 'no':
    
    if shuffle_or_not == 'yes':
        my_new = shuffle_string(new_string)
        print('Here is your password: %s' % my_new)
        print('***********************************************')
    
        print('')
        print('')

    shuffle_or_not = input("Do you want shuffle it ?: Yes or No: ")

print('')
print('')

print('***********************************************')
print("")
   

    
    


    

print('')
print('')












