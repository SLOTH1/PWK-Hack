import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("รันไฟล์Run.pyต่อ") 

shido = range(721000, 722000)
for n in shido:
  pok = n
  book = (f"jk" + str(pok) + ".jpg")
  with open("school.txt", "a") as f:
    f.write(book + "\n") 
