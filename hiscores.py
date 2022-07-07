from pprint import pprint
import cfg
import OSRSBytes as OSRS


def getUserStats(username):
    user = OSRS.Hiscores(username, actype="N", caching=True)
    cfg.user_skills = user.stats[user.username]
    cfg.current_total = int(cfg.user_skills['total']['level'])
    cfg.user_skills.pop('cache_ttl')
    cfg.user_skills.pop('total')   

def initializeTTLList():
    for skill in cfg.user_skills:
        cfg.time_to_level.append([skill, cfg.user_skills[skill]['level'], cfg.user_skills[skill]['exp_to_next_level'],int(cfg.user_skills[skill]['exp_to_next_level'])/cfg.skill_rate_dict[skill]])