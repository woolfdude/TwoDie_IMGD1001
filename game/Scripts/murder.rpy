label conflict:
    scene bg kitchen real at truecenter with fade
    with Pause(1)
    scene bg kitchen at truecenter with dissolve
    "After a tense dinner party with some of your closest friends, 
     you’re in the kitchen cleaning up and preparing dinner for 
     the upcoming week and trying not to think about the growing 
     rift between you and your spouse. They break the angry silence."
    
    show spouse at left with easeinleft
        
    spouse "[player_name], Honey, I… I can't. We can't. I'm leaving you. 
            You're not the person I married. You're always tense, distant. 
            I can't remember the last time you laughed and meant it. 
            Neither of us are happy, are we?"
    menu:
        "Let them go":
            jump letthemgo
        "Stop them":
            jump stopthem
    return
    
label stopthem:
    "You feel a spark inside your chest grow into a will to fight. “No,” 
     you say. “You can't just walk out on me, walk out on us. After all 
     we've been through, I think we deserve better than that.”"
    spouse "'No?' What are you going to do about it?"
    menu:
         "Suggest Counseling":
              jump counseling
         "Get Mad":
              jump murder
    return
    
label murder:
    hide spouse with dissolve
    "The butcher knife you were using to prepare tomorrow's dinner slips and 
     slices your spouse's neck. Six or seven times. At least, that's what 
     you'll tell people if anyone ever asks."
    "The truth is that you don't even remember doing it, just finding yourself 
     standing over their body with the bloody knife in hand, wondering how you 
     got there from only talking. But you always did have an angry streak."
    menu:
        "What have I done??":
            jump turnselfin
        "They deserved it, you decide, and like hell you’re going to take the fall 
         for it.":
            jump phonecall
        "I can’t let this ruin my life, you think.":
            jump phonecall
    return    
    
    
    
    
label phonecall:
    scene bg dining real at truecenter with fade
    with Pause(1)
    scene bg dining at truecenter with dissolve
    play sound ["Music/phoneRing.mp3"]
    "*phone rings*"
    show peggy at right with easeinright
    p "Hey [player_name],just calling to check up with you guys. How's 
       [spouse_name] doing?"
    "You decide to tell her that [spouse_name].."
    menu: 
        "..is out of town":
            p "Oh, well, we’ll have to catch up some other time, then. Toodleoo!"
            
        "decided to leave you":
            p "Oh, my God, that's horrible! How are you doing? How are they doing? 
            How is the kid doing? Are you going to move past this?"
            "You reassure her that it’s over, but you’re doing well. After some 
             back and forth, she tells you she has to go."
            p "I’m so sorry to hear that. Listen, if you ever need anything, I’m 
            always here for you. You’ll make it through this. Let’s catch up 
            later, yeah?"
            
    "Peggy hangs up."
    "You take a shower to try to wash away your crime. By the time you're done, the 
     action of the day overwhelms you, and you're asleep before your head hits the pillow." 
    scene black with fade
    jump day1start
    return