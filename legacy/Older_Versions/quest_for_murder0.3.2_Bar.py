import random
gamefinished = False
gameclosed = False
goMenu = False
gamewon = False
exited = False
fukkerr = "close"
maxhp = 18
dmg = 5
heal = 4
#stage vars
stage = 1
stageTo = 1
stageGo = "up"
stagechanged = False
stagechangeddialog = False
stagename = "Craphole"
encounterrandom = 42
lvlupd = 0
crtmdf = 0
acc = 0
armor = 1
acce = 0
crtmdfe = 0
armore = 0
dodge = 1
eweap = ""
#Prolog vars
dialog = 1
randomnumb = 12345678910111213
name = "Creative name."
drinksdrunken = 0
paid = False
#role vars
rolechosen = False
rolechosen2 = False
roleaccept = "shit"
roleacceptbool = False
roledescription = "I d0nt h8 u"
done = False
hpemax = 1
crte = 0
etimesattacked = 0
eturns = 1
multi = 1
dmgfinal = dmg * multi
#various vars
patchesdead = False
#Poison vars
psndur = 4
psnchance = 0
psnrsst = 0
psnleft = 0
detoxprot = True
#current poison duration
psncurdur = 0
#inv vars
healpots = 0
dmgpots = 0
holywater = 0
gold = 0
invdo = "MissingNo"
exittimes = 99
#Role selector
while not gamefinished:
    print("You find yourself in a dark bar. You dont remember anything, and you are slightly confused.")
    print("Your head lays in a puddle of vomit, which is stenching after strong alcohol.")
    print("The Bar keeper, the only other person in this room, nods to you. He says: Well, finally awake, are you? Let me introduce myself. I am Deuhtsh, the owner of this nasty little bar.")
    name = input("So whats your name?")
    print(name + ", you say? Well, it doesnt really matters to me. But I have some good advice for you. You have chosen a bad time to wake up from your slumber- Its the evening of bloodlust!")
    print("You have to be very carefully. If you arent, the monsters are going to take you!")
    print("Which monsters, you do ask?")
    dialog = input("yes/no")
    if dialog == "yes":
        print("You know, goblins, animals, and even worse, Humans. The usual stuff.")
    elif dialog == "no":
        print("Okay, as you want.")
    else:
        print("Whatever that means.")
    print("So this is my EPIC quest for you. End the evening of bloodlust by killing monsters.")
    print("Once this is done, you should return to me. Ill open a bottle of my really good stuff for you.")
    print("After Deuhtsh said this, he takes a huge bottle of whiskey, and makes it empty. He twists his eyes, and falls backwards. You decide to go.")
    print("In the floor, you see several boxes, each with the equip for a special class. You have to decide for one. Why not take them all? Well, because this stupid game doesnt allow it.")
    print("You can be a bandit, a knight or a cleric!")
    stage = 1
    rolechosen2 = False
    while not rolechosen2:
        rolechosen = False
        while not rolechosen:
            role = input("Which class do you choose?")
            if role == "knight":
                roledescription = "The knight is a tank. He has high armor, and high Hp. But he has low Heal and a decreased crit modifier, and isnt that good at dodging. He starts with 1 healing potion and with sword and shield."
                maxhp = 24
                dmg = 5
                armor = 3
                crtmdf = -1
                dodge = -2
                heal = 3
                crtmdfe = 1
                healpots = 1
                dmgpots = 0
                rolechosen = True
            elif role == "bandit":
                roledescription = "An agile assasin. He has a high crit modifier, and is really good at dodging. His damage is absolutely superior, but he has no armor and low health. He starts with a grenade and twin daggers."
                maxhp = 10
                dmg = 7
                armor = 0
                crtmdf = 2
                dodge = 3
                heal = 4
                crtmdfe = -1
                healpots = 0
                dmgpots = 1
                rolechosen = True
            elif role == "cleric":
                roledescription = "A filthy cleric, Patches doesnt like him. He has extremely high Heal, and a bit armored. He starts with a maze."
                maxhp = 14
                dmg = 4
                armor = 1
                crtmdf = 0
                dodge = 1
                heal = 8
                crtmdfe = 0
                psnrsst = 1
                healpots = 0
                dmgpots = 0
                rolechosen = True
            elif role == "glass cannon":
                roledescription = "He kills everything, as long he doesnt get hit."
                maxhp = 1
                dmg = 10
                armor = 0
                crtmdf = 5
                dodge = 0
                heal = 1
                crtmdfe = 20
                healpots = -20000
                dmgpots = 4
                rolechosen = True
            elif role == "godfather":
                roledescription = "Definitly balanced."
                maxhp = 50
                dmg = 9
                armor = 5
                crtmdf = 5
                dodge = 4
                heal = 12
                crtmdfe = -3
                healpots = 10
                dmgpots = 10
                rolechosen = True
            elif role == "crack addict":
                roledescription = "Extremely weak in every aspect, But has a lot of potions."
                maxhp = 8
                dmg = 2
                armor = 0
                crtmdf = 0
                dodge = 2
                heal = 5
                crtmdfe = 0
                psnrsst = 5
                healpots = 3
                dmgpots = 3
                rolechosen = True
            elif role == "sand sack":
                roledescription = "This is for testing purposes"
                maxhp = 200
                dmg = 10
                armor = 0
                crtmdf = 0
                dodge = -20
                heal = 5
                crtmdfe = 1
                psnrsst = -10
                healpots = 4
                dmgpots = 0 
                rolechosen = True
            elif role == "patches":
                print("Nice try.")
            elif role == "yes":
                print("Thats not how this works.")
            else:
                print("Please make a correct answer")
        print(roledescription + "Are you sure to proceed?")
        roleaccept = input("yes/no")
        roleacceptbool = False
        while not roleacceptbool:
            if roleaccept == "yes":
                rolechosen2 = True
                roleacceptbool = True
            elif roleaccept == "no":
                roleacceptbool = True
            else:
                print("Please make a correct answer.")
    hp = maxhp
    print("You have chosen the role " + role + ".")
    print("You leave the bar, unsure what to do. You just wander around, till you find a something... A village! You dont hear any sounds a Village would usually make, like the laughing of children, the barking of dogs. There is only silence and destruction. Even though the village didnt burn, its condition is horrible.")
    print("You enter it, and see some type of letter on a Wall.")
    print("It first page reads:")
    print("Type atk to attack, type heal to heal, type help for more commands")
    print("There are more letters, described with *help*")

    while stage < 6 and not gamefinished:
        if stage == 0:
            print("So you return to the bar. Deuhtsh is staring at you.")
            print("He asks: What do you want here, " + name + "?")
            while stage == 0:
                print("(1)What is the evening of bloodlust?")
                print("(2)How did i get here?")
                print("(3)Who are you?")
                print("(4)I just want to drink something.")
                dialog = input("(5)I just wanted to go.")
                if dialog == "1":
                    print("Well, nobody knows its origins, but everyone knows its consequences. It causes animals, humans and monsters to go mad, with an insatiable thirst for blood. From this point on, the being is no longer able to do social interactions, only the most primitve instincts and the thirst for blood remains.")
                    print("Somehow, beings that are infected by bloodlust arent attacking other infected beings. We dont know if its a curse or maybe heavenly punishment, but it is real, and is going to kill you really fast, if you arent careful.")
                elif dialog == "2":
                    print("Well i really dont know. Sometimes, people are waking up here, with no memory of what happened. They are just here when i dont look for a moment. This is happening since the evening of bloodlust started. You arent the first, and you probably also arent the last one. Thats all i can say to you.")
                elif dialog == "3":
                    print("As i already said, i am Deuhtsh, the owner of this bar. Also, i somehow became the quasi mentor of all poor souls that are awaking here without memories.")
                elif dialog == "4":
                    if drinksdrunken == 0:
                        print("Sure, this one is for free. What do you want?")
                        dialog = input("(1)Siegbräu  (2)Pisswasser  (3)Estus (4)W.A.T.E.R. (5) nothing")
                        paid = True
                    else:
                        print("Sure. What do you want?")
                        dialog = input("(1)Siegbräu 10G (2)Pisswasser 5G  (3)Estus 20G (4)W.A.T.E.R. 2G (5) nothing")
                        paid = True
                    if dialog == "1" and paid:
                        print("Well, here you have a Siegbräu, out of the far Lands of Catarina. You have no idea how hard it is to get it in these times, so enjoy it.")
                        print("As you drink the mug of Siegbräu, it surprisingly tastes really good, for some reason after herbs and onion.")
                        drinksdrunken += 1
                    elif dialog == "2" and paid:
                        print("As you drink the bottle of beer, it tastes like really old water. You decide that you do not want to know what its ingrediences are.")
                        drinksdrunken += 1
                    elif dialog == "3" and paid:
                        print("As you drink the bottle of yellow juice, it burns horrible in your throat, as if you just drank liquid fire.")
                        print("You have to get used to it, says Deuhtsh. It is really hard stuff, but said to have the power to keep one man from dying.")
                        drinksdrunken += 1
                        hp += 7
                    elif dialog == "4" and paid:
                        print("Well, here do you get your glass of W.A.T.E.R. Have fun.")
                        print("The W.A.T.E.R tastes like ordinary water. You feel refreshed.")
                        if drinksdrunken == 0:
                            drinksdrunken += 1
                        hp += 1
                    elif dialog == "5":
                        print("Nothing? Well, thats okay too.")
                elif dialog == "5":
                    print("You decide that its time for you to leave.")
                    stage = 1
                        
            else:
                print("You leave the bar.")
        #Here the Enemy type is selected
        monty = random.randint(1,5)
        amount = 1
        psnchance = 0
        psndur = 0
        if stage == 1:
            stagename = "village"
            if monty == 1:
                mnstrtp = "one-eyed goblin"
                title = "the "
                titleBig = "The "
                information = "This old, one-eyed Goblin has his best days behnd him. Killing him should be no Problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?"
                death_message = "You somehow made it. You got defeated by an old cripple of goblin. I would give you an medal, but unfortunaly you got feeded to 23 hungry goblin childrens. You are dead."
                hpemax = 10
                dmge = 4
                ecrt = 0
                armore = 0
                fireweakness = 10
            elif monty == 2:
                mnstrtp = "really fat cat"
                title = "the "
                titleBig = "The "
                information = "Wow, this cat is REALLY fat. Shes slow, but because of her fat belly quite tanky. Maybe you try fire?"
                death_message = "The cat mistakes you for a sofa, and completely scratches your skin of. You are dead."
                hpemax = 16
                dmge = 2
                ecrt = 0
                armore = 2
                fireweakness = 15
            elif monty == 3:
                mnstrtp = "devil-possessed baby"
                title = "the "
                titleBig = "The "
                information = "This is a baby, possessed by the devil. It doesnt have much health, but explodes when you bring it in contact with fire. So be cautionfull!"
                death_message = "It thinks you are his Mother! How cute! Except it killed all 243 mothers before. And so you. You are dead."
                hpemax = 8
                dmge = 5
                ecrt = 0
                armore = 0
                fireweakness = 50
            elif monty == 4:
                mnstrtp = "pidgeon of doom"
                title = "the "
                titleBig = "The "
                information = "This pidgeon is really annoying. In fact, it is so annoying that you just want to kill it. Which is pretty easy, because its an goddamn pidgeon."
                death_message = "It picks out your eyes, and while stumbling around blindly, you fall with your head into your weapon. You are dead."
                hpemax = 4
                dmge = 2
                ecrt = 5
                armore = 0
                fireweakness = 9
                psnchance = 2
                psndur = 1
            elif monty == 5:
                mnstrtp = "bloodlusting villager"
                title = "the "
                titleBig = "The "
                information = "A villager, corrupted by the evening of bloodlust. He has a flail, along with a rusty sickle."
                dialog = random.randint(1,2)
                if dialog == 1:
                    death_message = "He flails your bones to dust. While they are still in your body. You are dead."
                else:
                    death_message = "He cuts your throat with his sickle, and lustfully drinks your blood directly out of you caritod artery. You are dead."
                hpemax = 10
                dmge = 3
                armore = 1
                fireweakness = 12
        elif stage == 2:
            stagename = "great grasslands"
            if monty == 1:
                mnstrtp = "two-eyed goblin"
                title = "the "
                titleBig = "The "
                information = "This goblin is a bit tougher than the last one. He will maybe not be that that easy to kill. He also has a butter knife and a leather armor!"
                death_message = "He cuts your head off. You will may ask how he does that with a butter knife? Well, it takes lots of time and is a lot of Pain, but this doesnt matter to you. You are dead."
                hpemax = 15
                dmge = 6
                ecrt = 1
                armore = 2
                fireweakness = 13
            elif monty == 2:
                mnstrtp = "poisonos snake"
                title = "the "
                titleBig = "The "
                information = "This is an poisonos snake. I think thats nuff said."
                death_message = "It bites you, and poisons you. What did you expect? You are dead."
                hpemax = 12
                dmge = 4
                ecrt = 4
                armore = 0
                fireweakness = 10
                psnchance = 4
                psndur = 3
            elif monty == 3:
                mnstrtp = "paper-man!"
                title = "the "
                titleBig = "The "
                information = "This is a superhero, completely out of paper. His arms are really sharp, so watch out you dont get hit! What can I say except fire?"
                death_message = "It cuts you several times, till you die of wound infection. You are dead."
                hpemax = 16
                dmge = 6
                ecrt = 5
                armore = -2
                fireweakness = 420
            elif monty == 4:
                mnstrtp = "really fat old lady"
                title = "the "
                titleBig = "The "
                information = "Now this is probably the owner of the really fat cat. I think they are fitting very well. So same as the cat."
                death_message = "She sits down on you, and you get squished. Yeah, she is REALLY fat. You are dead."
                hpemax = 25
                dmge = 4
                ecrt = -1
                armore = 4
                fireweakness = 11
            elif monty == 5:
                mnstrtp = "child soldier"
                title = "the "
                titleBig = "The "
                information = "Well, its an Child. With an AK-47. Its heavy-armored, but has a terrible precision. That should be easy, right?"
                death_message = "It manages to shot you in the head. You are dead."
                hpemax = 10
                dmge = 10
                ecrt = -4
                armore = 3
                fireweakness = 11
        elif stage == 3:
            stagename = "swamp"
            if monty == 1:
                mnstrtp = "three-eyed goblin"
                title = "the "
                titleBig = "The "
                information = "What the chernobyl type of fuck is this??"
                death_message = "He tears out his third eyeball, and shoves it in your throat. You suffacate painfully. You are dead. "
                hpemax = 18
                dmge = 5
                ecrt = 3
                armore = 1
                fireweakness = 15
            elif monty == 2:
                mnstrtp = "imp"
                title = "the "
                titleBig = "The "
                information = "A nasty flying fucker who pokes you with his Pitchfork. Its a creature, straight out of Hell."
                death_message = "He pokes his pitchfork directly in your guts, and twirls them. You are dead."
                hpemax = 16
                dmge = 6
                ecrt = 4
                armore = 1
                fireweakness = 3
            elif monty == 3:
                mnstrtp = "giant slime cube"
                title = "the "
                titleBig = "The "
                information = "The obligatory. It has REALLY high armor, but low health. Also fire isnt effective against him. Just keep on hitting till its dead! But watch out, hes really acid."
                death_message = "He eats you via phagocytosis. You get solved by the acid. You are dead."
                hpemax = 12
                dmge = 8
                ecrt = -4
                armore = 7
                fireweakness = 5
                psnchance = 6
                psndur = 2
            elif monty == 4:
                mnstrtp = "reptiloid with a tie"
                title = "the "
                titleBig = "The "
                information = "It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue"
                death_message = "He convinces you to join an terror group, where you blow up yourself. You are dead."
                hpemax = 20
                dmge = 5
                ecrt = 4
                armore = 2
                fireweakness = 9
            elif monty == 5:
                mnstrtp = "litte brother"
                title = "the "
                titleBig = "The "
                information = "The worst nightmare..."
                death_message = "He bites you in the leg. Congratulations, you got infected with Hypermeasles, and you are unvaccinated. You are dead."
                hpemax = 22
                dmge = 8
                ecrt = 0
                armore = 1
                fireweakness = 20
        elif stage == 4:
            stagename = "source outskirts"
            if monty == 1:
                mnstrtp = "two goblins (2 eyes each)"
                title = ""
                information = "So yeah... there are two of them. They attack twice, and swarm around you. High armor is recommended, as each hit will deal less damage as your armor. You will have a hard time if you dont kill one quickly."
                death_message = "The goblins are gangbanging you. You die of shame afterwards. You are dead."
                hpemax = 34
                dmge = 7
                ecrt = 0
                armore = 2
                fireweakness = 13
                amount = 2
            elif monty == 2:
                mnstrtp = "boss"
                title = "your "
                titleBig = "Your "
                information = "If he defeats you, you are dead. If you defeat him, your fired. Also, his fire resistance is strenghent since he had a lot of BBQ partys with the wifes of all employees."
                death_message = "He cuts you into pieces, and feeds you to his dachshounds."
                hpemax = 42
                dmge = 10
                ecrt = 1
                armore = 1
                fireweakness = 7
            elif monty == 3:
                mnstrtp = "spider nest"
                title = "the"
                titleBig = "A "
                information = "Aww, lots of baby spiders! Hans, get se Flammenwerfer!!"
                death_message = "See it from a positive side, now all these cute spiders will have a dead body to play in! Btw: You are dead."
                hpemax = 45
                dmge = 7
                ecrt = 2
                armore = 0
                fireweakness = 16
                psnchance = 2
                pnsdur = 1
                amount = 5
            if role == "cleric":
                mnstrtp = "Patches"
                title = ""
                titleBig = ""
                information = "He fights with a spear and a tower shield. He really hates Clerics, and really likes kicking them into Traps. Curiosly, he doesnt seem to be affected by the curse of the evening of bloodlust."
                death_message = "He kicks you of a cliff, right into a bunch of skeletons. You are dead."
                hpemax = 44
                dmge = 6
                ecrt = 5
                armore = 3
                fireweakness = 10
            elif monty == 4:
                mnstrtp = "SUCKubus"
                title = "the "
                titleBig = "The "
                information = "Maybe defeat isnt always the worst option..."
                death_message = "She SUCKS it all out of you. And i do mean all: Blood, Sweat, Tears, Brain fluid... You are dead."
                hpemax = 38
                dmge = 12
                ecrt = 1
                armore = 0
                fireweakness = 4
            elif monty == 5:
                mnstrtp = "crying boy"
                title = "the "
                titleBig = "The "
                information = "He shoots tears at you. And for some reason, they hurt."
                death_message = "After a lot of tears, you suddenly pop and covering the floor with your inner organs. You are dead."
                hpemax = 38
                dmge = 8
                ecrt = 4
                armore = 0
                fireweakness = 13
        elif stage == 5:
            stagename = "champions plateau"
            if monty == 1:
                mnstrtp = "GLaDOS"
                title = ""
                information = "The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. "
                death_message = "GlaDOS makes tests with you. You are doing well, until you get to get the cake. You discover the truth, The cake is a lie. You are dead"
                hpemax = 70
                dmge = 14
                ecrt = 0
                armore = 2
                fireweakness = 15
            elif monty == 2:
                mnstrtp = "literal devil"
                title = "the "
                titleBig = "The "
                information = "He is going to send you straight to hell. Also, better not try to attack him with fire. I mean, he comes from hell, he eats fire for breakfast."
                death_message = "He takes you to hell, where you dissolve in a puddle of burned flesh and skin. You are dead."
                hpemax = 65
                dmge = 16
                ecrt = 3
                armore = 0
                fireweakness = 0
            elif monty == 3:
                mnstrtp = "LoL tryhard"
                title = "the "
                titleBig = "The "
                information = "He is the most toxiest being in the universe. He is also accucrate as fuck, since he makes nothing else than playing Lol."
                death_message = "He defeats you, and you land in the Elo Hell. You try to play your way out, but unfortunaly starve because you dont eat anything. You are dead."
                hpemax = 60
                dmge = 13
                ecrt = 4
                armore = 0
                fireweakness = 10
                psnchance = 6
                psndur = 4
            elif monty == 4:
                mnstrtp = "army"
                title = "the "
                titleBig = "A whole"
                information = "Well, you are fucked. Good luck winning against a whole army..."
                death_message = "You get poked, sliced, chopped, shot, grinded, and spiked by arrows and bolts. You are dead enough for twelve people. You are dead."
                hpemax = 88
                dmge = 4
                ecrt = 3
                armore = 0
                fireweakness = 16
                amount = 11
            elif monty == 5:
                mnstrtp = "goblin king"
                title = "the "
                titleBig = "The "
                information = "He is the king of all goblins, a really heavy armored, brutal guy. Maybe you want to check the help for tips. And yes, he does have 5 eyes."
                death_message = "You get sacrificed to some kind of goblin godess. You are dead."
                hpemax = 55
                dmge = 15
                ecrt = 3
                armore = 7
                fireweakness = 10



        if stagechanged:
            if stagename == "village":
                print("You return to the devastated village.")
            elif stagename == "great grasslands":
                print("You enter the great grasslands; a huge area full of grass, rivers, old, lonely trees and monsters.")
            elif stagename == "swamp":
                print("You enter the swamp. It is a dangerous, poisonos area, with many possibility to sink in the bog. You remember an old saying: At full moon, swamp chunks are slime chunks... You have no idea what this is supposed to mean.")
            elif stagename == "source outskirts":
                print("You enter the source outskirts, a hilly, vast area with wany high mountains. Here and there are vulcanos, lava streams, and oil lakes. On the horizont you see the plateau of champions...")
            elif stagename == "champions plateu":
                print("You finally reached the champions plateau, the place where the strongest of the strongest monsters live... And your oppurtunity to end the evening of bloodlust.")
                


        eweap = ""
        #Attributes
        attr = random.randint(0,100)
        if attr > 50 and attr < 100:
            adjective = ""
        elif attr > 99:
            adjective = "shiny "
        elif attr < 51 and attr > 39:
            adjective = "strong "
            dmge += stage
        elif attr < 41 and attr > 29:
            adjective = "weak "
            dmge = dmge - stage
        elif attr < 31 and attr > 19:
            adjective = "healthy "
            hpemax += stage*5
        elif attr < 21 and attr > 9:
            adjective = "unhealthy "
            hpemax += -stage*5
        elif attr < 11 and attr > -1:
            adjective = "cloned "
            amount += 1
            dmge = int((dmge + 3)/2)
                

        hpe = hpemax
        if stagename == "village":
            encounterrandom = random.randint(1,3)
            if encounterrandom == 1:
                print("In a shady side street, you hear something screaming. You run to it, but you only find a horribly torn corpse in wrecked pieces of armor. Resisting the urge to vomit, you turn yourself back to the entrance. But there is something...")
                print(titleBig + adjective + mnstrtp + eweap + " attacks you in the twilight of the street!")
            elif encounterrandom == 2:
                print("You see an old grocery store, it seems to be abandoned. You enter it in search of some goodies, you dont think the owner will have something against it...")
                print("You search in the building, but you dont find anything except a lot of non-human looking dung and spiderwebs. But suddenly something dashes at you, and you fall right into a table, which bursts.")
                print("You get up, but now there is " + title + adjective + mnstrtp + eweap + " attacking you!")
            elif encounterrandom == 3:
                print("You see the marketplace. Its devastated, plundered, from the formerly beautiful stands are just smoking splitters. There are no merchants there, dead or alive. Sunken in thought, you turn away. Jus as you want to go, you hear something.")
                print(titleBig + adjective + mnstrtp + eweap + " shovels itself free from splinters and attacks you!")

        elif stagename == "great grasslands":
            encounterrandom = random.randint(1,3)
            if encounterrandom == 1:
                print("You see an old, old tree, surrounded by many tree stumps. It is a sad appearance, and you decide to make your rest here. You think about god and the world, until you, hours later, hear something nearing, and roaring. It sounds almost like a chainsaw...")
                eweap = " with a chain saw"
                dmge += 3
                print(titleBig + adjective + mnstrtp + eweap + " sprints at you! Determined to save this tree, you fight back.")
            elif encounterrandom == 2:
                print("There is a cave, and for whatever stupid reason you decide to explore it. Inside you find a grenade, which you put to your arsenal. As you want to leave, something blocks your way...")
                dmgpots += 1
                print(titleBig + adjective + mnstrtp + " grunts at you and attacks you!")
            elif encounterrandom == 3:
                print("You find a abandoned campfire, burned down for a long time. There is a can with baked beans, already cooked... But do you really want to eat it?")
                dialog = input("yes/no")
                if dialog == "yes":
                    print("You decide to eat them.")
                    randomnumb = random.randint(1,3)
                    if randomnumb == 1:
                        print("They do not taste really good, but you still regain a bit of health.")
                        hp += 5
                        if hp > hpmax:
                            hp = hpmax
                    else:
                        print("They taste awfull, and you got food poison!")
                        psncurdur = 4
                else:
                    print("You decide not to eat them.")
                print("In the time you decided about the baked beans, a monster came! " + titleBig + adjective + mnstrtp + " seems to be hungry, but not to be interested in baked beans...")
                 
        elif stagename == "swamp":
            encounterrandom = random.randint(1,3)
            if encounterrandom == 1:
                print("On your wandering through the swamp, you step accidently in a moor... You somehow get out, but the noises you made upon doing so lured a monster to you!")
                print(titleBig + adjective + mnstrtp + " appears and lusts for your blood!")
            elif encounterrandom == 2:
                print("You find a old hut. Inside you find a couldron, lots of unreadable books and destroyed potions. Only a Health potion seems to be intact. You take it with you. You leave the hut, but in front of it there is now a monster, which promptly attacks you!")
                print("Its " + title + adjective + mnstrtp + eweap + "!")
            elif encounterrandom == 3:
                print("You wander for hours, through a forest of swamp shrubs. Then, seemingly out of nothing, you hear something behind you... It was an ambush!")
                print(titleBig + adjective + mnstrtp + " attacks you!")
        elif stagename == "source outskirts":
            encounterrandom == random.randint(1,3)
            if encounterrandom == 1:
                print("")
                
            








            
        print(titleBig + adjective + mnstrtp + " appears!")
        while hpe > 0 and hp > 0 and not gamefinished:
            if maxhp < hp:
                hp = maxhp
            while not done and not gamefinished and hp > 0:
                
                do = input("What ya gonna do?")
                if do == "atk":
                    acc = random.randint(7,13)/10 +(crtmdf/10)
                    hpe = hpe - int(dmg*acc)
                    if hpe < 1:
                        print("You attacked for " + str(int((dmg * acc)*multi)) + " damage, which was a lethal hit!")
                    else:
                        
                        print("You attacked for " + str(int(dmg * acc)) + " damage, " + title + mnstrtp + " has only " + str(int(hpe)) + " Hp left!")
                    done = True
                elif do == "heal":
                    hp = hp + heal
                    if maxhp < hp:
                        hp = maxhp
                    print("You healed yourself for " + str(heal) + " Hp, you now have " + str(hp) + " Hp left!")
                    done = True
                elif do == "info":
                    print(information)
                elif do == "fire":
                    if mnstrtp == "devil-possessed baby":
                        hpe = 0
                        hp = hp - (10 + random.randint(2,5) - armor)
                        dodge = dodge - 1
                        crtmdfe = crtmdfe + 1
                        print("As you hit " + title + mnstrtp + ", it exploded and covered you with its organs! You have " + str(hp) + " Hp left and your Dex decreased!")
                        done = True
                    else:
                        
                        hpe = hpe - int((dmg - (dmg/4)) * (fireweakness/10))
                        if hpe > 0:
                            print("You attacked " + title + mnstrtp + " with fire, which dealt " + str(int((dmg - dmg / 5) * (fireweakness/10))) + " fire damage. " + mnstrtp + " has now " + str(hpe) + " left!")
                        else:
                            print("You burned " + title + adjective + mnstrtp + " to ashes... Ashes with a smell of BBQ.")
                        done = True
                            
                elif do == "status":
                    print("Hp= " + str(hp) + " from " + str(maxhp))
                    print("Dmg= " + str(dmg))
                    print("crtmdf= " + str(crtmdf))
                    print("armor= " + str(armor))
                    print("heal= " + str(heal))
                    print("dodge= " + str(dodge))
                    print("crtmdfe= " + str(crtmdfe))
                elif do == "help":
                    print("atk to attack. Bonus hint: Attacking is key in killing enemys. Thank me later")
                    print("heal to heal. It heals you about your your heal value.")
                    print("fire to attack with fire damage. Fire does deal less base damage, but penetrates armor and is more or less efficient on specific enemys.")
                    print("detox to cure poison.")
                    print("info to gather bonus informations about your enemy.")
                    print("status to get info about yourself.")
                    print("enemystatus to see stage, stagename and enemys Hp.")
                    print("wait to wait one round.")
                    print("help to see all comments. I know, very useful.")
                    print("suicide to end run, exit to exit the program.")
                    print("mainmenu to start a new run immediatly.")
                    print("Bonus tip: Chose crack addict in the class chose room. It is very stronk.")
                elif do == "wait":
                    print("You are waiting one turn.")
                    done = True
                elif do == "enemystatus":
                    print("stage = " + str(stage))
                    print("stagename = " + stagename)
                    print("enemy hp = " + str(hpe))
                
                elif do == "detox":
                    if psncurdur > 0:
                        print("You cure your poison.")
                        done = True
                    else:
                        if detoxprot:
                            print("Wtf are you doing? You arent even poisoned!")
                            detoxprot = False
                        else:
                            print("As you want...")
                            done = True
                elif do == "inv":
                    print("Type the number of your choice.")
                    invdo = input("(1) Healing potion(" + str(healpots) + ")  (2) Grenade(" + str(dmgpots) + ")   (3) Exit(" + str(exittimes) + ")")
                    if invdo == "1":
                        if healpots > 0:
                            hp += int(heal*2.5)
                            healpots += -1
                            print("You healed yourself for " + str(int(heal*2.5)) + " Hp")
                            done = True
                        else:
                            print("You dont have any healing potions left.")
                    elif invdo == "2":
                        if dmgpots > 0:
                            hpe += int(-(dmg*2.5-armore))
                            dmgpots += -1
                            if hpe > 0:
                                print("You throw the grenade on " + title + mnstrtp + " , which dealt " + str(int(dmg*2.5-armore)) + " Damage. Your enemy has " + str(hpe) + " Hp left.")
                            else:
                                print("You make " + title + mnstrtp + " explode into a million small pieces.")
                            done = True
                        else:
                            print("You dont have any grenades left.")
                    elif invdo == "3":
                        exittimes += -1
                        if exittimes == 0:
                            print("You have serious dedication. In fact, you tried it so long that your skin became hard. Your armor increased.")
                            armor += 1
                        if exittimes == -5:
                            print("You waited longer, and died of old weakness. You are dead.")
                            death_message = ""
                            hp = -20000
                    
                #Little codes
                elif do == "FullHeal":
                    hp = maxhp
                elif do == "Invincible":
                    armor = 200
                elif do == "suicide":
                    hp = 0
                    death_message = "You end self by hitting your weapon through your stomach."
                    if role == "cleric":
                        death_message = "You end self by hitting your weapon through your stomach. I just dont know how you did this with a Mace."
                elif do == "OneHit":
                    dmg = 200
                elif do == "exit":
                    do = input("Really? (yes/no)")
                    if do == "yes":
                        gamefinished = True
                        gameclosed = True
                        exited = True
                elif do == "stageSkip":
                    stageTo = int(input(""))
                    stage = stageTo
                elif do == "mainmenu":
                    gamefinished = True
                    goMenu = True
                    
                else:
                    print("Please make a correct answer.")
            done = False
            if hpe > 0 and not gamefinished:
                etimesattacked = 0
                eturns = int(amount * hpe/hpemax)
                if eturns < 1:
                    eturns = 1
                while etimesattacked < eturns:
                    if dodge + random.randint(0,10) > 9:
                        print( title + adjective + mnstrtp + " attacked, but you dodged the attack!")
                    else:
                        acce = float((random.randint(5,11)+stage)/10 +((crtmdfe+crte)/10))
                        hp = hp - int(((dmge) * acce - armor))
                        if int(((dmge) * acce - armor)) > 0:
                            print(title + mnstrtp + " attacked you for " + str(int(((dmge) * acce - armor))) + " damage! You have " + str(hp) + " HP left!")
                        else:
                            print(title + mnstrtp + " attacked you, but didn`t do any damage!")
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
                fukkerr = input("type close to close the program, anything else to restart.")
                if fukkerr == "fuck you":
                    print("Fukk ju 2")
                elif fukkerr == "close":
                    gameclosed = True
                
        else:
            if not gamefinished:
                lvlupd = 0
                if stage > 2:
                    lvlupd = -1
                if stage > 4:
                    lvlupd = -2
                if adjective == "shiny":
                    lvlupd += -1
                print("You killed " + title + mnstrtp + "!")
                stagego = input("Do you want to go forward, go backward, or stay?")
                stagechangeddialog = False
                stagechanged = False
                while not stagechangeddialog:
                    if stagego == "up":
                        print("You decide to go an area forwards.")
                        stage += 1
                        stagechanged = True
                        stagechangeddialog = True
                    elif stagego == "down":
                        print("You decide to go an area downwards.")
                        stage += -1
                        stagechanged = True
                        stagechangeddialog = True
                    elif stagego == "stay":
                        print("You decide to wander around a bit in this area.")
                        stagechangeddialog = True
                    else:
                        print("Please make a correct answer.")
                        stagego = input("Type forward, backward or stay.")
                   
                
            if stage == 6 and not gamefinished:
                print("Yeah!")
                gamewon = True
            
            else:    
                while lvlupd < 1 and not gamefinished:
                    print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                    print("type help to get detailed descriptions of all stats, and help for nerds for really detailed descriptions.")
                    print("Additionaly you will regain a bit health.")
                    lvlup = (input("What is your choice?"))
                    if lvlup == "hp":
                        maxhp = int(maxhp + (maxhp/5) * (stage + 1 * 0.5) +1)
                        hp = hp + stage * stage + 1
                        print("You leveled up HP, now you have " + str(maxhp) + " maximum HP!")
                        lvlupd += 1
                    elif lvlup == "dmg":
                        dmg = int(dmg + stage + 1 + stage / 2)
                        hp = hp + stage * stage + 1
                        print("You leveled up damage, now you have " + str(dmg) + " damage!")
                        lvlupd += 1
                    elif lvlup == "heal":
                        heal = heal + stage * 2 + 2
                        hp = hp + stage * stage + 1
                        print("You leveled up healing, now you have " + str(heal) + " heal!")
                        lvlupd += 1
                    elif lvlup == "acc":
                        crtmdf = crtmdf + stage
                        hp = hp + stage * stage + 1
                        print("You leveled up your accuracy, now you have a modifier of " + str(crtmdf/10) + "!")
                        lvlupd += 1
                    elif lvlup == "amr":
                        armor = int(armor + stage + stage / 3)
                        psnrsst += 1
                        hp = hp + stage * stage + 1
                        print("You leveled up armor, now you have " + str(armor) + " armor!")
                        lvlupd += 1
                    elif lvlup == "dex":
                        dodge = dodge + 1
                        crtmdfe = crtmdfe - 1
                        hp = hp + stage * stage + 1
                        print("You leveled up dexterity, you are now more eager to dodge attacks!")
                        lvlupd += 1
                    elif lvlup == "help":
                        print("With hp you level up your maximal Health points, for increased tankiness.")
                        print("With dmg you level up your Damage, which is needed for killing stuff faster.")
                        print("With acc you level up your Accuracy, which increases your critical modifier, which increases your Damage by multiplying it with itself.")
                        print("With heal you level up your healing skill, which is directly added to your HP when healing.")
                        print("With dex you level up your dodging ability, making you more eager to dodge enemy attacks. Even if they hit you, they make less damage, because the ecrt value is also decreased. You shouldnt level dex though, because dex is for casuals.")
                        print("With amr you level up your Armor. Your Armor value is substracted on enemy damage, after the ecrt modifier came to play. This also increases your poison resistence.")
                    elif lvlup == "help for nerds":
                        print("hp ==> your maxhp + (maxhp/5) * (stage + 1 * 0.5) +1), rounded down")
                        print("dmg ==> Your damage + stage + 1 + stage / 2, rounded down")
                        print("acc ==> your accuracy + stage")
                        print("heal ==> your healing skill + stage * 2 + 2, rounded down")
                        print("dex ==> your dodge value + 1, enemy crit modifier -1")
                        print("amr ==> your armor + stage + stage / 3, rounded down")

                    else:
                        print("Please make a correct answer")
                
                
    else:
        if not goMenu:
            if gamewon:
                print("Congratulations, you have just won the game!")
            gamefinished = True
            if not exited:
                fukkerr = input("Type close to close the program, anything else to restart.")
        if fukkerr == ("fuck you"):
            print("Fukk ju 2")
        elif fukkerr == ("close"):
            gameclosed = True
        if not gameclosed:
            gamefinished = False
        
        #In this project went hours of labor and music, Dark Souls 3 Ost, Cosmo Sheldrake, Sabaton. It is still great fun to work on it, and i cant wait to see the end product.
                   
                
            
                

