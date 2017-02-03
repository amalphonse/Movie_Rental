with open('test_file.txt','w') as fle:
    fle.write("Hello World!! from Anju Mercian...")

#to read from file
with open("test_file.txt",'r') as f:
    print(f.readline())