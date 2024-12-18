nums = list( input("enter: ").split())

result = [[]]  
for num in nums:
    result += [curr + [num] for curr in result]  

print(result)  
