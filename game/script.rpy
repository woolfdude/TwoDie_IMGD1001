# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg lake = Image("images/bg_lake.png")
image logo = Image("images/dice.png")

# Declare characters used by this game.
define w = Character('Waifu', color="#c8ffc8")
define p = Character('Peggy', color="#c8ffc8")


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
    play music "Cheremisinov.mp3"
    scene bg lake at truecenter  with fade
    
    jump conflict
    return

label conflict:
    "Things were getting heated in a fight with your wife"
    w "I'm leaving you"
    menu:
        "Let her go":
            jump lethergo
        "Beg her":
            jump counseling
        "Stop her (however necisary)":
            jump murder
    return

label murder:
    
    "The large butcher knife you were using to slice potatoes slips out 
     of your hand and gashes your wifes neck. Six or seven times."
    "Yeah, she's dead"
    menu:
        "Oh god what have I done?":
            jump turnselfin
        "She deserved it and like hell I'm going to take the fall for it.":
            jump phonecall
        "I can't let this ruin my life":
            jump phonecall
    return

label phonecall:
    "RING RING"
    p "Hi! How is waifu?"
    menu: 
        "She is out of town":
            jump hidebody
        "She left me":
            jump hidebody
    return

label hidebody:
    "You have dinner guests coming over tonight, you had better hide the body"
    menu:
        "I mean, you also need to make food. Why not both?":
            jump feed
        "burying it in the garden. Your tomatoes haven't been doing so well this 
         year, and hopefully, this fertilizer will change that.":
            jump plants
        "dumping it in the lake":
            jump lake
        "bleach in the bahtub":
            jump bathtub
            
    return
    
label bathtub:
    "Unfortunately, you were never much good at chemistry, and you botch the whole 
     thing, clogging the shower drain in the process. The plumber you call in fixes 
     it for you, but by then, he knows too much. And anyway, what's one plumber among friends?"
    return
    
label lake:
    "The lake is dredged for dam renovations, and the body is found. Fortunately, 
     so are several others. Looks like you're in the clear for a while yet. "
    return
    
label plants:
    "Your tomatoes appreciate the extra nutrients and grow stronger than ever."
    return
    
label feed:
    "Your dinner guests tell you it's the most delicious meal they've ever had. 
     You go on to enter the dish in countless competitions, winning prizes left 
     and right. But soon, you run out of usable meat, and demand has not slowed 
     down. It looks like you'll just have to do what it takes to meet the requests."
    return
    
label turnselfin:
    "The guilt of what you've done overwhelms you, and you turn yourself in."
    return




label lethergo:
    "You're glad they're happy. You still talk sometimes, mostly about 
trivial things. The weather, new movie releases. It used to hurt, but 
now it's more of a dull ache, and it gets better every day. You'll find 
your own happiness somewhere, you're sure of it."
    return







label counseling:
    w "I mean..."
    w "We could try counseling?"
    "You now have counseling 14 times a week for 2 hours."
    menu:
        "Fuck that":
            jump divorce
        "Devote yourself":
            jump everafter
    return
label divorce:
    "You divorce years down the road, bitter and resentful of the time wasted."
    return
    
label everafter:
    "Live happily ever after"
    "For now"
    