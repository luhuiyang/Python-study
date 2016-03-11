# -*- coding: utf-8 -*-
def countVowels(s):
    count = 0
    for i in s:
        if i in 'aeiou':
         count += 1
    return 'Number of vowels: ' + str(count)
    
print countVowels('azcbobobegghakl')