# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define zrl = Character("Zach Latta", color="#C5DCA0")
define m = Character("Me", color="#CEFDFF")

define AkaalroopSingh = Character("Akaalroop Singh (@Akaalroop)")
image AkaalroopSinghImage = "game/images/ts/Akaalroop Singh.png"

define DanielLialin = Character("Daniel Lialin (@Daniel)")
image DanielLialinImage = "game/images/ts/Daniel Lialin.png"

define AileenRivera = Character("Aileen Rivera (@aïleen)")
image AileenRiveraImage = "game/images/ts/Aileen Rivera.png"




define AaravJ = Character("Aarav J (@Aarav J)")



define victorio = Character("Victorio (@Vic)")
define bolb2019 = Character("Bolb2019 (@Bolb2019)")
define ClayNicholson = Character("Clay Nicholson (@CAN)")
define Kashyap = Character("Kashyap (@kashsuks)")
define ShayaanAdib = Character("Shayaan Adib (@One For Freedom)")
define SatyamRaj = Character("Satyam Raj (@Satyam Raj)")
define AnahitaMayekar = Character("Anahita Mayekar (@Ana)")
define NishanthMynam = Character("Nishanth Mynam (@Chesspotato)")
define Youssef = Character("Youssef (@Youssef)")




image victorio = "ts/Victorio.png"
image bolb2019 = "ts/Bolb2019.png"
image ClayNicholson = "ts/Clay Nicholson.jpg"
image Kashyap = "ts/Kashyap.png"
image ShayaanAdib = "ts/Shayaan Adib.png"
image SatyamRaj = "ts/Satyam Raj.png"
image AnahitaMayekar = "ts/Anahita Mayekar.png"
image NishanthMynam = "ts/Nishanth Mynam.png"
image Youssef = "ts/Youssef.png"

transform half_size: 
    zoom 0.5

transform quarter_size:
    zoom 0.25



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

    scene bg alaska # see task list

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"

    m "Hello everyone! I can't wait to work with you all to make this happen! I think the first order of buisness is to create our flag."

    "You have everyone there nominate three artists to design what they think the Hack Land flag should look like."

    "Then, after each artist has created their flag, you put them all up on poles, and you all collectively vote on the best one."

    menu:

        "Which flag does the group choose?"

        "Blahaj Flag":
            jump blahajAlaska
        "Cat Flag":
            jump catAlaska
        "Paper Airplane Flag":
            jump airplaneFlag

label blahajAlaska:
    "The group decides on the Blahaj flag. The flag is raised up into the air"

    $ renpy.movie_cutscene("blahajAlaska.webm") # see task list

    show blahajAlaska at right

    "Everyone cheers!!"

label catAlaska:
    "The group decides on the cat flag. The flag is raised into the air"

    $ renpy.movie_cutscene("catAlaska.webm") # see task list

    show catAlaska at right

    "Everyone cheers!!"

label airplaneAlaska:
    "The group decides on the paper airplane flag. The flag is raised into the air"

    $ renpy.movie_cutscene("airplaneAlaska.webm") # see task list

    show airplaneAlaska at right

    "Everyone cheers!!"



label antartica:
    m "I have chosen Antartica to create a Hack Land"

    "You get on a plane and fly to Antartica."

    $ renpy.movie_cutscene("planeCutscene.webm")

    scene bg antartica # see task list

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"

    m "Hello everyone! I can't wait to work with you all to make this happen! I think the first order of buisness is to create our flag."

    "You have everyone there nominate three artists to design what they think the Hack Land flag should look like."

    "Then, after each artist has created their flag, you put them all up on poles, and you all collectively vote on the best one."

    menu:

        "Which flag does the group choose?"

        "Blahaj Flag":
            jump blahajAntartica
        "Cat Flag":
            jump catAntartica
        "Paper Airplane Flag":
            jump airplaneAntartica

label blahajAntartica:
    "The group decides on the Blahaj flag. The flag is raised up into the air"

    $ renpy.movie_cutscene("blahajAntartica.webm") # see task list

    show blahajAntartica at right

    "Everyone cheers!!"

label catAntartica:
    "The group decides on the cat flag. The flag is raised into the air"

    $ renpy.movie_cutscene("catAntartica.webm") # see task list

    show catAntartica at right

    "Everyone cheers!!"

label airplaneAntartica:
    "The group decides on the paper airplane flag. The flag is raised into the air"

    $ renpy.movie_cutscene("airplaneAntartica.webm") # see task list

    show airplaneAntartica at right

    "Everyone cheers!!"


label amazon:
    m "I have chosen the Amazon to create a Hack Land"

    "You get on a plane and fly to the Amazon."

    $ renpy.movie_cutscene("planeCutscene.webm")

    scene bg amazon # see task list

    "There you are greeted by some of your favorite Hack Clubbers, ready to help you start up Hack Land!"

    m "Hello everyone! I can't wait to work with you all to make this happen! I think the first order of buisness is to create our flag."

    "You have everyone there nominate three artists to design what they think the Hack Land flag should look like."

    "Then, after each artist has created their flag, you put them all up on poles, and you all collectively vote on the best one."

    menu:

        "Which flag does the group choose?"

        "Blahaj Flag":
            jump blahajAmazon
        "Cat Flag":
            jump catAmazon
        "Paper Airplane Flag":
            jump airplaneAmazon

label blahajAmazon:
    "The group decides on the Blahaj flag. The flag is raised up into the air"

    $ renpy.movie_cutscene("blahajAmazon.webm") # see task list

    show blahajAmazon at right

    "Everyone cheers!!"

label catAmazon:
    "The group decides on the cat flag. The flag is raised into the air"

    $ renpy.movie_cutscene("catAmazon.webm") # see task list

    show catAmazon at right

    "Everyone cheers!!"

label airplaneAmazon:
    "The group decides on the paper airplane flag. The flag is raised into the air"

    $ renpy.movie_cutscene("airplaneAmazon.webm") # see task list

    show airplaneAmazon at right

    "Everyone cheers!!"



# step 1: create a flag
# step 2: elect a honorary leader


# todo: 
# * create blahaj flag
# * create blahaj alaska flag cutscene
# * create blahaj antartica flag cutscene
# * create blahaj amazon flag cutscene

# * create cat flag
# * create cat alaska flag cutscene
# * create cat antartica flag cutscene
# * create cat amazon flag cutscene

# * create paper airplane flag
# * create paper airplane alaska flag cutscene
# * create paper airplane antartica flag cutscene
# * create paper airplane amazon flag cutscene

# * create alaska bg
# * create antartica bg
# * create amazon bg