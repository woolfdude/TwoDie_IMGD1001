label day1start:
    "INSERT DAY1 CHOICES"
    jump hidebody
    return







label hidebody:
    scene bg kitchen real at truecenter with fade
    with Pause(1)
    scene bg kitchen at truecenter with dissolve
    "You decide to hide the body. But where would be a good place it wouldn’t be 
     found?"
    menu:
        "You check your schedule. Ah, yes, the upcoming dinner party. Why not kill 
         two birds with one stone?":
            jump feed
        "You decide to bury the body in the garden. Your tomatoes haven’t been doing 
         so well this year, and hopefully, this fertilizer will change that.":
            jump plants
        "You dump the body, weighted down with your spouse’s old ankle weights, in the 
         local lake. It sinks to the bottom, never to be seen again… or so you hope.":
            jump lake
        "You decide to liquify the body in your bathtub. ":
            jump bathtub
            
    return        
    
label bathtub:
    scene bg bath real at truecenter with fade
    with Pause(1)
    scene bg bath at truecenter with dissolve
    "Unfortunately, you were never much good at chemistry, and you botch the whole 
     thing, clogging the shower drain in the process. The plumber you call in fixes 
     it for you, but by then, he knows too much. And anyway, what's one plumber among friends?"
    jump end
    return
    
label lake:
    scene bg lake real at truecenter with fade
    with Pause(1)
    scene bg lake at truecenter with dissolve
    "The lake is dredged for dam renovations, and the body is found. Fortunately, 
     so are several others. Looks like you're in the clear for a while yet. "
    jump end
    return
    
label plants:
    scene bg garden real at truecenter with fade
    with Pause(1)
    scene bg garden at truecenter with dissolve
    "Your tomatoes appreciate the extra nutrients and grow stronger than ever."
    jump end
    return
    
label feed:
    scene bg dining real at truecenter with fade
    with Pause(1)
    scene bg dining at truecenter with dissolve
    "Your dinner guests tell you it's the most delicious meal they've ever had. 
     You go on to enter the dish in countless competitions, winning prizes left 
     and right. But soon, you run out of usable meat, and demand has not slowed 
     down. It looks like you'll just have to do what it takes to meet the requests."
    jump end
    return