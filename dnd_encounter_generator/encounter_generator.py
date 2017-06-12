# This is an encounter generator, the user will be prompted through a series
# of questions before an encounter is generated.  A level and difficulty
# combat encounter will be generated, as will a loot table
# Author: Ryan Bomalaski

import math
import random
import csv
import sys
import os.path

def main(encounter_difficulty, party_size,party_levels,csv_name,report_name):

    #bring in data
    args = [encounter_difficulty, party_size,party_levels,csv_name,report_name]

    #data caries expectations, gotta check it
    args = sanitize_input(args)
    party_params = [args[0], args[1], args[2]]

    # create monster dictionary
    creature_dic = create_creature_dictionary(args[3])
    
    # use party parameters to get allotted xp
    xp_allotted = calc_encounter_xp(party_params)

    # calc size of enemy party
    num_enemies = generate_encounter_size()

    # calc xp multiplier due to enemy party size
    xp_multiplier = determine_size_multiplier(num_enemies)

    # generate enemy list
    list_enemy_party = generate_enemy_party(num_enemies,xp_allotted,xp_multiplier,creature_dic)
        
    # create encounter
    encounter1 = encounter(report_name,xp_allotted,num_enemies,xp_multiplier,list_enemy_party)

    #output to user
    print(encounter1.generate_encounter())
    
    return

# method for sanitizing input based on expectations
def sanitize_input(args):
    sanitary_arg = []
    difficulty = args[0]
    size = args[1]
    levels = args[2]
    csv_name = args[3]
    report_name = args[4]

    # check difficulty
    if difficulty < 1:
        difficulty = 1
    elif difficulty > 4:
        difficulty = 4
    sanitary_arg.append(difficulty)

    #check size
    if size != len(levels):
        print("Issue with party player party size!")
        size = len(levels)
    sanitary_arg.append(size)

    #check levels
    for i in (range(len(levels))):
        if levels[i] > 20:
            levels[i] = 20
        elif levels[i] < 0:
            levels[i] = 0
    sanitary_arg.append(levels)

    #check csv_name
    if not os.path.isfile(csv_name + ".csv"):
        print("Error with csv filename")
        print(csv_name + ".csv cannot be found.")
        sys.exit()
    sanitary_arg.append(csv_name)

    
    #check report_name
    sanitary_arg.append(report_name)

    return sanitary_arg

# Calculate the encounter XP
# Uses magic numbers in tables, due to WotC not having an obvious algorithm for calculating these values
def calc_encounter_xp(party_params):
    allotted_xp = 0
    difficulty = party_params[0]-1
    list_player_levels = party_params[2]

    #below values from Dungeon Master's Guide
    list_easy = [0,25, 50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    list_medium =[0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900,5700]
    list_hard = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    list_deadly = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]
    difficulty_matrix = [list_easy,list_medium,list_hard,list_deadly]

    for i in list_player_levels:
        allotted_xp = allotted_xp + difficulty_matrix[difficulty][i]
    return allotted_xp

# Creates a dictionray based on CSV file with creatures and XP values
# Data agnostic, so users can use their own creatures and update CSV file as new creatures
# get released.
def create_creature_dictionary(file_name):
    creature_dict = {}
    file_string = file_name + ".csv"
    with open(file_string) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Creature'],row['XP'])
            creature_dict[row['Creature']] = row['XP']
    return creature_dict

# There has got to be a better way to do this...
def generate_encounter_size():
    enemy_seed = random.randint(1,100)
    num_enemies = 0
    dict_size_percent = {}
    dict_size_percent['1'] = 1
    dict_size_percent['2'] = 19
    dict_size_percent['3'] = 49
    dict_size_percent['4'] = 67
    dict_size_percent['5'] = 76
    dict_size_percent['6'] = 81
    dict_size_percent['7'] = 86
    dict_size_percent['8'] = 89
    dict_size_percent['9'] = 92
    dict_size_percent['10'] = 94
    dict_size_percent['11'] = 96
    dict_size_percent['12'] = 97
    dict_size_percent['13'] = 98
    dict_size_percent['14'] = 99
    dict_size_percent['15'] = 100

    if enemy_seed==dict_size_percent['15']:
        num_enemies = 15
    elif enemy_seed==dict_size_percent['14']:
        num_enemies = 14
    elif enemy_seed==dict_size_percent['13']:
        num_enemies = 13
    elif enemy_seed==dict_size_percent['12']:
        num_enemies = 12
    elif enemy_seed==dict_size_percent['11']:
        num_enemies = 11
    elif dict_size_percent['10']<=enemy_seed<dict_size_percent['11']:
        num_enemies = 10
    elif dict_size_percent['9']<=enemy_seed<dict_size_percent['10']:
        num_enemies = 9
    elif dict_size_percent['8']<=enemy_seed<dict_size_percent['9']:
        num_enemies = 8
    elif dict_size_percent['7']<=enemy_seed<dict_size_percent['8']:
        num_enemies = 7
    elif dict_size_percent['6']<=enemy_seed<dict_size_percent['7']:
        num_enemies = 6
    elif dict_size_percent['5']<=enemy_seed<dict_size_percent['6']:
        num_enemies = 5
    elif dict_size_percent['4']<=enemy_seed<dict_size_percent['5']:
        num_enemies = 4
    elif dict_size_percent['3']<=enemy_seed<dict_size_percent['4']:
        num_enemies = 3
    elif dict_size_percent['2']<=enemy_seed<dict_size_percent['3']:
        num_enemies = 2
    else:
        num_enemies = 1

    return num_enemies

def determine_size_multiplier(num_enemies):
        if num_enemies == 1:
            multiplier = 1.0
        elif num_enemies == 2:
            multiplier = 1.5
        elif 3<=num_enemies<=6:
            multiplier = 2.0
        elif 7<=num_enemies<=10:
            multiplier = 2.5
        elif 11<=num_enemies<=14:
            multiplier = 3
        else:
            multiplier = 4
        return multiplier

def generate_enemy_party(num_enemies,allotted_xp,xp_multiplier,enemy_dictionary):
    return ["t","e","s","t"]
    
    

class encounter:
    def __init__(self, encounter_name,allotted_xp,size,xp_multiplier,enemy_list):
        self.encounter_name = encounter_name
        self.xp_allotted = allotted_xp
        self.num_enemies = size
        self.xp_multiplier = xp_multiplier
        self.enemy_list = enemy_list

    def generate_encounter(self):
        output = "Num enemies - " + str(self.num_enemies)
        output += " :: XP Allotted - " + str(self.xp_allotted)
        output += " :: Enounter Name - " +self.encounter_name
        output += " :: Multipler - " + str(self.xp_multiplier)
        output += " :: Actual XP to Spend - " +str(int(self.determine_spendable_xp()))
        output += " :: Enemy List - " + str(self.enemy_list)

        return output

    def determine_spendable_xp(self):
        spendable_xp = float(self.xp_allotted)/self.xp_multiplier
        return spendable_xp



#
#
#       UI STUFF I HERE
#
# optoinal UI elment, not necessary for function
# allows for smooth operation if you don't know format for main()
def ui():
    title_text_art = '''  _____         _____    ______                             _            
 |  __ \  ___  |  __ \  |  ____|                           | |           
 | |  | |( _ ) | |  | | | |__   _ __   ___ ___  _   _ _ __ | |_ ___ _ __ 
 | |  | |/ _ \/\ |  | | |  __| | '_ \ / __/ _ \| | | | '_ \| __/ _ \ '__|
 | |__| | (_>  < |__| | | |____| | | | (_| (_) | |_| | | | | ||  __/ |   
 |_____/ \___/\/_____/  |______|_| |_|\___\___/ \__,_|_| |_|\__\___|_|
                     v.1.0 by Ryan Bomalaski
                  
D&D Encounter is a quick python application for generating very simple D&D
Encounters and loot tables using a CSV with my figure list. God I'm bored.'''+'\n'
    print(title_text_art)
    i = 1
    ## Build dictionary of Monster Manual Creatures
    mon_man_data = str(input("What is the name of CSV with creature data?"))

    ## Create encounters until the user wants to quit
    stop = False
    while not stop:
        report_name = str(input("What is the name of this encounter? "))
        party_params = get_party_params()
        main(party_params[0], party_params[1], party_params[2],mon_man_data,report_name)
        i+=1
        set_correct = str(input("Create another encounter? [y/n] "))
        if(set_correct.lower()!='y'):
            stop = True
    

# walk user through series of questions to get party parameters
# might transition to C and switch to getopt, but not sure
def get_party_params():
    num_players = 0
    list_player_levels = []
    difficulty = 0
    while num_players ==0:
        try:
            num_players = int(input("How many players are in your group? "))
        except ValueError:
            print("Somethign went wrong. Let's try again.")
            print("Only enter a numerical value for the number of players.\n")

    for i in range(num_players):
        level_unset = True
        while level_unset:
            try:
                player_level = int(input("What is the level of character number " + str(i+1)+"? "))
                level_unset = False
                if player_level >20:
                    player_level = 20
                if player_level < 0:
                    player_level = 0
                list_player_levels.append(player_level)
            except ValueError:
                print("Something went wrong. Let's try again.")
                print("Be sure to enter only the number of levels.\n")
            
    while difficulty ==0:
        try:
            difficulty = int(input("On scale of 1 to 4, how hard is the enouncter? "))
        except ValueError:
            print("Somethign went wrong. Let's try again.")
            print("Only enter a numerical value for the difficulty.\n")
        if difficulty > 4:
            difficulty = 4
    party_params = [difficulty,num_players,list_player_levels]
    return party_params
