#Story 3 _____
image latar21 = "scene2/latar1.png" 
image latar22 = "scene2/latar2.png"
image latar23 = "scene2/latar19.png"
image latar24 = "scene2/Background Slide 23.png"
image latar25 = "scene2/.png"
label scene2:
    scene latar2
    show robot_l at pos_center
    show robot_l at unslump
    robot_n "Hey there! Ready for another day of saving the planet?"
    scene latar2
    show orang at pos_center
    show orang at bounce
    p_n "Absolutely!"
    p_n " Although, I was hoping for a coffee break before we dive into the heavy stuff."
    p_n "What will we do today?"
    scene latar21
    show robot_l at pos_center
    robot_n 'Ohh... i like the enthusiast!'
    scene latar21
    show robot at pos_center
    robot_n "We will learn about R.E. in our Mission."
    scene latar2
    show orang at pos_center
    p_n "R.E.?"
    #SHOWS A screen  with the letters R.E. on it and its explanation
    scene latar21
    show robot at pos_center
    robot_n "Yes, R.E. is called the Renewable Energy. These enery sources ca be renew and never run out"
    scene latar2
    show orang at pos_center
    p_n "So, it's coming from natural resources like sunlight, wind, and water, right?"
    scene latar22
    show robot at pos_center
    robot_n "That's right! Unlike fossil energy, RE is cleaner and friendlier to our environment."
    robot_n "As the name suggests, these energy should be unlimited."
    robot_n "These energy also reduce pollution, and have multiple other benefit"
    scene latar2
    show orang at pos_center
    p_n "Well, what can we do to enforce this?"
    scene latar23
    show robot at pos_center
    robot_n "we can support projects that aim to develop renewable energy"
    robot_n "like building wind farms or installing solar panels in suitable areas"
    scene latar2
    show orang at pos_center
    p_n " Is that enough?"
    scene latar24
    show robot at pos_center
    show robot at bounce
    robot_n "Not at all!"
    robot_n "There's so much more we can do with different types of renewable energy"
    scene latar2
    show orang at pos_center
    p_n "Really??"
    p_n "What are they?"
    scene latar23
    show robot at pos_center
    robot_n "Let me walk you through them"
    robot_n "Do you know about solar panel, wind turbin, geothermal, and Biomass before?"
    scene latar2
    show orang at pos_center
    p_n "yeah, i've heard of that before"
    p_n "I've always wondered, how do solar panels work?"
    
    robot_n "Great question!"
    robot_n "Ever seen solar panels glinting in the sun?"
    robot_n "Those panels, known as photovoltaics, convert sunlight directly into electricity"
    robot_n "They're pretty impressive, don't you think?"

    p_n "Yeah, I've seen them on some rooftops. Are they only for big installations?"
    
    robot_n "Not at all!"
    robot_n "They're super versatile and easy to install, whether it's a large solar farm or the rooftop of your house"
    robot_n "By using solar power, we reduce our reliance on fossil fuels for electricity"
    robot_n "It's like plugging into the endless power of the sun."

    p_n "That's amazing! But what about wind power?"
    p_n "I've seen those giant turbines before"

    robot_n "Ah, wind power! Imagine giant, graceful pinwheels standing tall, catching the wind to generate clean electricity."
    robot_n "Wind turbines harness the power of the wind, and they're especially efficient in areas with consistent breezes"
    robot_n "Whether they're perched on a coastline or spread across open plains, wind turbines are key players in our clean energy future"
   
    p_n "So we've got solar and wind"
    p_n "But isn't there something about using the Earth's heat?"

    robot_n "Absolutely! Have you ever thought about the heat beneath your feet?"
    robot_n "Deep down, the Earth is full of warmth. In certain regions"
    robot_n "especially volcanic ones"
    robot_n "this geothermal energy can be tapped to produce electricity or provide direct heating"
    robot_n "It's like the Earth sharing its warmth with us, day in and day out"

    p_n "That's really cool"
    p_n "there any other renewable energy sources?"

    robot_n "There sure are!"
    robot_n "Let me tell you about the recycling hero of energy: biomass"
    robot_n "energy comes from organic materials"
    robot_n "things like wood scraps, agricultural waste, and food leftovers"
    robot_n "Instead of letting these things end up as waste, we use them to generate heat or turn them into biofuels"
    robot_n "It's all about turning yesterday's scraps into tomorrow's energy, which reduces both waste and emissions"
   
    p_n "There really are a lot of options out there"
    
    robot_n "There are so many ways we can make real change"
    robot_n "And it all starts with awareness, just like you're doing right now"
    robot_n "From awareness, we can take real steps towards significant change"
    robot_n 'Well? what do you think? There are a lot of ways for us to do such a change, yeah?'
    robot_n "Okay then, shall we do this operation first?"
    #Option Yes:
        #GAME MENCOCOKKAN
        # robot_n "Not bad for a human" #First correct pair
        # robot_n "You're actually doing something for once" #Second correct pair
        # robot_n "...wait you arent actually cheating arent you?" #Third correct pair    
        # robot_n "Thats wrong, human" #First incorrect pair
        # robot_n "Im sure you just got unlucky, right?" #second incorrect pair
        # robot_n "You never learn, do you?" #Third Incorrect pair
        #Shows CUTSCENE
    #Option No:
        # robot_n "You really gave up at the first hurdle, huh?"
        #BAD END
    #After game
    show robot_l at unslump
    robot_n "THAT"
    show robot_l at slump
    robot_n "WAS"
    show robot_l at unslump
    robot_n "GREAT"
    robot_n "Even I, a robot doesn't know that you have it in you"
    show orang at creeped_left
    p_n "Can't you just trust me once?"
    robot_n "No can do"
    show robot_l at bounce
    robot_n "Anyway, thats a job well done"
    #SCENE 2 COMPLETED    