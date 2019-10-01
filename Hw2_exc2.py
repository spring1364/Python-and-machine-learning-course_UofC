people_list = []

while True:
  data = input("Enter name, age, height, type 'q' to quit: ")
  if data == 'q':
    break
  people_list.append(tuple(data.split(',')))

people_list.sort(key=lambda x: (x[0], x[1], x[2]))
print(people_list)