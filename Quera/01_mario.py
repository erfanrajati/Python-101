# get the input: cm, gm
cm, gm = input().split(' ')
cm = int(cm)
gm = int(gm)

# get the input: cs, gs
cs, gs = input().split(' ')
cs = int(cs)
gs = int(gs)

# get the input: rate
rate = int(input())


# convert mario's inventory to all coins
mario_coins = gm * rate + cm

# convert the price of the sword to all coins
sword_coins = gs * rate + cs

# can mario buy the sword?
if sword_coins <= mario_coins:
    print('Yes')
else:
    print('No')