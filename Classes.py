class Owner:

    def __init__(self, name):
        self.name = name



class Dog:

    def __init__(self, owner: Owner):
        self.num_barks = 0
        self.owner = owner

    def make_sound(self):
        print("woof")
        self.num_barks += 1


dog = Dog(owner=Owner(name="Johan"))
dog2 = Dog(owner=Owner(name="Joacim"))

for i in range(1000):
    dog.make_sound()
    if i == 500:
        dog2.make_sound()


print("The dog woofed", dog.num_barks, "times, and the owner is", dog.owner.name)

# F-string, typ string interpolation
message = f"The dog2 woofed {dog2.num_barks} times and the owner is {dog2.owner.name}"
print(message)


#Old ways
file = open("saved_data.txt", "a+")
file.writelines(message)
file.close()

file = open("saved_data.txt", "r")
loaded_message = file.read()
file.close()

print(loaded_message)

#New ways
with open("saved_data.txt", "w+") as f:
    f.write(message)