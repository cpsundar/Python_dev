class campaign():
    _name = ""
    _age = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display_object(self):
        print("Name of the object:{name} and age: {age}".format(name=self._name, age=self._age))


if __name__ == "__main__":
    camp = campaign("Sundar", 48)
    camp.display_object()
