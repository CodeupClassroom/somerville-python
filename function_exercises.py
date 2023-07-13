def is_two(input):
    if input == 2 or input == '2':
        return True
    else:
        return False
    
def is_vowel(input):
    if input in ('aeiou'):
        return True
    else:
        return False

def is_consonant(input):
    if is_vowel(input):
        return False
    else:
        return True

def cap_first(input):
    count = 0
    new_string = ''
    for letter in input:
        #take the first letter and capitalize if consonant
        if count == 0 and is_consonant(letter):
            new_string +=letter.upper()
            count =+1
        else:
            new_string += letter
            count += 1
    return new_string

def calculate_tip(bill, percentage):
    return bill * percentage

def apply_discount(price, discount):
    return price - (price * discount)

def handle_commas(input):
    new_number = ''
    for number in input:
        if number != ',':
            new_number += number
    return new_number

def get_letter_grade(input):
    if input >= 88: 
        return 'A'    
    elif input >= 80:   
        return('B')   
    elif input >= 67:   
        return('C')  
    elif input >= 60: 
        return('D') 
    else:  
        return('F')
    
def remove_vowels(input):
    new_string = ''
    for letter in input:
        if letter not in ('aeiou'):
            new_string += letter
    return new_string

def normalize_name(input):
    output = ''
    for char in input:
        if char.isalnum() or char == ' ':
            output += char
    return output.strip().lower().replace(' ','_').replace('__','_')

def cumulative_sum(input):
    new_list = []
    count = 1
    for num in input: 
        list_sum = sum(input[:count])
        new_list.append(list_sum)
        count += 1
    return new_list