import random

SUIT_TUPLE={'Spades','Hearts','Clubs','Diamonds'}
RANK_TUPLE={'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen',"King"}

NCARDS=8

def getCard(deckListIn):
    thisCard=deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut=deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

print('Welcome to Higher or Lower')
print('You have to choose whether the next card to be shown will be higher ovr lower than the current card.')

