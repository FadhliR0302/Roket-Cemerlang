#Story 6 _____
label scene5:
    #show
    #bglab
    #n
    #pos_center
    robot_n "Did you feel the difference now?"
    p_n "Yeah! I feel like my effort aren't in vain"
    #e
    robot_n "Well, you are correct!"
    #SHOWS DATA
    #sm
    #pos_left
    robot_n "With just R.E.C.H.A.R. we have already reach the target"
    robot_n "Of 1.5 celsius degree increase in global temperature"
    p_n "So can I go home now?"
    #c
    #pos_center
    robot_n "Nope, you already went to far now"
    robot_n "Going back would just reset all of your progress"
    p_n "That's true, I guess I have to see this through"
    p_n "...."
    #q
    robot_n "...."
    p_n "So... Are you going to explain this 'data' to me or what?"
    #bounce
    #sur
    robot_n "Ah! yes, sorry I was wondering why are you still here"
    p_n "You told me to stay here until the end..."
    #n
    #pos_left
    robot_n "Well, the data here shows that with both main ghg which is CO2 and CH4 decreasing 2% every year"
    robot_n "in 2100 we could reach 1.5 degree celsius in global temperature!"
    p_n "Now wait a second"
    #q
    robot_n "Yeah? any question?"
    p_n "Are you telling me that ghg is mainly made of CO2 and CH3?"
    #c
    robot_n "Its CH4... but yeah, that's correct"
    p_n "But, doesn't human exhale CO2 every time we breathe?"
    #sm
    robot_n "Yeah. but you human arent capable of even producing a dangerous amount of it"
    robot_n "It also a part of a closed loop"
    p_n "And what are these 1.5 degree celsius?"
    #d
    robot_n "Its the increase in temperature"
    p_n "Yeah, You said that already"
    #c
    robot_n "Are you really asking that?"
    p_n "Yeah?"
    #d
    #slump
    robot_n "Its the temperature increase caused by global warming that i have told you from the beggining"
    p_n "... sorry"
    #n
    robot_n "Well, before we move on lets give you another test first"
    p_n "Not again"
    #n
    #pos_center
    robot_n "With how much data I have shown, do you know what unit We used to count the concentration of ghg gasses?"
    #Option1: "In Part per million"
        #bounce
        #sur
        robot_p "You have some serious great memory"
    #Option2: "In dollar"
        #q
        #slump
        robot_p "What does the dollar of ghg even mean?"
    #Option3: "I would like to call a friend"  
        #sm
        robot_p "Nice try, you dont have friend"
        p_n "Ouch"
    #SCENE 5 COMPLETED