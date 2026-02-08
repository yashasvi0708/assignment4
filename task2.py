filename = "output.txt"
input1=input("Enter text to write on the file")
with open(filename, "w") as f:
    f.write(input1+'\n')
    print("File written successfully")
input2=input("Enter text to append in the file")
with open(filename, "a") as f:
    f.write(input2+'\n')
    print("File written successfully")
    print("File written successfully")
print(f"Final content of the file {filename}:")
with open(filename, "r") as f:
    print(f.read())

