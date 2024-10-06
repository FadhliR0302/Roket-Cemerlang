
image bgbg = "Background ___.png"
init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True

screen kipas:

    # A map as background.
    add "Background 38.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Windmill"
            droppable False
            dragged detective_dragged
            xpos 684 ypos 875

            add "kipas.png"
        drag:
            drag_name " "
            draggable False
            xpos 1338 ypos 714

            add "kipas.png" alpha 0.0

screen panel_surya:

    # A map as background.
    add "Background _.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Windmill"
            droppable False
            dragged detective_dragged
            xpos 910 ypos 910

            add "panel_surya.png"
        drag:
            drag_name " "
            draggable False
            xpos 960 ypos 453

            add "panel_surya.png" alpha 0.0
screen generator:

    # A map as background.
    add "Background __.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Windmill"
            droppable False
            dragged detective_dragged
            xpos 1070 ypos 895

            add "generator.png"
        drag:
            drag_name " "
            draggable False
            xpos 335 ypos 633

            add "generator.png" alpha 0.0
label game2__:
    "We need to investigate! Who should we send, and where should they go?"

    call screen kipas
    call screen panel_surya
    call screen generator
    show bgbg

    "Good Job."