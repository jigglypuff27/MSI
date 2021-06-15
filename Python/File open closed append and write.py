
f= open("textfile.txt","w+")         #textfile is the name of the file , w is the file mode , + sign indicate create a new file if it doesn't exist
for i in range(10):
    f.write("line number is written " + str(i) +"\r\n")     #writes in file
f.close()



f =open("textfile.txt","a")    #append mode
if f.mode == "a" :
    for i in range(11,15):
        f.write("new added line numbers are "+str(i)+"\r\n")
    f.close()

f = open("textfile.txt","r")
#contents=f.read()         #read functions to read
#print(contents)
content_in_lines=f.readlines()         #realines function to read
for i in content_in_lines:
    print(i)
f.close()