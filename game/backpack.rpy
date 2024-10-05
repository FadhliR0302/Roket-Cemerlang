transform button_menu_s:
    xanchor 0.5
    yanchor 0.5
    on hover:
        zoom 2.0
        ease 0.15 zoom 2.2
    on idle:
        ease 0.15 zoom 2.0
transform button_menu_s_:
    xalign 0.95
    yalign 0.9
    xanchor 0.5
    yanchor 0.5
    zoom 2.0
    ease 0.25 zoom 0.0
    
transform button_menu:
    xanchor 0.5
    yanchor 0.5
    zoom 0.0 
    pause 0.25
    ease 0.25 zoom 1.0 
    on hover:
        ease 0.25 zoom 1.2
    on idle:
        ease 0.25 zoom 1.0
transform items_backpack:
    xanchor 0.5
    yanchor 0.5
    yalign 0.8
    zoom 0.0 
    pause 0.25
    # on hover:
    #     im.matrix.brightness(1)
    ease 0.25 zoom 1.0 
    on hover:
        ease 0.25 zoom 0.96
    on idle:
        ease 0.25 zoom 1.0
transform explanation_picture:
    xanchor 0.5
    yanchor 0.5
    xalign 0.93
    yalign 0.4
    zoom 0.0
    ease 0.25 zoom 0.15
transform explanation:
    xanchor 0.5
    yanchor 0.5
    xalign 0.93
    yalign 0.7
    zoom 0.0
    ease 0.25 zoom 0.17



transform bigging:
    xanchor 0.5
    yanchor 0.5
    zoom 0.0
    ease 0.25 zoom 1.0
transform smalling:
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    ease 0.25 zoom 0.0
transform dissapaer:
    zoom 0.0
default state_= True
default sate = True
default number_expl = 0

#items variabel
# default ghgsource = False
# default fossilfuel = False
# default greenhousegasses = False
# default carbondioxide = False
# default methane = False
# default ghgsink = False
# default globalcarbonbudget = False
# default totalcarbonbudget = False
# default topdownestiomates = False
# default lateralfluxes = False
# default bottomupestimates = False

# screen backpack:
#     if state_ == True:
#         imagebutton:
#             xalign 0.95
#             yalign 0.9
            
#             idle  "backpack/backpack.png"
#             hover "backpack/backpack.png"at button_menu_s
#             action [ToggleVariable("state_"), ToggleVariable("sate")]
    # else:
    #     add "backpack/backpack.png" at button_menu_s_
        

image content_icon:
    "backpack/icon_item.png"
    xanchor 0
    yanchor 0
    zoom 1.3




image content_icon1:
    "back_pack_items/GHG Source.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon2:
    "back_pack_items/Fossil Fuel.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon3:
    "back_pack_items/GreenHouse Gasses.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon4:
    "back_pack_items/Carbon Dioxide.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon5:
    "back_pack_items/Methane.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon6:
    "back_pack_items/GHG Sink.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon7:
    "back_pack_items/Global Carbon Budget.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon8:
    "back_pack_items/Total Carbon Budget.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon9:
    "back_pack_items/TopDown Estimate.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon10:
    "back_pack_items/Lateral Fluxes.png"
    xanchor 0 yanchor 0 zoom 0.1
image content_icon11:
    "back_pack_items/Bottom Up Estimate.png"
    xanchor 0 yanchor 0 zoom 0.1

screen backpack_item:
    style_prefix "itemUi"
    if state_ == False:
        add "backpack/plate.png" xalign 0.5 yalign 0.5 at bigging
        # conten isi back pack
        # imagebutton:
        #     xalign 0.1
        #     yalign 0.1
        #     idle  "backpack/icon.png"
        #     hover "backpack/icon.png" at button_menu
        #     action NullAction()  
        frame :
            background None
            # xalign 0.45
            # yalign 0.1
            xanchor 0.5
            yanchor 0.5
            xoffset 800
            yoffset 555
            xmaximum 800
            hbox:
                vbox spacing 70:
                    hbox spacing 10:
                        imagebutton:
                            idle  "content_icon1"
                            hover "content_icon1" at items_backpack 
                            action SetVariable("number_expl", 1)
                        imagebutton:
                            idle  "content_icon2"
                            hover "content_icon2" at items_backpack 
                            action SetVariable("number_expl", 2)
                        imagebutton:
                            idle  "content_icon3"
                            hover "content_icon3" at items_backpack 
                            action SetVariable("number_expl", 3)
                        imagebutton:
                            idle  "content_icon4"
                            hover "content_icon4" at items_backpack 
                            action SetVariable("number_expl", 4)
                        
                    hbox spacing 10:
                        imagebutton:
                            idle  "content_icon5"
                            hover "content_icon5" at items_backpack 
                            action SetVariable("number_expl", 5)
                        imagebutton:
                            idle  "content_icon6"
                            hover "content_icon6" at items_backpack 
                            action SetVariable("number_expl", 6)
                        imagebutton:
                            idle  "content_icon7"
                            hover "content_icon7" at items_backpack 
                            action SetVariable("number_expl", 7)
                        imagebutton:
                            idle  "content_icon8"
                            hover "content_icon8" at items_backpack 
                            action SetVariable("number_expl", 8)
                         
                    hbox spacing 1:
                        imagebutton:
                            idle  "content_icon9"
                            hover "content_icon9" at items_backpack 
                            action SetVariable("number_expl", 9)
                        imagebutton:
                            idle  "content_icon10"
                            hover "content_icon10" at items_backpack 
                            action SetVariable("number_expl", 10)
                        imagebutton:
                            idle  "content_icon11"
                            hover "content_icon11" at items_backpack 
                            action SetVariable("number_expl", 11)
                        
                
                    
        if number_expl == 1:
            add "back_pack_items/GHG Source.png" at explanation_picture
            add "back_pack_items/GHG Source Tul.png" at explanation
        if number_expl == 2:
            add "back_pack_items/Fossil Fuel.png" at explanation_picture
            add "back_pack_items/Fossil Fuel Tul.png" at explanation
        if number_expl == 3:
            add "back_pack_items/GreenHouse Gasses.png" at explanation_picture
            add "back_pack_items/GreenHouse Gasses Tul.png" at explanation
        if number_expl == 4:
            add "back_pack_items/Carbon Dioxide.png" at explanation_picture
            add "back_pack_items/Carbon Dioxide Tul.png" at explanation
        if number_expl == 5:
            add "back_pack_items/Methane.png" at explanation_picture
            add "back_pack_items/Methane Tul.png" at explanation
        if number_expl == 6:
            add "back_pack_items/GHG Sink.png" at explanation_picture
            add "back_pack_items/GHG Sink Tul.png" at explanation
        if number_expl == 7:
            add "back_pack_items/Global Carbon Budget.png" at explanation_picture
            add "back_pack_items/Global Carbon Budget Tul.png" at explanation
        if number_expl == 8:
            add "back_pack_items/Total Carbon Budget.png" at explanation_picture
            add "back_pack_items/Total Carbon Budget Tul.png" at explanation
        if number_expl == 9:
            add "back_pack_items/TopDown Estimate.png" at explanation_picture
            add "back_pack_items/TopDown Estimate Tul.png" at explanation
        if number_expl == 10:
            add "back_pack_items/Lateral Fluxes.png" at explanation_picture
            add "back_pack_items/Lateral Fluxes Tul.png" at explanation
        if number_expl == 11:
            add "back_pack_items/Bottom Up Estimate.png" at explanation_picture
            add "back_pack_items/Bottom Up Estimate Tul.png" at explanation
        
        
        
    
        imagebutton:
            xalign 0.073
            yalign 0.89
            
            idle  "backpack/back_icon.png"
            hover "backpack/back_icon.png" at button_menu 
            action [ToggleVariable("state_"), ToggleVariable("sate")]
    # if sate == True and state_ == False  or sate == False and state_ == True:
    # if sate != state_:
    #     add "backpack/plate.png" xalign 0.5 yalign 0.5 at smalling
    #     add "backpack/back_icon.png" xalign 0.073 yalign 0.89 at dissapaer

        


    
style itemUi_vbox:
    yalign 0.5
style itemUi_hbox:
    xalign 0.4



    
