players =['charles','martina','micheal','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) #when we omit a starting point python auto-starts at the start of the list
print(players[2:]) #when we omit the second value python goes to the end of the list
print(players[-3:])#printer navnene til de siste tre spillerne

#We can also use slices to loop-itterate

players = ['charles', 'martina', 'michael', 'forence', 'eli']

print("Here are the best players on my team looped!")
for player in players[:3]:
    print(player.title())

