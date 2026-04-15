def maze():
    while not can_harvest():
        move(North)
    if get_ground_type()==Grounds.Soil:
        harvest()
        till()
        plant(Entities.Bush)
    else:
        harvest()
        plant(Entities.Bush)
    substance=get_world_size()*2**(num_unlocked(Unlocks.Mazes)-1)
    use_item(Items.Weird_Substances,substance)