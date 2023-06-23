words_list = ['каждый', 'фазан', 'желает']
my_text = 'каждый охотник желает знать где сидит фазан фазан каждый'
words_dict = dict()
for word in my_text.split(' '):
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for word in words_list:
    print(word, words_dict[word])
