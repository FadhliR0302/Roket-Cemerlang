image bgmvVR :
    "Movies/BackgroundMovie3.png"
image robot:
    "images/gameimg/Robot.png"

image movieVR = Movie(channel="movie", play="Movies/Video Virtual Reality.webm")
image blink = Movie(channel="movie", play="Movies/Blink.webm")
image movie1 = Movie(channel="movie", play="Movies/Video No 1.webm")
image movie2 = Movie(channel="movie", play="Movies/Video No 2.webm")
image movie4 = Movie(channel="movie", play="Movies/Video No 4.webm")
transform video:
    xysize (920, 510)
    xalign 0.52
    yalign 0.21

screen VR:
    add "bgmvVR"
    add "movieVR" at video
     
screen Video1:
    add "bgmvVR"
    add "movie1" at video
    
screen Video2:
    add "bgmvVR"
    add "movie2" at video
screen Video4:
    add "bgmvVR"
    add "movie4" at video



