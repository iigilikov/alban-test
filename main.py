import csv
points = 0
print("Добро пожаловать! На вопросы отвечайте строго как в вариантах ответа, то есть а) или b)")
user = input("вы готовы к тесту?")

def start():
  with open("1.csv", "r", newline="") as file:
      read = csv.reader(file)
      for row in read:
        print(row[0])
        print(row[1], row[2], row[3])
        i = input("")
        if i == row[4]:
          bal += 5
          print("true")
        elif i != row[4]:
          print("false")
  print("Вы набрали " + str(bal) + " баллов")
  if bal <= 60:
      print("Ваша оценка F")
  elif bal <= 65:
      print("Ваша оценка D")
  elif bal <= 70:
      print("Ваша оценка D+")
  elif bal <= 75:
      print("Ваша оценка C-")
  elif bal <= 80:
      print("Ваша оценка C")
  elif bal <= 85:
      print("Ваша оценка B-")
  elif bal <= 90:
      print("Ваша оценка B")
  elif bal <= 95:
      print("Ваша оценка A-")
  elif bal <= 100:
    print("Ваша оценка A")

if user == "да":
  start()
else:
  user = input("Напишите когда будете готовы!(да): ")
  if user == 'да':
    start()   
 
    

