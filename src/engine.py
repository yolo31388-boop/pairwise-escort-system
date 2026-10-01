"""押镖 - 带7个bug"""
from dataclasses import dataclass, field
import random

@dataclass
class Escort:
    eid: str
    level: int
    deposit: int
    reward: int
    hp: float
    route: str

class EscortSystem:
    def __init__(self):
        self.escorts: dict[str, Escort] = {}
        self.player_deposit = {}

    def accept(self, player_id, eid):
        escort = self.escorts[eid]
        # bug1: 不检查押金
        return True

    def get_time_limit(self, eid):
        # bug2: 固定10分钟
        return 600

    def rob_reward(self, eid):
        # bug3: 固定奖励
        return {"gold": 100}

    def on_robbed(self, player_id, eid):
        # bug4: 押金全扣
        self.player_deposit[player_id] = 0
        return {"deposit_returned": 0}

    def get_route(self, eid):
        # bug5: 固定路线
        return "route_a"

    def get_hp(self, eid):
        # bug6: 固定血量
        return 1000

    def complete(self, player_id, eid, bag_space=0):
        escort = self.escorts[eid]
        # bug7: 不检查背包
        return {"gold": escort.reward}
