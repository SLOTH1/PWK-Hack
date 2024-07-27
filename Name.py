import os
if os.path.exists("school.txt"):
  os.remove("school.txt")
else:
  print("รันไฟล์Run.pyต่อ") 
print("รันไฟล์Run.pyต่อ")

shido = range(803000, 804000)
for n in shido:
  pok = n
  book = (f"jk" + str(pok) + ".jpg")
  with open("school.txt", "a") as f:
    f.write(book + "\n") 
