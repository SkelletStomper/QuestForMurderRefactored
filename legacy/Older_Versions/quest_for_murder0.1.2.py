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
etimesattacked = 0
eturns = 1
multi = 1
dmgfinal = dmg * multi
poisondur = 4
print("You can be a bandit, a knight or a cleric!")
#Role selector
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

while stage < 6:
    #here the Enemy type is selected
    monty = random.randint(1,5)
    amount = 1
    if stage == 1:
        if monty == 1:
            mnstrtp = ("one-eyed goblin")
            title = ("The")
            information = str("This old, one-eyed Goblin has his best days behnd him. Killing him should be no Problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?")
            death_message = ("You somehow made it. You got defeated by an old cripple of goblin. I would give you an medal, but unfortunaly you got feeded to 23 hungry goblin childrens. You are dead.")
            hpemax = 10
            dmge = 4
            ecrt = 0
            armore = 0
            fireweakness = 10
        elif monty == 2:
            mnstrtp = ("really fat cat")
            title = ("The")
            information = str("Wow, this cat is REALLY fat. Shes slow, but because of her fat belly quite tanky. Maybe you try fire?")
            death_message = ("The cat mistakes you for a sofa, and completely scratches your skin of. You are dead.")
            hpemax = 16
            dmge = 2
            ecrt = 0
            armore = 2
            fireweakness = 15
        elif monty == 3:
            mnstrtp = ("devil-possessed baby")
            title = ("The")
            information = str("This is a baby, possessed by the devil. It doesnt have much health, but explodes when you bring it in contact with fire. So be cautionfull!")
            death_message = ("It thinks you are his Mother! How cute! Except it killed all 243 mothers before. And so you. You are dead.")
            hpemax = 8
            dmge = 5
            ecrt = 0
            armore = 0
            fireweakness = 50
        elif monty == 4:
            mnstrtp = ("pidgeon of doom")
            title = ("The")
            information = str("This pidgeon is really annoying. In fact, it is so annoying that you just want to kill it. Which is pretty easy, because its an goddamn pidgeon.")
            death_message = ("It picks out your eyes, and while stumbling around blindly, you fall with your head into your weapon. You are dead.")
            hpemax = 4
            dmge = 2
            ecrt = 5
            armore = 0
            fireweakness = 9
        elif monty == 5:
            mnstrtp = ("normal man with no weapon")
            title = ("The")
            information = str("Hes not strong, hes not fast, hes not tall. But he wants to kill you because he gets minority complexes when he sees you. Dunno, maybe hes going to srtangle you with his tie or pokning you with his biro or something.")
            death_message = ("He sticks his biro in your eye, and tackers you to the ground. As soon as the eye begins to infect, you are dead.")
            hpemax = 10
            dmge = 3
            armore = 1
            fireweakness = 12
    elif stage == 2:
        if monty == 1:
            mnstrtp = ("two-eyed goblin")
            title = ("The")
            information = str("This goblin is a bit tougher than the last one. He will maybe not be that that easy to kill. He also has a butter knife and a loin cloth armor!")
            death_message = ("He cuts your Head off. You will may ask how he does that with a butter knife? Well, it takes lots of time and is a lot of Pain, but this doesnt matter to you. You are dead.")
            hpemax = 15
            dmge = 6
            ecrt = 1
            armore = 0
            fireweakness = 13
        elif monty == 2:
            mnstrtp = ("poisonos snake")
            title = ("The")
            information = str("This is an poisonos snake. I think thats nuff said.")
            death_message = ("It bites you, and poisons you. What did you expect? You are dead.")
            hpemax = 12
            dmge = 4
            ecrt = 4
            armore = 0
            fireweakness = 10
        elif monty == 3:
            mnstrtp = ("paper-man!")
            title = ("The")
            information = str("This is a superhero, completely out of paper. His arms are really sharp, so watch out you dont get hit! What can I say except fire?")
            death_message = ("It cuts you several times, till you die of wound infection. You are dead.")
            hpemax = 16
            dmge = 6
            ecrt = 5
            armore = -2
            fireweakness = 420
        elif monty == 4:
            mnstrtp = ("really fat old lady")
            title = ("The")
            information = str("Now this is probably the owner of the really fat cat. I think they are fitting very well. So same as the cat.")
            death_message = ("She sits down on you, and you get squished. Yeah, she is REALLY fat. You are dead.")
            hpemax = 25
            dmge = 4
            ecrt = -1
            armore = 4
            fireweakness = 11
        elif monty == 5:
            mnstrtp = ("child soldier")
            title = ("The")
            information = str("Well, its an Child. With an AK-47. Its heavy-armored, but has a terrible precision. That should be easy, right?")
            death_message = ("It manages to shot you in the head. You are dead.")
            hpemax = 10
            dmge = 10
            ecrt = -4
            armore = 3
            fireweakness = 11
    elif stage == 3:
        if monty == 1:
            mnstrtp = ("three-eyed goblin")
            title = ("The")
            information = str("What the chernobyl type of fuck is this??")
            death_message = ("He tears out his third eyeball, and shoves it in your throat. You suffacate painfully. You are dead. ")
            hpemax = 18
            dmge = 5
            ecrt = 3
            armore = 1
            fireweakness = 15
        elif monty == 2:
            mnstrtp = ("imp")
            title = ("The")
            information = str("A nasty flying fucker who pokes you with his Pitchfork. Its a creature, straight out of Hell.")
            death_message = ("He pokes his pitchfork directly in your guts, and twists with it. You are dead.")
            hpemax = 16
            dmge = 6
            ecrt = 4
            armore = 1
            fireweakness = 3
        elif monty == 3:
            mnstrtp = ("giant slime cube")
            title = ("The")
            information = str("The obligatory. It has REALLY high armor, but low health. Also fire isnt effective against him. Just keep on hitting till its dead! But watch out, hes really acid.")
            death_message = ("He eats you via phagocytosis. You get solved by the acid. You are dead.")
            hpemax = 12
            dmge = 8
            ecrt = -4
            armore = 7
            fireweakness = 5
        elif monty == 4:
            mnstrtp = ("reptiloid with a tie")
            title = ("The")
            information = str("It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue")
            hpemax = 20
            dmge = 5
            ecrt = 4
            armore = 2
            fireweakness = 9
        elif monty == 5:
            mnstrtp = ("litte brother")
            title = ("The")
            information = str("The worst nightmare...")
            hpemax = 22
            dmge = 8
            ecrt = 0
            armore = 1
            fireweakness = 20
    elif stage == 4:
        if monty == 1:
            mnstrtp = ("two goblins (2 eyes each)")
            title = ("")
            information = str("So yeah... there are two of them. They attack twice, and swarm around you. High armor is Recomended, as each hit will deal less damage as your armor. You will have a hard time if you dont kill one quickly.")
            hpemax = 30
            dmge = 6
            ecrt = 0
            armore = 0
            fireweakness = 13
            amount = 2
        if monty == 2:
            mnstrtp = ("boss")
            title = ("your")
            information = str("If he defeats you, you are dead. If you defeat him, your fired. Also, his fire resistance is strenghent since he had a lot of BBQ partys with the wifes of all employees.")
            hpemax = 35
            dmge = 7
            ecrt = 1
            armore = 1
            fireweakness = 7
            
    elif stage == 5:
        if monty == 1:
            mnstrtp = ("GLaDOS")
            title = ("")
            information = str("The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. ")
            hpemax = 41
            dmge = 13
            ecrt = 0
            armore = 2
            fireweakness = 15
        elif monty == 2:
            mnstrtp = ("literal devil")
            title = ("the")
            information = str("He is going to send you straight to hell. Also, better not try to attack him with fire. I mean, he comes from hell, he eats fire for breakfast.")
            hpemax = 50
            dmge = 10
            ecrt = 3
            armore = 0
            fireweakness = 0

    hpe = hpemax
    print(title + " " + mnstrtp + " appeared!")
    while hpe > 0:
        if maxhp < hp:
            hp = maxhp
        while done == False:
            
            do = input("What ya gonna do?")
            if do == ("atk"):
                acc = random.randint(7,13)/10 +(crtmdf/10)
                hpe = hpe - int(dmg*acc)
                if hpe < 1:
                    print("You attacked for " + str(int((dmg * acc)*multi)) + " damage, which was a lethal hit!")
                else:
                    
                    print("You attacked for " + str(int(dmg * acc)) + " damage, " + title + mnstrtp + " has only " + str(int(hpe)) + " Hp left!")
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
                    print("As you hit " + title + mnstrtp + ", it exploded and covered you with its organs! You have " + str(hp) + " Hp left and your Dex decreased!")
                    done = True
                else:
                    
                    hpe = hpe - int((dmg - (dmg/4)) * (fireweakness/10))
                    print("You attacked " + title + mnstrtp + " with fire, which dealt " + str(int((dmg - dmg / 5) * (fireweakness/10))) + " fire damage. " + mnstrtp + " has now " + str(hpe) + " left!")
                    done = True
            elif do == ("status"):
                print("Hp= " + str(hp) + " from " + str(maxhp))
                print("Dmg= " + str(dmg))
                print("crtmdf= " + str(crtmdf))
                print("armor= " + str(armor))
                print("heal= " + str(heal))
                print("dodge= " + str(dodge))
                print("crtmdfe= " + str(crtmdfe))
            elif do == ("help"):
                print("atk to attack. Bonus hint: Attacking is key in killing enemys. Thank me later")
                print("heal to heal. It heals you about your your heal value.")
                print("fire to attack with fire damage. Fire does deal less base damage, but penetrates armor and is more or less efficient on specific enemys.")
                print("detox to cure poison.(not yet implimentated)")
                print("info to gather bonus informations about your enemy.")
                print("help to see all comments. I know, very useful.")
                print("Bonus tip: Chose crack addict in the class chose screen. It is very stronk.")
                
            else:
                print("Please make a correct answer")
        done = False
        if hpe > 0:
            etimesattacked = 0
            eturns = int(amount * hpe/hpemax)
            if eturns < 1:
                eturns = 1
            while etimesattacked < eturns:
                if dodge + random.randint(0,10) > 9:
                    print( title + " " + mnstrtp + " attacked, but you dodged the attack!")
                else:
                    acce = float((random.randint(5,11)+stage)/10 +((crtmdfe+crte)/10))
                    hp = hp - str(int(((dmge) * acce - armor)))
                    print(title +" "+ mnstrtp + " attacked you for " + str(int(((dmge) * acce - armor))) + " damage! You have " + str(hp) + " HP left!")
                etimesattacked += 1
        if hp < 1:
            print("Oh no! You lost! Now the monsters will eat your corpse and destroy your dream of glory.")
            exit()    
    else:
        lvlupd = 0
        if stage > 2:
            lvlupd = -1
        print("You killed " + title + " " + mnstrtp + "!")
        if stage == 6:
            print("Yeah!")
        
        else:    
            while lvlupd < 1:
                print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                print("Additionaly you will regain a bit health.")
                lvlup = (input("What is your choice?"))
                if lvlup == ("hp"):
                    maxhp = int(maxhp + (maxhp/5) * (stage + 1 * 0.5) +1)
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
               
            
        
            
