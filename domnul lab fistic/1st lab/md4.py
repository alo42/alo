vars = ['x', 'y', 'z', 'k']  
expr = input("Enter the expression: ").replace("!", "not").replace("+", "or").replace("*", "and")


n = len(vars)
for i in range(2 ** n):
    
    values = [int((i // (2 ** j)) % 2) for j in range(n)]
    env = dict(zip(vars, values))
    
    result = eval(expr, {}, env)
    
    print(" | ".join(map(str, values)) + " | " + str(result))
