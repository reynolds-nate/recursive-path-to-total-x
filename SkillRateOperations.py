import json
from pprint import pprint
import cfg

def readRates():
    with open('skillRates.json', "r") as loadData:
        cfg.skill_rate_dict = json.load(loadData)
    
def printRates():
    pprint(cfg.skill_rate_dict)

def updateRate(skill, rate):
    cfg.skill_rate_dict[skill]=rate
    
def writeRates():
    with open('skillRates.json', "w") as outfile:
        json.dump(cfg.skill_rate_dict, outfile)

#tests
# readRates()
# printRates()
# updateRate("agility", 50000)
# printRates()
# writeRates()