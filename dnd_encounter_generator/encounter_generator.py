# This is an encounter generator, the user will be prompted through a series
# of questions before an encounter is generated.  A level and difficulty
# combat encounter will be generated, as will a loot table
# Author: Ryan Bomalaski

import math
from datetime import datetime

def main():
        ## Main Function, called at start
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
    stop = False
    while not stop:
        encounter_generator(i)
        i+=1
        set_correct = str(input("Create another encounter? [y/n] "))
        if(set_correct.lower()!='y'):
            stop = True
        

def encounter_generator(i):
    user_input = 0
    while user_input == 0:
        print("\nThis is encounter number " + str(i))
        report_name = str(input("What is the name of this encounter? "))
        set_correct = 'n'
        while (set_correct.lower()!='y'):
            xp_allotted = process_user_input()
            print ('\n'+str(xp_allotted)+' is the allotted XP for the encounter.')
            set_correct = str(input("Does this look correct? [y/n] "))
            if(set_correct.lower()!='y'):
                print("\nOK, let's try again")
            else:
                user_input = 1
    encounter1 = encounter(report_name,xp_allotted)
    print(encounter1.generate_encounter())
    

def process_user_input():
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
    allotted_XP = calc_encounter_xp(difficulty,num_players,list_player_levels)            
    return allotted_XP

def calc_encounter_xp(difficulty,num_players,list_player_levels):
    allotted_xp = 0
    difficulty = difficulty-1
    list_easy = [0,25, 50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    list_medium =[0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900,5700]
    list_hard = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    list_deadly = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]
    difficulty_matrix = [list_easy,list_medium,list_hard,list_deadly]

    for i in list_player_levels:
        allotted_xp = allotted_xp + difficulty_matrix[difficulty][i]
    return allotted_xp
    

class encounter:
    def __init__(self, encounter_name,allotted_xp):
        self.encounter_name = encounter_name
        self.xp_allotted = allotted_xp
        self.num_enemies = 0

    def generate_encounter(self):
        output = "Num enemies - " + str(self.num_enemies) + " :: XP Allotted - " + str(self.xp_allotted) + " :: Enounter Name - " +self.encounter_name
        return output

    
