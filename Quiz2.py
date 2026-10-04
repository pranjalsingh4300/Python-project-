# for i in range(1,11):
#   print(i, i*2, i*3)


print('Welcome to the QUIZ Zone....\n')

print('Q1. WHat is the first alphabet of English? \na.B    b.Y\nc.A    d.E\n')
ans1 = input("enter your choice....")
print('Q2. Who is theNational Animal of INdia? \na.Bear    b.Giraffe  \nc.Lion    d.Tiger\n')
ans2 = input("enter your choice....")
print('Q3. Who is the National Bird of INdia? \na.Peacock    b.Nightingale   \nc.Hen        d.Crow\n')
ans3 = input("enter your choice....")
print('Q4. HOw many COntinents are there in world? \na.4    b.12   \nc.7    d.9\n')
ans4 = input("enter your choice....")

total = 0

if ans1 == 'c' or ans1 == 'C':
  total+= 5
if ans2 == 'd' or ans2 == 'D':
  total+= 5
if ans3 == 'A' or ans3 == 'a':
  total+= 5
if ans4 == 'c' or ans4 == 'C':
  total+= 5

print(total)

if total == 20:
  print('Congratulations... you have got 1st position')
elif total == 15:
  print('Congratulations... you have got 2nd position')
elif total == 10:
  print('you have successfully passed the quiz with average score of 10...')
else:
  print('Better Luck next time...')








