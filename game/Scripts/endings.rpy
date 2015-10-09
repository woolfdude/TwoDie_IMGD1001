label turnselfin:
    scene bg station real at truecenter with fade
    with Pause(1)
    scene bg station at truecenter with dissolve
    "The guilt of your actions overwhelms you, and you call for both an ambulance 
     and the police. But by the time the ambulance gets there, it's already too 
     late."
    "The police give you a moment to mourn your dead spouse before they haul you 
     away to the police station, bloody clothes and all."
    "As they begin to drag 
     you towards the squad car, all you can think is that life changes before 
     you even know it's happened."
    jump end
    return

label letthemgo:
    "You let them go without a fight. To tell the truth, you feel like 
     the fight left you a long time ago. Now you’re just tired."
    
    spouse "That's it? You agree just like that? God, I thought for sure 
            you'd try to stop me. But I guess I don't know you the way I 
            thought I did. Goodbye."
    
    "The days turn into weeks, and the weeks turn into months. It takes a 
     while, but you move on. You're glad they're happy. You still talk 
     sometimes, mostly about trivial things. The weather, new movie releases. 
     It used to hurt, but now it's more of a dull ache, and it gets better 
     every day. You'll find your own happiness somewhere, you're sure of it."
    jump end
    return

label counseling:
    spouse "I guess we could go to counseling. But it’s a lot of work. Are you 
       willing to put in the effort?"
    
    scene bg therapist real at truecenter with fade
    with Pause(1)
    scene bg therapist at truecenter with dissolve
    show spouse at left with easeinleft
        
    menu:
        "I'll do my best":
            "The worthwhile things in life all take effort. 
            That's what makes them worthwhile."
            "You schedule the counseling and attend every meeting. Your genuine desire
            to make this work shows. You give it your all, and your hard work pays off.
            The two of you live happily ever after."
        "I think we can make it":
            "You start the counseling with the best of intentions, but life always seems 
            to get in the way. Sometimes it's your job. Sometimes it's your friends. 
            Sometimes it's just your vindictive nature. But whatever the case, your 
            marriage continues to crumble. You wonder if your heart was ever in it in 
            the first place."
            "You divorce years down the road, bitter and resentful of the time wasted."
    jump end
    return
    
label end:
    scene black at truecenter with fade 
    pause (3)
    return