#Story 7 _____
label scene6:
    show orang_l at pos_right
    show robot at pos_left
    robot_n "Now for the last but deffinetly not least"
    p_n "G.E right? what does it mean?"
    p_n "and what are the plans?"
    #bounce
    #sur
    robot_n "You really have gone a long way human"
    #h
    robot_n "You even remember that its G.E as the last operation"
    p_n "Oddly enough, I feel really interested and invested in this now"
    #e
    robot_n "Good, thats what I want to hear!"
    robot_n "So... G.E"
    #SHOWS  A SCREEN WITH A BIG G.E AND SOME EXPLANATION
    #n
    #pos_left
    robot_n "G.E is Global Engagement"
    p_n "I-I'm not ready to commit in a relationship like that"
    #cr
    #creep
    robot_n "Not THAT kind of engagement"
    robot_n "Enought with the jokes"
    p_n "yes, yes. What are the plans then?"
    #n
    robot_n "I need you to either create or join a community, and do all the communal task"
    robot_n "With that in mind, do you ready to do this?"
    #Option Yes:
    #     #e
    #     #bounce
    #     robot_n "Lets do this!"
    #     #MEMORY CARD GAME
    #     #Scenario 1&2&3:
    #     #bgGE1
    #         #FAILS:
    #             #n
    #             robot_n "You really have the memory of a goldfish" #1st fail
    #             #s
    #             robot_n "You just do that to check the cards right?" #2nd fail
    #             #c
    #             robot_n "You really have the memory of a goldfish."
    #             #d
    #             robot_n "Yes, i repeat that since i know you already forgot the first time" #3rd fail
    #             #n
    #             robot_n "I dont even want to comment on that move" #every other fail
    #         #SUCCESS:
    #             #sur
    #             robot_n "You actually got that?" #1st success
    #             #am
    #             robot_n "How are kept on doing that?" #2nd success
    #             #h
    #             robot_n "You are actually good at this" #3rd success
    #             #e
    #             robot_n "I'm impressed" #every other success
    #         #bgGE2
    #         #FAILS:
    #             #n
    #             robot_n "You really have the memory of a goldfish" #1st fail
    #             #s
    #             robot_n "You just do that to check the cards right?" #2nd fail
    #             #c
    #             robot_n "You really have the memory of a goldfish."
    #             #d
    #             robot_n "Yes, i repeat that since i know you already forgot the first time" #3rd fail
    #             #n
    #             robot_n "I dont even want to comment on that move" #every other fail
    #         #SUCCESS:
    #             #sur
    #             robot_n "You actually got that?" #1st success
    #             #am
    #             robot_n "How are kept on doing that?" #2nd success
    #             #h
    #             robot_n "You are actually good at this" #3rd success
    #             #e
    #             robot_n "I'm impressed" #every other success
    #         #bgGE3
    #         #FAILS:
    #             #n
    #             robot_n "You really have the memory of a goldfish" #1st fail
    #             #s
    #             robot_n "You just do that to check the cards right?" #2nd fail
    #             #c
    #             robot_n "You really have the memory of a goldfish."
    #             #d
    #             robot_n "Yes, i repeat that since i know you already forgot the first time" #3rd fail
    #             #n
    #             robot_n "I dont even want to comment on that move" #every other fail
    #         #SUCCESS:
    #             #sur
    #             robot_n "You actually got that?" #1st success
    #             #am
    #             robot_n "How are kept on doing that?" #2nd success
    #             #h
    #             robot_n "You are actually good at this" #3rd success
    #             #e
    #             robot_n "I'm impressed" #every other success        
    #     #q
    #     robot_n "Maybe you have a photographic memory? actually scratch that"
    #     p_n "Why?"
    # #Option No:
    #     #q
    #     robot_n "Who would start doing it if not you?"
    #     #d
    #     robot_n "With no one keeping the progress everything will return to how it all began"
    #     #BAD END because everyone stopped doing these changes thus undoing all the changes the player made
    #e
    #bounce
    robot_n "There we go!"
    p_n "We actually did it!"
    #h
    robot_n "No... YOU did it"
    #SCENE 6 COMPLETED