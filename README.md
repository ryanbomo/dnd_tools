# DND Tools

This is the README.md for some DND Tools that I have been wanting to create. Initially they'll be written in Python and executed on Ubuntu, but I would like to port them to other platforms in the future.

## Goal

My goal is to create a robust suite of DND tools for 5e DND. Ideally, there will be both player and DM tools, but since I am perma-DM, most of my tools will tend to that side.

## Encounter Generator

Encounter Generator is exactly what it sounds like. It takes the user through a series of prompts to find the number of players, their levels and what difficulty of encounter is desired.

Currently, it then totals the experience that is allotted to that difficulty level for that group. Going forward, it will use a CSV sheet with the Dungeon Master's Guide creatures to "purchase" creatures for the encounter. Purchases are based on CR/XP for the encounter.

### Current Features

Below are the projected features for the DND Encounter Tool

  * Take User Input
  * Calculate total Allotted Encounter XP
  * Generate Number of Enemy Combatants
  * Purchase enemies to fill enemy team based on XP buy system
  * Full CSV of both DMG

### Current Version (1.0)

Does all of the above, but right now creating the encounter is completely random. This results in some weird combos, like 2 enemy encounter with a Mindflayer and a Baboon (which is going to be used in my current campaign, because why not).

Below is an example output for iteration 1:
![Alt text](https://github.com/ryanbomo/dnd_tools/blob/master/dnd_encounter_generator/sample_output/best_encounter.png?raw=true)

### Future Features
  * Cluster Enemy Generation - instead of grabbing random singletons, implement a way to attempt groups
  * Link enemies based on themes or tags - Allow for more flavorful group creation

