def say_hello_for(name: str, times: int):
    for i in range(times, 0, -2):
        print(i, name)

say_hello_for("Johan", 8)


def say_hello_while(name: str, times: int):
    i = 0
    while i < times:
        print(i, name)
        if i == 5:
            break
        elif i == 4:
            name = "johan"
        else:
            name = "Billie"
        i+=1

say_hello_while("Joakim", 10)