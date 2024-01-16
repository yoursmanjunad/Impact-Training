# Creating dictionary.
example = {'Name': 'Manjunath', 'RollNo': 54, 'Field':'DevOps'}
example2 = {'Name': 'Hussain', 'RollNo':56, 'Field':'Xerox' }
# print('Name',example['Name'])
example.update(example2)
merged_dict = dict(example,**example2)
print(merged_dict.pop('RollNo'))
print(merged_dict)
my_dict = {'banana': 3, 'apple': 1, 'orange': 2}

# Sort the dictionary by keys and print the result
# sorted_dict_by_keys = dict(sorted(my_dict.items()))
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Keys:",sorted_dict_by_values)

