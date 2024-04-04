# class
class Human:
    name = "Zainab"
    sex = "Female"

    def get_name_sex(self):
        return self.name + ":" + self.sex


# Object initialization
human = Human()

#print attributes and method
print(human.name, human.sex, human.get_name_sex())

# just the method
print(human.get_name_sex())