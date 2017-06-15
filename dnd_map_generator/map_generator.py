import random

def main(map_dimensions,num_attempts):

    ## Creat the Blank Map
    blank_map = create_blank_map(map_dimensions)

    ## Add rooms to the map
    roomed_map = add_rooms(blank_map,num_attempts)

    ## Add hallways to the map (NOT YET IMPLEMENTED)
    hallway_map = add_halls(roomed_map)

    ## Export Map - Currently ASCII, future to TXT and maybe draw to PDF
    export_map(hallway_map)

    return

# Creates the blank map by occuping the dimensions with X to designate
# solid wall.  Simple enough that it could have been implemented in main()
# but this keeps thing organized.
def create_blank_map(map_dimensions):
    map_height = map_dimensions[0]
    map_width = map_dimensions[1]
    blank_map = [["X"]*map_height for n in range(map_width)]
    return blank_map


# Add rooms to the map using random behavior
# Future implementations will hopefully be able to seed the behavior and use
# room shapes other than rectangle
def add_rooms(blank_map,attempts):
    #get map dimensions
    map_height = len(blank_map)
    map_width = len(blank_map[0])

    # Get max room dimensions, using .4 as a magic number
    # Seems to make rooms that seem appropriatley sized for the board
    # This numer will probably be user customizable in the future
    max_room_height = int(.4*map_height)
    max_room_width = int(.4*map_width)
    if max_room_height > 20:
        max_room_height = 20
    if max_room_width >20:
        max_room_width = 20
    
    #for each attempt, create a room and try to place it
    taken_coords = []  # contains all coords that are already "room"
    room_number = 1
    for i in range(attempts):
        #create a room
        room_height = random.randint(2,max_room_height)
        room_width = random.randint(2,max_room_width)

        #get random spot to place
        max_Y = map_height - room_height
        max_X = map_width - room_width

        X_coord = random.randint(0,max_X)
        Y_coord = random.randint(0,max_Y)

        # check that everything is kosher but seeing
        # if any of the rooms coordinates are already
        # rooms.  Not very efficient, might look into
        # optimizing here.
        room_fail = False
        tested_coords = []
        for i in range(room_height):
            for j in range(room_width):
                test_x = j+X_coord
                test_y = i+Y_coord
                this_test = [test_x,test_y]
                tested_coords.append(this_test)
                if this_test in taken_coords:
                    room_fail = True
                    
        # If the room passed the test, add it to the map
        if not room_fail:
            for i in range(room_height):
                for j in range(room_width):
                    place_x = j+X_coord
                    place_y = i+Y_coord
                    blank_map[place_y][place_x] = room_number
            # And add the coordinates to the list of occupied coordinates
            for i in tested_coords:
                taken_coords.append(i)
            room_number+=1
    # Send back that now not so blank map
    return blank_map

def add_halls(roomed_map):
    # To be implemented
    return roomed_map

def export_map(hallway_map):
    width = len(hallway_map[0])
    for i in hallway_map:
        row = ""
        for j in i:
            if j != "X":
                row+=" "
            else:
                row += j
        print(row)

main([22,25],200)
