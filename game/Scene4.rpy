#Story 5 _____

label scene4:
    #bglab
    #show
    #pos_center
    #n
    robot_n "This time, you will carry out the C.H.A.R part of the operation"
    #SHOWS A SCREEN WITH C.H.A.R
    p_n "Again with the accronym"
    p_n "Can't you just tell me the name and the plan?"
    #a
    #pos_left
    robot_n "While I like that you want to hear the plan immediately"
    robot_n "Just let me talk before you cut me off"
    p_n "Okay, i'll listen well"
    #SHOWS A SCREEN WITH C.H.A.R but now underneath it there is the full name of it
    #n
    #pos_right
    robot_n "So. C.H.A.R. is Carbon Harnessing and Reducing"
    p_n "And what does this 'Harnessing' and 'Reducing' mean?"
    p_n "'Harnessing'? is that even english? Mi no habla espanol"
    #bounce
    #a
    robot_n "I thought You say that you're gonna listen well?"
    p_n "ah... my bad, continue please"
    #n
    robot_n "Anyway, Harnessing and reducing in this term means that"
    robot_n "You are going to reduce the amount of carbon in the atmosphere"
    p_n "By capturing them?"
    #n
    robot_n "By capturing them"
    p_n "HOW?"
    #sm
    robot_n "Well, I know that you arent capable of doing it"
    #n
    robot_n "Thats why I have a plan, just for you"
    p_n "Alright, whats the plan?"
    #n
    robot_n "You are to reduce your energy consumption, use public transportation, eat healthier"
    robot_n "Plant some tree, and recycle some trash"
    p_n "That sounds like a hassle"
    #d
    #slump
    robot_n "Talking to you is a hassle"
    robot_n "So are you going to do it or no?" 
    #Option Yes:
        #Point and click game:
        #Scenario 1:  
            #show
            #bgCHAR1
            #If clicked wrong:
                #d
                robot_n "Out of all the things you could pick, you choose the wrong one"
            #If clicked correct:
                #h
                robot_n "Nice! with you saving some energy"
                #am
                robot_n "The power plant wouldn't need to work as hard"
        #Scenario 2:  
            #show
            #bgCHAR2
            #If clicked wrong:
                #d
                robot_n "Did you not hear me when i said to use  public transportation?"
            #If clicked correct:
                #n
                robot_n "Nice choice!"
                #h
                robot_n "You know? public transportation isn't THAT bad"
                #am
                robot_n "well unless at some certain time..."
        #Scenario 3:  
            #show
            #bgCHAR3
            #If clicked wrong:
                #d
                robot_n "Not only are you harming the earth, you also harm your own body" #IF THE SCALE IS BIGGER THAN 0.7kg
                #c
                robot_n "Look, I know saving the earth is important, but your human body is more important" #IF THE SCALE IS SMALLER THAN 0.7kg
            #If clicked correct:
                #am
                robot_n "Healthy food, healthy life!"
                #sm
                robot_n "Who need the meat guy anyway?"
                #h
                robot_n "Less cow, less pollution"
        #Scenario 4:  
            #show
            #bgCHAR4
            #If clicked wrong:
                #d
                robot_n "There cant be any tree if you never planted one" #MISTAKE PLANTING THE SEED
                #s
                robot_n "You need food to survive, its the same for the tree" #MISTAKE USING THE COMPOST
                #c
                robot_n "Obviously after eating you need some drink, no?" #MISTAKE WATERING CAN
            #If clicked correct:
                #e
                robot_n "In goes the seed" #CLICKING THE SEED
                #h
                robot_n "Compost will help the tree grows healthier" #CLICKING THE COMPOST
                #am
                robot_n "Life, in the end originate from the water" #CLICKING THE WATERING CAN
        #Scenario 5: 
            #show
            #bgCHAR5 
            #If clicked wrong:
                #d
                robot_n "Keep yourself together human, we only need the trash in the trashcan. Not you"
            #If clicked correct:
                #e
                robot_n "Off with the trash!"
                #c
                robot_n "Why do people even throw these things anywhere BUT the trashcan?"
                #h
                robot_n "Cleaner road, Cleaner air"
                #n
                robot_n "Every trash need a trashcan"
        #GAME END
    #Option No:
        #d
        robot_n "Do what you want, the world can end as long as i care"
        #show
        #bgBE
        #BAD END
    #sm
    robot_n "Maybe I do have a great eyes for people huh?"
    p_n "Uhhh? Hello? dont you see that I did all the work here?"
    #n
    robot_n "Yeah, i did see that"
    #sm
    robot_n "But its ME who brought you here, dont forget that human"
    p_n "yeah, yeah. Whatever"
    #SCENE 4 COMPLETED
