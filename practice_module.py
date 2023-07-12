def is_vowel(input):
    if input in ('aeiou'):
        return True
    else:
        return False
    
def is_two(input):
    if input == 2 or input == '2':
        return True
    else:
        return False
    
def is_consonant(input):
    if is_vowel(input):
        return False
    else:
        return True
    
name = 'Nikki'