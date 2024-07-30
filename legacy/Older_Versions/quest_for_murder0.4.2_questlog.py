import random

#To Do:
#-Quest log (done)
#-Armmor and Weapons
#-Special abilities
#-Gold and Merchants
patchesdead = False
gamefinished = False

while not gamefinished:
    gamefinished = False
    gameclosed = False
    goMenu = False
    gamewon = False
    exited = False
    fukkerr = "close"
    maxhp = 18
    dmg = 5
    heal = 4
    #quest log
    questlog = []
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
    #Monster vars
    mnstrtp = ""
    mnstrchoosen = False
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
    sirendead = False
    gkingdead = False
    reptiloiddead = False
    isaacdead = False
    GLaDEaD = False
    hagcalm = False
    hagboss = False
    hagvisited = False
    pgrec = False
    swahu = False
    #Poison vars
    psndur = 4
    psnchance = 0
    psnrsst = 0
    psnleft = 0
    detoxprot = True
    #current poison duration
    psncurdur = 0
    #inv vars
    inv = []
    healpots = 0
    dmgpots = 0
    holywater = 0
    gold = 0
    invdo = "MissingNo"
    exittimes = 99
    #Start of the Game
    print("You find yourself in a dark bar. You do not remember anything, and you are slightly confused.")
    print("Your head lays in a puddle of vomit, which is stenching like strong alcohol.")
    name = input("The Bar keeper, the only other person in this room, nods to you. He says: \"Well, finally awake, are you? Let me introduce myself. I am Deuhtsh, the owner of this nasty little bar. So what is your name?\"")
    print("\""+ name + ", you say? Well, it doesnt really matters to me. But I have some good advice for you. You have chosen a bad time to wake up from your slumber- Its the evening of bloodlust!")
    print("You have to be very carefully. If you are not careful, the monsters are going to take you!")
    print("Which monsters, you do ask?\"")
    dialog = input("yes/no")
    if dialog == "yes":
        print("\"You know, goblins, animals, and even worse, humans, infested with the bloodlust. The usual stuff.")
    elif dialog == "no":
        print("\"Okay, as you want.")
    else:
        print("\"Whatever that means.")
    print("So this is my EPIC quest for you. End the evening of bloodlust by killing monsters. For this, I give you the quest log. With this tool you will be able to quickly remind you of your actions.")
    print("Once you are finished with, make sure to return to me. I will open a bottle of my really good stuff for you.\"")
    questlog.append("Quest: End the evening of bloodlust! ////   Just end it as Deuhtsh said, kill monsters.")
    print("After Deuhtsh said this, he takes a huge bottle of whiskey, and drinks it faster than you can look. His eyes twist, and he falls backwards. You decide to go.")
    print("In the floor, you see several boxes, each with the equip for a special class. You have to decide for one. Why not take them all? Well, because this stupid game doesnt allow it.")
    print("You can be a bandit, a knight or a cleric!")
    stage = 1
    rolechosen2 = False
    while not rolechosen2:
        rolechosen = False
        while not rolechosen:
            #Role selector
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
                psnrsst = 0
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
                psnrsst = 0
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
                dmg = 15
                armor = 0
                crtmdf = 5
                dodge = 0
                heal = 0
                crtmdfe = 200000
                healpots = -20000
                psnrsst = 0
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
                roledescription = "This is for testing Puroses."
                maxhp = 200
                dmg = 4
                armor = 0
                crtmdf = 0
                dodge = -20
                heal = 5
                crtmdfe = 1
                psnrsst = 0
                healpots = 69
                dmgpots = 69
                rolechosen = True
            elif role == "patches":
                if not patchesdead:
                    print("Nice try, not yet.")
                else:
                    roledescription = "The equipment of the unbreakable Patches, strapped of his corpse. At the end, he wasnt that unbreakable. It contains a spear, a tower shield and a reinforced leather armor, dyed black. "
                    maxhp = 200
                    dmg = 4
                    armor = 0
                    crtmdf = 0
                    dodge = -20
                    heal = 5
                    crtmdfe = 1
                    psnrsst = 0
                    healpots = 69
                    dmgpots = 69
                    rolechosen = True
            elif role == "yes":
                print("Thats not how this works.")
            else:
                print("Please make a correct answer")
        print(roledescription + " Are you sure to proceed?")
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
                roleaccept = input("yes/no")
                
    hp = maxhp
    print("You have chosen the role " + role + ".")
    print("You leave the bar, unsure what to do. You just wander around, till you find something... A village! You dont hear any sounds a village would usually make, like the laughing of children, the barking of dogs. There is only silence and destruction. Even though the village didnt burn out, its condition is horrible.")
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
                    print("Well I really dont know. Sometimes, people are waking up here, with no memory of what happened. They are just here when I dont look for a moment. This is happening since the evening of bloodlust started. You arent the first, and you probably also arent the last one. Thats all I can say to you.")
                elif dialog == "3":
                    print("As I already said, I am Deuhtsh, the owner of this bar. Also, I somehow became the quasi mentor of all poor souls that are awaking here without memories.")
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
        if stagename == "swamp hut":
            hagvisited = True
            if not GLaDEaD:
                print("You decide to rest at the Hut. A few minutes later an old Woman appears, and looks at you in scept.")
                print("\"Who are you? And why are you in front of my house? Answer!\"")
                while stagename == "swamp hut":
                    print("(1) I am " + name + ", I came to your house while wandering in the swamp. As I stayed here for a little rest, a monster came and I killed it.")
                    print("(2) Who are you? Anybody could just come and say its her house and be rude to me.")
                    print("(3) Where am I?")
                    print("(4) Can you tell me anything about this Land? I sadly lost my memory.")
                    print("(5) I am leaving now.")
                    dialog = input("")
                    if dialog == "1":
                        if hagcalm:
                            print("\"You know you already said that, do you? Well, as i said, theres a healing potion in the hut\".")
                        else:
                            print("\"Oh, I am sorry, I didnt knew that.\" She looks to the corpse of " + title + mnstrtp + ". \"Thanks for that, that would have been a bad surprise if you were not here.")
                            print("There is a healing potion in the hut, take it if you want. By the way, Im Cehl, it is nice to meet you.\"")
                            hagcalm = True
                    elif dialog == "2":
                        if hagcalm:
                            print("\"Well, you are probably right. I am Cehl, and I live in this hut. I am nothing but an old hag, which was drawn in this land by the forces of the evening of bloodlust.\"")
                        else:
                            print("\"Who the hell do you think you are?? You are coming to my house, and have the audacity to ask me what im doing here?? Leave! Now!\"")
                    elif dialog == "3":
                        if hagcalm:
                            print("\"Do you mean specifically here or in which land you are?\"")
                            dialog = input("here/this land")
                            if dialog == "here":
                                print("\"You are at my house, deep in the swamp. There is really nothing much here, except some fine mushrooms and a lot of monsters. \"")
                            elif dialog == "this land":
                                print("\"I guess you woke up in Deuhtshs bar, did you? Well, I cant tell you really much about this land before the evening of bloodlust, for I am not born here. I got drawn into this world, also waking up in the bar. This is now really long time ago. But I think the same happened to you, although I dont know why it happened.")
                                print("My best guess is that the bloodlust searches for prey and draws them through room, time, hell, maybe even through dimensions! For some reason they all wake up in the bar. Most of them die early, only a few persevere. I dont know what, but something is special about Deuhtsh. In all the time I spent here, he seems to have aged no bit.\"")
                            else:
                                print("\"What?\"")
                        else:
                            print("\"I would not know what it interests you. Now get away, thug!\"")
                    elif dialog == "4":
                        if hagcalm:
                            print("\"Well, actually yes. If you should someday come to the plateau of champions, then wander till you come to an wheat field. In the center there should be an type of cabin, were should be some interesting stuff.\" Her eyes seem to glow as she said this.")
                            questlog.append("Quest: Search the cabin in the fields and get the loot out of it.")
                            hagboss = True
                        else:
                            print("\"Get away, you bandit!\"")
                    elif dialog == "5":
                        if hagcalm:
                            print("\"Thanks for killing " + title + mnstrtp + " for me. See you again!\"")
                        else:
                            print("\"Yeah, get away already, moron!\"")
                        stagename = "swamp"
            else:
                print("You return to the Hut. Cehl sits infront of it, cutting mushrooms in a stew. When she notices you, her eyes get brighter.")
                print("\"Hello " + name + "! Coming over again, do you? Well, just in time, I made a delicious soup which will be ready in a few minutes.\"")
                while stagename == "swamp hut":
                    print("(1) I was at the cabin like you told me, what happened then is a long story...")
                    print("(2) What is in this soup?")
                    print("(3) I am sorry, but I have to leave now.")
                        
                    dialog = int(input(""))
                    if dialog == 1:
                        print("You start telling the story of what you found in and under the cabin. Once you are finished, Cehl seems to be thinking. She sits there for a few minutes, not saying a word, until she finally says:")
                        print("\"I did not expect this to be honest. When I left there, I made a deal with her- I will send her a new test subject. I am really sorry that this had to be you. Well, I guess I have to apologize. But please, take this as compensation.")
                        print("She goes into the hut, and comes back with the futuristic gun you saw earlier.")
                        print("\"Here, this is for you. It is a device to create quantum tunnels, modified to work on every even surface. It will maybe come in handy while traveling. Now please, go. I do not want you to see my face who sent you right into a trap. But I am glad you made it out alive, and even more, defeated her.")
                        print("As she asked, you leave, a bit confused about the meeting.")
                        pgrec = True
                        stagename = "swamp"
                    elif dialog == 2:
                        print("\"Well, just a bit meat of the monster you killed earlier, plus a few herbs. Do you want to have some? It is ready now.\"")
                        dialog = input("yes/no")
                        if dialog == "yes":
                            print("\"Here, have some.\"")
                            print("It does surprisingly taste really good!")
                            hp += maxhp/2
                        else:
                            print("Well, that means more soup for me.")
                    elif dialog == 3:
                        print("\"Well, leaving so soon? Then here, take at least this!\"")
                        print("She gives you a grenade. \"Do not ask me where I got it, may it help you on your journy!\"")
                        dmgpots += 1
                        stagename = "swamp"
        #Here the Enemy type is selected
        monty = random.randint(1,5)
        amount = 1
        psnchance = 0
        psndur = 0
        while mnstrchoosen == False:
            if stage == 1:
                stagename = "village"
                if monty == 1:
                    mnstrtp = "one-eyed goblin"
                    title = "the "
                    titleBig = "The "
                    information = "This old, one-eyed Goblin has his best days behnd him. Killing him should be no Problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?"
                    death_message = "You somehow made it. You got defeated by an old cripple of goblin. I would give you an medal, but unfortunaly you got feeded to 23 hungry goblin childrens. You are dead."
                    hpemax = 12
                    dmge = 4
                    ecrt = 0
                    armore = 0
                    fireweakness = 10
                    mnstrchoosen = True
                elif monty == 2:
                    mnstrtp = "really fat cat"
                    title = "the "
                    titleBig = "The "
                    information = "Wow, this cat is REALLY fat. Shes slow, but because of her fat belly quite tanky. Maybe you try fire?"
                    death_message = "The cat *mistakes* you for a sofa, and completely scratches your skin of. You are dead."
                    hpemax = 16
                    dmge = 3
                    ecrt = 0
                    armore = 2
                    fireweakness = 15
                    mnstrchoosen = True
                elif monty == 3:
                    mnstrtp = "devil-possessed baby"
                    title = "the "
                    titleBig = "The "
                    information = "This is a baby, possessed by the devil. It doesnt have much health, but explodes when you bring it in contact with fire. So be cautionfull!"
                    death_message = "It thinks you are his Mother! How cute! Except it killed all 243 mothers before. And so you. You are dead."
                    hpemax = 11
                    dmge = 5
                    ecrt = 0
                    armore = 0
                    fireweakness = 50
                    mnstrchoosen = True
                elif monty == 4:
                    mnstrtp = "pidgeon of doom"
                    title = "the "
                    titleBig = "The "
                    information = "This pidgeon is really annoying. In fact, it is so annoying that you just want to kill it. Which is pretty easy, because its an goddamn pidgeon."
                    death_message = "It picks out your eyes, and while stumbling around blindly, you fall with your head into your weapon. You are dead."
                    hpemax = 4
                    dmge = 5
                    ecrt = 5
                    armore = 0
                    fireweakness = 9
                    psnchance = 2
                    psndur = 1
                    mnstrchoosen = True
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
                    dmge = 4
                    armore = 1
                    fireweakness = 12
                    mnstrchoosen = True
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
                    mnstrchoosen = True
                elif monty == 2:
                    mnstrtp = "poisonos snake"
                    title = "the "
                    titleBig = "The "
                    information = "This is an poisonos snake. I think thats nuff said."
                    death_message = "It bites you, and poisons you. What did you expect? You are dead."
                    if role == "crack addict":
                        death_message = "You dont die of poison, your resistance is to high. You are dying because of hundreds of bites. You are dead."
                    hpemax = 12
                    dmge = 4
                    ecrt = 4
                    armore = 0
                    fireweakness = 10
                    psnchance = 4
                    psndur = 3
                    mnstrchoosen = True
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
                    mnstrchoosen = True
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
                    mnstrchoosen = True
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
                    mnstrchoosen = True
            elif stage == 3:
                stagename = "swamp"
                if monty == 1:
                    mnstrtp = "three-eyed goblin"
                    title = "the "
                    titleBig = "The "
                    information = "What the chernobyl type of fuck is this??"
                    death_message = "He tears out his third eyeball, and shoves it in your throat. You suffacate painfully. You are dead. "
                    hpemax = 18
                    dmge = 8
                    ecrt = 3
                    armore = 1
                    fireweakness = 15
                    mnstrchoosen = True
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
                    mnstrchoosen = True
                elif monty == 3:
                    mnstrtp = "giant slime cube"
                    title = "the "
                    titleBig = "The "
                    information = "The obligatory. It has REALLY high armor, but low health. Also fire isnt really effective against him, but still does damage. Just keep on hitting till its dead! But watch out, hes really acid."
                    death_message = "He eats you via phagocytosis. You get solved by the acid. You are dead."
                    hpemax = 12
                    dmge = 5
                    ecrt = -4
                    armore = 7
                    fireweakness = 5
                    psnchance = 6
                    psndur = 2
                    mnstrchoosen = True
                elif monty == 4 and not reptiloiddead:
                    mnstrtp = "reptiloid with a tie"
                    title = "the "
                    titleBig = "The "
                    information = "It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue."
                    death_message = "He convinces you to join an terror group, where you blow up yourself. You are dead."
                    hpemax = 20
                    dmge = 5
                    ecrt = 4
                    armore = 2
                    fireweakness = 9
                    mnstrchoosen = True
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
                    mnstrchoosen = True
            elif stage == 4:
                stagename = "source outskirts"
                if monty == 1:
                    mnstrtp = "two goblins (2 eyes each)"
                    title = ""
                    information = "So yeah... there are two of them. They attack twice, and swarm around you. High armor is recommended, as each hit will deal less damage as your armor. You will have a hard time if you dont kill one quickly."
                    death_message = "The goblins are gangbanging you. You die of shame afterwards. You are dead."
                    hpemax = 44
                    dmge = 4
                    ecrt = 0
                    armore = 2
                    fireweakness = 13
                    amount = 3
                    mnstrchoosen = True
                elif monty == 2:
                    mnstrtp = "siren" and not sirendead
                    title = "the "
                    titleBig = "The "
                    information = "A beautiful, but cruel and malevolent miscreature, with unknown origins. It feeds from suffering, and is not affected by the evening of bloodlust. It lures her prey with divine songs, just to use the oil pund shes living in for weaken it and finally killing it. It does with joy, your only hope to defeat this monster not just by shape but by mind, is to prove strength, endurance and poison resistance."
                    death_message = "Sometimes, hunter becomes prey, for you are no match for the siren. It feeds from your suffer, until it finds an end. You are dead."
                    hpemax = 60
                    dmge = 14
                    ecrt = 1
                    armore = 0
                    fireweakness = 18
                    sirendead = True
                    mnstrchoosen = True
                elif monty == 3:
                    mnstrtp = "spider nest"
                    title = "the"
                    titleBig = "A "
                    information = "Aww, lots of baby spiders! Hans, get se Flammenwerfer!!"
                    death_message = "See it from a positive side, now all these cute spiders will have a dead body to play in! Btw: You are dead."
                    hpemax = 50
                    dmge = 6
                    ecrt = 2
                    armore = 0
                    fireweakness = 16
                    psnchance = 2
                    pnsdur = 1
                    amount = 7
                    mnstrchoosen = True
                if role == "cleric" and not patchesdead:
                    mnstrtp = "Patches"
                    title = ""
                    titleBig = ""
                    information = "He fights with a spear and a tower shield. He really hates Clerics, and really likes kicking them into Traps. Curiosly, he doesnt seem to be affected by the curse of the evening of bloodlust."
                    death_message = "He kicks you of a cliff, right into a bunch of skeletons. You are dead."
                    hpemax = 49
                    dmge = 6
                    ecrt = 5
                    armore = 3
                    fireweakness = 10
                    patchesdead = True
                    mnstrchoosen = True
                elif monty == 4:
                    mnstrtp = "SUCKubus"
                    title = "the "
                    titleBig = "The "
                    information = "Maybe defeat isnt always the worst option..."
                    death_message = "She SUCKS it all out of you. And I do mean all: Blood, Sweat, Tears, Brain fluid... You are dead."
                    hpemax = 56
                    dmge = 12
                    ecrt = 1
                    armore = 2
                    fireweakness = 4
                    mnstrchoosen = True
                elif monty == 5 and not isaacdead:
                    mnstrtp = "crying boy"
                    title = "the "
                    titleBig = "The "
                    information = "He has big, bloody eyes, out of which he shoots tears at you. And for some reason, they hurt."
                    death_message = "After a lot of tears, you suddenly pop and covering the ground with your inner organs. You are dead."
                    hpemax = 43
                    dmge = 11
                    ecrt = 4
                    armore = 0
                    fireweakness = 13
                    mnstrchoosen = True
                    isaacdead = True
                
            elif stage == 5:
                stagename = "champions plateau"
                if monty == 1 and not GLaDEaD and hagboss:
                    mnstrtp = "???"
                    title = ""
                    information = "The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. "
                    death_message = "GlaDOS makes tests with you. You are doing well, until you get to get the cake. You discover the truth, The cake is a lie. You are dead"
                    hpemax = 70
                    dmge = 14
                    ecrt = 0
                    armore = 2
                    fireweakness = 15
                    GLaDEaD = True
                    mnstrchoosen = True
                elif monty == 2:
                    mnstrtp = "literal devil"
                    title = "the "
                    titleBig = "The "
                    information = "He is going to send you straight to hell. Also, better not try to attack him with fire. I mean, he comes from hell, he eats fire for breakfast."
                    death_message = "He takes you to hell, where you slowly, painfully dissolve in a puddle of burned flesh and skin. You are dead."
                    hpemax = 86
                    dmge = 16
                    ecrt = 3
                    armore = 0
                    fireweakness = 0
                    mnstrchoosen = True
                elif monty == 3:
                    mnstrtp = "LoL tryhard"
                    title = "the "
                    titleBig = "The "
                    information = "He is the most toxiest being in the universe. He is also accurate as fuck, since he makes nothing else than playing LoL. He is fat, and his fat gives him a little bit armor."
                    death_message = "He defeats you, and you land in the Elo Hell. You try to play your way out, but unfortunaly starve because you dont eat anything. You are dead."
                    hpemax = 76
                    dmge = 13
                    ecrt = 4
                    armore = 1
                    fireweakness = 10
                    psnchance = 6
                    psndur = 4
                    mnstrchoosen = True
                elif monty == 4:
                    mnstrtp = "army"
                    title = "the "
                    titleBig = "A whole"
                    information = "Well, you are fucked. Good luck winning against a whole army of welltrained soldiers... I hope you brought some armor with you."
                    death_message = "You get poked, sliced, chopped, grinded, and spiked by arrows and bolts. You are dead enough for twelve people. You are dead."
                    hpemax = 140
                    dmge = 6
                    ecrt = 3
                    armore = 0
                    fireweakness = 16
                    amount = 11
                    mnstrchoosen = True
                elif monty == 5 and not gkingdead:
                    mnstrtp = "goblin king"
                    title = "the "
                    titleBig = "The "
                    information = "Someday in the past, Goblins made peace with the Humans, after decades of war, and saw that they arent to different to Humans. But because of the evening of bloodlust nearly all living beings became corrupted, the goblins were no exception. Their King is a humongous beast, with gigantic curved swords and iron plate armor."
                    death_message = "You get sliced in halves, and the minor goblins, formerly just watching the fight, are feasting on your blood. You are dead."
                    hpemax = 65
                    dmge = 15
                    ecrt = 3
                    armore = 7
                    fireweakness = 9
                    gkingdead = True
                    mnstrchoosen = True


        mnstrchoosen = False
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
        if not stage == 5:
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
                print("You see the marketplace. Its devastated, plundered, from the formerly beautiful stands are just smoking splitters. There are no merchants there, dead or alive. Sunken in thought, you turn away. Just as you want to go, you hear something.")
                print(titleBig + adjective + mnstrtp + eweap + " shovels itself free from splinters and attacks you!")

        elif stagename == "great grasslands":
            encounterrandom = random.randint(1,3)
            if encounterrandom == 1 and not hagcalm:
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
                        if hp > maxhp:
                            hp = maxhp
                    else:
                        print("They taste awfull, and you got food poison!")
                        psncurdur = 4
                else:
                    print("You decide not to eat them.")
                print("In the time you decided about the baked beans, a monster came! " + titleBig + adjective + mnstrtp + eweap + " seems to be hungry, but not to be interested in baked beans...")
                 
        elif stagename == "swamp":
            encounterrandom = random.randint(1,3)
            if encounterrandom == 1:
                print("On your wandering through the swamp, you step accidently in a moor... You somehow get out, but the noises you made upon doing so lured a monster to you!")
                print(titleBig + adjective + mnstrtp + eweap + " appears and lusts for your blood!")
            elif encounterrandom == 2 and not hagvisited:
                print("You find a old hut. Inside you find a couldron, lots of unreadable books and destroyed potions, plus something that is kind of looking like a futuristic tool. Only a Health potion seems to be intact. You take it with you. You leave the hut, but in front of it there is now a monster, which promptly attacks you!")
                healpot += 1
                print("Its " + title + adjective + mnstrtp + eweap + "!")
                stagename = "swamp hut"
            elif encounterrandom == 3:
                print("You wander for hours, through a forest of swamp shrubs. Then, seemingly out of nothing, you hear something behind you... It was an ambush!")
                print(titleBig + adjective + mnstrtp + eweap + " attacks you!")
        elif stagename == "source outskirts":
            encounterrandom == random.randint(1,3)
            if mnstrtp == "siren":
                print("On your Journey, you suddenly hear overworldly singing. You just have to search for the source of this songs...  you finally come to an oil pond, a hole filled with black, bubbling goo, emitting explosive, toxinous gases. There are not a few corpses around, some looking human, others do not, all in different states of rot.")
                print("It does smell terrible and you are wondering what produced those sounds... Then you see it, lurking in the pond - A siren! It doesnt seem to be very friendly...")
            
            elif encounterrandom == 1:
                print("While wandering, you see some really big dust clouds approuching you on your left side... A scree avalanche! You run for your life, blind for everything but escaping the deadly threat. Even though you manage to get enough distance, you didnt see that you ran straight into a monster sleeping place.")
                print(titleBig + adjective + mnstrtp + eweap + "positions itself in front of you, in expectation of a fresh ration blood!")
            elif encounterrandom == 2:
                print("You find an old garden with herbs and flowers. A sweet smell flies into your nose as you enter it. You search for goodies, but you dont find anything.")
                print("But then you smell something different...  You follow the stench until you find a pale corpse with bloody, open throat, in a advanced state of rot. Even though it roumors in your stomach, you journey prepared you for the most things. But this corpse didnt only lure you to this place...")
                print(titleBig + adjective + mnstrtp + eweap + "thinks you are a much better snack than a bloodless corpse!")
            elif encounterrandom == 3:
                print("You encounter a weird shaped rock formation. It somehow emits a weird radiance, but you do not know what this is about. Maybe you will find out later...")
                print("While riddling about this phenomen, a monster found you: " + titleBig + adjective + mnstrtp + eweap + "!")
        elif stagename == "champions plateau":
            encounterrandom = random.randint(1,3)
            if mnstrtp == "goblin king":
                print("You enter a wide circle, full of tents in a really bad condition. A terrible smell approaches you, like from a horde of unwashed goblins. As you see, you arent to wrong with your guess, as suddenly three couples of small, green heads look at you. A big goblin with a crown, curved swords and an armor comes in you direction.")
                print("The goblin king wants you to feed his crew with your own blood!")
            elif mnstrtp == "literal devil":
                print("You find a ladder, leading into the underground. As you climb down, you sense the air getting hotter and hotter. Finally, you come to a cave which is lighted by bright lava. In the middle of it there stands a giant creature with red skin, horns and yellow eyes.")
                print("It is the Devil, ready to take you to hell!")
            elif mnstrtp == "???":
                print("You follow the tip of the old hag, and come to a dry field with a cabin in the middle.")
                print("You notice a door in it, and as soon as you enter it, youre inside of some kind of lift. The doors close behind you, and the chamber moves down. On your way down, you hear some kind of orchestra, which leaves you in wonder.")
                print("Finally, the lift comes to its deepest point. You find yourself in a very large room, with something almost body-shaped hanging from the ceiling. Suddenly, it awakes, and starts to attack you!")
                eweap = ""
            elif mnstrtp == "army":
                print("After a good amount of time passed, you decide it is a good time to rest. So you gather some twigs and dead bushes, and make yourself a nice campfire.")
                print("You manage to fall asleep, but a few hours later you wake up over the sound of marching feet, only to find yourself surrounded by a small army, with a strength of a couple soldiers.")
                print("The person who seems to be their leader starts to speak:\"I do not know if you are corrupted, but we can take no risks. So please, surrender, and your death will be quick and painless.\"")
                print("Then they start to attack. You decide not to surrender.")
                
                

            else:
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
                        randomnumb = random.randint(1,10)
                        if randomnumb == 1:
                            print("You attacked " + title + mnstrtp + " for " + str(int(dmg * acc)) + " Damage, and chopped its head off!")
                        elif randomnumb == 2:
                            print("You attacked for " + str(int((dmg * acc)*multi)) + " damage, which was a lethal hit!")
                        elif randomnumb == 3:
                            print("You attacked for " + str(int((dmg * acc)*multi)) + " damage, and crushed the monsters skull!")
                        else:
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
                    elif mnstrtp == "literal devil":
                        hpe += dmg
                        if hpe > hpemax:
                            hpe = hpemax
                        print("Your fire Damage healed the devil, it now has " + str(hpe) + " Hp!")
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
                    print("questlog to list all your current quests.")
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
                elif do == "questlog":
                    print(questlog)
                
                elif do == "detox":
                    if psncurdur > 0:
                        print("You cure your poison.")
                        psncurdur = 0
                        done = True
                    else:
                        if detoxprot:
                            print("Wtf are you doing? You arent even poisoned!")
                            detoxprot = False
                        else:
                            print("As you want...")
                            done = True
                elif do == "poison":
                    psncurdur = int(input("How many rounds do you want to poison youself?"))
                
                elif do == "inv":
                    print("Type the number of your choice.")
                    invdo = input("(1) Healing potion(" + str(healpots) + ")  (2) Grenade(" + str(dmgpots) + ")   (3) Exit(" + str(exittimes) + ")")
                    if invdo == "1":
                        if healpots > 0:
                            hp += int(heal*2.5)
                            healpots += -1
                            if hp > maxhp:
                                hp = maxhp
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
                    death_message = "You end yourself by hitting your weapon through your stomach."
                    if role == "cleric":
                        death_message = "You end yourself by hitting your weapon through your stomach. I just dont know how you did this with a Mace."
                elif do == "OneHit":
                    dmg = 200
                elif do == "tphut":
                    hpe = 0
                    stagename = "swamp hut"
                    sage = 3
                elif do == "Death Note":
                    dialog = input("")
                    if dialog == mnstrtp:
                        hpe = 0
                        print(mnstrtp + " died of heart attack!")
                        done = True
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
                        print( titleBig + adjective + mnstrtp + " attacked, but you dodged the attack!")
                    else:
                        acce = float((random.randint(5,11)+stage)/10 +((crtmdfe+crte)/10))
                        if int(((dmge) * acce - armor)) > 0:
                            hp = hp - int(((dmge) * acce - armor))
                        if int(((dmge) * acce - armor)) > 0:
                            print(titleBig + mnstrtp + " attacked you for " + str(int(((dmge) * acce - armor))) + " damage! You have " + str(hp) + " HP left!")
                        else:
                            print(titleBig + mnstrtp + " attacked you, but didn`t do any damage!")
                        if psnchance > 0:
                            if (psnchance - psnrsst)-random.randint(1,10) > 0:
                                psncurdur += psndur
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
                #if stage > 2:
                #    lvlupd = -1
                #if stage > 4:
                #    lvlupd = -2
                if adjective == "shiny":
                    lvlupd += -1
                print("You killed " + title + mnstrtp + "!")
                stagego = input("Do you want to go forward, go backward, or stay?")
                stagechangeddialog = False
                stagechanged = False
                while not stagechangeddialog:
                    if not stagename == "swamp hut":
                        if stagego == "forward":
                            print("You decide to go an area forwards.")
                            stage += 1
                            stagechanged = True
                            stagechangeddialog = True
                        elif stagego == "backward":
                            print("You decide to go an area backwards.")
                            stage += -1
                            stagechanged = True
                            stagechangeddialog = True
                        elif stagego == "stay":
                            print("You decide to wander around a bit in this area.")
                            stagechangeddialog = True
                        else:
                            print("Please make a correct answer.")
                            stagego = input("Type forward, backward or stay.")
                    else:
                        stagechangeddialog = True
                
            if stage == 6 and not gamefinished:
                print("Yeah!")
                gamewon = True
            
            else:    
                while lvlupd < 1 and not gamefinished:
                    print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                    print("type help to get detailed descriptions of all stats, and help for nerds for really detailed descriptions.")
                    print("You can also type pass to not level up.")
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
                    elif lvlup == "pass":
                        lvlupd = 1

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
input("Press Enter to close the game window.")
        #Everything: Ole Haufschild
        #There are a lot of references in this game, good luck to find them.
                   
                
            
                

