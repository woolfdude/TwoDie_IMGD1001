label endreturn:
    scene black with dissolve
    return

label end_divorce:
    scene black with fade
    call screen end_divorce()

    "The days turn into weeks, and the weeks turn into months. It takes a while, but you move on. 
    They’re with someone else now. You thought you would be angry about it, but you're glad they're happy. 
    You still talk sometimes, mostly about trivial things. The weather, new movie releases. 
    It used to hurt, but now it's more of a dull ache, and it gets better every day. You'll find your own happiness somewhere, you're sure of it."
    jump endreturn
label end_surrender:
    scene black with fade
    call screen end_surrender()
    scene black with fade
    "The judge went easy on you, all things considered. You were originally charged with second degree murder, but you had a good lawyer, and you 
     managed to get away with voluntary manslaughter charges, instead."
    "You spent ten years of a 15 year sentence in prison, but your good behavior got you out early. Today is the day of your release, and you can't 
     help but speculate on different ways that your story could have gone all those years ago…."
    jump endreturn
label end_dont_surrender:
    scene black with fade
    call screen end_dont_surrender()
    scene black with fade
    "All things considered, you made it out better than expected. You were originally charged with second degree murder and obstruction of justice, 
     but your cooperation with the investigation was taken into account, and you managed to get away with voluntary manslaughter charges, instead." 
    "You spent ten years of a 15 year sentence in prison, but your good behavior got you out early. Today is the day of your release, and you can't help 
     but speculate on different ways that your story could have gone all those years ago…."
    jump endreturn

label end_garden:
    scene black with fade   
    call screen end_garden()
    scene black with fade
    "Ten years down the road, you find someone new. You meet them at the local flower shop buying tomatoes, of all plants, and you hit it off right away. 
     [HeShe] love gardening, too, it turns out, and you think they might be a chance at a new beginning."
    "The first time [heshe] sees your garden, they compliment your tomatoes. It brings back memories you'd rather had stayed buried, and you end up cutting 
     the date short."
    "After they've left, you sit at your kitchen table and wonder about the different ways that your story could have gone all those years ago…. "
    jump endreturn
label end_chef:
    scene black with fade   
    call screen end_chef()
    scene black with fade
    "Ten years down the road, you're a celebrated chef, and your secret recipe is the speculation of the masses. For years, you've declined to reveal your secret ingredient, 
     which only fuels the hype surrounding your dishes. "
    "As your fame as a chef grows, so does the fame of the Cannibal Killer, as they've come to be called, a result of the time one of your half eaten bodies was accidentally 
     found. Fortunately, no one has linked the two yet."
    "As you sit behind the set of your cooking show, waiting to go out to film the latest episode, you can't help but speculate on different ways that your story could have 
     gone all those years ago…."
    jump endreturn

label end_chem:
    scene black with fade   
    call screen end_chem()
    scene black with fade
    "Five years down the road, you've just finished your Master's in chemistry, and you're a champion at 
     liquefying bodies or whatever else needs destroying. No more clogged drains for you, no sirree." 
    "As you sit on stage, waiting to go out and receive your diploma, you can't help but speculate on different 
     ways that your story could have gone all those years ago…."
    jump endreturn
