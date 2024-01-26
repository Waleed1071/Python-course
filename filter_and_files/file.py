file = open("output.txt", "w")

# Write the text into the file
file.write("Hello, world!")

# Close the file
file.close()

read = open("readOnly.txt","r")

test=read.readlines()
for x in test:
    print(x)