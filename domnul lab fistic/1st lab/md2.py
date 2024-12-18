a = int(input("first (0 or 1): "))
b = int(input("second (0 or 1): "))

result = not (a or b) or (a and b)

print(f"result: {int(result)}")  
