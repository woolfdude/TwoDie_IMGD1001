# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg lake = "Lake.jpg"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define s = Character('Saul', color="#c8ffc4")


# The game starts here.

label start:
    play music "Cheremisinov.mp3"
    scene bg lake at truecenter  with fade
    
    "Welcome to the example game."
    "Here you get to make a choice!!!"
    menu:
        "So you could choose this":
            jump option1
        "... Or This":
            jump option2
        "... Or just go back":
            jump start
    return


label option1:
    e "You chose option 1, Bitch."
    return
    
label option2:
    s "You chose option 2, Bitch."
    return
    