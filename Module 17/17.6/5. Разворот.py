
example_string = 'thqwehrty'
cut_line = example_string[example_string.index('h') + 1::]
full_line = cut_line[:cut_line.index('h'):]
print(cut_line)
for i in (reversed(full_line)):
    print(i, end='')