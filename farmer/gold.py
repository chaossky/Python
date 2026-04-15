def gold():
    directions=[North,East,South,West]
    index=0
    while True:
        if get_entity_type()==Entities.Treasure:
            harvest()
            break
        if can_move(directions[(index+1)%4]):
            index=(index+1)%4
            move(directions[index])
        elif can_move(directions[(index)%4]):
            move(directions[])
        else:
            index=(index-1)%4
            move(directions[index])