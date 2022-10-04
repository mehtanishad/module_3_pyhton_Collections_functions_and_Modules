# Write a Python program to check multiple keys exists in a dictionary.
student = {
  'name': 'nishad',
  'class': '10',
  'roll_id': '3'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'nishad'})
print(student.keys() >= {'roll_id', 'name'})