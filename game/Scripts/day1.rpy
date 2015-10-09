


label day1start:
    define currentchoice = "none"
    "You wake up in a cold sweat."
    "You wonder how to move forward after last night. You decide to check the calendar."
    "The calendar is fairly empty, you have a brunch with friends later today, andare hosting a dinner 
     party tomorrow."
    
    menu:
        "Lay low for a while":
            "You decide to lay low for a while, avoid the public eye. You burn the 
             bloody clothes in the fireplace and clean up around the house, doing 
            all the chores you never seemed to have the time to do before."
            jump day1mid
        "Hide the Body":
            jump hidebody
    return


label day1mid:
    scene bg living real at truecenter with fade
    with Pause(1)
    scene bg living at truecenter with dissolve
    "It's almost time for your weekly brunch with Sam and Patricia."
    "Shit!  They'll be expecting you. Both of you. What do you do?"
    menu:
        "Go to brunch":
            jump brunch
        "Skip it":
            jump skipbrunch
    return
    
label day1end:
    if currentchoice == "none":
        jump hidebody
    scene black with fade
    "That night, as you drift off to sleep, you're filled with anticipation for what's to come."
    jump day2start
    return


label skipbrunch:
    play sound ["Music/phoneRing.mp3"]
    "*phone rings*"
    sam "Hello?"
    "'*violently coughing* Ugh, sorry. Hey, this is ____. I'm just calling to let you know that we 
     won't be able to make it to brunch today. We've come down with something awful, and we want to 
     make sure it's not contagious.'"
    sam "Oh, man, that's too bad. Alright, I'll let Patricia know. Here's hoping you guys feel 
         better soon. "
    "'Yeah, thanks. Enjoy your brunch.'"
    "You're glad that that's out of the way. You're not sure how convincing a job you could have 
     done of explaining away your spouse's absence in person."

label brunch:
    "You decide to to the brunch anyway."
    show patricia at left with easeinleft
    show sam at right with easeinright
    sam "Hey, [player_name], how are you?"
    patricia "Say, where's [spouse_name]?"
    "It's the question you've been dreading. How do you explain away your spouse's absence?"
    menu:
        "[spouse_name] is on a business trip.":
            patricia "I thought they stayed at home?"
            "She immediately looks embarrassed at what she has said."
            patricia "I mean, not that there's anything wrong with that, of course. I just thought..."
            "Sam shushes her."
            sam "Don't be rude, Patricia. Maybe they got a new job."
            "He turns to you. "
            sam "“I, for one, am glad to hear about this development in their career. You must be very 
                 proud. 
            A toast to [spouse_name]!"
            "You all raise your glasses in a toast."
            "The rest of the brunch goes uneventfully. You silently breathe a sigh of relief as you head 
             back home."
            jump day1end
        "[spouse_name] is home sick.":
            patricia "Oh, my God, that's terrible! "
            "She eyes you warily. "
            patricia "Is it contagious?"
            menu:
                "You assure her it's not and that she just didn't want her being under the weather to 
                 ruin the mood for everyone else.":
                    "The rest of the brunch goes uneventfully. You silently breathe a sigh of relief as 
                     you head back home."
                    jump day1end
                "'You know, I'm really not sure...'":
                    "Patricia and Sam surreptitiously lean away from you."
                    sam "Well, maybe it's better if you stay home, too. Wouldn't want to risk it, you 
                          know."
                    "You agree and say your goodbyes. You silently breathe a sigh of relief as you head 
                    back home."
                    jump day1end
    return

label hidebody:
    scene bg kitchen real at truecenter with fade
    with Pause(1)
    scene bg kitchen at truecenter with dissolve
    "You decide to hide the body. But where would be a good place it wouldn’t be 
     found?"
    menu:
        "The Dinner Party":
            $ currentchoice = "feed"
            jump feed
        "The Garden":
            $ currentchoice = "garden"
            jump plants
        "The lake":
            $ currentchoice = "lake"
            jump lake
        "The Bathtub":
            $ currentchoice = "bath"
            jump bathtub
            
    return        
    
label bathtub:
    scene bg bath real at truecenter with fade
    with Pause(1)
    scene bg bath at truecenter with dissolve
    "You decide to liquefy the body in your bathtub. You've seen enough TV shows and 
     movies where this happens, so you figure you've got this covered. Unfortunately, 
     you were never much good at chemistry, and you botch the whole thing, clogging the 
     shower drain in the process. "
    "'Well shit. Now what am I supposed to do?'"
    "You glance at the clock. It's getting late."
    "'Well, there's no time to deal with this now. I'll figure something out later.'"
    jump day1end
    return
    
label lake:
    scene bg lake real at truecenter with fade
    with Pause(1)
    scene bg lake at truecenter with dissolve
    play sound ["Music/splashCut.mp3"]
    "You dump the body, weighted down with your spouse's old ankle weights, in the local 
     lake. It's harder to do than you thought it would be. There's heavy machinery and 
     construction workers all over the place, and you have to wait until they all leave 
     before you make your move.  "
    "The body sinks to the bottom, never to be seen again… or so you hope. "
    jump day1end
    return
    
label plants:
    scene bg garden real at truecenter with fade
    with Pause(1)
    scene bg garden at truecenter with dissolve
    "You wait until nightfall. It wouldn't do for people to see you burying body parts."
    "By the light of the moon, you bury the body in the garden. Your tomatoes haven't 
     been doing so well this year, and hopefully, this fertilizer will change that. "
    jump day1end
    return
    
label feed:
    scene bg dining real at truecenter with fade
    with Pause(1)
    scene bg dining at truecenter with dissolve
    "Ah, yes, the upcoming dinner party. Why not kill two birds with one stone, so to 
     speak? You spend the rest of the day running various recipes through your head, 
     sifting through your cookbooks and discarding different dishes until you settle
     on the perfect meal. "
    jump day1end
    return