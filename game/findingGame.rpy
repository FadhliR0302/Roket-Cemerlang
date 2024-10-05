image bgGame:
    "gameimg/BGGM.png"
image robot:
    "gameimg/Robot.png"
    zoom 0.7
    xanchor 0.5
    yanchor 0.5
image plant:
    "gameimg/Plant.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    xalign 0.12
    yalign 0.38
image beferage:
    "gameimg/Minuman.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    yalign 0.65
    xalign 0.725
image train:
    "gameimg/Kereta.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    yalign 0.65
    xalign 0.12
image gas:
    "gameimg/Pom Bensin.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    yalign 0.65
    xalign 0.275
image plug:
    "gameimg/Power Charge.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    xalign 0.88
    yalign 0.38
image cement:
    "gameimg/Semen dan Sekop.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    yalign 0.38
    xalign 0.275
image chicken:
    "gameimg/Ayam.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    xalign 0.725
    yalign 0.38
image bottle:
    "gameimg/Botol Minum.png"
    zoom 0.2
    xanchor 0.5
    yanchor 0.5
    xalign 0.88
    yalign 0.65
image inventori:
    "gameimg/invntry.png"
    zoom 0.9
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.95
    


image ayam2:
    "gameimg/Ayam Tok.png"
    
image bottle2:
    "gameimg/Botol Minum Tok.png"
    
image train2:
    "gameimg/Kereta Tok.png"
    
image beferage2 :
    "gameimg/Minum tok.png"
    
image plant2:
    "gameimg/Plant Tok.png"
    
image gas2:
    "gameimg/Pom Bensin tok.png"
    
image plug2:
    "gameimg/Power Charge tok.png"
  
    
image cement2:
    "gameimg/Semen dan Sekop Tok.png"
    
transform button:
    zoom 0.2
    xanchor 1.0
    yanchor 0.5
    yalign 0.5
    xalign 1.0
    pause 0.25
    ease 0.25 zoom 0.2 
    on hover:
        ease 0.25 zoom 0.16 
    on idle:
        ease 0.25 zoom 0.2
transform inventori:
    zoom 0.1
    xanchor 0.5
    yanchor 0.5 
    xalign 0.5
    yalign 0.8
transform inventori_ayam:
    zoom 0.1
    xanchor 0.5
    yanchor 0.5 
    xalign 0.5
    yalign 0.8


label finding_game:
    scene bgGame
    show robot at center 
    show plant
    show beferage
    show train
    show gas
    show plug
    show cement
    show chicken
    show bottle
    
    
    e "we can’t move on. You need to find these items first. In case you forgot, that is the result product of C.H.A.R mission. 
Let’s check in here!"
    scene bgGame
    
    
    call screen gamestart

    return

# default plugfind = False
# default trainfind = False
# default plantfind = False
# default cementfind = False
# default gasfind = False
# default bottlefind = False
# default ayamfind = False
# default beferagefind = False
default plugfind = False
default trainfind = False
default plantfind = False
default cementfind = False
default gasfind = False
default bottlefind = False
default ayamfind = False
default beferagefind = False

transform plug:
    zoom 0.07
    # xoffset 300
    # yoffset 125
    xpos 300
    ypos 125

transform cement:
    zoom 0.08
    xpos 1555
    ypos 20

transform train:
    zoom 0.15
    xpos 600
    ypos 500

transform gas:
    zoom 0.125
    xpos 1100
    ypos 458

transform bottle:
    zoom 0.08
    xpos 1150
    ypos 600

transform ayam:
    zoom 0.07
    xpos 1450
    ypos 470

transform beferage:
    zoom 0.1
    xpos 10
    ypos 475

transform plant:
    zoom 0.1
    xpos -50
    ypos 90

screen gamestart:
    add "bgGame"
    if plugfind == False:
        imagebutton:
            idle "plug2" hover "plug2" at plug action ToggleVariable("plugfind")
    if cementfind == False:            
        imagebutton:
            idle "cement2" hover "cement2" at cement action ToggleVariable("cementfind")
    if trainfind == False:
        imagebutton:
            idle "train2" hover "train2" at train action ToggleVariable("trainfind")
    if gasfind == False:
        imagebutton:
            idle "gas2" hover "gas2" at gas action ToggleVariable("gasfind")
    if bottlefind == False:
        imagebutton:
            idle "bottle2" hover "bottle2" at bottle action ToggleVariable("bottlefind")
    if ayamfind == False:
        imagebutton:
            idle "ayam2" hover "ayam2" at ayam action ToggleVariable("ayamfind")
    if beferagefind == False:
        imagebutton:
            idle "beferage2" hover "beferage2" at beferage action ToggleVariable("beferagefind")
    if plantfind == False:
        imagebutton:
            idle "plant2" hover "plant2" at plant action ToggleVariable("plantfind")

    add "inventori"


    hbox xalign 0.5 yalign 0.92:
        if ayamfind == True:
            add "gameimg/Ayam Tok.png" at inventori_ayam
        if beferagefind == True:
            add "gameimg/Minum tok.png" at inventori
        if bottlefind == True:
            add "gameimg/Botol Minum Tok.png" at inventori
        if cementfind == True:
            add "gameimg/Semen dan Sekop Tok.png" at inventori
        if plantfind == True:
            add "gameimg/Plant Tok.png" at inventori
        if gasfind == True:
            add "gameimg/Pom Bensin tok.png" at inventori
        if trainfind == True:
            add "gameimg/Kereta Tok.png" at inventori
        if plugfind == True:
            add "gameimg/Power Charge tok.png" at inventori

    # if ayamfind == beferagefind == bottlefind == cementfind == plantfind == gasfind == trainfind == plugfind == True:
    #     pass
    if all([ayamfind, beferagefind, bottlefind, cementfind, plantfind, gasfind, trainfind, plugfind]):
        imagebutton:
            idle "gameimg/Tanda Panah.png" hover "gameimg/Tanda Panah.png" at button action Jump("winning")


label winning:
    show robot at center
    e "Great! All items has found.  Now, you will head to our last mission... "