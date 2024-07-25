shido = range(721000, 722000)
for n in shido:
  pok = n
  book = (f"jk" + str(pok) + ".jpg")
  with open("school.txt", "a") as f:
    f.write(book + "\n") 
