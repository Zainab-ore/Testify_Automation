class Human:
    # def __init__(self):
    leg_count = 4
    can_walk = True


    def get_description(self):
        print("This is human")

    def number_of_legs(self):
        return self.leg_count

# Instantiate the class
human_being = Human()


# Invoke the methods
human_being.get_description()
count_legs = human_being.number_of_legs()
# human_being.number_of_legs()
print(count_legs)