#Quest for Murder
#A text RPG by SkelletStomper
#To Do:
#-Quest log (done)-Quests get removed after completion(done)
#-Armmor and Weapons (done) -add more!
#-Special abilities(done)
#-Gold and Merchants
#-Portal Gun must do stuff (done)
#-better map system
#bugs:
#portal gun: first time portal set gives no output  (fixed)
#
#
import random
patchesdead = False
gamefinished = False
true = True
false = False



while not gamefinished:
    gamefinished = False
    gameclosed = False
    goMenu = False
    gamewon = False
    exited = False
    fukkerr = "ARRRR"
    maxhp = 18
    basedmg = 0
    dmg = 5
    efficiency = 1
    heal = 4
    testmode = False
    ng = 1
    #quest log
    questlog = []
    achievments = []
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
    armormod = 0
    acce = 0
    crtmdfe = 0
    armore = 0
    dodge = 1
    dodgemod = 0
    #Monster vars
    mnstrtp = ""
    mnstrchoosen = False
    eweap = ""
    typ = "human"
    bloodpossessed = True
    #Prolog vars
    dialog = 1
    randomnumb = 12345678910111213
    boolean = False
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
    #various vars
    ckey = False
    sirendead = False
    devildead = False
    gkingdead = False
    reptiloiddead = False
    isaacdead = False
    guardiandead = False
    GLaDEaD = False
    hagcalm = False
    hagboss = False
    hagvisited = False
    pgrec = False
    p1 = "not set"
    p2 = "not set"
    swahu = False
    level = 1
    typewrong = 0
    endgame = False
    #Poison vars
    psndur = 4
    psnchance = 0
    psnrsst = 0
    psnleft = 0
    detoxprot = True
    #Special abilities
    abilityid = 0
    abilityname = ["Ultra hit","Master of the shadows","Heavenly heal","Invincibility","God rays","Emergency supplies","Explode","Kick"]
    abilitydescription = ["You lay all of your strength in one single hit. With this power, you do 50% more damage if you attack in the same round.","Your evasive skills are second to none. With this skill, they improve further for 3 rounds.","The gods grant you a relieve from your worldly pain, healing your tp to its max.","With this ability are you protected for one round.","You are the godfather, and your enemy shall perish through the holy light. Deals massive, nonscaling damage.","You know where to get your stuff. With this ability you either get one Healing potion or one grenade.","You sacrifice half of your hp for the sake of a massive explosion, dealing thrice the damage of your sacrificed hp.","One is for sure, the Unbreakable Patches knows how to kick. And you do so, too."]
    abilitytimer = 0
    abilityduration = [1,3,0,1,0,0,0,0]
    abilityreload = [10,15,12,7,6,3,5]
    abilityreloadtimer = 0
    #weapons
    weaponid = 0
    weaponname = ["bare fist","longsword","curved dagger","mace","spoon","spear","heavy warhammer","rusty knife","flail","paperblade","broken AK-47","pitchfork","giant curved sword","pizza cutter","greatsword of the demonslayer","goblinslayers short sword","slaughtering axe","mancutter","chainsaw","guardian claw","long stick"]
    weapondmg = [0,3,2,2,0,3,5,1,2,2,1,3,5,1,8,3,4,5,6,5,2]
    weaponamr = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    weaponweight = [0,3,1,2,0,3,7,1,3,0,3,2,6,1,11,2,3,3,4,2,1]
    weaponclass = ["fist","sword","dagger","mace","joke","spear","mace","dagger","mace","sword","mace","spear","sword","joke","greatsword","sword","axe","scythe","sword","sword","staff"]
    weaponstartattribute = ["none","none","none","blessed","mirror","none","heavy","rusty","none","inflamable","none","firy","none","none","demon-slaying","goblin-slaying","animal-slaying","human-slaying","none","none","none"]
    weaponattribute = weaponstartattribute[weaponid]
    weaponsmithed = "classic"

    #offhand weapons
    offhandid = 0
    offhandname = ["bare fist","knight shield","curved dagger","baked beans","tower shield","head of the devil-possessed baby","energy drink","the lie"]
    offhanddmg = [0,0,2,0,0,0,1,0]
    offhandamr = [0,2,0,0,3,0,0,0]
    offhandheal = [0,0,0,3,0,0,3,7]
    offhandweight = [0,2,1,1,4,1,1,2]
    offhandclass = ["fist","shield","dagger","trinket","shield","joke","trinket","trinket"]
    offhandstartattribute = ["none","none","none","none","none","inflamable","none","delicious and moist"]
    offhandattribute = offhandstartattribute[offhandid]
    offhandsmithed = "classic"
    
    #armor
    armorid = 0
    armorname = ["normal clothing","plate armor","smooth leather armor","dirty rags","scale cloth","light army protection","ninja suit","guardian hide armor"]
    armoramr = [0,3,1,0,1,2,1,4]
    armorweight = [0,4,1,0,0,1,0,2]
    armorstartattribute = ["none","heavy","none","stenching","none","none","evasive","none"]
    armorattribute = armorstartattribute[armorid]
    armorsmithed = "classic"

    #Weight watcher
    totalweight = 0
    naturalweight = 0
    weightmalus = 0
    #LOOOT!!
    lootlist = ["w-1-classic","a-2-classic","o-2-classic"]
    loot = 0
    loottype = 0
    lootid = 0
    lootsmithed = 0
    randomnumb = random.randint(0,len(lootlist)-1)
    loot = lootlist[randomnumb]
    #current poison duration
    psncurdur = 0
    #inv vars
    inv = []
    healpots = 0
    dmgpots = 0
    steelpills = 0
    holywater = 0
    firyresin = 0
    gold = 0
    invdo = "MissingNo"
    exittimes = 99
    #Start of the Game
    print("You find yourself in a dark bar. You do not remember anything, and you are slightly confused.")
    print("Your head lays in a puddle of vomit, which is stenching like strong alcohol.")
    name = input("The Bar keeper, the only other person in this room, nods to you. He says: \"Well, finally awake, are you? Let me introduce myself. I am Deuhtsh, the owner of this nasty little bar. So what is your name?\"")
    if name == "":
        print("\"You say you do not have a name? Well, I got to respect that. But I have some good advice for you. You have chosen a bad time to wake up from your slumber- Its the evening of bloodlust!")
    else:
        print("\""+ name + ", you say? Well, it does not really matter to me. But I have some good advice for you. You have chosen a bad time to wake up from your slumber- Its the evening of bloodlust!")
    print("You have to be very carefully. If you are not careful, the monsters are going to take you!")
    print("Which monsters, you do ask?\"")
    dialog = input("yes/no")
    if dialog == "yes":
        print("\"You know, goblins, animals, and even worse, humans, infested with the bloodlust. The usual stuff.")
    elif dialog == "no":
        print("\"Okay, as you want.")
    else:
        print("\"Whatever that means.")
    print("So this is my EPIC quest for you. End the evening of bloodlust by killing monsters. For this, I will give you the quest log. With this tool you will be able to quickly remind you of your actions.")
    print("Once you are finished with this, make sure to return to me. I will open a bottle of my really good stuff for you.\"")
    questlog.append("Quest: End the evening of bloodlust! ////   Just end it as Deuhtsh said, kill monsters.")
    print("Quest added: End the evening of Bloodlust!")
    print("After Deuhtsh said this, he takes a huge bottle of whiskey, and drinks it faster than you can look. His eyes twist, and he falls backwards. You decide to go.")
    print("In the floor, you see several boxes, each with the equip for a special class. You have to decide for one. Why not take them all? Well, because this stupid game does not allow it.")
    print("You can be a bandit, a knight or a cleric!")
    stage = 1
    stagename = "village"
    rolechosen2 = False
    while not rolechosen2:
        rolechosen = False
        while not rolechosen:
            #Role selector
            role = input("Which class do you choose?")
            if role == "knight":
                roledescription = "The knight is a tank. He has high armor, and high Hp. But he has low Heal and a decreased crit modifier, and is not that good at dodging. He starts with 1 healing potion and with sword and shield."
                maxhp = 24
                basedmg = 2
                weaponid = 1
                offhandid = 1
                armorid = 1
                armor = 1
                crtmdf = 0
                dodge = 0
                heal = 3
                crtmdfe = 0
                healpots = 1
                dmgpots = 0
                psnrsst = 0
                abilityid = 0
                rolechosen = True
            elif role == "bandit":
                roledescription = "An agile assasin. He has a high crit modifier, and is really good at dodging. His damage is absolutely superior, but he has no armor and low health. He starts with a grenade and twin daggers."
                maxhp = 10
                basedmg = 3
                weaponid = 2
                offhandid = 2
                armorid = 2
                armor = 0
                crtmdf = 2
                dodge = 3
                heal = 4
                crtmdfe = -1
                healpots = 0
                dmgpots = 1
                psnrsst = 0
                abilityid = 1
                rolechosen = True
            elif role == "cleric":
                roledescription = "A filthy cleric, Patches does not like him. He has extremely high Heal, and is a bit armored. He starts with a mace, which is blessed."
                maxhp = 14
                basedmg = 2
                weaponid = 3
                offhandid = 0
                armorid = 0
                armor = 1
                crtmdf = 0
                dodge = 1
                heal = 8
                crtmdfe = 0
                psnrsst = 1
                healpots = 0
                dmgpots = 0
                abilityid = 2
                rolechosen = True
            elif role == "glass cannon":
                roledescription = "He kills everything, as long he does not get hit."
                maxhp = 1
                basedmg = 15
                weaponid = 4
                offhandid = 0
                armorid = 0
                armor = 0
                crtmdf = 5
                dodge = 0
                heal = 0
                crtmdfe = 200000
                healpots = -20000
                psnrsst = 0
                dmgpots = 4
                abilityid = 3
                rolechosen = True
            elif role == "godfather":
                roledescription = "Definitly balanced."
                maxhp = 50
                basedmg = 9
                weaponid = 4
                offhandid = 0
                armorid = 0
                armor = 5
                crtmdf = 5
                dodge = 4
                heal = 12
                crtmdfe = -3
                healpots = 10
                dmgpots = 10
                abilityid = 4
                rolechosen = True
            elif role == "crack addict":
                roledescription = "Extremely weak in every aspect, but has a lot of potions. Armed only with a spoon and clothed in dirty rags."
                maxhp = 8
                basedmg = 2
                weaponid = 4
                offhandid = 0
                armorid = 0
                armor = 0
                crtmdf = 0
                dodge = 0
                heal = 5
                crtmdfe = 0
                psnrsst = 5
                healpots = 3
                dmgpots = 3
                abilityid = 5
                rolechosen = True
            elif role == "sand sack":
                roledescription = "This is for testing purposes."
                maxhp = 200
                basedmg = 4
                weaponid = 4
                offhandid = 0
                armorid = 0
                armor = 0
                crtmdf = 0
                dodge = -20
                heal = 5
                crtmdfe = 1
                psnrsst = 0
                healpots = 69
                dmgpots = 69
                abilityid = 6
                rolechosen = True
            elif role == "patches":
                if not patchesdead:
                    print("Nice try, not yet.")
                else:
                    roledescription = "The equipment of the unbreakable Patches, strapped of his corpse. At the end, he wasnt that unbreakable. It contains a spear, a tower shield and a reinforced leather armor, dyed black. "
                    maxhp = 15
                    basedmg = 4
                    weaponid = 5
                    offhandid = 4
                    armorid = 2
                    armor = 2
                    crtmdf = 1
                    dodge = 1
                    heal = 5
                    crtmdfe = 1
                    psnrsst = 1
                    healpots = 1
                    dmgpots = 1
                    abilityid = 7
                    rolechosen = True
            elif role == "yes":
                print("Thats not how this works.")
            else:
                print("Please make a valid answer")
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
                print("Please make a valid answer.")
                roleaccept = input("yes/no")
    abilityreloadtimer = abilityreload[abilityid]         
    hp = maxhp
    print("You have chosen the role " + role + ".")
    print("You leave the bar, unsure what to do. You just wander around, till you find something... A village! You dont hear any sounds a village would usually make, like the laughing of children, the barking of dogs. There is only silence and destruction. Even though the village didnt burn out, its condition is horrible.")
    print("You enter it, and see some type of letter on a Wall.")
    print("It first page reads:")
    print("Type atk to attack, type heal to heal, type help for more commands")
    print("There are more letters, described with *help*")

    while stage < 6 and not gamefinished and not goMenu:
        if stage == 0:
            print("You return to the bar. Deuhtsh is staring at you.")
            if name == "":
                print("What do you want here, nameless hero?")
            else:
                print("\"What do you want here, " + name + "?\"")
            while stage == 0 and not goMenu and not endgame:
                print("(1)What is the evening of bloodlust?")
                print("(2)How did I get here?")
                print("(3)Who are you?")
                print("(4)Do you have anything else for me?")
                print("(5)I just want to drink something.")
                dialog = input("(6)I just wanted to go.")
                if dialog == "1":
                    print("\"Well, nobody knows its origins, but everyone knows its consequences. It causes animals, humans and monsters to go mad, with an insatiable thirst for blood. From this point on, the being is no longer able to do social interactions, only the most primitve instincts and the thirst for blood remains.")
                    print("Somehow, beings that are infected by bloodlust are not attacking other infected beings. We dont know if it is a curse or maybe heavenly punishment, but it is real, and is going to kill you really fast, if you are not careful.\"")
                elif dialog == "2":
                    print("\"Well, I really do not know. Sometimes, people are waking up here, with no memory of what happened. They are just here when I do not look for a moment. This is happening since the evening of bloodlust started. You are not the first, and you probably also are not the last. That is all I can say to you.\"")
                elif dialog == "3":
                    print("As I already said, I am Deuhtsh, the owner of this bar. Also, I somehow became the quasi mentor of all poor souls that are awaking here without memories.")
                elif dialog == "4":
                    print("\"Well, You could go into my cellar. Here, I give you the key. Ther could be something useful around. But beware, its infested.\"")
                    print("Cellar key received")
                    ckey = True
                elif dialog == "5":
                    #if drinksdrunken == 0:
                    if 0 == 0:
                        print("\"Sure, this one is for free. What do you want?\"")
                        dialog = input("(1)Siegbräu  (2)Pisswasser  (3)Estus (4)W.A.T.E.R. (5) nothing")
                        paid = True
                    #else:
                    #   print("\"Sure. What do you want?\"")
                    #    dialog = input("(1)Siegbräu 10G (2)Pisswasser 5G  (3)Estus 20G (4)W.A.T.E.R. 2G (5) nothing")
                    #    paid = True
                    if dialog == "1" and paid:
                        print("\"Well, here you have a Siegbräu, out of the far lands of Catarina. You have no idea how hard it is to get it in these times, so enjoy it.\"")
                        print("As you drink the mug of Siegbräu, it surprisingly tastes really good, for some reason after herbs and onion.")
                        drinksdrunken += 1
                    elif dialog == "2" and paid:
                        print("As you drink the bottle of beer, it tastes like really old water. You decide that you do not want to know what its ingrediences are.")
                        drinksdrunken += 1
                    elif dialog == "3" and paid:
                        print("As you drink the bottle of yellow juice, it burns horrible in your throat, as if you just drank liquid fire.")
                        print("\"You have to get used to it\", says Deuhtsh. \"That is really hard stuff, but it is said to have the power to keep one man from dying.\"")
                        drinksdrunken += 1
                        hp += 7
                    elif dialog == "4" and paid:
                        print("\"Well, here do you get your glass of W.A.T.E.R. Have fun.\"")
                        print("The W.A.T.E.R tastes like ordinary water. How intriguing.")
                        if drinksdrunken == 0:
                            drinksdrunken += 1
                        hp += 1
                    elif dialog == "6":
                        print("\"Nothing? Well, thats okay too.\"")
                elif dialog == "6":
                    print("You decide that it is time for you to leave.")
                    if not ckey:
                        stage = 1
                        stagename = "village"
                    else:
                        print("(1) Village")
                        dialog = input("(2) Cellar")
                        if dialog == "1":
                            stage = 1
                            stagename = "village"
                        elif dialog == "2":
                            stage = 2
                            stagename = "cellar"
                        
            else:
                print("You leave the bar.")
            while stage == 0 and not goMenu and not gamefinished:
                print("You finally return to the Bar. Deuhtsh is sitting at a Table, seemingly waiting for you.")
                print("\"Oh, you are back? How did you get the beast? Well, it does not matter. So, did you do what I said?\"")
                boolean = True
                while boolean:
                    dialog = input("yes/no")
                    if dialog == "yes":
                        if "Quest: Return to the Bar. ////    You can enter the Bar by going backwards in the Village." in questlog:
                            questlog.remove("Quest: Return to the Bar. ////    You can enter the Bar by going backwards in the Village.")
                            print("Quest finished: Return to the Bar.")
                        print("\"Oh, of course, I can feel it already. The lifted curse... Well, remember what I said back then? Let me just get it.\"")
                        print("He stands up, and walks to the shelf with all the Bottles. He pulls one out, which seems to be different to the others. He then sits back at the table.")
                        print("\"Here, you got to try this out. This is the best stuff you ever got, I promise.\"")
                        print("He opens the bottle, and fills two small shot glasses. \"One for you, one for me. Go on, take it, taste it.\"")
                        if name == "":
                            print("As soon as you drink the shot, your mind becomes Blank. You see Deuhtsh standing in front of you. You do not see his head, but hear his Voice: \"Good Night, nameless.\"")
                        else:
                            print("As soon as you drink the shot, your mind becomes Blank. You see Deuhtsh standing in front of you. You do not see his head, but hear his Voice: \"Good Night, " + name + ".\"")
                        print("After that, you pass out completely.")
                        print("The end.")
                        boolean = False
                        gamefinished = True
                    elif dialog == "no":
                        print("Well, then come back as soon as you are finished with everything, I would say.")
                        boolean = False
                        stage = 1
                    else:
                        print("Please make a valid answer.")
        if stagename == "swamp hut":
            hagvisited = True
            if not GLaDEaD:
                print("You decide to rest at the Hut. A few minutes later an old woman appears, and looks at you in scept.")
                print("\"Who are you? And why are you in front of my house? Answer!\"")
                while stagename == "swamp hut" and not goMenu:
                    if name == "":
                        print("(1) I am sorry, I cannot say you my name, for I have none. I came to your house while wandering in the swamp. As I stayed here for a little rest, a monster came and I killed it.")
                    else:
                        print("(1) I am " + name + ", I came to your house while wandering in the swamp. As I stayed here for a little rest, a monster came and I killed it.")
                    print("(2) Who are you? Anybody could just come and say its her house and be rude to me.")
                    print("(3) Where am I?")
                    print("(4) Can you tell me anything about this Land? I sadly lost my memory.")
                    print("(5) I am leaving now.")
                    dialog = input("")
                    if dialog == "1":
                        if hagcalm:
                            print("\"You know you already said that, do you? Well, as I said, theres a healing potion in the hut\".")
                        else:
                            print("\"Oh, I am sorry, I did not knew that.\" She looks to the corpse of " + title + mnstrtp + ". \"Thanks for that, that would have been a bad surprise if you were not here.")
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
                                print("\"I guess you woke up in Deuhtshs bar, did you? Well, I cannot tell you really much about this land before the evening of bloodlust, for I am not born here. I got drawn into this world, also waking up in the bar. This is now really long time ago. But I think the same happened to you, although I dont know why it happened.")
                                print("My best guess is that the bloodlust searches for prey and draws them through room, time, hell, maybe even through dimensions! For some reason they all wake up in the bar. Most of them die early, only a few persevere. I dont know what, but something is special about Deuhtsh. In all the time I spent here, he seems to have aged no bit.\"")
                            else:
                                print("\"What?\"")
                        else:
                            print("\"I would not know what it interests you. Now get away, thug!\"")
                    elif dialog == "4":
                        if hagcalm:
                            print("\"Well, actually yes. If you should someday come to the plateau of champions, then wander till you come to an wheat field. In the center there should be an type of cabin, were should be some interesting stuff.\" Her eyes seem to glow as she said this.")
                            questlog.append("Quest: Search the cabin in the fields. ////    It should be somewhere on the Champions Plateau.")
                            print("Quest added: Search the cabin in the fields.")
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
                print("You return to the hut. Cehl sits infront of it, cutting mushrooms in a stew. When she notices you, her eyes get brighter.")
                if name == "":
                    print("\"Hello! Coming over again, do you? Well, just in time, I made a delicious soup which will be ready in a few minutes.\"")
                else:
                    print("\"Hello " + name + "! Coming over again, do you? Well, just in time, I made a delicious soup which will be ready in a few minutes.\"")
                while stagename == "swamp hut" and not goMenu:
                    print("(1) I was at the cabin like you told me, what happened then is a long story...")
                    print("(2) What is in this soup?")
                    print("(3) I am sorry, but I have to leave now.")
                        
                    dialog = int(input(""))
                    if dialog == 1:
                        print("You start telling the story of what you found in and under the cabin. Once you are finished, Cehl seems to be thinking. She sits there for a few minutes, not saying a word, until she finally says:")
                        print("\"I did not expect this, to be honest. When I left there, I made a deal with her- I will send her a new test subject. I am really sorry that this had to be you. Well, I guess I have to apologize. But please, take this as a compensation.\"")
                        print("She goes into the hut, and comes back with the futuristic gun you saw earlier.")
                        print("\"Here, this is for you. It is a device to create quantum tunnels, modified to work on every even surface. It will maybe come in handy while traveling. Now please, go. I do not want you to see my face who sent you right into a trap. But I am glad you made it out alive, and even more, defeated her.")
                        print("As she asked, you leave, a bit confused about the meeting.")
                        if "Return to Cehl. ////    She is in the swamp, you might have to wander around a bit to find her." in questlog:
                            questlog.remove("Return to Cehl. ////    She is in the swamp, you might have to wander around a bit to find her.")
                            print("Quest finished: Return to Cehl.")
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
                            print("\"Well, I guess that means more soup for me.\"")
                    elif dialog == 3:
                        print("\"Well, leaving so soon? Then here, take at least this!\"")
                        print("She gives you a grenade. \"Do not ask me where I got it, may it help you on your journy!\"")
                        if "Return to Cehl. ////    She is in the swamp, you might have to wander around a bit to find her." in questlog:
                            questlog.remove("Return to Cehl. ////    She is in the swamp, you might have to wander around a bit to find her.")
                            print("Quest finished: Return to Cehl.")
                        dmgpots += 1
                        stagename = "swamp"
       
            
            
        #Here the Enemy type is selected
        monty = random.randint(1,5)
        amount = 1
        psnchance = 0
        psndur = 0
        while not mnstrchoosen and not goMenu and not gamefinished:
            
            if stage == 1:
                if stagename == "village":
                    if endgame and not guardiandead:
                        mnstrtp = "last guardian"
                        title = "the "
                        titleBig = "The "
                        information = "This gigantic beast seems to protect the bar. It is really, really big, and has a huge health pool. You want to really kill this one quick."
                        death_message = "It kills you in a undescribable way. You are dead."
                        hpemax = 250
                        dmge = 12
                        ecrt = 0
                        armore = 4
                        fireweakness = 10
                        mnstrchoosen = True
                        typ = "unclassified"
                        bloodpossessed = False
                        lootlist = ["w-19-classic","a-7-classic"]
                    elif monty == 1:
                        mnstrtp = "one-eyed goblin"
                        title = "the "
                        titleBig = "The "
                        information = "This old, one-eyed Goblin has his best days behind him. Killing him should be no problem. But just think of his remaining family... Do you really want to kill the grandpa of 23 goblin childrens?"
                        death_message = "You somehow made it. You got defeated by an old cripple of goblin. I would give you an medal, but unfortunaly you got eaten by 23 hungry goblin childrens. You are dead."
                        hpemax = 12
                        dmge = 4
                        ecrt = 0
                        armore = 0
                        fireweakness = 10
                        mnstrchoosen = True
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","w-7-classic"]
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
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
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
                        typ = "demon"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","o-5-classic"]
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
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 5:
                        mnstrtp = "bloodlusting villager"
                        title = "the "
                        titleBig = "The "
                        information = "A villager, corrupted by the evening of bloodlust. He has a flail, along with a rusty sickle."
                        randomnumb = random.randint(1,2)
                        if randomnumb == 1:
                            death_message = "He flails your bones to dust. While they are still in your body. You are dead."
                        else:
                            death_message = "He cuts your throat with his sickle, and lustfully drinks your blood directly out of you caritod artery. You are dead."
                        hpemax = 10
                        dmge = 4
                        armore = 1
                        fireweakness = 12
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","w-7-classic","w-8-classic","a-3-classic"]
            elif stage == 2:
                if stagename == "great grasslands":
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
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","w-7-classic"]
                    elif monty == 2:
                        mnstrtp = "poisonos snake"
                        title = "the "
                        titleBig = "The "
                        information = "This is an poisonos snake. I think thats nuff said."
                        death_message = "It bites you, and poisons you. What did you expect? You are dead."
                        if role == "crack addict":
                            death_message = "You do not die of poison, your resistance is to high. You are dying because of hundreds of bites. You are dead."
                        hpemax = 12
                        dmge = 4
                        ecrt = 4
                        armore = 0
                        fireweakness = 10
                        psnchance = 4
                        psndur = 3
                        mnstrchoosen = True
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","a-4-classic"]
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
                        typ = "unclassified"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","w-9-classic"]
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
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 5:
                        mnstrtp = "child soldier"
                        title = "the "
                        titleBig = "The "
                        information = "Well, it is a Child. With an AK-47. Its heavy-armored, but has a terrible precision. That should be easy, right?"
                        death_message = "It manages to shot you in the head. You are dead."
                        hpemax = 10
                        dmge = 10
                        ecrt = -4
                        armore = 3
                        fireweakness = 11
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","w-10-classic"]
                elif stagename == "cellar":
                    if monty == 1:
                        mnstrtp = "giant rat"
                        title = "the "
                        titleBig = "The "
                        information = "This is a rat. It is bigger than other rats. Way bigger. Also it is poisonos, so beware."
                        death_message = "Rats eat almost everything, and they also eat dead humans. If they are not dead, they usually not eat them. But at this size, they can just kill their prey. And so they did. You are dead."
                        hpemax = 21
                        dmge = 4
                        ecrt = 0
                        armore = 0
                        fireweakness = 15
                        psnchance = 3
                        psndur = 4
                        mnstrchoosen = True
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 2:
                        mnstrtp = "silvermoth"
                        title = "the "
                        titleBig = "The "
                        information = "A large moth, as big as your head. Fragile, but hard to hit. It is drawn to the flame like a mmoth is drawn to the flame."
                        death_message = "It bites you very often, and while one bite does just hurt, many bites kill you. You are dead."
                        hpemax = 10
                        dmge = 6
                        ecrt = -4
                        armore = 0
                        fireweakness = 20
                        mnstrchoosen = True
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 3:
                        mnstrtp = "beggar"
                        title = "the "
                        titleBig = "The "
                        information = "A normal beggar? He fights you with a long staff, nothing more than a long stick."
                        death_message = "He beats you to death with his stick. You are dead."
                        hpemax = 18
                        dmge = 3
                        ecrt = 4
                        armore = 1
                        fireweakness = 10
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","w-20-classic"]
                    elif monty == 4:
                        mnstrtp = "half-rotten goblin"
                        title = "the "
                        titleBig = "The "
                        information = "This goblin is on the edge of death."
                        death_message = "Congratulation. You got defeated by the worst enemy in history."
                        hpemax = 6
                        dmge = 1
                        ecrt = 0
                        armore = 0
                        fireweakness = 10
                        mnstrchoosen = True
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 5:
                        mnstrtp = "cellar demon"
                        title = "the "
                        titleBig = "The "
                        information = "It lurks in the dark and waits for prey. Resistent to fire."
                        death_message = "It kills you. You are dead."
                        hpemax = 30
                        dmge = 5
                        ecrt = 1
                        armore = 2
                        fireweakness = 4
                        mnstrchoosen = True
                        typ = "devil"
                        bloodpossessed = False
                        lootlist = ["w-0-classic"]
            elif stage == 3:
                if stagename == "swamp":
                    if monty == 1:
                        mnstrtp = "three-eyed goblin"
                        title = "the "
                        titleBig = "The "
                        information = "What the chernobyl type of fuck is this??"
                        death_message = "He tears out his third eyeball, and shoves it in your throat. You suffacate painfully. You are dead. "
                        hpemax = 24
                        dmge = 8
                        ecrt = 3
                        armore = 0
                        fireweakness = 15
                        mnstrchoosen = True
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    elif monty == 2:
                        mnstrtp = "imp"
                        title = "the "
                        titleBig = "The "
                        information = "A nasty flying fucker who pokes you with his Pitchfork. Its a creature, straight out of Hell."
                        death_message = "He pokes his pitchfork directly in your guts, and twirls them. You are dead."
                        hpemax = 21
                        dmge = 6
                        ecrt = 4
                        armore = 2
                        fireweakness = 3
                        mnstrchoosen = True
                        typ = "demon"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","w-11-classic"]
                    elif monty == 3:
                        mnstrtp = "giant slime cube"
                        title = "the "
                        titleBig = "The "
                        information = "The obligatory. It has REALLY high armor, but low health. Also fire is not really effective against him, but still does damage. Just keep on hitting till its dead! But watch out, hes really acid."
                        death_message = "He eats you via phagocytosis. You get solved by the acid. You are dead."
                        hpemax = 12
                        dmge = 5
                        ecrt = -4
                        armore = 7
                        fireweakness = 5
                        psnchance = 6
                        psndur = 2
                        mnstrchoosen = True
                        typ = "unclassified"
                        bloodpossessed =  True
                        lootlist = ["w-0-classic"]
                    elif monty == 4 and not reptiloiddead:
                        mnstrtp = "reptiloid with a tie"
                        title = "the "
                        titleBig = "The "
                        information = "It resembles to high-tier politicians nowadays... Its scales are giving him a bit armor, and it has a nasty tongue."
                        death_message = "He convinces you to join an terror group, where you blow up yourself. You are dead."
                        hpemax = 30
                        dmge = 5
                        ecrt = 4
                        armore = 2
                        fireweakness = 9
                        mnstrchoosen = True
                        typ = "unclassified"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","a-4-classic"]
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
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
            elif stage == 4:
                if stagename == "source outskirts":
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
                        amount = 2
                        mnstrchoosen = True
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
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
                        typ = "unclassified"
                        bloodpossessed = False
                        lootlist = ["w-0-classic"]
                    elif monty == 3:
                        mnstrtp = "spider nest"
                        title = "the"
                        titleBig = "A "
                        information = "Aww, lots of baby spiders! Hans, get se Flammenwerfer!!"
                        death_message = "See it from a positive side, now all these cute spiders will have a dead body to play in! By the way: You are dead."
                        hpemax = 50
                        dmge = 6
                        ecrt = 2
                        armore = 0
                        fireweakness = 16
                        psnchance = 2
                        pnsdur = 1
                        amount = 7
                        mnstrchoosen = True
                        typ = "animal"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                    if role == "cleric" and not patchesdead:
                        mnstrtp = "Patches"
                        title = ""
                        titleBig = ""
                        information = "He fights with a spear and a tower shield. He really hates clerics, and really likes kicking them into traps. Curiosly, he does not seem to be affected by the curse of the evening of bloodlust."
                        death_message = "He kicks you off a cliff, right into a bunch of skeletons. You are dead."
                        hpemax = 49
                        dmge = 6
                        ecrt = 5
                        armore = 3
                        fireweakness = 10
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","w-5-classic","o-4-classic"]
                    elif monty == 4:
                        mnstrtp = "SUCKubus"
                        title = "the "
                        titleBig = "The "
                        information = "Maybe defeat is not always the worst option..."
                        death_message = "She SUCKS it all out of you. And I do mean all: blood, sweat, tears, brain fluid... You are dead."
                        hpemax = 56
                        dmge = 12
                        ecrt = 1
                        armore = 2
                        fireweakness = 4
                        mnstrchoosen = True
                        typ = "demon"
                        bloodpossessed = False
                        lootlist = ["w-0-classic"]
                    elif monty == 5 and not isaacdead:
                        mnstrtp = "crying boy"
                        title = "the "
                        titleBig = "The "
                        information = "He has big, bloody eyes, out of which he shoots tears at you. And for some reason, they hurt."
                        death_message = "After a lot of tears, you suddenly pop and cover the ground with your inner organs. You are dead."
                        hpemax = 43
                        dmge = 11
                        ecrt = 4
                        armore = 0
                        fireweakness = 13
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = True
                        lootlist = ["w-0-classic"]
                
            elif stage == 5:
                if stagename == "champions plateau":
                    if monty == 1 and not GLaDEaD and hagboss:
                        mnstrtp = "???"
                        title = ""
                        information = "The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie. The cake is a lie."
                        death_message = "GlaDOS makes tests with you. You are doing well, until you get to get the cake. You discover the truth, The cake is a lie. You are dead"
                        hpemax = 70
                        dmge = 14
                        ecrt = 0
                        armore = 2
                        fireweakness = 15
                        mnstrchoosen = True
                        typ = "unclassified"
                        bloodpossessed = False
                        lootlist = ["o-7-delicious and moist"]
                    elif monty == 2 and not devildead:
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
                        typ = "demon"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","w-11-classic"]
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
                        typ = "human"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","o-6-classic","w-13-classic"]
                    elif monty == 4:
                        mnstrtp = "army"
                        title = "the "
                        titleBig = "A whole"
                        information = "Well, you are fucked. Good luck winning against a whole army of welltrained soldiers... I hope you brought some armor with you."
                        death_message = "You get poked, sliced, chopped, grinded, and spiked by arrows and bolts. You are dead enough for twelve people. You are dead."
                        hpemax = 144
                        dmge = 5
                        ecrt = 3
                        armore = 0
                        fireweakness = 16
                        amount = 11
                        mnstrchoosen = True
                        typ = "human"
                        bloodpossessed = False
                        lootlist = ["w-0-classic","w-3-classic","w-1-classic","w-6-classic","o-1-classic","a-6-classic"]
                    elif monty == 5 and not gkingdead:
                        mnstrtp = "goblin king"
                        title = "the "
                        titleBig = "The "
                        information = "Someday in the past, Goblins made peace with the Humans, after decades of war, and saw that they are not to different to Humans. But the evening of bloodlust corrupted nearly all living beings, and the goblins were no exception. Their King is a humongous beast, with gigantic curved swords and iron plate armor."
                        death_message = "You get sliced in halves, and the minor goblins, formerly just watching the fight, are feasting on your blood. You are dead."
                        hpemax = 63
                        dmge = 15
                        ecrt = 3
                        armore = 7
                        fireweakness = 9
                        mnstrchoosen = True
                        typ = "goblin"
                        bloodpossessed = True
                        lootlist = ["w-0-classic","a-1-classic","w-12-classic"]
                        
        mnstrchoosen = False
        if stagechanged and not gamefinished:
            if stagename == "village":
                print("You return to the devastated village.")
            elif stagename == "great grasslands":
                print("You enter the great grasslands; a huge area full of grass, rivers, old, lonely trees and monsters.")
            elif stagename == "swamp":
                print("You enter the swamp. It is a dangerous, poisonos area, with many possibility to sink in the bog. You remember an old saying: At full moon, swamp chunks are slime chunks... You have no idea what this is supposed to mean.")
            elif stagename == "source outskirts":
                print("You enter the source outskirts, a hilly, vast area with many high mountains. Here and there are vulcanos, lava streams, and oil lakes. On the horizont you see the plateau of champions...")
            elif stagename == "champions plateu":
                print("You finally reached the champions plateau, the place where the strongest of the strongest monsters live... And your oppurtunity to end the evening of bloodlust.")
                


        eweap = ""
        #Attributes
        attr = random.randint(0,100)
        if not stage == 5 or not stage == 1 and not guardiandead and endgame:
            if attr > 55 and attr < 100:
                adjective = ""
            elif attr > 99:
                adjective = "shiny "
            elif attr > 50 and attr < 56:
                adjective = "poisonos "
                psnchance += 3
                psndur += 3
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
                if hpemax > 1:
                    print(titleBig + adjective + mnstrtp + " was so weak that it failed to live.")
            elif attr < 11 and attr > -1:
                adjective = "cloned "
                amount += 1
                dmge = int((dmge + 3)/2)
                

        hpe = hpemax
        if not gamefinished:
            if stagename == "village":
                encounterrandom = random.randint(1,3)
                if endgame and not guardiandead:
                    print("In front of the bar something waits for you. It is a giant beast, and it appears that it guards the Bar... But from what?")
                    print("However, you have to get in there, and so you attack.")
                if encounterrandom == 1:
                    print("In a shady side street, you hear something screaming. You run to it, but you only find a horribly torn corpse in wrecked pieces of armor. Resisting the urge to vomit, you turn yourself back to the entrance. But there is something...")
                    print(titleBig + adjective + mnstrtp + eweap + " attacks you in the twilight of the street!")
                elif encounterrandom == 2:
                    print("You see an old grocery store, it seems to be abandoned. You enter it in search of some goodies, you dont think the owner does have anything against it...")
                    print("You search in the building, but you dont find anything except a lot of non-human looking dung and spiderwebs. But suddenly something dashes at you, and you fall right into a table, which bursts.")
                    print("You get up, but now there is " + title + adjective + mnstrtp + eweap + " attacking you!")
                elif encounterrandom == 3:
                    print("You see the marketplace. Its devastated, plundered, from the formerly beautiful stands are just smoking splitters left. There are no merchants there, dead or alive. Sunken in thought, you turn away. Just as you want to go, you hear something.")
                    print(titleBig + adjective + mnstrtp + eweap + " shovels itself free from splinters and attacks you!")

            elif stagename == "great grasslands":
                encounterrandom = random.randint(1,3)
                if encounterrandom == 1 and not hagcalm:
                    print("You see an old, old tree, surrounded by many tree stumps. It is a sad appearance, and you decide to make your rest here. You think about god and the world, until you, hours later, hear something nearing, and roaring. It sounds almost like a chainsaw...")
                    eweap = " with a chain saw"
                    dmge += 3
                    lootlist.append("w-18-classic")
                    print(titleBig + adjective + mnstrtp + eweap + " sprints at you! Determined to save this tree, you fight back.")
                elif encounterrandom == 2:
                    print("There is a cave, and for whatever stupid reason you decide to explore it. Inside you find a grenade, which you put to your arsenal. As you want to leave, something blocks your way...")
                    dmgpots += 1
                    print(titleBig + adjective + mnstrtp + " grunts at you and attacks you!")
                elif encounterrandom == 3:
                    print("You find a abandoned campfire, burned down for a long time. There is a can with baked beans, already cooked... But do you really want to eat it? Perhaps you can also use the mas an offhand weapon?")
                    dialog = input("yes/no/use")
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
                    elif dialog == "use":
                        offhandid = 3
                        print("You put your former offhand weapon away and use the can of baked beans instead")
                    else:
                        print("You decide not to eat them.")
                    print("In the time you decided about the baked beans, a monster came! " + titleBig + adjective + mnstrtp + eweap + " seems to be hungry, but not to be interested in baked beans...")
                     
            elif stagename == "swamp":
                encounterrandom = random.randint(1,3)
                if encounterrandom == 1 and not offhandid == 3:
                    print("On your wandering through the swamp, you step accidently in a moor... You somehow get out, but the noises you made upon doing so lured a monster to you!")
                    print(titleBig + adjective + mnstrtp + eweap + " appears and lusts for your blood!")
                elif encounterrandom == 2 and not hagvisited:
                    print("You find a old hut. Inside you find a caldron, lots of unreadable books and destroyed potions, plus something that is kind of looking like a futuristic tool. Only a Health potion seems to be intact. You take it with you. You leave the hut, but in front of it there is now a monster, which promptly attacks you!")
                    healpots += 1
                    print("Its " + title + adjective + mnstrtp + eweap + "!")
                    stagename = "swamp hut"
                elif encounterrandom == 3:
                    print("You wander for hours, through a forest of swamp shrubs. Then, seemingly out of nothing, you hear something behind you... It was an ambush!")
                    print(titleBig + adjective + mnstrtp + eweap + " attacks you!")
            elif stagename == "source outskirts":
                encounterrandom == random.randint(1,3)
                if mnstrtp == "siren":
                    print("On your Journey, you suddenly hear overworldly singing. You just have to search for the source of this songs...  you finally come to an oil pond, a hole filled with black, bubbling goo, emitting explosive, toxinous gases. There are not a few corpses around, some looking human, others do not, all in different states of rot.")
                    print("It does smell terrible and you are wondering what produced those sounds... Then you see it, lurking in the pond - A siren! It does not seem to be very friendly...")
                
                elif encounterrandom == 1:
                    print("While wandering, you see some really big dust clouds approuching you on your left side... A scree avalanche! You run for your life, blind for everything but escaping the deadly threat. Even though you manage to get enough distance, you didnt see that you ran straight into a monster sleeping place.")
                    print(titleBig + adjective + mnstrtp + eweap + " positions itself in front of you, in expectation of a fresh ration blood!")
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
                    hagboss = False
                    if "Quest: Search the cabin in the fields. ////    It should be somewhere on the Champions Plateau." in questlog:
                        questlog.remove("Quest: Search the cabin in the fields. ////    It should be somewhere on the Champions Plateau.")
                        print("Quest finished:Search the cabin in the fields.")
                        questlog.append("Kill the unknown being. ////    Just do it somehow, it does not matter how.")
                        print("Quest added: Kill the unknown being.")
                    eweap = ""
                elif mnstrtp == "army":
                    print("After a good amount of time passed, you decide it is a good time to rest. So you gather some twigs and dead bushes, and make yourself a nice campfire.")
                    print("You manage to fall asleep, but a few hours later you wake up over the sound of marching feet, only to find yourself surrounded by a small army, with a strength of a couple soldiers.")
                    print("The person who seems to be their leader starts to speak:\"I do not know if you are corrupted, but we can take no risks. So please, surrender, and your death will be quick and painless.\"")
                    print("Then they start to attack. You decide not to surrender.")
                    
                    

            else:
                 print(titleBig + adjective + mnstrtp + " appears!")






            
        
        while hpe > 0 and hp > 0 and not gamefinished and not goMenu:
            typewrong = 0
            if maxhp < hp:
                hp = maxhp
            #temporary fire modifire
            tempfiremod = 0
            if weaponattribute == "firy":
                tempfiremod += 2
            if offhandattribute == "firy":
                tempfiremod += 2
            #efficiency stuff
            efficiency = 1
            if typ == weaponattribute.split("-")[0]:
                efficiency += 0.2
            #temporary armor modifier
            armormod = 0
            #ability stuff
            abilityreloadtimer += 1
            if abilityreloadtimer > abilityreload[abilityid]:
                abilityreloadtimer = abilityreload[abilityid]
            abilitytimer += -1
            if abilitytimer < 0:
                abilitytimer = 0
            #dodge modifier(temp)
            dodgemod = -weightmalus
            if abilitytimer > 0 and abilityname[abilityid] == "Master of the shadows":
                dodgemod += 5


            while not done and not gamefinished and hp > 0 and not goMenu:
                #smithed attributes
                if weaponid == 0:
                    weaponsmithed = "classic"
                if offhandid == 0:
                    offhandsmithed = "classic"
                if weaponsmithed == "classic":
                    weaponattribute = weaponstartattribute[weaponid]
                else:
                    weaponattribute = weaponsmithed
                if offhandsmithed == "classic":
                    offhandattribute = offhandstartattribute[offhandid]
                else:
                    offhandattribute = offhandsmithed
                if armorsmithed == "classic":
                    armorattribute = armorstartattribute[armorid]
                else:
                    armorattribute = armorsmithed
                #Weight watcher
                totalweight = weaponweight[weaponid] + offhandweight[offhandid] + armorweight[armorid] + naturalweight
                if weaponattribute == "heavy" or offhandattribute == "heavy" or armorattribute == "heavy":
                    totalweight += int(totalweight/3)
                if totalweight < 1:
                    weightmalus = -1
                elif totalweight < 3:
                    weightmalus = 0
                elif totalweight < 5:
                    weightmalus = 1
                elif totalweight < 7:
                    weightmalus = 2
                elif totalweight < 11:
                    weightmalus = 3
                elif totalweight < 16:
                    weightmalus = 4
                else:
                    weightmalus = 5
                #Here are the possibilities that you have
                do = input("What do you want to do?")
                #Here are the inputs listed    
                if do == "atk":    
                    dmg = basedmg + (weapondmg[weaponid] + offhanddmg[offhandid])*efficiency
                    acc = random.randint(7,13)/10 +(crtmdf-weightmalus)/10
                    if acc > 1.3:
                        acc = 1.3
                    hpe = hpe - int((dmg)*acc)
                    if hpe < 1:
                        randomnumb = random.randint(1,10)
                        if randomnumb == 1:
                            print("You attacked " + title + mnstrtp + " for " + str(int((dmg)*acc)) + " damage, and chopped its head off!")
                        elif randomnumb == 2:
                            print("You attacked for " + str(int((dmg)*acc)) + " damage, which was a lethal hit!")
                        elif randomnumb == 3:
                            print("You attacked for " + str(int((dmg)*acc)) + " damage, and crushed the monsters skull!")
                        elif randomnumb == 4:
                            print("You attacked for " + str(int((dmg)*acc)) + " damage, and destroyed an important organ. " + mnstrtp + " falls backwards and does not get up again.")
                        elif randomnumb == 5:
                            print("You attacked for " + str(int((dmg)*acc)) + " damage, and slice the monster in half.")
                        else:
                            print("You attacked for " + str(int((dmg)*acc)) + " damage, which was a lethal hit!")
                    else:
                        
                        print("You attacked for " + str(int((dmg)*acc)) + " damage, " + title + mnstrtp + " has only " + str(int(hpe)) + " Hp left!")
                    done = True
                elif do == "heal":
                    hp += heal + offhandheal[offhandid]
                    if maxhp < hp:
                        hp = maxhp
                    print("You healed yourself for " + str(heal + offhandheal[offhandid]) + " Hp, you now have " + str(hp) + " Hp left!")
                    done = True
                elif do == "info":
                    print(information)
                elif do == "fire":
                    if mnstrtp == "paper-man!" or mnstrtp == "devil-possessed baby":
                        lootlist = ["w-0-classic"]
                    if mnstrtp == "devil-possessed baby":
                        hpe = 0
                        hp = hp - (10 + random.randint(2,5) - armor)
                        dodge = dodge - 1
                        crtmdfe = crtmdfe + 1
                        print("As you hit " + title + mnstrtp + ", it explodes and covers you with its organs! You have " + str(hp) + " Hp left and your Dex decreased!")
                        death_message = "After this heavy explosion, all that is left of you are some pieces, spreaded in a 10m radius. You are dead."
                        done = True
                    elif mnstrtp == "literal devil":
                        hpe += dmg + weapondmg[weaponid] + offhanddmg[offhandid]
                        if hpe > hpemax:
                            hpe = hpemax
                        print("Your fire damage healed the devil, it now has " + str(hpe) + " Hp!")
                        done = True
                    elif weaponattribute == "inflamable" or offhandattribute == "inflamable":
                        hpe = hpe - int(((basedmg+weapondmg[weaponid]+offhanddmg[offhandid])*3) * ((fireweakness + tempfiremod)/10))
                        if hpe > 0:
                            print("You attacked " + title + mnstrtp + " with fire, which dealt " + str(int(((basedmg+weapondmg[weaponid]+offhanddmg[offhandid])*3) * ((fireweakness + tempfiremod)/10))) + " fire damage. " + mnstrtp + " has now " + str(hpe) + " left!")
                        else:
                            print("You burned " + title + adjective + mnstrtp + " to ashes... ashes with a slight smell of BBQ.")
                        print("In this progress your inflamable piece of equipment burned, dealing a lot of extra damage, but it is gone now.")
                        if weaponattribute == "inflamable":
                            weaponid = 0
                        elif offhandattribute == "inflamable":
                            offhandid = 0
                        done = True
                    else:
                        
                        hpe = hpe - int(((basedmg+weapondmg[weaponid]+offhanddmg[offhandid]) - ((basedmg+weapondmg[weaponid]+offhanddmg[offhandid])/4)) * ((fireweakness + tempfiremod)/10))
                        if hpe > 0:
                            print("You attacked " + title + mnstrtp + " with fire, which dealt " + str(int(((basedmg+weapondmg[weaponid]+offhanddmg[offhandid]) - ((basedmg+weapondmg[weaponid]+offhanddmg[offhandid])/4)) * ((fireweakness + tempfiremod)/10))) + " fire damage. " + mnstrtp + " has now " + str(hpe) + " left!")
                        else:
                            print("You burned " + title + adjective + mnstrtp + " to ashes... ashes with a slight smell of BBQ.")
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
                    print("inv to open your inventory.")
                    print("drop to drop one of your items, if you decide to do so.")
                    print("ability to use your special ability")
                    print("abilityinfo to see details about your special ability.")
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
                elif do == "ability":
                    if abilityreloadtimer >= abilityreload[abilityid]:
                        abilityreloadtimer = 0
                        abilitytimer = abilityduration[abilityid]
                        if abilityname[abilityid] == "Ultra hit":
                            efficiency += efficiency/2
                        elif abilityname[abilityid] == "Master of the shadows":
                            dodgemod += 5
                        elif abilityname[abilityid] == "Heavenly heal":
                            hp = maxhp
                            done = True
                        elif abilityname[abilityid] == "Invincibility":
                            armormod += 2**31-1
                        elif abilityname[abilityid] == "God rays":
                            hpe += -50
                        elif abilityname[abilityid] == "Emergency supplies":
                            randomnumb = random.randint(1,2)
                            if randomnumb == 1:
                                healpots += 1
                            else:
                                dmgpots += 1
                        elif abilityname[abilityid] == "Explode":
                            hpe += int((hp/2)*3)
                            hp = int(hp/2)
                            done = True
                        elif abilityname[abilityid] == "Kick":
                            hpe += -10 -int(stage*(stage/2))
                            done = True
                            
                        
                    else:
                        print("Your ability is not ready yet.")
                elif do == "abilityinfo":
                    print(abilityname[abilityid])
                    print(abilitydescription[abilityid])
                    if abilityreloadtimer == 0:
                        print("Ability charge: 0%")
                    else:
                        print("Ability charge: " + str((abilityreloadtimer/abilityreload[abilityid]*100)) + "%")
                
                elif do == "detox":
                    if psncurdur > 0:
                        print("You cure your poison.")
                        psncurdur = 0
                        done = True
                    else:
                        if detoxprot:
                            print("Wtf are you doing? You are not even poisoned!")
                            detoxprot = False
                        else:
                            print("As you want...")
                            done = True
                
                elif do == "drop":
                    dialog = input("What do you want to drop? (weapon/offhand/armor/nothing)")
                    if dialog == "weapon":
                        print("Are you sure you want to drop your weapon? It cannot be recovered.")
                        dialog = input("(yes/no)")
                        if dialog == "yes":
                            print("You dropped your weapon.")
                            weaponid = 0
                        else:
                            print("You do not drop your weapon.")
                    elif dialog == "offhand":
                        print("Are you sure you want to drop your offhand weapon? It cannot be recovered.")
                        dialog = input("(yes/no)")
                        if dialog == "yes":
                            print("You dropped your offhand weapon.")
                            offhandid = 0
                        else:
                            print("You do not drop your offhand weapon.")
                    elif dialog == "armor":
                        print("Are you sure you want to drop your armor? It cannot be recovered.")
                        dialog = input("(yes/no)")
                        if dialog == "yes":
                            print("You dropped your armor.")
                            armorid = 0
                        else:
                            print("You do not drop your armor.")
                    else:
                        print("You do drop nothing.")
                elif do == "inv":
                    print("Type the number of your choice.")
                    invdo = input("(1) Usable Items (2) I want to see my stuff!  (3) Exit")
                    if invdo == "1":
                        if healpots > 0:
                            print("(1)Healing potion (" + str(healpots) + ")")
                        else:
                            print("(1)???")
                        if dmgpots > 0:
                            print("(2)Grenade (" + str(dmgpots) + ")")
                        else:
                            print("(2)???")
                        if steelpills > 0:
                            print("(3)Steel Pill (" + str(steelpills) + ")")
                        else:
                            print("(3)???")
                        if holywater > 0:
                            print("(4)Vial with holy water (" + str(holywater) + ")")
                        else:
                            print("(4)???")
                        
                        
                        invdo = input("What do you want you use?")
                        #Healing potions
                        if invdo == "1":
                            if healpots > 0:
                                hp += int(heal*2.5)
                                healpots += -1
                                if hp > maxhp:
                                    hp = maxhp
                                print("You healed yourself for " + str(int(heal*2.5)) + " Hp")
                                done = True
                            else:
                                print("You dont have anything of this type.")
                        #grenades
                        if invdo == "2":
                            if dmgpots > 0:
                                hpe += int(-(dmg*2.5-armore))
                                dmgpots += -1
                                if hpe > 0:
                                   print("You throw a grenade on " + title + mnstrtp + " , which dealt " + str(int(dmg*2.5-armore)) + " damage. Your enemy has " + str(hpe) + " Hp left.")
                                else:
                                    print("You make " + title + mnstrtp + " explode into a million small pieces.")
                                done = True
                            else:
                                print("You dont have anything of this type.")
                        #Steel pills
                        if invdo == "3":
                            if steelpills > 0:
                                armormod += 6
                                steelpills += -1
                                print("You take one steel pill, which strenghtens your defense.")
                            else:
                                print("You dont have anything of this type.")
                        #Holy Water
                        if invdo == "4":
                            if holywater > 0:
                                if typ == "demon":
                                    hpe += -(7+stage*3)
                                    print("You throw a Vial with holy water on your demonic foe, which deals massive damage!")
                                else:
                                    hpe += 1
                                    print("You throw a Vial with holy water on " + mnstrtp + ", but it only refreshed him a bit.")
                                holywater += -1
                        if invdo == "5":
                            print("You do not use an item.")
                        
                        
                            
                        
                    elif invdo == "2":
                        print("Weapon name: " + weaponname[weaponid])
                        print("Weapon damage: " + str(weapondmg[weaponid]))
                        print("Weapon protection: " + str(weaponamr[weaponid]))
                        print("Weapon weight: " + str(weaponweight[weaponid]))
                        print("Weapon attribute: " + weaponattribute)
                        print("Offhand name: " + offhandname[offhandid])
                        print("Offhand damage: " + str(offhanddmg[offhandid]))
                        print("Offhand protection: " + str(offhandamr[offhandid]))
                        print("Offhand heal: " + str(offhandheal[offhandid]))
                        print("Offhand weight: " + str(offhandweight[offhandid]))
                        print("Offhand attribute: " + offhandattribute)
                        print("Armor name: " + armorname[armorid])
                        print("Armor protection: " + str(armoramr[armorid]))
                        print("Armor weight: " + str(armorweight[armorid]))
                        print("Armor attribute: " + armorattribute)
                    elif invdo == "3":
                        print("You do not do anything in your inventory.")
                    
                    
                #Little codes
                elif do == "minsky":
                    if testmode:
                        print("Test mode deactivated.")
                        testmode = False
                    else:
                        print("Test mode activated.")
                        testmode = True
                elif do == "FullHeal" and testmode:
                    hp = maxhp
                    print("You get fully healed")
                elif do == "Invincible" and testmode:
                    armor = 200
                    print("You are more or less invincible now")
                elif do == "suicide":
                    hp = 0
                    death_message = "You end yourself by hitting your weapon through your stomach."
                    if weaponclass[weaponid] == "mace":
                        death_message = "You end yourself by hitting your weapon through your stomach. I just dont know how you did this with a mace."
                elif do == "OneHit" and testmode:
                    basedmg = 200
                    print("You suddenly get the powers of One Punch man.")
                elif do == "tphut" and testmode:
                    hpe = 0
                    stagename = "swamp hut"
                    stage = 3
                elif do == "Death Note" and testmode:
                    dialog = input("")
                    if dialog == mnstrtp:
                        hpe = 0
                        print(mnstrtp + " died of heart attack!")
                        done = True
                elif do == "pg" and testmode:
                    if pgrec:
                        print("pg removed")
                        pgrec = False
                    else:
                        print("pg received")
                        pgrec = True
                elif do == "cons99":
                    healpots = 99
                    dmgpots = 99
                    steelpills = 99
                    holywater = 99
                    print("You suddenly found a chest with a bunch of items!")
                elif do == "cons0":
                    healpots = 0
                    dmgpots = 0
                    steelpills = 0
                    holywater = 0
                    print("All of your consumable items spoiled suddenly.")
                elif do == "exit":
                    do = input("Really? (yes/no)")
                    if do == "yes":
                        gamefinished = True
                        gameclosed = True
                        exited = True
                elif do == "poison" and testmode:
                    psncurdur = int(input("How many rounds do you want to poison youself?"))
                elif do == "stageSkip" and testmode:
                    stageTo = int(input("Which stage?"))
                    stage = stageTo
                elif do == "mainmenu":
                    gamefinished = True
                    goMenu = True
                elif do == "give" and testmode:
                    dialog = input("Which type of item?")
                    if dialog == "weapon":
                        dialog = int(input("Which ID?"))
                        weaponid = dialog
                        print("Weapon received")
                    elif dialog == "offhand":
                        dialog = int(input("Which ID?"))
                        offhandid = dialog
                        print("Offhand received")
                    elif dialog == "armor":
                        dialog = int(input("Which ID?"))
                        armorid = dialog
                        print("Armor received")
                elif do == "SuperSmith" and testmode:
                    dialog = input("Which type?")
                    if dialog == "w":
                        weaponsmithed = input("Which modifier?")
                    elif dialog == "o":
                        offhandsmithed = input("Which modifier?")
                    elif dialog == "a":
                        armorsmithed = input("Which modifier?")
                elif do == "WeightWatcher":
                    print(str(totalweight))
                    print(str(weightmalus))
                elif do == "AddLoot" and testmode:
                    loot = input("Which loot?")
                    lootlist.append(loot)
                    print(loot + " added to loot list.")
                elif do == "endgame" and testmode:
                    endgame = True
                else:
                    print("Please make a valid answer.")
                    typewrong += 1
                    if typewrong > 2:
                        print("You can type help to see a detailed list of all commands.")
                        typewrong = 0
            done = False
            if hpe > 0 and not gamefinished:
                etimesattacked = 0
                eturns = int(amount * hpe/hpemax)
                if eturns < 1:
                    eturns = 1
                while etimesattacked < eturns and hp > 0:
                    if armorattribute == "evasive" and not goMenu:
                        dodgemod += 3
                    if dodge + random.randint(2,10) + dodgemod > 9:
                        print( titleBig + adjective + mnstrtp + " attacked, but you dodged the attack!")
                    else:
                        acce = float((random.randint(5,11)+stage)/10 +((crtmdfe+weightmalus+crte)/10))
                        if acce > 1.6 + stage:
                            acce = 1.6 + stage
                        if int(((dmge) * acce - (armor + armoramr[armorid] + armormod))) > 0:
                            hp = hp - int(((dmge) * acce - (armor + armoramr[armorid] + armormod)))
                        if int(((dmge) * acce - (armor + armoramr[armorid] + armormod))) > 0:
                            print(titleBig + mnstrtp + " attacked you for " + str(int(((dmge) * acce - (armor + armoramr[armorid] + armormod)))) + " damage! You have " + str(hp) + " HP left!")
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
                    gameclosed = True
                    gamefinished = True
                elif fukkerr == "close":
                    gameclosed = True
                    gamefinished = True
                else:
                    goMenu = True
                    gamefinished = False
                
        else:
            if not gamefinished:
                if mnstrtp == "last guardian":
                    guardiandead = True
                elif mnstrtp == "reptiloid with a tie":
                    reptiloiddead = True
                elif mnstrtp == "crying boy":
                    isaacdead = True
                elif mnstrtp == "siren":
                    sirendead = True
                elif mnstrtp == "literal devil":
                    devildead = True
                elif mnstrtp == "goblin king":
                    gkingdead = True
                    print("As you kill their leader, the goblins run away. Which is weird, because they were infected. But you do not complain.")
                elif mnstrtp == "???":
                    GLaDEaD = True
                    print("Achievment earned: You monster.")
                    if "Kill the unknown being. ////    Just do it somehow, it does not matter how." in questlog:
                        questlog.remove("Kill the unknown being. ////    Just do it somehow, it does not matter how.")
                        print("Quest finished: Kill the unknown being.")
                        questlog.append("Return to Cehl. ////    She is in the swamp, you might have to wander around a bit to find her.")
                        print("Quest added: Return to Cehl.")
                lvlupd = 0
                #if stage > 2:
                #    lvlupd = -1
                #if stage > 4:
                #    lvlupd = -2
                if adjective == "shiny ":
                    lvlupd += -1
                if not gamefinished and not goMenu:
                    print("You killed " + title + adjective + mnstrtp + "!")
                while lvlupd < 1 and not gamefinished and not goMenu:
                    print("Now type hp, dmg, acc, amr, dex or heal to either level up your health maximum, your damage, your accuracy, your armor, your dexterity, or your healing skill!")
                    print("type help to get detailed descriptions of all stats, and help for nerds for really detailed descriptions.")
                    print("You can also type pass to not level up.")
                    print("Additionaly you will regain a bit health.")
                    lvlup = (input("What is your choice?"))
                    if lvlup == "hp":
                        maxhp = int(maxhp + (maxhp/5) * (stage + 1 * 0.5) +1)
                        hp = hp + stage * stage + 1
                        if role == "glass cannon":
                            maxhp = 1
                        print("You leveled up HP, now you have " + str(maxhp) + " maximum HP!")
                        lvlupd += 1
                        level += 1
                    elif lvlup == "dmg":
                        basedmg += int(stage + 1 - stage / 3)
                        hp = hp + (stage * stage)/2 + 1
                        print("You leveled up damage, now you have " + str(dmg) + " damage!")
                        lvlupd += 1
                        level += 1
                    elif lvlup == "heal":
                        heal = heal + stage * 2 + 2
                        hp = hp + stage * stage + 1
                        print("You leveled up healing, now you have " + str(heal) + " heal!")
                        lvlupd += 1
                        level += 1
                    elif lvlup == "acc":
                        crtmdf = crtmdf + stage
                        hp = hp + stage * stage + 1
                        print("You leveled up your accuracy, now you have a modifier of " + str(crtmdf/10) + "!")
                        lvlupd += 1
                        level += 1
                    elif lvlup == "amr":
                        armor = int(armor + 1 + stage - stage / 2)
                        psnrsst += 1
                        hp = hp + stage * stage + 1
                        print("You leveled up armor, now you have " + str(armor) + " armor!")
                        lvlupd += 1
                        level += 1
                    elif lvlup == "dex":
                        dodge = dodge + 1
                        if dodge > 5:
                            dodge = 5
                        crtmdfe = crtmdfe - 1
                        hp = hp + stage * stage + 1
                        print("You leveled up dexterity, you are now more eager to dodge attacks!")
                        lvlupd += 1
                        level += 1
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
                        print("amr ==> your armor + stage + stage / 3, rounded down.     Also psnrsst + 1")
                    elif lvlup == "pass":
                        lvlupd = 1

                    else:
                        print("Please make a valid answer")

                    #LOOT!
                    randomnumb = random.randint(1,len(lootlist))
                    randomnumb += -1
                    loot = lootlist[randomnumb]
                    if loot != "w-0-classic":
                        loot = loot.split("-")
                        loottype = loot[0]
                        lootid = int(loot[1])
                        lootsmithed = loot[2]
                        boolean = False
                        if loottype == "w":
                            print("You found a weapon, " + weaponname[lootid] + ". It has the following stats:")
                            print("Weapon damage: " + str(weapondmg[lootid]))
                            print("Weapon protection: " + str(weaponamr[lootid]))
                            print("Weapon weight: " + str(weaponweight[lootid]))
                            if lootsmithed == "classic":
                                if weaponstartattribute[lootid] == "none":
                                    print("It has no special modifier on it.")
                                else:
                                    print("It has the following modifier on it: " + weaponstartattribute[lootid])
                            elif lootsmithed == "none":
                                print("It is smithed to have no modifier on it.")
                            else:
                                print("It was smithed to have the following modifier on it: " + lootsmithed)
                        elif loottype == "o":
                            print("You found an offhand item, " + offhandname[lootid] + ". It has the following stats:")
                            print("Offhand damage: " + str(offhanddmg[lootid]))
                            print("Offhand protection: " + str(offhandamr[lootid]))
                            print("Offhand heal: " + str(offhandheal[lootid]))
                            print("Offhand weight: " + str(offhandweight[lootid]))
                            if lootsmithed == "classic":
                                if offhandstartattribute[lootid] == "none":
                                    print("It has no special modifier on it.")
                                else:
                                    print("It has the following modifier on it: " + offhandstartattribute[lootid])
                            elif lootsmithed == "none":
                                print("It is smithed to have no modifier on it.")
                            else:
                                print("It was smithed to have the following modifier on it: " + lootsmithed)
                        elif loottype == "a":
                            print("You found an set of armor, " + armorname[lootid] + ". It has the following stats:")
                            print("Armor protection: " + str(armoramr[lootid]))
                            print("Armor weight: " + str(armorweight[lootid]))
                            if lootsmithed == "classic":
                                if armorstartattribute[lootid] == "none":
                                    print("It has no special modifier on it.")
                                else:
                                    print("It has the following modifier on it: " + armorstartattribute[lootid])
                            elif lootsmithed == "none":
                                print("It is smithed to have no modifier on it.")
                            else:
                                print("It was smithed to have the following modifier on it: " + lootsmithed)
                        while not boolean and not goMenu:
                            print("Do you want to pick it up? This will replace your currently equipped item and destroy it, so think over it! You can also type current to see your currently equipped item for this slot.")
                            dialog = input("yes/no/current")
                            if dialog == "yes":
                                if loottype == "w":
                                    weaponid = lootid
                                    weaponsmithed = lootsmithed
                                elif loottype == "o":
                                    offhandid = lootid
                                    offhandsmithed = lootsmithed
                                elif loottype == "a":
                                    armorid = lootid
                                    armorsmithed = lootsmithed
                                print("You decide to pick it up and equip it.")
                                boolean = True
                            elif dialog == "no":
                                print("You decide not to pick it up.")
                                boolean = True
                            elif dialog == "current":
                                if loottype == "w":
                                    print("Weapon name: " + weaponname[weaponid])
                                    print("Weapon damage: " + str(weapondmg[weaponid]))
                                    print("Weapon protection: " + str(weaponamr[weaponid]))
                                    print("Weapon weight: " + str(weaponweight[weaponid]))
                                    print("Weapon attribute: " + weaponattribute)
                                elif loottype == "o":
                                    print("Offhand name: " + offhandname[offhandid])
                                    print("Offhand damage: " + str(offhanddmg[offhandid]))
                                    print("Offhand protection: " + str(offhandamr[offhandid]))
                                    print("Offhand heal: " + str(offhandheal[offhandid]))
                                    print("Offhand weight: " + str(offhandweight[offhandid]))
                                    print("Offhand attribute: " + offhandattribute)
                                elif loottype == "a":
                                    print("Armor name: " + armorname[armorid])
                                    print("Armor protection: " + str(armoramr[armorid]))
                                    print("Armor weight: " + str(armorweight[armorid]))
                                    print("Armor attribute: " + armorattribute)
                            else:
                                print("Please make a valid answer.")
                    else:
                        print("You do not find any useful piece of equipment.")
                    


                
                stagechangeddialog = False
                stagechanged = False
                while not stagechangeddialog and not goMenu:
                    if not pgrec:
                        stagego = input("Do you want to go forward, go backward, or stay?")
                    else:
                        stagego = input("Do you want to go forward, go backward, or stay? You can also use the Quantum tunneling device: p1 to place the first, p2 to place the second portal. traverse to go through the portals. this is only possible if one of the portals is on your stage. Placing portals does not consume an action. type pinfo to see where you placed both portals.")
                    if not stagename == "swamp hut":
                        if stagego == "forward":
                            if stagename == "village":
                                dialog = input("(1) great grasslands")
                                if dialog == "1":
                                    stage = 2
                                    stagename = "great grasslands"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")

                            elif stagename == "great grasslands":
                                dialog = input("(1) swamp")
                                if dialog == "1":
                                    stage = 3
                                    stagename = "swamp"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")

                            elif stagename == "swamp":
                                dialog = input("(1) source outskirts")
                                if dialog == "1":
                                    stage = 4
                                    stagename = "source outskirts"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")

                            elif stagename == "source outskirts":
                                dialog = input("(1) champions plateau")
                                if dialog == "1":
                                    stage = 5
                                    stagename = "champions plateau"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                                    
                            elif stagename == "champions plateau":
                                print("You cannot go any further from this point. A giant, unpassable ravine blocks the Path.")
                                
                            elif stagename == "cellar":
                                print("The entrance to the caves is locked.")  


                        elif stagego == "backward":
                            if stagename == "village":
                                dialog = input("(1) bar")
                                if dialog == "1":
                                    stage = 0
                                    stagename = "bar"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                                    
                            elif stagename == "great grasslands":
                                dialog = input("(1) village")
                                if dialog == "1":
                                    stage = 1
                                    stagename = "village"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                                    
                            elif stagename == "swamp":
                                dialog = input("(1) great grasslands")
                                if dialog == "1":
                                    stage = 2
                                    stagename = "great grasslands"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")

                            elif stagename == "source outskirts":
                                dialog = input("(1) village")
                                if dialog == "1":
                                    stage = 3
                                    stagename = "swamp"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                                    
                            elif stagename == "champions plateau":
                                dialog = input("(1) source outskirts")
                                if dialog == "1":
                                    stage = 4
                                    stagename = "source outskirts"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                                    
                            elif stagename == "cellar":
                                dialog = input("(1) bar")
                                if dialog == "1":
                                    stage = 0
                                    stagename = "bar"
                                    stagechanged = True
                                    stagechangeddialog = True
                                else:
                                    print("Please make a valid answer.")
                            
                            stagechanged = True
                            stagechangeddialog = True
                        elif stagego == "stay":
                            print("You decide to wander around a bit in this area.")
                            stagechangeddialog = True
                        elif stagego == "p1" and pgrec:
                            p1 = str(stage)+"-"+str(stagename)
                            print("You place the first portal at " + str(stage) + "-" + str(stagename))
                        elif stagego == "p2" and pgrec:
                            p2 = str(stage)+"-"+str(stagename)
                            print("You place the second portal at " + str(stage) + "-" + str(stagename))
                        elif stagego == "pinfo" and pgrec:
                            print("Portal 1: " + p1)
                            print("Portal 2: " + p2)
                        elif stagego == "traverse":
                            if str(stage)+"-"+str(stagename) == p1 and p2 != "not set":
                                stage = int(p2.split("-")[0])
                                stagename = p2.split("-")[1]
                                print("Using the portal device, you travelled to " + str(stage) + "-" + stagename)
                                if p1 != p2:
                                    stagechanged = True
                                stagechangeddialog = True
                            elif str(stage)+"-"+str(stagename) == p2 and p1 != "not set":
                                stage = int(p1.split("-")[0])
                                stagename = p1.split("-")[1]
                                print("Using the portal device, you travelled to " + str(stage) + "-" + stagename)
                                if p1 != p2:
                                    stagechanged = True
                                stagechangeddialog = True
                            else:
                                print("Either one or both portals are not set yet!")
                        else:
                            print("Please make a valid answer.")
                    else:
                        stagechangeddialog = True
                
            if stage == 5 and not gamefinished:
                print("You have beaten a mighty enemy, as Deuhtsh. He said that the curse of the evening will lift after that. You remember his words: \"Once you are finished with this, make sure to return to me. I will open a bottle of my really good stuff for you.\"")
                print("You can now go back to the Bar to end the game.")
                if "Quest: End the evening of bloodlust! ////   Just end it as Deuhtsh said, kill monsters." in questlog:
                    questlog.remove("Quest: End the evening of bloodlust! ////   Just end it as Deuhtsh said, kill monsters.")
                    questlog.append("Quest: Return to the Bar. ////    You can enter the Bar by going backwards in the Village.")
                    print("Quest added: Return to the Bar.")
                    endgame = True
            
                
    else:
        if not goMenu:
            gamefinished = True
            if not exited and not fukkerr == "close":
                fukkerr = input("Type close to close the program, anything else to restart.")

        if fukkerr == ("fuck you"):
            print("Fukk ju 2")
            gamefinished = True
        elif fukkerr == ("close"):
            gameclosed = True
        if not gameclosed:
            gamefinished = False
            goMenu = True
input("Press enter to close the game window.")
#Everything: SkelletStomper
#There are a lot of references in this game, good luck to find them.
                   
                
            
                

