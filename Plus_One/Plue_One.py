class Solution:
    def plusOne(self, digits):
        number_str = ''
        out_list = []
        for i in digits:
            number_str += str(i)
        to_add = str(int(number_str) + 1)
        for i in to_add:
            out_list.append(int(i))
        return out_list


# Driver Code

s = Solution()

print(s.plusOne([1,2,3]))
