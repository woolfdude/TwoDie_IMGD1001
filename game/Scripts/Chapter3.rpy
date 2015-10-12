label chapter3:
    if currentchoice == "garden":
        jump day2garden
    elif currentchoice == "lake":
        jump day2lake
    elif currentchoice == "bath":
        jump day2bath
    elif currentchoice == "feed":
        jump day2feed
    return
  
  
label day2bath:
  "You check your schedule for the day. A dinner party tonight that you're hosting, but that's it."
  menu:
        "Call the plumber":
            scene bg bath real at truecenter with fade
            with Pause(1)
            scene bg bath at truecenter with dissolve
            "The bathtub you tried to destroy the body in is getting seriously disgusting. It's almost as 
            bad as that time the shower drain was clogged and no one bothered to get it fixed for at 
            least a month. You shudder at the memory. You can't let that happen again."
            "You do a quick Internet search for cheap plumbers and make a couple calls. You let them know 
            you want to pay in cash. They probably assume it's for tax evasion purposes, and you don't 
            bother correcting them that it's because you don't want a paper trail linking them to you. 
            Finally, one plumber tells you he can make it in later that day. You tell him that would be great."
            show plumber at right with easeinright
            "He gets there a couple hours later, looks at the bathtub, and then looks at you. “It's, uh, that 
             time of the month?” you hazard, trying to explain away the blood."
            "He seems unconvinced."
            "You promise him twice the pay you told him over the phone, and his eyes light up with greed, no 
             more questions asked. Of course, by the time he's done fixing your problem, he already knows too 
             much. And anyway, what's one plumber among friends?"
            scene bg dining real at truecenter with fade
            with Pause(1)
            scene bg dining at truecenter with dissolve
            "Once he's been… dealt with, you get to work right away preparing the food for your guests. You've 
             always been a stellar host, and you're not about to stop now. "
            "By the time they arrive, everything is ready. The dinner goes uneventfully. It was good to be able 
             to catch up with friends. "
            "After the last guest leaves, you're just about ready to take your nightly shower before going to 
             bed, but as you draw back the shower curtain, you remember just how bad you were at chemistry 
             because it looks like you've botched the job for a second time."
            "You swear to yourself and grumble all the way to bed. Tomorrow you'll look up how to liquefy a body
             properly, you decide. There are weirder things in your Internet search history, anyway."
            jump end_chem
        "You decide to relax for the day. ":
            "It's been a stressful weekend for you." 
            "You call the dinner party guests and let them know you need to cancel. You tell them it's a family 
             emergency, and they tell you that they understand."
            "You spend all day lounging around the house, working on those things you always wanted to do but 
             never seemed to find the time for before today. You know how to treat yourself right. But it gets 
             to the point where you realize you'd like to be able to soak in the bath, and right now, that's 
             not really an option."
            scene bg bath real at truecenter with fade
            with Pause(1)
            scene bg bath at truecenter with dissolve
            
            "The bathtub you tried to destroy the body in is getting seriously disgusting. It's almost as bad 
             as that time the shower drain was clogged and no one bothered to get it fixed for at least a month. 
             You shudder at the memory. You can't let that happen again."
            "You do a quick Internet search for cheap plumbers and make a couple calls. You let them know you 
             want to pay in cash. They probably assume it's for tax evasion purposes, and you don't bother 
             correcting them that it's because you don't want a paper trail linking them to you. Finally, 
             one plumber tells you he can make it in later that day. You tell him that would be great."
            show plumber at right with easeinright
            "He gets there a couple hours later, looks at the bathtub, and then looks at you. “It's, uh, that 
             time of the month?” you hazard, trying to explain away the blood. "
            "He seems unconvinced."
            "You promise him twice the pay you told him over the phone, and his eyes light up with greed, no more 
             questions asked. Of course, by the time he's done fixing your problem, he already knows too much. And 
             anyway, what's one plumber among friends?"
            jump end_chem


label day2feed:
    "You check your schedule for the day. The dinner party tonight that you're hosting, but that's it."
    menu:
        "You decide to relax for a couple hours. ":
            "It's been a stressful weekend for you." 
            "You spend a few hours lounging around the house, soaking in the bath, working on those things 
             you always wanted to do but never seemed to find the time for before today. You know how to treat 
             yourself right."
            "After that, you get to work right away preparing the food for your guests. You've always been a 
             stellar host, and you're not about to stop now. "
        "Prepare for the dinner part.":
            "You get to work right away preparing the food for your guests. You've always been a stellar host, 
             and you're not about to stop now. "
    scene bg kitchen real at truecenter with fade
    with Pause(1)
    scene bg kitchen at truecenter with dissolve       
    "The meat is different than you're used to, tough and difficult to prepare properly. But if there's 
    one thing you're good at, it's cooking, and by the time your guests arrive, everything is ready. 
    The dinner goes as it usually does. Your friends tell you it's the most delicious meal they've ever 
    had, and you're inclined to agree. "
    "You go on to enter the dish in countless competitions, winning prizes left and right. But soon, you 
    run out of usable meat, and demand has not slowed down. It looks like you'll just have to do what it 
    takes to meet the requests…"
    jump end_chef

  
label day2garden:
    "You wake up unusually calm, all things considered. You got a considerably amount of sleep
     and feel well rested."
    "You wonder what to do today"
    menu:
        "You decide to relax.":
            scene bg kitchen real at truecenter with fade
            with Pause(1)
            scene bg kitchen at truecenter with dissolve
            "It's been a stressful weekend for you." 
            "You call the dinner party guests and let them know you need to cancel. You tell them 
             it's a family emergency, and they tell you that they understand."
            "You spend all day lounging around the house, soaking in the bath, working on those 
             things you always wanted to do but never seemed to find the time for before today. 
             You know how to treat yourself right."
            "That night, as twilight falls, you look out over your garden appreciatively. It's 
             been a long weekend, but gardening always brought you a sense of peace. "
            scene bg garden real at truecenter with fade
            scene bg garden at truecenter with dissolve 
            "As you take a sip of your coffee, you let out a hum of contentment. Your tomatoes 
             seem to have appreciated the extra nutrients, and they are growing stronger than ever. 
             You think you will, too. "
            jump end_garden
        "You decide to prepare for the dinner party.":
            scene bg kitchen real at truecenter with fade
            with Pause(1)
            scene bg kitchen at truecenter with dissolve
            "You get to work right away preparing the food for your guests. You've always been a 
             stellar host, and you're not about to stop now. By the time they arrive, everything is 
             ready. The dinner goes uneventfully. It was good to be able to catch up with friends." 
            "After the last guest leaves, as twilight falls, you look out over your garden 
             appreciatively. It's been a long weekend, but gardening always brought you a sense of peace. "
            scene bg garden real at truecenter with fade
            with Pause(1)
            scene bg garden at truecenter with dissolve        
            "As you take a sip of your coffee, you let out a hum of contentment. Your tomatoes seem to 
             have appreciated the extra nutrients, and they are growing stronger than ever. You think 
             you will, too."
            jump end_garden

label day2lake:
    play sound ["Assets/Music/doorbell.mp3"]
    "You wake up to the sound of your doorbell. You peer out the peephole. The police!"
    scene bg garden real at truecenter with fade
    with Pause(1)
    scene bg garden at truecenter with dissolve
    show officer1 at left with easeinleft
    show officer2 at right with easeinright
    "'Excuse me, how can I help you today, officers?'"
    o1 "We just have some questions we'd like to ask you, if you wouldn't mind coming down to the station 
        with us."
    "They say it like a question, but you know it isn't. You go voluntarily."
    scene bg station real at truecenter with fade
    with Pause(1)
    scene bg station at truecenter with dissolve
    "When you get to the station, they put you in an interrogation room for an hour before anyone comes to 
     speak with you."
    "One of the officers enters and sits down at the table across from you."
    show officer2 at left with easeinleft
    o2 "Do you know why you're here?" 
    menu:
        "Yes.":
            o2 "Are you ready to confess, then?"
            menu:
                "Confess.":
                    jump confess
                "Don't confess.":
                    o2 "You know why you're here, but you won't confess?" 
                    "The officer looks at you skeptically before sighing in frustration."
                    o2 "Why can't you make this easier on all of us and just sign the damn confession?"
                    menu:
                        "Confess.":
                            jump confess
                        "Don't confess.":
                            "The officer growls at you. He leans across the table towards you and lowers his voice." 
                            o2 "That was your last chance, and you've just made the second biggest mistake 
                            of your life after what you did. You're going away for a long, long time." 
                            "He storms out of the room."
                            hide officer2 with dissolve
                            "Weeks pass before your trial, but you discover that you dumped the body at the most 
                             inconvenient time possible; the lake was dredged for dam renovations the very next day, 
                             and the body was found. Without the time to decompose properly, the police were able to 
                             identify the body. Dumping it with your spouse's wallet probably wasn't the wisest idea,
                             either, but it's not like you've done this before, so you cut yourself some slack. The 
                             jury, however, not so much, and you'll spend the rest of your foreseeable life in 
                             prison."
                            jump end_dont_surrender

                
        "No.":
            "The officer growls at you. He leans across the table towards you and lowers his voice."
            o2 "Don't play stupid with me. You know exactly why you're here, and you've just made 
                       the second biggest mistake of your life after what you did. You're going away for a long, 
                       long time."
            "He storms out of the room."
            hide officer2 with dissolve
            "Weeks pass before your trial, but you discover that you dumped the body at the most inconvenient time 
             possible; the lake was dredged for dam renovations the very next day, and the body was found. Without 
             the time to decompose properly, the police were able to identify the body." 
            "Dumping it with [spouse_name]'s wallet probably wasn't the wisest idea, either, but it's not like you've 
             done this before, so you cut yourself some slack. The jury, however, not so much, and you'll spend the 
             rest of your foreseeable life in prison."
            jump end_dont_surrender

label confess:
    "It's been a long couple days. You rub your eyes. You haven't felt this tired since that time you had to program 
     a game in seven weeks in college." 
    "With a sigh, you nod."
    "'I'm ready to pay the price,' you say as you sign the confession."
    "You only hope you get time off for good behavior."
    jump end_surrender