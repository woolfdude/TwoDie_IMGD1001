# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bath = Image("images/Assets/Background/bg-bath.jpg")
image bg dining = Image("images/Assets/Background/bg-dining.jpg")
image bg garden = Image("images/Assets/Background/bg-garden.jpg")
image bg kitchen = Image("images/Assets/Background/bg-kitchen.jpg")
image bg lake = Image("images/Assets/Background/bg-lake.jpg")
image bg living = Image("images/Assets/Background/bg-living.jpg")
image bg room = Image("images/Assets/Background/bg-room.jpg")
image bg therapist = Image("images/Assets/Background/bg-therapist.jpg")
image bg station = Image("images/Assets/Background/bg-station.jpg")
image peggy = Image("images/Assets/Character/ch-neighbor.png")
image spousem = Image("images/Assets/Character/ch-spouse-m.png")
image spousef = Image("images/Assets/Character/ch-spouse-f.png")


define gender = "female"
image logo = Image("images/Assets/Misc/ms-logo.png")

# Declare characters used by this game.
define p = Character('Peggy', color="#c8ffc8")

$ suspicion = 0
# The game starts here.

label splashscreen:
    scene black 
    with Pause(1)
    show logo at truecenter with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return
    

label start: 
    play music ["Music/music2.mp3", "Music/music6.mp3"] loop
    jump intro

label intro: 
    scene black 
    menu:
        "Male":
            $ gender = "male"
        "Female":
            $ gender = "female"
    if gender == "male":
        $ player_name = renpy.input("What is your name?")
        if player_name == "":
            $ player_name="Kiran"
        $ spouse_name = renpy.input("And your wife's name?")
        if spouse_name == "":
            $ spouse_name="Sharon"
        
        
    elif gender == "female":
        $ player_name = renpy.input("What is your name?")
        if player_name == "":
            $ player_name="Sharon"
        $ spouse_name = renpy.input("And your husband's name?")
        if spouse_name == "":
            $ spouse_name="Kiran"
    
    define player = Character('[player_name]', color="#c8ffc8")
    define spouse = Character('[spouse_name]', color="#c8ffc8")
    "I'm sorry to break it to you, [player_name], but..."
    
    jump conflict






label conflict:
    scene bg kitchen at truecenter with fade
    "After a tense dinner party with some of your closest friends, 
     you’re in the kitchen cleaning up and preparing dinner for 
     the upcoming week and trying not to think about the growing 
     rift between you and your spouse. They break the angry silence."
    
    if gender == "male":
        show spousef at left with easeinleft
    elif gender == "female":
        show spousem at left with easeinleft
        
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
    "You feel a spark inside your chest grow into a will to fight. “No,” you say."
    spouse "'No?' What are you going to do about it?"
    hide spouse with dissolve
    menu:
         "Suggest Counseling":
              jump counseling
         "Get Mad":
              jump murder
    return
    
    
    
label murder:
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
    scene bg living with fade
    "*phone rings*"
    show peggy at right with easeinright
    p "Hey [player_name],just calling to check up with you guys. How's the 
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
    "Peggy hangs up"
    jump hidebody
    return
    
label hidebody:
    scene bg kitchen with fade
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
    scene bg bath with fade
    "Unfortunately, you were never much good at chemistry, and you botch the whole 
     thing, clogging the shower drain in the process. The plumber you call in fixes 
     it for you, but by then, he knows too much. And anyway, what's one plumber among friends?"
    return
    
label lake:
    scene bg lake with fade
    "The lake is dredged for dam renovations, and the body is found. Fortunately, 
     so are several others. Looks like you're in the clear for a while yet. "
    return
    
label plants:
    scene bg garden with fade
    "Your tomatoes appreciate the extra nutrients and grow stronger than ever."
    return
    
label feed:
    scene bg dining with fade
    "Your dinner guests tell you it's the most delicious meal they've ever had. 
     You go on to enter the dish in countless competitions, winning prizes left 
     and right. But soon, you run out of usable meat, and demand has not slowed 
     down. It looks like you'll just have to do what it takes to meet the requests."
    return
    
label turnselfin:
    scene bg station with fade
    "The guilt of your actions overwhelms you, and you call for both an ambulance 
     and the police. But by the time the ambulance gets there, it's already too 
     late."
    "The police give you a moment to mourn your dead spouse before they haul you 
     away to the police station, bloody clothes and all. As they begin to drag 
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
    return



label counseling:
    spouse "I guess we could go to counseling. But it’s a lot of work. Are you 
       willing to put in the effort?"
    
    scene bg therapist with fade
    if gender == "male":
        show spousef at left with easeinleft
    elif gender == "female":
        show spousem at left with easeinleft
        
    "The worthwhile things in life all take effort. 
    That's what makes them worthwhile."

    "You schedule the counseling and attend every meeting. Your genuine desire
    to make this work shows. You give it your all, and your hard work pays off.
    The two of you live happily ever after."
    
    "You start the counseling with the best of intentions, but life always seems 
    to get in the way. Sometimes it's your job. Sometimes it's your friends. 
    Sometimes it's just your vindictive nature. But whatever the case, your 
    marriage continues to crumble. You wonder if your heart was ever in it in 
    the first place."
    "You divorce years down the road, bitter and resentful of the time wasted."
    jump end
    return
    
    
label end:
    scene black with fade
    if gender == "male":
        hide spousef with fade
    elif gender == "female":
        hide spousem with fade
    stop music fadeout .1
    with Pause(4)