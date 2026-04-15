def wood():
     while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                    plant(Entities.Tree)
                    use_items(Items.Fertilizer)
                    use_items(Items.Water)
                move(North)
            move(East)
        break