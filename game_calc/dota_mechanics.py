'''Dota 2 mechanics computing module.'''

from dataclasses import dataclass
from typing import List, Optional
from math import prod


@dataclass
class ArcticBurnParams:
    '''Arctic burn params.'''

    dmg_per_sec: float = 0.1
    debuff_duration: int = 8
    movespeed_slow: float = 0.4


@dataclass
class Hero:
    '''Hero params and spells.'''

    intelligence: int = 0
    health: int = 0
    armor: int = 0
    mgc_dmg_mult: float = 1
    mgc_resist_mult: float = 0.0
    mgc_resist: float = 0.0
    negation_mult: float = 0

    def set_mgc_dmg_mult(self,
                         mgc_dmg_bonuses: Optional[List[float]] = None,
                         etherial_bonuses: Optional[List[float]] = None,
                         ) -> None:
        '''Calculates the mgc dmg multiplier.'''
        mgc_increase_mults: List[float] = []
        if mgc_dmg_bonuses is not None:
            mgc_increase_mults = [1 + bonus
                                  for bonus in mgc_dmg_bonuses]
        if etherial_bonuses is not None:
            mgc_increase_mults.append(1 + max(etherial_bonuses))
        self.mgc_dmg_mult = prod(mgc_increase_mults)

    def set_mgc_resist_mult(self,
                            mgc_resist_bonuses: Optional[List[float]] = None,
                            negation_mult: float = 0
                            ) -> None:
        '''TODO'''
        mgc_resist_mults: List[float] = []
        if mgc_resist_bonuses is not None:
            mgc_resist_mults = [1 - bonus for bonus in mgc_resist_bonuses]
        self.mgc_resist_mult = ((1 - (0.25 + 0.001 * self.intelligence)
                                * (1 - negation_mult))
                                * prod(mgc_resist_mults))
        self.mgc_resist = 1 - self.mgc_resist_mult

    def set_mgc_resist(self,
                       mgc_resist_bonuses: Optional[List[float]] = None,
                       ) -> None:
        '''TODO'''
        if mgc_resist_bonuses is None:
            return
        self.set_mgc_resist_mult(mgc_resist_bonuses)
        self.mgc_resist_mult = 1 - self.mgc_dmg_mult

    def get_arctic_burn_dmg(self,
                            enemy_hero,
                            spell_params: ArcticBurnParams
                            ) -> float:
        '''Calculates arctic burn dmg.'''
        total: float = 0
        cur_health: float = float(self.health)
        for _ in range(spell_params.debuff_duration):
            cur_dmg = (cur_health
                       * spell_params.dmg_per_sec
                       * enemy_hero.mgc_dmg_mult
                       * self.mgc_resist_mult)
            cur_health -= cur_dmg
            total += cur_dmg
        return total


if __name__ == '__main__':
    wyvern = Hero()
    wyvern.set_mgc_dmg_mult([0.18, 0.12])
    print(f'mgc_dmg_mult = {wyvern.mgc_dmg_mult}')

    cm = Hero(health=4738, intelligence=128)
    cm.set_mgc_resist_mult(negation_mult=0)
    print(f'mgc_resist = {cm.mgc_resist}')
    print(f'mgc_resist_mult = {cm.mgc_resist_mult}')

    arctic_burn_params = ArcticBurnParams()

    damage = cm.get_arctic_burn_dmg(wyvern, arctic_burn_params)
    print(f'arctic_burn_dmg = {damage}')
    print(f'hp after dmg    = {cm.health - damage}')
    print(damage / cm.health)
