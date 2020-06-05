def increment_string(strng):
    if len(strng) == 0:
        return strng + '1'
    elif strng[-1].isdigit() == False:
        return strng + '1'
    if strng[-1] == 0:
        strng = strng[:-1] + '1'
        return strng

    for i in strng:
        if i.isdigit():
            if (i == '0') & (strng[-1] != '9'):
                continue
            else:
                num = int(strng[strng.index(i):]) + 1
                strng = strng[:strng.index(i)] + str(num)
            break
    return strng

##Test Cases##
print(increment_string("foo001"))
print(increment_string("foo0499"))
print(increment_string("foo023"))
print(increment_string(""))
print(increment_string("foobar099"))

#####

'''
Title: Duplicate Encoder
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
'''

def duplicate_encode(word):
    cache = {}
    new_word = ''
    word = word.lower()
    for i in word:
        if i in cache:
            if cache[i] != ')':
                cache[i] = ')'
                new_word = new_word[:word.index(i)] + ')' + new_word[word.index(i)+1:]
            new_word = new_word + ')'
        else:
            cache[i] = word.index(i)
            new_word = new_word + '('
    return new_word

print(duplicate_encode("recede"))
print(duplicate_encode("Success"))

'''
Optimal solution
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
'''
####


