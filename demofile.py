#f = open("demo.txt")
#f = open("demo.txt", "rt")

#f = open("demo.txt", "r")
#print(f.read())

f = open("demo2.txt", "a")
f.write("Now the file has more content!\n")
f.write("Pranay\n")
f.write("nishchay\n")
f.close()

f = open("demo2.txt", "r")
print(f.read())