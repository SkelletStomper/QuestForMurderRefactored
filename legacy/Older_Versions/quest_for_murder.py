import random
maxhp = int(18)
dmg = int(5)
heal = int(4)
stage = int(1)
lvlupd = int(0)
crtmdf = 0
acc = 0
armor = 1
acce = 0
crtmdfe = 0
armore = 0
dodge = 1
rolechosen = False
done = False
hpemax = 1
crte = 0
print("You can be a bandit, a knight or a cleric!")
while rolechosen == False:
    role = input("What will you be?")
    if role == ("knight"):
        maxhp = 24
        dmg = 5
        armor = 3
        crtmdf = -1
        dodge = -2
        heal = 3
        crtmdfe = 1
        rolechosen = True
    elif role == ("bandit"):
        maxhp = 11
        dmg = 7
        armor = 0
        crtmdf = 2
        dodge = 3
        heal = 4
        crtmdfe = -1
        rolechosen = True
    elif role == ("cleric"):
        maxhp = 16
        dmg = 4
        armor = 1
        crtmdf = 0
        dodge = 1
        heal = 8
        crtmdfe = 0
        rolechosen = True
    elif role == ("glass cannon"):
        maxhp = 1
        dmg = 10
        armor = 0
        crtmdf = 5
        dodge = 0
        heal = 1
        crtmdfe = 20
        rolechosen = True
    elif role == ("godfather"):
        maxhp = 50
        dmg = 9
        armor = 5
        crtmdf = 5
        dodge = 4
        heal = 12
        crtmdfe = -3
        rolechosen = True
    elif role == ("crack addict"):
        maxhp = 8
        dmg = 2
        armor = 0
        crtmdf = 0
        dodge = 2
        heal = 5
        crtmdfe = 0
        rolechosen = True
    else:
        print("Please make a correct answer")
print("You have choosen the role " + role + ".")
hp = int(maxhp)   
print("Type atk to attack, type heal to heal, help for more commands")
mnstrtp = str("goblin")

while stage < 6:
    monty = random.randint(1,5)
    if stage == 1:
        if monty == 1:
            mnstrtp = ("one-eyed goblin")
            information = str("This old, one-eyed Goblin has his best days behnd him. Killing him should be no Problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?")
            hpemax = 10
            dmge = 4
            ecrt = 0
            armore = 0
            fireweakness = 10
        elif monty == 2:
            mnstrtp = ("really fat cat")
            information = str("Wow, this cat is REALLY fat. Shes slow, but because of her fat belly quite tanky. Maybe you try fire?")
            hpemax = 16
            dmge = 2
            ecrt = 0
            armore = 2
            fireweakness = 15
        elif monty == 3:
            mnstrtp = ("devil-possessed baby")
            information = str("This is a baby, possessed by the devil. It doesnt have much health, but explodes when you bring it in contact with fire. So be cautionfull!")
            hpemax = 8
            dmge = 5
            ecrt = 0
            armore = 0
            fireweakness = 50
        elif monty == 4:
            mnstrtp = ("pidgeon of doom")
            information = str("this pidgeon is really annoying. In fact, it is so annoying that you just want to kill it. Which is pretty easy, because its an goddamn pidgeon.")
            hpemax = 4
            dmge = 2
            ecrt = 5
            armore = 0
            fireweakness = 9
        elif monty == 5:
            mnstrtp = ("normal man with no weapon")
            information = str("Hes not strong, hes not fast, hes not tall. But he wants to kill you because he gets minority complexes when he sees you. Dunno, maybe hes going to srtangle you with his tie or pokning you with his biro or something.")        
            hpemax = 10
            dmge = 3
            armore = 1
            fireweakness = 12
    elif stage == 2:
        if monty == 1:
            mnstrtp = ("two-eyed goblin")
            information = str("This goblin is a bit tougher than the last one. He will maybe not be that that easy to kill. He also has a butter knife and a loin cloth armor!")
            hpemax = 15
            dmge = 6
            ecrt = 1
            armore = 0
            fireweakness = 13
        elif monty == 2:
            mnstrtp = ("poisonos snake")
            information = str("This is an poisonos snake. I think thats nuff said.")
            hpemax = 12
            dmge = 4
            ecrt = 4
            armore = 0
            fireweakness = 10
        elif monty == 3:
            mnstrtp = ("paper-man!")
            information = str("This is a superhero, completely out of paper. His arms are really sharp, so watch out you dont get hit! What can I say except fire?")
            hpemax = 16
            dmge = 6
            ecrt = 5
            armore = -2
            fireweakness = 420
        elif monty == 4:
            mnstrtp = ("really fat old lady")
            information = str("Now this is probably the owner of the really fat cat. I think they are fitting very well. So same as the cat.")
            hpemax = 25
            dmge = 4
            ecrt = -1
            armore = 4
            fireweakness = 11
        elif monty == 5:
            mnstrtp = ("child soldier")
            information = str("Well, its an Child. With an AK-47. Its heavy-armored, but has a terrible precision. That should be easy, right?")
            hpemax = 10
            dmge = 10
            ecrt = -4
            armore = 3
            fireweakness = 11
    elif stage == 3:
        if monty == 1:
            mnstrtp = ("three-eyed goblin")
            information = str("What the chernobyl type of fuck is this??")
            hpemax = 18
            dmge = 5
            ecrt = 3
            armore = 1
            fireweakness = 15
        elif monty == 2:
            mnstrtp = ("imp")
            information = str("A nasty flying fucker who pokes you with his Pitchfork. Its a creature, straight out of Hell.")
            hpemax = 16
            dmge = 6
            ecrt = 4
            armore = 1
            fireweakness = 3
        elif monty == 3:
            mnstrtp = ("giant slime cube")
            information = str("The obligatory. It has REALLY high armor, but low health. Also fire isnt effective against him. Just keep on hitting till its dead! But watch out, hes really acid.")
            hpemax = 12
            dmge = 8
            ecrt = -4
            armore = 7
            fireweakness = 5
        elif monty == 4:
            mnstrtp = ("reptiloid with a tie")
            information = str("It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue")
            hpemax = 20
            dmge = 5
            ecrt = 4
            armore = 2
            fireweakness = 9
        elif monty == 5:
            mnstrtp = ("litte brother")
            information = str("The worst nightmare...")
            hpemax = 22
            dmge = 8
            ecrt = 0
            armore = 1
            fireweakness = 20
    elif stage == 5:
        if monty == 1:
            mnstrtp = ("GLaDOS")
            information = str("The worst nightmare...")
            hpemax = 22
            dmge = 8
            ecrt = 0
            armore = 1
            fireweakness = 20
    hpe = hpemax
    print("A wild " + mnstrtp + " appeared!")
    while hpe > 0:
        if maxhp < hp:
            hp = maxhp
        while done == False:
            
            do = input("What ya gonna do?")
            if do == ("atk"):
                acc = random.randint(7,13)/10 +(crtmdf/10)
                hpe = hpe - int(dmg*acc)
                if hpe < 1:
                    print("You attacked for " + str(int(dmg * acc)) + " damage, which was a lethal hit!")
                else:
                    
                    print("You attacked for " + str(int(dmg * acc)) + " damage, the " + mnstrtp + " has only " + str(int(hpe)) + " Hp left!")
                done = True
            elif do == ("heal"):
                hp = hp + heal
                if maxhp < hp:
                    hp = maxhp
                print("You healed yourself for " + str(heal) + " Hp, you now have " + str(hp) + " Hp left!")
                done = True
            elif do == ("info"):
                print(information)
            elif do == ("fire"):
                if mnstrtp == ("devil-possessed baby"):
                    hpe = 0
                    hp = hp - (10 + random.randint(2,5) - armor)
                    dodge = dodge - 1
                    crtmdfe = crtmdfe + 1
                    print("As you hit the " + mnstrtp + ", it exploded and covered you with its organs! You have " + str(hp) + " Hp left and your Dex decreased!")
                    done = True
                else:
                    
                    hpe = hpe - int((dmg - (dmg/5)) * (fireweakness/10))
                    print("You attacked the " + mnstrtp + " with fire, which dealt " + str(int((dmg - dmg / 5) * (fireweakness/10))) + " fire damage. The " + mnstrtp + " has now " + str(hpe) + " left!")
                    done = True
            elif do == ("status"):
                print("Hp= " + str(hp) + " from " + str(maxhp))
                print("Dmg= " + str(dmg))
                print("crtmdf= " + str(crtmdf))
                print("armor= " + str(armor))
                print("heal= " + str(heal))
                print("dodge= " + str(dodge))
                print("crtmdfe= " + str(crtmdfe))
                
            else:
                print("Please make a correct answer")
        done = False
        if hpe > 0:
            if dodge + random.randint(0,10) > 9:
                print("The " + mnstrtp + " attacked, but you dodged the attack!")
            else:
                acce = float((random.randint(5,11)+stage)/10 +((crtmdfe+crte)/10))
                hp = hp - int(((stage + stage*2) * acce - armor))
                print("The " + mnstrtp + " attacked you for " + str(int(((dmge) * acce - armor))) + " damage! You have " + str(hp) + " HP left!")
        if hp < 1:
            print("Oh no! You lost! Now the monsters will eat your corpse and destroy your dream of glory.")
            exit()    
    else:
        lvlupd = 0
        if stage > 2:
            lvlupd = -1
        print("You killed the " + mnstrtp + "!")
        if stage == 6:
            print("Yeah!")
        
        else:    
            while lvlupd < 1:
                print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                print("Additionaly you will regain a bit health.")
                lvlup = (input("What is your choice?"))
                if lvlup == ("hp"):
                    maxhp = int(maxhp + (maxhp/5) * (stage * 0.5) +1)
                    hp = hp + stage * stage + 1
                    print("You leveled up HP, now you have " + str(maxhp) + " maximum HP!")
                    lvlupd = 1
                elif lvlup == ("dmg"):
                    dmg = int(dmg + stage + 1 + stage / 2)
                    hp = hp + stage * stage + 1
                    print("You leveled up damage, now you have " + str(dmg) + " damage!")
                    lvlupd = 1
                elif lvlup == ("heal"):
                    heal = heal + stage * 2 + 2
                    hp = hp + stage * stage + 1
                    print("You leveled up healing, now you have " + str(heal) + " heal!")
                    lvlupd = 1
                elif lvlup == ("acc"):
                    crtmdf = crtmdf + stage
                    hp = hp + stage * stage + 1
                    print("You leveled up your accuracy, now you have a modifier of " + str(crtmdf/10) + "!")
                    lvlupd = 1
                elif lvlup == ("amr"):
                    armor = armor + stage*2 -1
                    hp = hp + stage * stage + 1
                    print("You leveled up armor, now you have " + str(armor) + " armor!")
                    lvlupd = 1
                elif lvlup == ("dex"):
                    dodge = dodge + 1
                    crtmdfe = crtmdfe - 1
                    hp = hp + stage * stage + 1
                    print("You leveled up dexterity, you are now more eager to dodge attacks!")
                    lvlupd = 1
                else:
                    print("Please make a correct answer")
            else:
                stage = stage + 1
else:
    print("Congratiolations, you have just won the game!")
               
            
        
            
