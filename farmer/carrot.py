def carrot():
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if get_ground_type()==Grounds.Grassland:
                    harvest()
                    till()
                    plant(Entities.Carrot)
                    use_item(Items.Fertilizer)
                    use_item(Items.Water)
                else:
                    harvest()
                    plant(Entities.Carrot)
                    use_item(Items.Fertilizer)
                    use_item(Items.Water)
                move(North)
            move(East)
        break