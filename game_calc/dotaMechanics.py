def magical_damage_multipler(negation_multipler=1, intelligence=0, magic_resistance_modifiers=[]):
    magical_damage_multipler = 1 - negation_multipler * (0.25 + 0.001 * intelligence)
    for magic_resistance_modifier in magic_resistance_modifiers:
        magical_damage_multipler *= 1 - magic_resistance_modifier
    return magical_damage_multipler

def total_magic_resistance(negation_multipler=1, intelligence=0, magic_resistance_modifiers=[]):
    return 1 - magical_damage_multipler(negation_multipler, intelligence, magic_resistance_modifiers)

def arctic_burn_damage(hp, dps=0.1, duration=5, damage_modifier=0.75):
    total = 0
    for i in range(duration):
        damage = hp * dps * damage_k
        hp -= damage
        total += damage
    return total

if __name__ == '__main__':
    # print(arctic_burn_damage(hp=5682, dps=0.13, duration=5, damage_k=0.75))
    print(total_magic_resistance(intelligence=750, magic_resistance_modifiers=[0]))