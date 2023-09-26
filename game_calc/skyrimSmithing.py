MATERIALS_COST = [7, 3, 40] # Iron_Ingot, Leather_Strips, Corundum_Ingot
TOTAL_XP = 91601
with open('test.txt') as f:
    data = dict()
    for i in f.readlines():
        row = i.split()
        item, cost, materials = row[0], int(row[1]), [int(j) for j in row[2:]]
        item_xp = 25 + (3 * cost**0.65)
        item_count = TOTAL_XP / item_xp
        print(f"Предмет: {item : <20} | ", end='')
        print(f"Количество: {int(item_count) : <4} | ", end='')
        print(f"Стоимость материалов: {int(item_count * sum(materials) * 3)}")