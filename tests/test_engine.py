"""押镖测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import EscortSystem, Escort

class TestAccept:
    def test_deposit_required(self):
        es = EscortSystem()
        es.escorts = {"e1": Escort("e1",5,1000,500,1000,"a")}
        es.player_deposit = {"p1": 0}
        assert not es.accept("p1", "e1"), "押金未检查"

class TestRob:
    def test_partial_deposit_return(self):
        es = EscortSystem()
        es.player_deposit = {"p1": 1000}
        result = es.on_robbed("p1", "e1")
        assert result["deposit_returned"] > 0, "被劫押金全扣"
