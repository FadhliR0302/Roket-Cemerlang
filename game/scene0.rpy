
#Story 1 RECHARGE
image latar1  = "scene1/latar1.png"
image latar2  = "scene1/latar2.png"
image latar3  = "scene1/latar3.png"
label scene0:
    scene latar1
    show orang_l at pos_center
    p_n "Hello, I heard this place offers free food if we participate in the VR simulation."
    scene latar1
    show robot at pos_center
    robot_n "Yes, that's correct. You will receive free food as long as you participate in the simulation program and meet the other requirements."
    robot_n "By the way, what's your name?"
    scene latar1
    show orang at pos_center
    p_n "I'm Zika. Hurry, I can't wait to star— I mean, to try this simulation!"
    scene latar1
    show robot at pos_center
    robot_n "Please be patient, Zika. This is the VR set you will use."
    #video
    scene latar1
    show orang at pos_center
    p_n "Thank you, I'm ready!"
    #img with running text
    "{i}The world is reaching its final days everyone{/i}"
    #img with running text
    "{i}In just 25 years, we have bring upon this{/i}"
    #img with running tex
    "{i}This nightmare that will befall all of us{/i}"
    #img with running text
    "{i}It is with saddening heart that I say{/i}"
    "...."

    #Efek mata kedip
    "..."
    #aksi lepas VR kita
    scene latar2
    show robot at pos_center
    robot_n "So... How is the simulation?"
#scene lab cumputer
    
    robot_n "What are the things that you see?"
    scene latar2
    show orang at pos_center
    p_n "It was terrible..."
    
    p_n "The forest was burning, the sky was almost pitch black, and the people were suffering!"
    
    p_n "The world was basically ending!"
    show orang at bounce
    p_n "...It is NOT good."
    
    p_n "Why did you make the story so depressing?"
    scene latar2
    show robot at pos_center
    robot_n "What do you mean by story?"
    robot_n "What you have seen is climate change. These changes are happening even right now as we speak"
    scene latar2
    show orang at pos_center
    show orang at bounce
    p_n "Climate what?"
    scene latar2
    show robot at pos_center
    robot_n "Are you serious..."
    show robot at slump
    robot_n "Human theese days..."
    scene latar2
    show orang at pos_center
    p_n "Chill out, Bro. I came here for a free food at the first place"
    scene latar2
    show robot at pos_center
    robot_n "You know how it feels hotter each year?"
    robot_n "This is what we call global warming"
    
    robot_n "It's happening because humans have been abusing and increasing the output of greenhouse gasses everyday."
    scene latar2
    show orang at pos_center  
    p_n "Okay..."
    
    p_n "And WHAT is these greenhouse gasses thingy?"
    scene latar2
    show robot at pos_center
    robot_n "Greenhouse gases are the gasses that trap heat from the Earth and send it back to the earth"
    
    robot_n "So, it makes the earth warmer"
    scene latar2
    show orang at pos_center  
    p_n"Wait, wait..."
    
    p_n "This is too much information for me right now"
    scene latar2
    show robot at pos_center  
    robot_n "In Conclusion. The world could end up dying from human activity just like the simulation you just saw"
    scene latar2
    show orang at pos_center  
    show orang at bounce    
    p_n "THAT what makes it even more depressing"
    scene latar2
    show orang at pos_center   
    robot_n "Well, the main point is that this VR should make people more aware of the danger of climate change"
    scene latar2
    show orang at pos_center     
    p_n "I came here, for the free food, not a depressing reality..."
    scene latar2
    show robot at pos_center    
    robot_n 'Climate change are a very real and imminent thing'
    robot_n "This phenomenon are caused by human activity, my team are trying to prevent this from happening"
    robot_n "So, what do you say about joining our operation now?"
    scene latar2
    show orang at pos_center     
    p_n "Uhm... you know... climate change is super important..." 
    
    p_n "but my goldfish has separation anxiety, so I can't really commit right now-"
    scene latar2
    show robot at pos_center
    robot_n "The cost for using robot services is 250 USD. The food, prepared by one of the top robot developers, is 50 USD. The VR experience is an additional 100 USD." 
    scene latar2
    show orang at pos_center     
    show orang at unslump
    p_n "WHAT, the poster said it's all FREE!"
    scene latar2
    show robot at pos_center
    robot_n "It seems you humans should work on improving your literacy skills by stopping at just reading the poster headlines."
    robot_n "Please proceed to the officer at the front for payment."
    robot_n "Or..."
    show robot at unslump
    robot_n "You know what to do, right?"
    menu:
        "Join the Mission":
            pass
        "Leave":
            pass
    robot_n "That's exactly what I want to hear, partner!"
    show robot at bounce
    robot_n "Welcome to R.E.C.H.A.R.G.E!"
#Story 1 CLEAR
#New Collection Added
#GHGs GHG Source