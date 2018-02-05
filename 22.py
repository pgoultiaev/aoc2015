SPELL_COST = {'M': 53, 'D': 73, 'S': 113, 'P': 173, 'R': 229}


def battle(player_hp, player_mana, boss_hp, mana_spent, poison_left,
           shield_left, recharge_left, chain, first, spell, hard_mode):
    if hard_mode:
        player_hp -= 1
        if player_hp <= 0:
            return

    if not first:
        if SPELL_COST[spell] > player_mana:
            return
        elif spell == 'S' and shield_left > 1:
            return
        elif spell == 'P' and poison_left > 1:
            return
        elif spell == 'R' and recharge_left > 1:
            return
        else:
            player_hp, player_mana, boss_hp, poison_left, shield_left, recharge_left, armor = handle_buffs(
                player_hp, player_mana, boss_hp, poison_left, shield_left,
                recharge_left)
            player_hp, player_mana, boss_hp, poison_left, shield_left, recharge_left = my_turn(
                spell, player_hp, player_mana, boss_hp, poison_left,
                shield_left, recharge_left)
            player_hp, player_mana, boss_hp, poison_left, shield_left, recharge_left, armor = handle_buffs(
                player_hp, player_mana, boss_hp, poison_left, shield_left,
                recharge_left)
            player_hp = boss_turn(player_hp, armor)

    if boss_hp <= 0:
        mana_spent_wins.add(mana_spent)
        return
    elif player_hp <= 0 or player_mana <= 0 or mana_spent >= min(
            mana_spent_wins):
        return

    for spell in 'RSPDM':
        battle(player_hp, player_mana, boss_hp, mana_spent + SPELL_COST[spell],
               poison_left, shield_left, recharge_left, chain + spell, False,
               spell, hard_mode)


def handle_buffs(player_hp, player_mana, boss_hp, poison_left, shield_left,
                 recharge_left):
    if poison_left:
        boss_hp -= 3
        poison_left = max(poison_left - 1, 0)
    if shield_left:
        armor = 7
        shield_left = max(shield_left - 1, 0)
    else:
        armor = 0
    if recharge_left:
        player_mana += 101
        recharge_left = max(recharge_left - 1, 0)
    return player_hp, player_mana, boss_hp, poison_left, shield_left, recharge_left, armor


def my_turn(spell, player_hp, player_mana, boss_hp, poison_left, shield_left,
            recharge_left):
    if spell == 'M':
        boss_hp -= 4
    elif spell == 'D':
        boss_hp -= 2
        player_hp += 2
    elif spell == 'S':
        shield_left = 6
    elif spell == 'P':
        poison_left = 6
    elif spell == 'R':
        recharge_left = 5
    player_mana -= SPELL_COST[spell]
    return player_hp, player_mana, boss_hp, poison_left, shield_left, recharge_left


def boss_turn(player_hp, armor):
    player_hp -= max(9 - armor, 1)
    return player_hp


mana_spent_wins = set([5000])
battle(50, 500, 51, 0, 0, 0, 0, '', True, '', False)
print(min(mana_spent_wins))
mana_spent_wins = set([5000])
battle(50, 500, 51, 0, 0, 0, 0, '', True, '', True)
print(min(mana_spent_wins))
