# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define zrl = Character("Zach Latta", color="#C5DCA0")
define m = Character("Me", color="#CEFDFF")

define victorio = Character("Victorio")
define bolb2019 = Character("Bolb2019")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    "It's a sunny day. You log onto Slack to see how many notifications have accumulated while you were gone."

    "After checking all of your notifications, you start to feel a little distant"

    "You wish there was a place you could go that was full of Hack Clubbers, just Hack Clubbers and no one else"

    "You open Slack back up. In your personal channel, you vent about this wish."

    "Suddenly, the unbelievable happens. You see the typing indicator for none other than Zach. The Zachary Latta!"

    zrl "You should make it happen."

    "So you decide. You are going to do it. You are going to create a Hack Land!"

    "First you need to figure out where."

    menu:

        m "Where should I create Hack Land?"

        "Alaska":
            jump alaska
        "Antartica":
            jump antartica
        "The Amazon":
            jump amazon

label alaska:
    m "I have chosen Alaska to create a Hack Land"

    "You get on a plane and fly to Alaska."

    $ renpy.movie_cutscene("planeCutscene.webm")

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"


label antartica:
    m "I have chosen Antartica to create a Hack Land"

    "You get on a plane and fly to Antartica."

    $ renpy.movie_cutscene("planeCutscene.webm")

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"

label amazon:
    m "I have chosen the Amazon to create a Hack Land"

    "You get on a plane and fly to the Amazon."

    $ renpy.movie_cutscene("planeCutscene.webm")

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


# step 1: create a flag
