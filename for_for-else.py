word = 'emango'

# 'e' 있으면 1을 출력
# 'e' 없으면 0을 출력

is_end = False 
for char in word:
    if char == 'e':
        is_end = True
        break
    
if is_end:
    print(1)
else:
    print(0)

print('=======================')

for char in word:
    if char == 'e':
        print(1)
        break
    print(0)
    
