my_dictionary = {
    "person1": {
        "name": "Arcris",
        "age": "27",
        "skills": {
            "programming": {
                "java", "php"
            }
        }
    },
    "person2": {
        "name": "John",
        "age": "27",
    },
    "person3": {
        "name": "Peter",
        "age": "27",
    }
}

for key in my_dictionary:
    print(f"{my_dictionary[key]['name']} {my_dictionary[key]['age']}")
