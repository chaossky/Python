def how_much_i_love_you(nb_petals):
    return ["not at all", "I love you", "a little", "a lot", "passionately", "madly"][nb_petals % 6]


print(how_much_i_love_you(7))