nums = [2,7,11,15]

# This is Working Branch


target = 9

Output_List = []

a = 0

for i in range(len(nums)):
    value = nums[i]
    for j in range(len(nums)):
        if i != j:
            value += nums[j]
            if value == target:
                Output_List.append(i)
                Output_List.append(j)
                a = 1
                break
    if a == 1:
        break

print(Output_List)

print('Hello World')