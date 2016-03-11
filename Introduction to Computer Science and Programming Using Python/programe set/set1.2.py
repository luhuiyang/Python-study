def checkbob(s):
    count = 0
    for i in range(len(s)):
        print s[i: i+3]
        if s[i] == 'b':
            if s[i:i+3]=='bob':
                count += 1
                
    return 'Number of times bob occurs is: ' + str(count)
    
print checkbob('azcbobobegghaklbob')