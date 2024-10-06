label scene7:
    scene bgb
    # Time skip into 2050
    # Shows scene 1 again, but now the world is much healthier

    scene bghe
    # Shows a healthy world

    "Good morning world! What a beautiful planet that we live in."

    scene bgff
    # Shows a flourishing green and lush forest of Kalimantan, but make it more green

    "With how the world is right now..."

    scene bgfz
    # Shows a happy family going to the zoo
    "It would be a miss if you don't go out and see this beautiful Earth."

    scene bgmc
    # Shows a magazine with the player as the cover of the green movement

    "And here we have the hero of the green movement!"

    scene bghs
    # Transition to the player looking at the city from his seat on the hillside
    show robot at pos_right
    show orang_l at pos_left

    robot_n "Well, if it isn't the hero of the Earth."

    robot_n "So, how does it feel?"

    p_n "It still feels super weird."

    p_n "Maybe I will never get used to the fame."

    robot_n "Wow... spoken like a true hero, being humble and all that."

    p_n "..."

    p_n "But I do gotta say that it feels refreshing."

    p_n "I never thought that my small actions could make such a big impact."

    robot_n "Well, you did make a big impact, and it's not just you."

    robot_n "It's all of you humans that have made this impact."

    robot_n "But it all does start with one person, and that person is you."

    p_n "Stop that! You're making me feel embarrassed now."

    robot_n "It always starts with small steps to traverse a large land; you can even cover an entire mountain with those small steps."

    p_n "Yeah... and I gotta say."

    p_n "I'm glad that I can be that person."

    p_n "Thank you for bringing me to this point."

    robot_n "Well... Thank YOU for doing everything for the betterment of the Earth."

    # Robot looking into the actual player rather than the character
    show robot at pos_center
    robot_n "Now it's YOUR turn. Would you do these changes that may seem small?"

    robot_n "These changes that may be a hassle, that may be a challenge."

    robot_n "For a brighter and better future?"

    menu:
        "Yeah, I will do it":
            # Roll the end Credit
            scene bgb
            "Thank you for making a difference, hero."

    # Scene 7 COMPLETED

# #Story 8 _____
# label scene7:
#     #show
#     #bgb
#     #Time skip into 2050
#     #bghe
#     #Shows scene 1 again,  but now the world is much more healthier
#     {TV Narrator} "Good morning world! What a beautiful planet that we live in"
#     #bgff
#     #Shows a flourishing green and lush forest of kalimantan, but make it more green
#     {TV Narrator} "With how the world are right now"
#     #bgfz
#     #Shows a happy family going to the zoo 
#     {TV Narrator} "It would be a miss if  you don't go out and see this beautiful earth"
#     #bgmc
#     #Shows a magazine with the player as the cover of the green movement
    
#     #bghs
#     #Transition into the player looking the city from his city on the hillside
#     #sm
#     #slide
#     #pos_center
#     show robot at pos_right
#     show orang_l at pos_left
#     robot_n "Well if it isn't the hero of the earth"
#     #q
#     robot_n "So, how does it feel?"
#     p_n "It still feels super weird"
#     p_n "Maybe i will never get used to the fame"
#     #cr
#     robot_n "wow... spoken like a true hero, being humble and all that"
#     p_n "..."
#     p_n "But I do gotta says that it feels refreshing"
#     p_n "I never tought that my small actions could make such a big impact"
#     #h
#     robot_n "Well, you did make a big impact, and it's not just you"
#     robot_n "Its all of you humans that have made these impact"
#     #e
#     robot_n "But it all does start with one person, and that person is you"
#     p_n "Stop that! you making me feels embarrased now"
#     #h
#     robot_n "It always start with small steps to traverse a large land, you can even cover an entire mountain with those small steps"
#     p_n "yeah... and I gotta say"
#     p_n "I'm glad that I can be that person"
#     p_n "Thank you for bringing me until this point"
#     #am
#     robot_n "Well... Thank YOU for doing everything for the betterment of the earth"
#     #Robot Looking into the actual player rather than the character
#     #pop
#     #bgd
#     #se
#     #pos_center
#     robot_n "Now its YOUR turn. Would you do these changes that may seems small"
#     #c
#     robot_n "These changes that may be a hassle, that may be a challenge"
#     #e
#     robot_n "For a brighter and better future?"
#     # #Option Yes:
#     #     User "Yeah, I will do it"
#     #     #Roll the end Credit
#     #     #bgb
#     # #Scene 7 COMPLETED