# Write a Python script to check if a given key already exists in a dictionary.
d={1:100, 2:200, 3:300, 4:400, 5:500, 6:600}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(1)
is_key_present(8)