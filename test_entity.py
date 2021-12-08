import pytest
import os

from entity import Entity,Monster,Boss,Player

@pytest.fixture
def monster_test():
    return Monster("Gobelin",20,20,5)

@pytest.fixture
def boss_test():
    return Boss("Dracula",35,35,10)

class TestMonster:
    def test_init(self,monster_test):
        assert monster_test.name == "Gobelin"
        assert monster_test.hp == 20
        assert monster_test.hp_max == 20
        assert monster_test.attack == 5

    def test_level(self,monster_test):
        assert monster_test.level(3,0.2) == (15, 15, 6, 30)

    # def test_attack(self,monster_test):
    #     assert monster_test.attack() ==

    # def test_death(self,monster_test):
    #     assert monster_test.death() == 0


class TestBoss :
    def test_init(self,boss_test):
        assert boss_test.name == "Dracula"
        assert boss_test.hp == 35
        assert boss_test.hp_max == 35
        assert boss_test.attack == 10

    def test_level(self,boss_test):
        assert boss_test.level(5,0.3) == (27, 27, 11, 54)

    # def test_attack(self,boss_test):
    #     boss_test.attack()

    # def test_death(self,boss_test):
    #     boss_test.death()
    #     assert boss_test.name == None

    def test_defense(self,boss_test):
        assert boss_test.defense() == 3

@pytest.fixture
def player_test():
    return Player("claire",50,50,4)
@pytest.fixture
def player_test_defense():
    player_test_defense = Player("claire",50,50,4)
    player_test_defense.defense = 2
    return player_test_defense
# @pytest.fixture
# def monster_test():
#     return Player()

class Test_Player:
    def test_init(self, player_test):
        assert player_test.attack == 4
        assert player_test.name == "claire"
        
    #def test_attack(self,player_test,6):
    
    
    
    
    def test_defense_player(self,player_test,player_test_defense):
        assert player_test.defense_player() == 3
        assert player_test_defense.defense_player() == 2
        
    def test_death(self,player_test):
        assert player_test.death() == (False, 0)
        
    def test_drink_potion(self,player_test):
        assert player_test.drink_potion() == (50, 2) # 返回多个值时 需要括号
        player_test.hp = 10
        assert player_test.drink_potion() == (30, 1)
     
    def test_quit(self,player_test):
        assert player_test.quit() == False  