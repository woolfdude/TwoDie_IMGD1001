    label opening:
        scene bg kitchen real at truecenter with fade
        with Pause(1)
        scene bg kitchen at truecenter with dissolve
        show spouse at left with easeinleft
        spouse "Honey, I… I can’t. We can’t. I’m leaving you. You’re not the [manwoman] I married." 
        spouse "You’re always tense, distant. I can’t remember the last time you laughed and meant it." 
        spouse "Neither of us are happy, are we?"
        menu:
            "Let them go":
                    "You let them go without a fight. To tell the truth, you feel like the fight left you a long time ago. Now you’re just tired."
                    spouse "That’s it? You agree just like that? God, you’re pathetic!"
                    "You don’t even see the slap coming until it’s already happened. You stare at your spouse in disbelief. After that, everything happens in a blur." 
                    jump murder
            "Stop Them":
                    "You feel a spark inside your chest grow into a will to fight." 
                    player "No,"
                    player "You can’t just walk out on me, walk out on us. After all we’ve been through, I think we deserve better than that."
                    spouse "'No?’ What are you going to do about it?"
                    menu:
                            "Suggest counseling":
                                    spouse "I guess we could go to counseling. But it’s a lot of work. Are you willing to put in that kind of effort?"
                                    scene bg therapist real at truecenter with fade
                                    with Pause(1)
                                    scene bg therapist at truecenter with dissolve
                                    player "The worthwhile things in life all take effort. That’s what makes them worthwhile."
                                    "You start the counseling with the best of intentions, but life always seems to get in the way."
                                    "Sometimes it’s your job. Sometimes it’s your friends. Sometimes it’s just your vindictive nature."
                                    "But whatever the case, your marriage continues to crumble. You wonder if your heart was ever in it in the first place. "
                                    "You divorce years down the road, bitter and resentful of the time wasted."
                                    jump end_divorce
                            "Kill them":
                                jump murder

    label murder:
        "The butcher knife you were using to prepare tomorrow’s dinner slips and slices your spouse’s neck. Six or seven times." 
        hide spouse with dissolve
        "At least, that’s what you’ll tell people if anyone ever asks. The truth is that you don’t even remember doing it, just finding yourself standing over their body with the 
         bloody knife in hand, wondering how you got there from only talking. But you always did have an angry streak." 
        menu:
            "What have I done? I have to turn myself in...":
                "The guilt of your actions overwhelms you, and you call for both an ambulance and the police." 
                
                show officer1 at center with easeinright
                show officer2 at right with easeinright
                "By the time the ambulance gets there, it's already too late. 
                 The police give you a moment to mourn before they haul you away to the police station, bloody clothes and all. As they begin to drag you 
                 towards the squad car, all you can think is that life changes before you even know it's happened."
                jump end_surrender
            "[HeShe] deserved it, you decide, and like hell you're going to take the fall for it.":
                player "I can't let this ruin my life."
                
    label phonecall:
        scene bg living real at truecenter with fade
        with Pause(1)
        scene bg living at truecenter with dissolve
        play sound ["Assets/Music/phoneRing.mp3"]
        show peggy at right with easeinright
        p "Hey, [player_name], just calling to check up with you guys. How's [spouse_name] doing?"
        player "[HeShe]..."
        menu:
            "... is out of town":
                "Oh, well, we'll have to catch up some other time, then. Toodleoo!"
            "decided to leave you.":
                p "Oh, Oh, my God, that's horrible! How are you doing? How is [heshe] doing? How are you going to move past this?"
                "You reassure her that it's over, but you're doing well. After some back and forth, she tells you she has to go."
                p "I'm so sorry to hear that. Listen, if you ever need anything, I'm always here for you. You'll make it through this. 
                   Let's catch up later, yeah?"
        "Peggy hangs up."
        scene black with fade
        "You take a shower to try to wash away your crime. By the time you're done, the action of the day overwhelms you, and you're asleep before your head hits the pillow. "
        jump chapter2
                