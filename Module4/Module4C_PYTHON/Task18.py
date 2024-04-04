class Human:
    leg_count = 4
    can_walk = True

    def __init__(self):
        self.leg_count = 4
        self.can_walk = True


# Optionally you can instantiate the class and prints out the leg_count and can_walk attributes.
human_sample = Human()

print("Infor Output:" , human_sample.leg_count, " and ", human_sample.can_walk)