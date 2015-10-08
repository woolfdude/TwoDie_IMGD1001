image bg bath = Image("images/Assets/Background/bg-bath.jpg")
image bg bath real = Image("images/Assets/Background/Originals/bg-bath-original.jpg")
image bg dining = Image("images/Assets/Background/bg-dining.jpg")
image bg dining real = Image("images/Assets/Background/Originals/bg-dining-original.jpg")
image bg garden = Image("images/Assets/Background/bg-garden.jpg")
image bg garden real = Image("images/Assets/Background/Originals/bg-garden-original.jpg")
image bg kitchen = Image("images/Assets/Background/bg-kitchen.jpg")
image bg kitchen real = Image("images/Assets/Background/Originals/bg-kitchen-original.jpg")
image bg lake = Image("images/Assets/Background/bg-lake.jpg")
image bg lake real = Image("images/Assets/Background/Originals/bg-lake-original.jpg")
image bg living = Image("images/Assets/Background/bg-living.jpg")
image bg living real = Image("images/Assets/Background/Originals/bg-living-original.jpg")
image bg room = Image("images/Assets/Background/bg-room.jpg")
image bg room real = Image("images/Assets/Background/Originals/bg-room-original.jpg")
image bg therapist = Image("images/Assets/Background/bg-therapist.jpg")
image bg therapist real = Image("images/Assets/Background/Originals/bg-therapist-original.jpg")
image bg station = Image("images/Assets/Background/bg-station.jpg")
image bg station real = Image("images/Assets/Background/Originals/bg-station-original.jpg")

image peggy = Image("images/Assets/Character/ch-neighbor.png")
define p = Character('Peggy', color="#c8ffc8")

define gender = "female"
image logo = Image("images/Assets/Misc/ms-logo.png")
$ suspicion = 0


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
            
    image spouse = ConditionSwitch("gender == \"male\"", "images/Assets/Character/ch-spouse-f.png",
                               "gender == \"female\"", "images/Assets/Character/ch-spouse-m.png")
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
    
    
    
    
    
    
    