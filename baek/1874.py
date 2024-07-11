n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        result.append('+')
        
    
    if num == stack[-1]:
        result.append('-')
        stack.pop()
    else:
        print('NO')
        exit(0)
    
print('\n'.join(result))