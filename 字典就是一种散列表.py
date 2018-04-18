voted = {}

def check_voter(name):
    if voted.get(name): 
        print("Kick {} out!".format(name))
    else:
        voted[name] = True
        print("Let {} vote!".format(name))

check_voter("Nancy")
check_voter("Mike")
check_voter("Mike")

print(voted)