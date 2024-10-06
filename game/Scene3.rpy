
label scene3:
    #Bglab
    show robot at pos_left
    show orang_l at pos_right
    p_n "So... You're actually praising me"
    p_n "but..."
    #q
    robot_n "but??"
    p_n "What did I actually do?"
    #n
    robot_n "Well thanks for your action"
    robot_n "We have made some pretty big impapct"
    #SHOWS DATA
    p_n "What are these lines mean exactly?"
    #d
    #slump

    robot_n "This human..."
    #n
    robot_n "These are the data of how much greenhouse gasses that have been reduced"
    p_n "Did I really decrease it by THAT much?"
    #n
    robot_n "No"
    p_n "wha-"
    #bounce
    #h
    robot_n "BUT! If you keep on doing this, you might be able to decrease it by that much"
    p_n "WOW."
    robot_n "I know that emotion, its called sarcasm isn't it? you puny human"
    p_n "At least explain to me the graph in human language"
    #d
    #slump
    robot_n "*exhale heavily* Well... This graph shows that"
    p_n "Wait... did this robot just exhale?" #IN HIS MIND
    #n

    robot_n "If you kept on decreasing the GHG output even at 0.5\% each year"
    robot_n "It will actually save the earth"
    p_n "Am I actually capable of saving the earth?"
    #e
    #slide

    robot_n "Obviously! if it's not you humans then who else would be capable?"
    p_n "Did you really just encourage me?"
    #n

    robot_n "Well, anyway. Let's move into the next mission"
    # robot_n "But before we move on, do you know why with only 0.5\% decrease"
    # robot_n "You can save the earth?"
    
    #=========================================================================================================================================
    #  Tambahan Shallu dari slide 63  #
    #=========================================================================================================================================

    # Kondisi ketika user memilih Yes, I want. 
    # Maka akan lanjut ke penjelasan C.H.A.R atau ke Scene 4.

    # Kondisi ketika user memilih Umm...I'm not sure, 
    # maka akan lanjut ke tahap berikut:
    robot_n "What makes you did not sure?"
    p_n "How can I. Does a single person bring any change?"
    robot_n "It always start with one person, and if even just half of the human population do it, then nothing is impossible."
    p_n "Should I really do this change that might hinder the convenience of my daily life?"
    robot_n "Yeah. If you not taking action now, these things might happen to our future."
    robot_n "Fires, floods, storms, droughts, hunger, conflict, poverty, grief, anxiety."
    robot_n "By 2050 pollution may be so bad! there might not be fresh air to breathe."
    robot_n "Rising ocean temperatures could destroy nearly all the world's coral decimating our fish stocks."
    robot_n "Global harvests will likely be failing sending our food prices skyrocketing and even more people into food poverty."
    robot_n "Our world could be so catastrophically hot that sea level rise would displace millions increased risk of disease war" 
    robot_n "and mass migration would create global chaos."
    # tampilkan video ada di slide 71 - 72 
    # blinking
    # Slide The END (Ada dua pilihan, Try Again = Kembali ke line 53, Give Up = kembali ke main menu)
    
    #=========================================================================================================================================
    
    # #Option1: "With the decrease of one ghg gas it created a chain reaction making that would end up having a big impact"
    #     #h
    #     robot_n "Thats absolutely correct"
    # #Option2: "Because when the ghg gas is decreasing the other gases will start to decrease as well"
    #     #n
    #     robot_n "Yeah? thanks captain obvious"
    #     robot_n "I asked you why did it decrease the other ghg as well"
    # #Option3:  "I don't know, I'm just a human"
    #     #d
    #     #creep
    #     robot_n "You know what? I'm not even surprised anymore at this point"
    # #SCENE 3 COMPLETED