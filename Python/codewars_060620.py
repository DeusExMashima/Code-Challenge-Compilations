'''
Unique in Order
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.
'''

def unique_in_order(iterable):
    new_iterable = []
    current = None
    for i in iterable:
        if i != current:
            current = i
            new_iterable.append(i)
    return new_iterable

#test cases#
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))
print(unique_in_order(''))

###

'''
Highest Scoring Word
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet:
a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
'''

def high(x):
    best_word = ''
    best_score = 0
    word_score = 0
    print(ord(x[0]))
    for i in x:
        if i == ' ':
            if word_score > best_score:
                best_score = word_score
                best_word = x[:x.index(i)]
            word_score = 0
            x = x[x.index(i)+1: ]
        else:
            word_score = word_score + (ord(i) - 96)

    print(word_score, x)
    print(best_score, best_word)
    if word_score > best_score:
        return x
    return best_word


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))

'''
Break camelCase
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

Complete the solution so that the function will break up camel casing,
using a space between words.

OPTIMAL SOLUTION
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

'''

def solution(s):
    new_word = ''
    
    for i in s:
        if i.isupper() and (s.index(i) != 0):
            new_word += ' '
            
        new_word += i

    return new_word

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))

'''
Array.,diff
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
'''


def array_diff(a,b):
    return [i for i in a if i not in b]

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))

'''

'''


def order_weight(strng):
    cache = {}
    array = strng.split(' ')
    for i in array:
        the_sum = 0
        
    new_cache = sorted(cache)

    new_list = ''
    for i in cache:
        new_list += cache[i]
    return new_list
    

print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
