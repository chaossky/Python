def hay():
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest
                else:
                    if get_ground_type()==Ground.Soil:
                        till()
                        plant(Entities.Grass)
                move(North)
            move(East)
        break