word = 'shacnidw'
left_part = ''
right_part = ''
count = 0
for letter in word:
    count += 1
    if count % 2 == 0:
        right_part = letter + right_part
    else:
        left_part += letter
print(left_part + right_part)
