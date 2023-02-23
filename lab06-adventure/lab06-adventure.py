class Room:
    """Room"""
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    current_room = 0
    room_list = []
    room0 = Room("You find yourself in an open space, you are blinded by the pure white lights from the ceiling. \nThe room seems to continue up ahead.",
                1,
                None,
                None,
                None)

    done = False
    room_list.append(room0)
    while not done:
        print("")
        print(room_list[current_room].description)

main()