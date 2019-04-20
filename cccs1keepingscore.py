cards = input("enter cards: ")
clist = []
dlist = []
hlist = []
slist = []
cardlist = ["J","Q","K","A","T"]
floatinglist = ["C", "D", "H", "S"]
conversion = {"J":1,"Q":2,"K":3,"A":4, "T":0}
extrapoints = {0:3,1:2,2:1}
floatingcard = cards[0]
points = {"C": 0,"D": 0,"H": 0, "S": 0}
for i in range(0,len(cards)):
    if cards[i] in floatinglist:
        floatingcard = cards[i]
        #print("floating card is now: "+floatingcard)       
    elif cards[i] in cardlist:
        #print("im in the cardlist if: " + cards[i])
        points[floatingcard] += conversion.get(cards[i])  
    if floatingcard == "C" and cards[i] != "C":
        clist.append(cards[i])        
    elif floatingcard == "D" and cards[i] != "D":
        dlist.append(cards[i])      
    elif floatingcard == "H" and cards[i] != "H":
        hlist.append(cards[i])   
    elif floatingcard == "S" and cards[i] != "Spades Points: {}, Cards:":
        slist.append(cards[i])
try:
    points["C"] += int(extrapoints[len(clist)])
except KeyError:
    pass
try:
    points["D"] += int(extrapoints[len(dlist)])
except KeyError:
    pass
try:
    points["H"] += int(extrapoints[len(hlist)])
except KeyError:
    pass
try:
    points["S"] += int(extrapoints[len(slist)])
except KeyError:
    pass
print("Cards Dealt              Points")
print("Clubs ".format,end="")
print(*clist,end="")
print("Diamond Points: {}, Cards:".format(points["D"]), end="")
print(*dlist)
print("Heart Points: {}, Cards:".format(points["H"]), end="")
print(*hlist)
print("Spades Points: {}, Cards:".format(points["S"]), end="")
print(*slist)
total = int(points["C"])+ int(points["D"]) + int(points["H"]) + int(points["S"])
print("Total: {total}".format(total=total))