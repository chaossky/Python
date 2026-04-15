import maze
import gold
import hay
import wood
import carrot

while True:
    if num_items(Itenms.Hay)<=8000:
        change_hat(Hats.Purple_Hat)
        hay.hay()
    elif num_items(Items.Wood)<13000:
        change_hat(Hats.Brown_Hat)
        wood.wood()
    elif num_items(Items.Gold)<=4300:
        change_hat(Hats.Gold_Hat)
        maze.maze()
        gold.gold()
    else:
        change_hat(Hats.Carrot_Hat)
        carrot.carrot()