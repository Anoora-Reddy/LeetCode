s = "MCMXCIV"
value = 0
i = 0
while i < len(s):
    
    if s[i:i+2] == 'IV':
        print(s[i:i+2])
        value += 4
        i += 2
    elif s[i:i+2] == 'IX':
        value += 9
        i += 2
    elif s[i:i+2] == 'XL':
        value += 40
        i += 2
    elif s[i:i+2] == 'XC':
        value += 90
        i += 2
    elif s[i:i+2] == 'CD':
        value += 400
        i += 2
    elif s[i:i+2] == 'CM':
        value += 900
        i += 2        
    elif s[i] == 'I':
        value += 1
        i += 1
    elif s[i] == 'V':
        value += 5
        i += 1
    elif s[i] == 'X':
        value += 10
        i += 1
    elif s[i] == 'L':
        value += 50
        i += 1
    elif s[i] == 'C':
        value += 100
        i += 1
    elif s[i] == 'D':
        value += 500
        i += 1
    elif s[i] == 'M':
        value += 1000
        i += 1
print(value)
