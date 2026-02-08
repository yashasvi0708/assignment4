filename= "sample.txt"
try:
    with open(filename, "r") as f:
        print("reading file content")
        print(f.read())
except FileNotFoundError:
    print("file not found")


