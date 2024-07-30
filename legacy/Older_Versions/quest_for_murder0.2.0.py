import random
maxhp = 18
dmg = 5
heal = 4
stage = 1
lvlupd = 0
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
#Poison vars
psndur = 4
psnchance = 0
psnrsst = 0
psnleft = 0
detoxprot = True
#current poison duration
psncurdur = 0
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
        psnrsst = 1
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
        psnrsst = 5
        rolechosen = True
    elif role == ("sand sack"):
        maxhp = 200
        dmg = 10
        armor = 0
        crtmdf = 0
        dodge = -20
        heal = 5
        crtmdfe = 1
        psnrsst = -10
        
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
    psnchance = 0
    psndur = 0
    if stage == 1:
        if monty == 1:
            mnstrtp = ("one-eyed goblin")
            title = ("the")
            information = ("This old, one-eyed Goblin has his best days behnd him. Killing him should be no Problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?")
            death_message = ("You somehow made it. You got defeated by an old cripple of goblin. I would give you an medal, but unfortunaly you got feeded to 23 hungry goblin childrens. You are dead.")
            hpemax = 10
            dmge = 4
            ecrt = 0
            armore = 0
            fireweakness = 10
        elif monty == 2:
            mnstrtp = ("really fat cat")
            title = ("the")
            information = ("Wow, this cat is REALLY fat. Shes slow, but because of her fat belly quite tanky. Maybe you try fire?")
            death_message = ("The cat mistakes you for a sofa, and completely scratches your skin of. You are dead.")
            hpemax = 16
            dmge = 2
            ecrt = 0
            armore = 2
            fireweakness = 15
        elif monty == 3:
            mnstrtp = ("devil-possessed baby")
            title = ("the")
            information = ("This is a baby, possessed by the devil. It doesnt have much health, but explodes when you bring it in contact with fire. So be cautionfull!")
            death_message = ("It thinks you are his Mother! How cute! Except it killed all 243 mothers before. And so you. You are dead.")
            hpemax = 8
            dmge = 5
            ecrt = 0
            armore = 0
            fireweakness = 50
        elif monty == 4:
            mnstrtp = ("pidgeon of doom")
            title = ("the")
            information = ("This pidgeon is really annoying. In fact, it is so annoying that you just want to kill it. Which is pretty easy, because its an goddamn pidgeon.")
            death_message = ("It picks out your eyes, and while stumbling around blindly, you fall with your head into your weapon. You are dead.")
            hpemax = 4
            dmge = 2
            ecrt = 5
            armore = 0
            fireweakness = 9
            psnchance = 2
            psndur = 1
        elif monty == 5:
            mnstrtp = ("normal man with no weapon")
            title = ("the")
            information = ("Hes not strong, hes not fast, hes not tall. But he wants to kill you because he gets minority complexes when he sees you. Dunno, maybe hes going to srtangle you with his tie or pokning you with his biro or something.")
            death_message = ("He sticks his biro in your eye, and tackers you to the ground. As soon as the eye begins to infect, you are dead.")
            hpemax = 10
            dmge = 3
            armore = 1
            fireweakness = 12
    elif stage == 2:
        if monty == 1:
            mnstrtp = ("two-eyed goblin")
            title = ("the")
            information = ("This goblin is a bit tougher than the last one. He will maybe not be that that easy to kill. He also has a butter knife and a loin cloth armor!")
            death_message = ("He cuts your Head off. You will may ask how he does that with a butter knife? Well, it takes lots of time and is a lot of Pain, but this doesnt matter to you. You are dead.")
            hpemax = 15
            dmge = 6
            ecrt = 1
            armore = 0
            fireweakness = 13
        elif monty == 2:
            mnstrtp = ("poisonos snake")
            title = ("the")
            information = ("This is an poisonos snake. I think thats nuff said.")
            death_message = ("It bites you, and poisons you. What did you expect? You are dead.")
            hpemax = 12
            dmge = 4
            ecrt = 4
            armore = 0
            fireweakness = 10
            psnchance = 4
            psndur = 3
        elif monty == 3:
            mnstrtp = ("paper-man!")
            title = ("the")
            information = ("This is a superhero, completely out of paper. His arms are really sharp, so watch out you dont get hit! What can I say except fire?")
            death_message = ("It cuts you several times, till you die of wound infection. You are dead.")
            hpemax = 16
            dmge = 6
            ecrt = 5
            armore = -2
            fireweakness = 420
        elif monty == 4:
            mnstrtp = ("really fat old lady")
            title = ("the")
            information = ("Now this is probably the owner of the really fat cat. I think they are fitting very well. So same as the cat.")
            death_message = ("She sits down on you, and you get squished. Yeah, she is REALLY fat. You are dead.")
            hpemax = 25
            dmge = 4
            ecrt = -1
            armore = 4
            fireweakness = 11
        elif monty == 5:
            mnstrtp = ("child soldier")
            title = ("the")
            information = ("Well, its an Child. With an AK-47. Its heavy-armored, but has a terrible precision. That should be easy, right?")
            death_message = ("It manages to shot you in the head. You are dead.")
            hpemax = 10
            dmge = 10
            ecrt = -4
            armore = 3
            fireweakness = 11
    elif stage == 3:
        if monty == 1:
            mnstrtp = ("three-eyed goblin")
            title = ("the")
            information = ("What the chernobyl type of fuck is this??")
            death_message = ("He tears out his third eyeball, and shoves it in your throat. You suffacate painfully. You are dead. ")
            hpemax = 18
            dmge = 5
            ecrt = 3
            armore = 1
            fireweakness = 15
        elif monty == 2:
            mnstrtp = ("imp")
            title = ("the")
            information = ("A nasty flying fucker who pokes you with his Pitchfork. Its a creature, straight out of Hell.")
            death_message = ("He pokes his pitchfork directly in your guts, and twirls them. You are dead.")
            hpemax = 16
            dmge = 6
            ecrt = 4
            armore = 1
            fireweakness = 3
        elif monty == 3:
            mnstrtp = ("giant slime cube")
            title = ("the")
            information = ("The obligatory. It has REALLY high armor, but low health. Also fire isnt effective against him. Just keep on hitting till its dead! But watch out, hes really acid.")
            death_message = ("He eats you via phagocytosis. You get solved by the acid. You are dead.")
            hpemax = 12
            dmge = 8
            ecrt = -4
            armore = 7
            fireweakness = 5
            psnchance = 6
            psndur = 2
        elif monty == 4:
            mnstrtp = ("reptiloid with a tie")
            title = ("the")
            information = str("It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue")
            death_message = ("He convinces you to join an terror group, where you blow up yourself. You are dead.")
            hpemax = 20
            dmge = 5
            ecrt = 4
            armore = 2
            fireweakness = 9
        elif monty == 5:
            mnstrtp = ("litte brother")
            title = ("the")
            information =("The worst nightmare...")
            death_message = ("He bites you in the leg. Congratulations, you got infected by Hypermeasles, and you are unvaccinated. You are dead.")
            hpemax = 22
            dmge = 8
            ecrt = 0
            armore = 1
            fireweakness = 20
    elif stage == 4:
        if monty == 1:
            mnstrtp = ("two goblins (2 eyes each)")
            title = ("")
            information = str("So yeah... there are two of them. They attack twice, and swarm around you. High armor is recommended, as each hit will deal less damage as your armor. You will have a hard time if you dont kill one quickly.")
            death_message = ("The goblins are gangbanging you. You die of shame afterwards. You are dead.")
            hpemax = 30
            dmge = 6
            ecrt = 0
            armore = 0
            fireweakness = 13
            amount = 2
        if monty == 2:
            mnstrtp = ("boss")
            title = ("your")
            information = ("If he defeats you, you are dead. If you defeat him, your fired. Also, his fire resistance is strenghent since he had a lot of BBQ partys with the wifes of all employees.")
            death_message = ("He cuts you into pieces, and feeds you to his dachshounds.")
            hpemax = 35
            dmge = 7
            ecrt = 1
            armore = 1
            fireweakness = 7
        if monty == 2:
            mnstrtp = ("boss")
            title = ("your")
            information = ("If he defeats you, you are dead. If you defeat him, your fired. Also, his fire resistance is strenghent since he had a lot of BBQ partys with the wifes of all employees.")
            death_message = ("He cuts you into pieces, and feeds you to his dachshounds.")
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
            death_message = ("GlaDOS makes tests with you. You are doing well, until you get to get the cake. You discover the truth, The cake is a lie. You are dead")
            hpemax = 70
            dmge = 14
            ecrt = 0
            armore = 2
            fireweakness = 15
        elif monty == 2:
            mnstrtp = ("literal devil")
            title = ("the")
            information = str("He is going to send you straight to hell. Also, better not try to attack him with fire. I mean, he comes from hell, he eats fire for breakfast.")
            death_message = ("He takes you to hell, where you dissolve in a puddle of burned flesh and skin. You are dead.")
            hpemax = 65
            dmge = 16
            ecrt = 3
            armore = 0
            fireweakness = 0
        elif monty == 3:
            mnstrtp = ("LoL tryhard")
            title = ("the")
            information = ("He is the most toxiest being in the universe. He is also accucrate as fuck, since he makes nothing else than playing Lol.")
            death_message = ("He defeats you, and you land in the Elo Hell. You try to play your way out, but unfortunaly starve becaus you dont eat anything. You are dead.")
            hpemax = 60
            dmge = 13
            ecrt = 4
            armore = 0
            fireweakness = 10
            psnchance = 6
            psndur = 4
        elif monty == 4:
            mnstrtp = ("whole army")
            title = ("a")
            information = ("Well, you are fucked. Good luck winning against a whole army...")
            death_message = ("You get poked, sliced, chopped, shot, grinded, and spiked by arrows and bolts. You are dead enough for twelve people. You are dead.")
            hpemax = 88
            dmge = 3
            ecrt = 3
            armore = 0
            fireweakness = 16
            amount = 11
        elif monty == 4:
            mnstrtp = ("goblin king")
            title = ("the")
            information = ("He is the king of all goblins, a really heavy armored, brutal guy. Maybe you want to check the help for tips.")
            death_message = ("You get poked, sliced, chopped, shot, grinded, and spiked by arrows and bolts. You are dead enough for twelve people. You are dead.")
            hpemax = 55
            dmge = 15
            ecrt = 3
            armore = 7
            fireweakness = 10

    hpe = hpemax
    print(title + " " + mnstrtp + " appears!")
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
                    
                    print("You attacked for " + str(int(dmg * acc)) + " damage, " + title + " " + mnstrtp + " has only " + str(int(hpe)) + " Hp left!")
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
                    print("As you hit " + title + " " + mnstrtp + ", it exploded and covered you with its organs! You have " + str(hp) + " Hp left and your Dex decreased!")
                    done = True
                else:
                    
                    hpe = hpe - int((dmg - (dmg/4)) * (fireweakness/10))
                    print("You attacked " + title + " " + mnstrtp + " with fire, which dealt " + str(int((dmg - dmg / 5) * (fireweakness/10))) + " fire damage. " + mnstrtp + " has now " + str(hpe) + " left!")
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
                print("wait to wait one round.")
                print("help to see all comments. I know, very useful.")
                print("Bonus tip: Chose crack addict in the class chose screen. It is very stronk.")
            elif do == ("wait"):
                print("You are waiting one turn.")
                done = True
            elif do == ("detox"):
                if psncurdur > 0:
                    print("You cure your poison.")
                    done = True
                else:
                    if detoxprot
                        print("Wtf are you doing? you arent even poisond! 
                done = True
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
                    hp = hp - int(((dmge) * acce - armor))
                    print(title +" "+ mnstrtp + " attacked you for " + str(int(((dmge) * acce - armor))) + " damage! You have " + str(hp) + " HP left!")
                    if psnchance > 0:
                        if (psnchance - psnrsst)-random.randint(1,10) > 0:
                            psndurcur += psndur
                            print("You got poisoned for " + str(psncurdur) + " rounds in total, dealing " + str(stage) + " damage per round until you heal yourself!")
                    if psncurdur > 0:
                        hp = hp - stage
                        if psnrsst > -1:
                            psncurdur = psncurdur - (1 + psnrsst)
                        print("You got " + str(stage) + " poison damage, leaving you with " + str(hp) + " and " + str(psncurdur) + " rounds left poisoned!")
                    
                etimesattacked += 1
        if hp < 1:
            print(death_message)
            fukkerr = input("type anything to close the program")
            exit()    
    else:
        lvlupd = 0
        if stage > 2:
            lvlupd = -1
        if stage > 4:
            lvlupd = -2
            
        print("You killed " + title + " " + mnstrtp + "!")
        if stage == 6:
            print("Yeah!")
        
        else:    
            while lvlupd < 1:
                print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                print("type help to get detailed descriptions of all stats, and help for nerds for really detailed descriptions.")
                print("Additionaly you will regain a bit health.")
                lvlup = (input("What is your choice?"))
                if lvlup == ("hp"):
                    maxhp = int(maxhp + (maxhp/5) * (stage + 1 * 0.5) +1)
                    hp = hp + stage * stage + 1
                    print("You leveled up HP, now you have " + str(maxhp) + " maximum HP!")
                    lvlupd += 1
                elif lvlup == ("dmg"):
                    dmg = int(dmg + stage + 1 + stage / 2)
                    hp = hp + stage * stage + 1
                    print("You leveled up damage, now you have " + str(dmg) + " damage!")
                    lvlupd += 1
                elif lvlup == ("heal"):
                    heal = heal + stage * 2 + 2
                    hp = hp + stage * stage + 1
                    print("You leveled up healing, now you have " + str(heal) + " heal!")
                    lvlupd += 1
                elif lvlup == ("acc"):
                    crtmdf = crtmdf + stage
                    hp = hp + stage * stage + 1
                    print("You leveled up your accuracy, now you have a modifier of " + str(crtmdf/10) + "!")
                    lvlupd += 1
                elif lvlup == ("amr"):
                    armor = armor + stage + stage / 3
                    psnrsst += 1
                    hp = hp + stage * stage + 1
                    print("You leveled up armor, now you have " + str(armor) + " armor!")
                    lvlupd += 1
                elif lvlup == ("dex"):
                    dodge = dodge + 1
                    crtmdfe = crtmdfe - 1
                    hp = hp + stage * stage + 1
                    print("You leveled up dexterity, you are now more eager to dodge attacks!")
                    lvlupd += 1
                elif lvlup == ("help"):
                    print("With hp you level up your maximal Health points, for increased tankiness.")
                    print("With dmg you level up your Damage, which is needed for killing stuff faster.")
                    print("With acc you level up your Accuracy, which increases your critical modifier, which increases your Damage by multiplying it with itself.")
                    print("With heal you level up your healing skill, which is directly added to your HP when healing.")
                    print("With dex you level up your dodging ability, making you more eager to dodge enemy attacks. Even if they hit you, they make less damage, because the ecrt value is also decreased. You shouldnt level dex though, because dex is for casuals.")
                    print("With amr you level up your Armor. Your Armor value is substracted on enemy damage, after the ecrt modifier came to play. This also increases your poison resistence.")
                elif lvlup == ("help for nerds"):
                    print("hp ==> your maxhp + (maxhp/5) * (stage + 1 * 0.5) +1)")
                    print("dmg ==> Your damage + stage + 1 + stage / 2")
                    print("acc ==> your accuracy + stage")
                    print("heal ==> your healing skill + stage * 2 + 2")
                    print("dex ==> your dodge value + 1, enemy crit modifier -1")
                    print("amr ==> your armor + stage + stage / 3")

                else:
                    print("Please make a correct answer")
            else:
                stage = stage + 1
else:
    print("Congratiolations, you have just won the game!")
    fukkerr = input("type anything to close the program")
    if fukkerr == ("fuck you"):
        print("Fukk ju 2")
    exit()
    
               
            
        
            
