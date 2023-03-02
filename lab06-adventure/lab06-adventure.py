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
    current_roomt = 0
    next = " "
    room_list = []

    #Rooms
    room0 = Room("You find yourself in an open space, you are blinded by the pure white lights from the ceiling. \nThe room seems to continue up ahead.",
                1,
                None,
                None,
                None)

    room1 = Room(
        "The small door leads to a less lit room. \nIt is slightly decorated with a pot on top of a shelf. There is only one door ahead.",
        2,
        None,
        0,
        None)

    room2 = Room(
        "You are at one end of a long corridor. You can hear the echo of your own steps. \nThere is a door straight ahead and a window on the right wall.",
        4,
        3,
        2,
        None)

    room3 = Room(
        "You look though the window to see a giant bosnian flag. \nYou are at a high floor and the wind feels nice.",
        4,
        5,
        1,
        2)

    room4 = Room(
        "The room you entered is dark and you can't see anything. The light of the corridor does not reach",
        None,
        None,
        2,
        None)

    room5 = Room(
        "You jump out of the window. You died.",
        None,
        None,
        None,
        None)

    done = False
    room_list.append(room0)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)

    while not done:

        if current_room == 5 or next == "END":
            done = True
        print("")
        print(room_list[current_room].description)
        if not done:
            print("")
            next = str(input("Which direction should you go next? "))
            next = next.upper()
        while not done and next != "N" and next != "S" and next != "E" and next != "W" and next != "END":
            print("Sorry, I didn't get that.")
            next = str(input("Which direction should you go next?"))
            next = next.upper()
        if next == "N":
            current_roomt = room_list[current_room].north
        elif next == "E":
            current_roomt = room_list[current_room].east
        elif next == "S":
            current_roomt = room_list[current_room].south
        elif next == "W":
            current_roomt = room_list[current_room].west

        while (not done) and (current_roomt == None):
           print("")
           print("You can't go there")
           next = str(input("Which direction should you go next?"))
           next = next.upper()

           while next != "N" and next != "S" and next != "E" and next != "W" and next != "END":
               print("Sorry, I didn't get that.")
               next = str(input("Which direction should you go next?"))
               next = next.upper()



           if next == "N":
               current_roomt = room_list[current_room].north
           elif next == "E":
               current_roomt = room_list[current_room].east
           elif next == "S":
               current_roomt = room_list[current_room].south
           elif next == "W":
               current_roomt = room_list[current_room].west


        if current_roomt != None:
            current_room = current_roomt



main()