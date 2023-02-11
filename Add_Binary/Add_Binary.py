class Solution:
    def addBinary(self, a: str, b: str) -> str: # Easy to implement
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        out = ''
        carry = 0
        while max_len > 0:
            if int(a[max_len - 1]) + int(b[max_len - 1]) + carry == 1:
                out =  '1' + out
                carry = 0
            elif int(a[max_len - 1]) + int(b[max_len - 1]) + carry < 1:
                out =  '0' + out
                carry = 0
            elif int(a[max_len - 1]) + int(b[max_len - 1]) + carry == 3:
                out = '1' + out
                carry = 1
            elif int(a[max_len - 1]) + int(b[max_len - 1]) + carry > 1:
                out = '0' + out
                carry = 1
            max_len -= 1
        if carry == 1:
            out =  '1' + out
        
        return out


    def addBinary_Solution2(self, a: str, b: str) -> str:  # Faster way to implement
        i = len(a) - 1
        j = len(b) - 1
        out = ''
        carry = 0
        while i > -1 and j > -1:
            if int(a[i]) + int(b[j]) + carry == 1:
                out =  '1' + out
                carry = 0
            elif int(a[i]) + int(b[j]) + carry < 1:
                out =  '0' + out
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 3:
                out = '1' + out
                carry = 1
            elif int(a[i]) + int(b[j]) + carry > 1:
                out = '0' + out
                carry = 1
            i -= 1
            j -= 1
        while i > -1 :
            if int(a[i]) + carry < 1:
                out =  '0' + out
                carry = 0
            elif int(a[i]) + carry == 1:
                out =  '1' + out
                carry = 0
            elif int(a[i]) + carry > 1:
                out = '0' + out
                carry = 1
            i -= 1
        while j > -1 :
            if int(b[j]) + carry < 1:
                out =  '0' + out
                carry = 0
            elif int(b[j]) + carry == 1:
                out =  '1' + out
                carry = 0
            elif int(b[j]) + carry > 1:
                out = '0' + out
                carry = 1
            j -= 1
        if carry == 1:
            out =  '1' + out
        
        return out


# Driver Code

s = Solution()

a = input()
b = input()

print(s.addBinary(a, b))