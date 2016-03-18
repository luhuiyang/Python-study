def function(L, F):
    for i in range(len(L)):
        L[i] = F(L[i])
        
f = [abs, int, str]
l = [-0.1, -1.2, 58978]

function(l, str)
print l