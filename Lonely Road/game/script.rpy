# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kira = DynamicCharacter("Kira_name")
define me = DynamicCharacter("Me_name")
define bartender = Character(_('Bartender'))
define policeman = Character(_('Policeman'))

image kira_dafault = 'sprites/sprite-default.png'
image kira_baka = 'sprites/sprite-baka.png'
image kira_angry = 'sprites/sprite-angry.png'
image kira_sad = 'sprites/sprite-sad.png'
image kira_idontcare = 'sprites/sprite-idontcare.png'
image kira_mi = 'sprites/sprite-mi.png'
image kira_shock = 'sprites/sprite-shock.png'
image kira_superangry = 'sprites/sprite-superangry.png'
image kira_thinking = 'sprites/sprite-thinking.png'

image bg_bar = 'background/bar.jpg'
# image bg_street = None

# $ centre-lower = Position(xanchor=0.5,xpos=0.5, yanchor=0.8, ypos=1.0)

style centered_style:
    xalign 0.5
    yalign 0.5
    # xanchor 0.5
    # xpos 0.5
    # yanchor 0.8
    # ypos 1.0

screen act_button(number=0, text_size=40):
    hbox:
        style "centered_style"
        xmaximum 300
        $ text_input = "Акт " + str(number) 
        textbutton text_input:
            action None
            text_size text_size
# The game starts here.


label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ Me_name = _('Me')
    $ Kira_name = _('Girl')

    show screen act_button(1)

label act_0:
    "Act 1"
    jump act_0_street
label act_1:
    "Act 2"
    jump act_1_bar
label act_2:
    "Act 3"
    jump act_2_bar
label act_3:
    "Act 4"
    jump act_3_bar
label act_4:
    "Act 5"
    jump act_4_street

    # These display lines of dialogue.

label end_game:
    # This ends the game.
    "To be continued..."
    return


# label credits:
#     mail = 'vereline8991@gmail.com'
#     music1 = 'liscence and title'
#     music2 = 'liscence and title'
#     music3 = 'liscence and title'
#     back_and_sprites_scenario = 'me'