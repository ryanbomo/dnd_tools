import random

def main(map_dimensions,num_attempts):
    blank_map = create_blank_map(map_dimensions)

    roomed_map = add_rooms(blank_map,num_attempts)

    hallway_map = add_halls(roomed_map)

    export_map(hallway_map)

    return


def create_blank_map(map_dimensions):
    map_height = map_dimensions[0]
    map_width = map_dimensions[1]
    row_template = []
    blank_map = [["X"]*map_height for n in range(map_width)]

    return blank_map


def add_rooms(blank_map,attempts):
    #get map dimensions
    map_height = len(blank_map)
    map_width = len(blank_map[0])

    #get max room dimensions
    max_room_height = int(.4*map_height)
    max_room_width = int(.4*map_width)

    list_of_taken_coords = []

    #for each attempt, create a room and try to place it
    
    taken_coords = []
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

        #check that everything is kosher
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
            
        if not room_fail:

            for i in range(room_height):
                for j in range(room_width):
                    place_x = j+X_coord
                    place_y = i+Y_coord
                    blank_map[place_y][place_x] = "R"
                    
            for i in tested_coords:
                taken_coords.append(i)
            room_number+=1
    return blank_map

def add_halls(roomed_map):
    return roomed_map

def export_map(hallway_map):
    width = len(hallway_map[0])
    for i in hallway_map:
        row = ""
        for j in i:
            row += j
        print(row)

main([22,25],10)
