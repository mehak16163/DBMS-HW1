file_name = input("Enter file name ")
table = open(file_name,"r",1)
print("Name of the file: ", table.name)
File_content = table.readlines()
length = len(File_content)
i=0;
while i<length:
    print(File_content[i])
    i=i+1
table.close()
