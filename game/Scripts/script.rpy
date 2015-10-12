image bg bath = Image("Assets/images/Background/bg-bath.jpg")
image bg bath real = Image("Assets/images/Background/Originals/bg-bath-original.jpg")
image bg dining = Image("Assets/images/Background/bg-dining.jpg")
image bg dining real = Image("Assets/images/Background/Originals/bg-dining-original.jpg")
image bg garden = Image("Assets/images/Background/bg-garden.jpg")
image bg garden real = Image("Assets/images/Background/Originals/bg-garden-original.jpg")
image bg kitchen = Image("Assets/images/Background/bg-kitchen.jpg")
image bg kitchen real = Image("Assets/images/Background/Originals/bg-kitchen-original.jpg")
image bg lake = Image("Assets/images/Background/bg-lake.jpg")
image bg lake real = Image("Assets/images/Background/Originals/bg-lake-original.jpg")
image bg living = Image("Assets/images/Background/bg-living.jpg")
image bg living real = Image("Assets/images/Background/Originals/bg-living-original.jpg")
image bg room = Image("Assets/images/Background/bg-room.jpg")
image bg room real = Image("Assets/images/Background/Originals/bg-room-original.jpg")
image bg therapist = Image("Assets/images/Background/bg-therapist.jpg")
image bg therapist real = Image("Assets/images/Background/Originals/bg-therapist-original.jpg")
image bg station = Image("Assets/images/Background/bg-station.jpg")
image bg station real = Image("Assets/images/Background/Originals/bg-station-original.jpg")

image peggy = Image("Assets/images/Character/ch-neighbor.png")
image sam = Image("Assets/images/Character/ch-atendee-2.png")
image patricia = Image("Assets/images/Character/ch-atendee-3.png")
image officer1 = Image("Assets/images/Character/ch-officer-1.png")
image officer2 = Image("Assets/images/Character/ch-officer-2.png")
image plumber = Image("Assets/images/Character/ch-plumber.png")

image logo = Image("Assets/images/Misc/ms-logo.png")

define s = Character('Sam', color="#c8ffc8")
define p = Character('Peggy', color="#c8ffc8")
define pa = Character('Patricia', color="#c8ffc8")
define o2 = Character('Second Officer', color="#c8ffc8")
define o1 = Character('First Officer', color="#c8ffc8")


define gender = "female"


label splashscreen:
    scene black 
    with Pause(1)
    show logo at truecenter with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return


label start:
    play music ["Assets/Music/music2.mp3", "Assets/Music/music6.mp3"] loop
    jump intro



label intro: 
    scene black 
    menu:
        "Male":
            $ gender = "male"
        "Female":
            $ gender = "female"
            
    image spouse = ConditionSwitch("gender == \"male\"", "Assets/images/Character/ch-spouse-f.png",
                               "gender == \"female\"", "Assets/images/Character/ch-spouse-m.png")
    if gender == "male":
        $ player_name = renpy.input("What is your name?")
        if player_name == "":
            $ player_name="Kiran"
        $ spouse_name = renpy.input("And your wife's name?")
        if spouse_name == "":
            $ spouse_name="Sharon"
        $ heshe = "she"
        $ manwoman = "man"
        $ HeShe = "She"
    elif gender == "female":
        $ player_name = renpy.input("What is your name?")
        if player_name == "":
            $ player_name="Sharon"
        $ spouse_name = renpy.input("And your husband's name?")
        if spouse_name == "":
            $ spouse_name="Kiran"
        $ heshe = "he"
        $ HeShe = "He"
        $ manwoman = "woman"
    define player = Character('You', color="#66bdc9")
    define spouse = Character('[spouse_name]', color="#c8ffc8")
    "I'm sorry to break it to you, [player_name], but..."
    jump opening
