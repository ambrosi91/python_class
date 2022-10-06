FRUIT_LIST_dict = {'FRUIT_LIST_1': ["apple", "pear", "banana"], 'FRUIT_LIST_2': ["mango", "melon", "cherry"], 'FRUIT_LIST_3': ["peach", "apricot", "kiwi"]}
search_value = str(input('What value are you looking for? '))
for key, value in FRUIT_LIST_dict.items():
  if search_value in value:
    print(f'Your search value of {search_value} was found in {key}')