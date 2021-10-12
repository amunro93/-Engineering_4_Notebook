#Python Program 03

#Angus Munro

#09/28/21

sentence= input("Type text, then press Enter: ")

words = sentence.split()
#splits the words in the sentence



animals = ["lion","starfish","eagle"]
for x in words:
    for n in x:
        print(n)
    print("-")
