from typing import Dict, List

#List


names: list[str] = ["johan", "Joakim", "Billie"]


greetings = ["Hello", "Welcome", "What's up"]

for i in range(len(names)):
    print(names[i])

for name in names:
    for greeting in greetings:
        print(greeting, name)

for name, greeting in zip(names, greetings):
    print(greeting, name)


#Dictionary
person_data: Dict[str, int] = {"Johan": [33, 34], "Joakim": 32, "Billie": '7 mån'}

for age in person_data["Johan"]:
    print(age)


advanced_person_date = {
    "Johan": {
        "Age": 33,
        "Address": "Österbo 105, 791 92 Falun",
        "Children": ["billie"]
    },
    "Joakim": {
            "Age": 32,
            "Address": "Stockholm",
            "Children": []
    }
}

if len(advanced_person_date["Joakim"]["Children"]) == 0:
    advanced_person_date["Joakim"]["Children"].append("Cesar")


print(advanced_person_date)