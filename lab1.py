s = input('input the string to execute: ')
result = ''
for i in s[::-1].lower():
    result += str(ord(i) - ord('a') + 1) + ' '
print(result)