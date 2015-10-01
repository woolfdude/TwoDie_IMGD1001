# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bath = Image("images/Assets/Background/bg-bath.jpg")
image bg dining = Image("images/Assets/Background/bg-dining.jpg")
image bg garden = Image("images/Assets/Background/bg-garden.jpg")
image bg kitchen = Image("images/Assets/Background/bg-kitchen.jpg")
image bg lake = Image("images/Assets/Background/bg-lake.jpg")
image bg living = Image("images/Assets/Background/bg-dining.jpg") #REVERT BACK TO LIVING
image bg room = Image("images/Assets/Background/bg-room.jpg")
image bg station = Image("images/Assets/Background/bg-station.jpg")
image spouse = Image("images/Assets/Character/ch-spouse-f.png")


image peggy = Image("images/Assets/Character/ch-neighbor.png")

image logo = Image("images/Assets/Misc/ms-logo.png")

# Declare characters used by this game.
define spouse = Character('Spouse', color="#c8ffc8")
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
    play music "Cheremisinov.mp3"
    return
    

label start:  
    jump intro
    return

label intro:
    scene black 
    $ player_name = renpy.input("What is your name?")
    if player_name == "":
        $ player_name="Kiran"
    $ spouse_name = renpy.input("And your spouse's name?")
    if spouse_name == "":
        $ spouse_name="Sharon"
    define spouse = Character('[spouse_name]', color="#c8ffc8")
    "I'm sorry to break it to you, [player_name], but..."
    jump conflict

label conflict:
    scene bg kitchen at truecenter with fade
    "After a tense dinner party with some of your closest friends, 
     you’re in the kitchen cleaning up and preparing dinner for 
     the upcoming week and trying not to think about the growing 
     rift between you and your spouse. They break the angry silence."
    show spouse at left with easeinleft
    spouse "[player_name], I… I can’t. We can’t. I’m leaving you."
    hide spouse with dissolve
    menu:
        "Let them go":
            jump lethergo
        "Stop them":
            jump stopthem
    return

label stopthem:
    "You feel a spark inside your chest grow into a will to fight. “No,” you say."
    show spouse at left
    spouse "'No?' What are you going to do about it?"
    hide spouse with dissolve
    menu:
         "Go to counseling":
              jump counseling
         "Kill them":
              jump murder
    return
label murder:
    "The butcher knife you were using to prepare tomorrow’s dinner slips 
    and slices your spouse’s neck. Six or seven times."
    menu:
        "The guilt of what you’ve done overwhelms you, and you turn yourself in.":
            jump turnselfin
        "They deserved it, you decide, and like hell you’re going to take the fall for it.":
            jump phonecall
        "I can’t let this ruin my life, you think.":
            jump phonecall
    return

label phonecall:
    scene bg living with fade
    "*phone rings*"
    show peggy at right with easeinright
    p "Hi! How is [spouse_name]?"
    menu: 
        "She is out of town":
            show peggy at right with easeinright
            p "Oh, well, we’ll have to catch up some other time, then. Toodleoo!"
            jump hidebody
        "She left me":
            show peggy at right with easeinright
            p "Oh, my God, that’s horrible! How are you doing? How is she doing? 
               How is the kid doing? Are you going to move past this?"
            "You reassure her that it’s over, but you’re doing well. After some 
             back and forth, she tells you she has to go."
            show peggy at right
            p "I’m so sorry to hear that. Listen, if you ever need anything, I’m 
               always here for you. You’ll make it through this. Let’s catch up 
               later, yeah?"
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
    "The guilt of what you've done overwhelms you, and you turn yourself in."
    return




label lethergo:
    "You let them go without a fight. To tell the truth, you feel like 
     the fight left you a long time ago. Now you’re just tired."
    "It takes a while, but you move on. You're glad they're happy. 
     You still talk sometimes, mostly about trivial things. The weather, 
     new movie releases. It used to hurt, but now it's more of a dull ache, 
     and it gets better every day. You'll find your own happiness somewhere, 
     you're sure of it."
    return



label counseling:
    show spouse at left
    spouse "I guess we could go to counseling. But it’s a lot of work. Are you 
       willing to put in the effort?"
    "You give it your all, and your hard work pays off. The two of you 
       live happily ever after."
    "You promise to try your best, but secretly, your heart was never in it. 
     You divorce years down the road, bitter and resentful of the time wasted."
    return