#File I/O in Python
#Python can be used to perform operations on a file. (read & write data)

#Types of all files-
#1. Text Files: .txt, .docx, .log etc.
#2. Binary Files: .mp4, .mov, .png, .jpeg etc.

#We have to open a file before reading or writing.
# f= open("file_name", "mode")

f = open("demo.txt", "a")
#to read 
#line1 = f.read()
#print(line1)

#to write
f.write("Then I'll move to ReactJS")

f.close()