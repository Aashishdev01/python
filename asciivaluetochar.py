ltr = 't'
print(ord(ltr))

# chr() ascii value to char

num = 99
print(chr(num))


for i in range(65,91):
  print(chr(i),end=' ')

start_char = str(input('Enter char to Start .... '))
end_char = str(input('Enter char to end .... '))

start = ord(start_char)
end = ord(end_char)

for i in range(start,end+1):
  print(chr(i),end=' ')
