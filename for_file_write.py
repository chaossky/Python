with open('teletoby.txt','w') as file:
    for i in range(5):
        file.write("Hello, dear {0}\n".format(i))