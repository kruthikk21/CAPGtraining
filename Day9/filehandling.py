file=open("file","w")
file.write("Hello World")
file.close()
file=open("jfile.txt","r")
#print(file.read())
file.close()
file=open("file.txt","w")
file.write("this is day 9 of python")
file.close
file=open("file.txt","r")
#print(file.read())
with open("file.txt","r") as file:
    for line in file:
        print(line.strip())