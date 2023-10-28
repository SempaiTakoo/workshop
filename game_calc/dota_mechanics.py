'''Модуль вычислений механик Dota 2.'''

from dataclasses import dataclass


@dataclass
class ArcticBurnParams:
    '''Параметры способности arctic burn.'''
    periodic_damage: float = 0.1
    duration: int = 8
    slow: float = 0.4
    magic_damage_multiplier: float = 1


@dataclass
class HeroParams:
    '''Параметры героя и эффекты на нём.'''
    health: int = 100
    health_regen: float = 0
    magic_resist: float = 0.25


# def magic_damage_multiplier(hero_params: HeroParams) -> float:
#     '''Вычисляет коэффициент исходящего магического урона.'''
#     result = (1 - self.magic_resist_negation_multipler
#               * (0.25 + self.intelligence * 0.001))
#     if self.magic_resist_modifiers is None:
#         return result
#     for magic_resist_modifier in self.magic_resist_modifiers:
#         result *= 1 - magic_resist_modifier
#     return result


def arctic_burn_damage(spell_params: ArcticBurnParams,
                       enemy_params: HeroParams) -> float:
    '''Вычисляет количество исходящего урона от способности.'''
    cur_hp: float = enemy_params.health
    result: float = 0.0
    for _ in range(spell_params.duration):
        damage_per_tick = (cur_hp
                           * spell_params.periodic_damage
                           * (1 - enemy_params.magic_resist)
                           * spell_params.magic_damage_multiplier
                           - enemy_params.health_regen)
        cur_hp -= damage_per_tick
        result += damage_per_tick
    return result


if __name__ == '__main__':
    spell_parameters = ArcticBurnParams()
    enemy_parameters = HeroParams()
    print(arctic_burn_damage(spell_parameters, enemy_parameters))
