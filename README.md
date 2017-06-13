# DND Tools

This is the README.md for some DND Tools that I have been wanting to create. Initially they'll be written in Python and executed on Ubuntu, but I would like to port them to other platforms in the future.

## Goal

My goal is to create a robust suite of DND tools for 5e DND. Ideally, there will be both player and DM tools, but since I am perma-DM, most of my tools will tend to that side.

## Encounter Generator

Encounter Generator is exactly what it sounds like. It takes the user through a series of prompts to find the number of players, their levels and what difficulty of encounter is desired.

Currently, it then totals the experience that is allotted to that difficulty level for that group. Going forward, it will use a CSV sheet with the Dungeon Master's Guide creatures to "purchase" creatures for the encounter. Purchases are based on CR/XP for the encounter.

### Current Features

Below are the curent features for the DND Encounter Tool

  * Take User Input
  * Calculate total Allotted Encounter XP
  * Generate Number of Enemy Combatants
  * Purchase enemies to fill enemy team based on XP buy system
  * Full CSV of both DMG
  * Use accurate range to figure out encounter
  * Create more homogenous groups

### User Manual

After running the code, calling ui() will start the user interface version of the program. Conversely, when it has been loaded into memory, if you know your parameters or want to script with this stuff, main() can be called and run without needing further user input.

#### main()
The main() function follows the following parameters:
main(*encounter\_difficulty*, *party\_size*,*party\_levels*,*csv\_name*,*report\_name*)

**encounter\_difficulty** - takes an integer value between 1 and 4, 1 = Easy, 2 = Medium, 3 = Hard, 4 = Deadly

**party\_size** - is an integer value for the size of the party

**party\_levels** - is a list of the levels of each member of the party

**csv\_name** - the name of the csv file **DO NOT INCLUDE .CSV**

**report\_name** - string name of the encounter being generated

Currently main() will give an output based on the party. This will be updated in the future to simply create a .txt file with the encounter information. The idea is to have no actual input or output from anything if ui() is not called.


### Current Version (1.3)

Does all of the above, but right now creating the encounter is completely random. This results in some weird combos, like 2 enemy encounter with a Mindflayer and a Baboon (which is going to be used in my current campaign, because why not).

Below is the output for the current version (1.3)
![Alt text](https://github.com/ryanbomo/dnd_tools/blob/master/dnd_encounter_generator/sample_output/version_1_3.png?raw=true)

Older outputs are in the sample output folders

### Future Features
  * Link enemies based on themes or tags - Allow for more flavorful group creation
  * Ensure set up is actually possible - some setups don't work. For example, there is no possibly way to create a 15 creature encounter that is easy for 2 level 1 players. Need a way to weed these out.
  * The DMG has player party size considerations that I would like to implement \[DMG 83\]

## Map Generator

Still a WIP. Once a preliminary version is working, this will be uploaded

### Future Features
  * Procedurally Generate Maps using different types - Cave, Castle, Maze, Forest, etc.
  * Export maps to PDF (both true to size 1" grids, and page fitting for documentation)
  * Optionally Link with Encounter Generator and Loot Generator

## Loot Generator

WIP. Once a preliminary version is working, this will be uploaded. But it is pretty much exactly what it sounds like. Using the tables from the DMG, I am implenting a loot roller.

### Future Features
  * Randomly Generate Loot from DMG loot tables
  * Seed loot generation so that it is creature/encounter appropriate

## BBEG Generator
Big Bad Evil Guy Generator. I want to make a quick "quirkey bad guy" creator. This is just a small thing to work on sometimes. This idea may get chopped.

### Future Features
  * Using a predetermined list of quirks and traits, make a bad guy
  * Will do race, gender, age, stats, motivation, small back story, quirks
  * Initially randomly assigned, but I would like to make a way for them to link naturally as well (i.e. a quirk of wanting to sound smart despite being fairly dumb would not be assigned to a high intelligence dude).

