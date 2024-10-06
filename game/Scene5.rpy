image bgsubv = "Background Slide 11.png"
label scene5:
    scene bgsubv
    show robot_l at pos_right
    show orang at pos_left

    robot_n "Did you feel the difference now?"

    scene bgsubv
    show orang at pos_center
    p_n "Yeah! I feel like my effort isn't in vain."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Well, you are correct!"

    # SHOWS DATA
    robot_n "With just R.E.C.H.A.R., we have already reached the target."

    robot_n "Of 1.5 degrees Celsius increase in global temperature."

    scene bgsubv
    show orang at pos_center
    p_n "So, can I go home now?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "Nope, you've already come too far now."

    robot_n "Going back would just reset all of your progress."

    scene bgsubv
    show orang at pos_center
    p_n "That's true, I guess I have to see this through."

    p_n "...."

    scene bgsubv
    show robot_l at pos_right
    robot_n "...."

    scene bgsubv
    show orang at pos_center
    p_n "So... Are you going to explain this 'data' to me or what?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "Ah! Yes, sorry, I was wondering why you are still here."

    scene bgsubv
    show orang at pos_center
    p_n "You told me to stay here until the end..."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Well, the data here shows that with both main GHG, which are CO2 and CH4, decreasing by 2\% every year..."

    robot_n "In 2100, we could reach a 1.5-degree Celsius increase in global temperature!"

    scene bgsubv
    show orang at pos_center
    p_n "Now wait a second."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Yeah? Any questions?"

    scene bgsubv
    show orang at pos_center
    p_n "Are you telling me that GHG is mainly made of CO2 and CH3?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "It's CH4... but yeah, that's correct."

    scene bgsubv
    show orang at pos_center
    p_n "But, don't humans exhale CO2 every time we breathe?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "Yeah. But you humans aren't capable of even producing a dangerous amount of it."

    robot_n "It's also a part of a closed loop."

    scene bgsubv
    show orang at pos_center
    p_n "And what are these 1.5 degrees Celsius?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "It's the increase in temperature."

    scene bgsubv
    show orang at pos_center
    p_n "Yeah, you said that already."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Are you really asking that?"

    scene bgsubv
    show orang at pos_center
    p_n "Yeah?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "It's the temperature increase caused by global warming that I have told you about from the beginning."

    scene bgsubv
    show orang at pos_center
    p_n "... Sorry."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Well, before we move on, let's give you another test first."

    scene bgsubv
    show orang at pos_center
    p_n "Not again."

    scene bgsubv
    show robot_l at pos_right
    robot_n "With all the data I have shown, do you know what unit we use to count the concentration of GHG gases?"

    menu:
        "In Parts per Million":
            scene bgsubv
            show robot_l at pos_right
            robot_n "You have some seriously great memory."

        "In Dollars":
            scene bgsubv
            show robot_l at pos_right
            robot_n "What does the dollar of GHG even mean?"

        "I would like to call a friend":
            scene bgsubv
            show robot_l at pos_right
            robot_n "Nice try, but you don't have friends."

            scene bgsubv
            show orang at pos_center
            p_n "Ouch."

    scene bgsubv
    show robot_l at pos_right
    robot_n "Maybe I do have a great eye for people, huh?"

    scene bgsubv
    show orang at pos_center
    p_n "Uhhh? Hello? Don’t you see that I did all the work here?"

    scene bgsubv
    show robot_l at pos_right
    robot_n "Yeah, I did see that."

    robot_n "But it's ME who brought you here, don’t forget that, human."

    scene bgsubv
    show orang at pos_center
    p_n "Yeah, yeah. Whatever."

    # SCENE 5 COMPLETED
    jump scene6

# #Story 6 _____
# label scene5:
#     show robot_l at pos_right
#     show orang at pos_left
#     robot_n "Did you feel the difference now?"
#     p_n "Yeah! I feel like my effort aren't in vain"
#     #e
#     robot_n "Well, you are correct!"
#     #SHOWS DATA
#     #sm
#     #pos_left
#     robot_n "With just R.E.C.H.A.R. we have already reach the target"
#     robot_n "Of 1.5 celsius degree increase in global temperature"
#     p_n "So can I go home now?"
#     #c
#     #pos_center
#     robot_n "Nope, you already went to far now"
#     robot_n "Going back would just reset all of your progress"
#     p_n "That's true, I guess I have to see this through"
#     p_n "...."
#     #q
#     robot_n "...."
#     p_n "So... Are you going to explain this 'data' to me or what?"
#     #bounce
#     #sur
#     robot_n "Ah! yes, sorry I was wondering why are you still here"
#     p_n "You told me to stay here until the end..."
#     #n
#     #pos_left
#     robot_n "Well, the data here shows that with both main ghg which is CO2 and CH4 decreasing 2% every year"
#     robot_n "in 2100 we could reach 1.5 degree celsius in global temperature!"
#     p_n "Now wait a second"
#     #q
#     robot_n "Yeah? any question?"
#     p_n "Are you telling me that ghg is mainly made of CO2 and CH3?"
#     #c
#     robot_n "Its CH4... but yeah, that's correct"
#     p_n "But, doesn't human exhale CO2 every time we breathe?"
#     #sm
#     robot_n "Yeah. but you human arent capable of even producing a dangerous amount of it"
#     robot_n "It also a part of a closed loop"
#     p_n "And what are these 1.5 degree celsius?"
#     #d
#     robot_n "Its the increase in temperature"
#     p_n "Yeah, You said that already"
#     #c
#     robot_n "Are you really asking that?"
#     p_n "Yeah?"
#     #d
#     #slump
#     robot_n "Its the temperature increase caused by global warming that i have told you from the beggining"
#     p_n "... sorry"
#     #n
#     robot_n "Well, before we move on lets give you another test first"
#     p_n "Not again"
#     #n
#     #pos_center
#     robot_n "With how much data I have shown, do you know what unit We used to count the concentration of ghg gasses?"
#     # #Option1: "In Part per million"
#     #     #bounce
#     #     #sur
#     #     robot_p "You have some serious great memory"
#     # #Option2: "In dollar"
#     #     #q
#     #     #slump
#     #     robot_p "What does the dollar of ghg even mean?"
#     # #Option3: "I would like to call a friend"  
#     #     #sm
#     #     robot_p "Nice try, you dont have friend"
#     #     p_n "Ouch"
#     # #SCENE 5 COMPLETED