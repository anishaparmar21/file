# from os import close


file =open("people1-exercise.txt","r")
counter=0
content=file.read()
colist=content.split("\n")
for i in colist:
    counter+=1
print("the count of lines is:",counter)

