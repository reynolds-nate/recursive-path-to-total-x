#Imports
import json
import os
import sys
import cfg
import LevelPathFinder as lpf
import SkillRateOperations as sro
import hiscores as hs
from pprint import pprint




def printMenu():
    print("1. Read skills rates")
    print("2. Update skill rates")
    print("3. Write updated rates to file")
    print("4. Check Total Level")
    print("5. Set Total Level Goal")
    print("6. Calculate Optimal Path")
    print("7. Exit")
def menuChoice():
    match int(input("What is your choice?: ")):
        case 1:
            sro.printRates()
        case 2:
            for skill in cfg.skill_rate_dict:
                print(skill)
            sro.updateRate(input("Which skill rate would you like to update?"), input("What would you like the updated rate to be? :"))
        case 3:
            sro.writeRate()
        case 4:
            print(cfg.current_total)
        case 5:
            cfg.goal_total = int(input("What is your goal total level?: "))
            cfg.levels_to_goal = cfg.goal_total - cfg.current_total
            print(f"You have {cfg.levels_to_goal} levels until your goal level.")
        case 6:
            lpf.calcPath(cfg.levels_to_goal)
        case 7:
            print("Goodbye for now.")
            exit()


sro.readRates()
print("Welcome to optimal path to total levle X calculator. Select an option from the menu.")
hs.getUserStats(input("What is your username?"))
hs.initializeTTLList()


while True:
    printMenu()
    menuChoice()