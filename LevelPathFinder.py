import json
import cfg
from pprint import pprint

def closestLevel():
    min=1000
    action_index=0
    for skill in cfg.time_to_level:
        if skill[3]<min and skill[1]!=99:
            min=skill[3]
            action_index=cfg.time_to_level.index(skill)
    print(action_index)    
    return action_index
#todo fix here somwhere
def ttlUpdate(index):
    cfg.time_to_level[index][1]+=1
    print(cfg.time_to_level[index][1])
    cfg.time_to_level[index][2] = int(cfg.expDict[str(int(cfg.time_to_level[index][1])-1)])
    print(cfg.time_to_level[index][2])
    cfg.time_to_level[index][3]= int(cfg.time_to_level[index][2])/cfg.skill_rate_dict[cfg.time_to_level[index][0]]
    print(cfg.time_to_level[index][3])
def calcPath(LevelsToGo=0):
    if LevelsToGo == 0:
        pprint(cfg.level_path)
        return
    else:
        """
        find next fastest level and append to path of levels
        update time_to_level list with new level, xp_to_level and ttl for appended level
        de-increment count
        """
        index = closestLevel()
        temp = cfg.time_to_level[index].copy()
        cfg.level_path.append(temp)
        ttlUpdate(index)
        LevelsToGo-=1
        calcPath(LevelsToGo)
        
# def sumPath():
#     for action in cfg.level_path:


