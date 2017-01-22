
label mai_begin_hunt:
    
    image bg battle_bg = "battle_bg.jpg"

    image mai_target:
        "hunt/mai_head.png"

    $ targets_needed = 4

    $ shots_fired = 0
    $ targets_hit = 0

    call mai_hunting

label mai_finished_him:
    return
    
label mai_hunting:
    
    $ import random
    $ xposi = random.randint(340, 940)
    $ yposi = random.randint(100, 420)

    transform mai_moving_target:
        ypos yposi - 50
        linear 3.0 xpos 2000
        xpos -300

    scene bg battle_bg
    show mai_target at mai_moving_target
    $ position = At(ImageReference("mai_target"), mai_moving_target)
    show expression position

    $ ui.imagebutton("hunt/fist.png", "hunt/fist_hover.png", 
        clicked = ui.returns("fired"), xpos= xposi, ypos = yposi)
    $ fired_gun = ui.interact()
    

    show expression position
    if position.xpos > xposi - 50:
        if position.xpos < xposi + 50:
            $ targets_hit = targets_hit + 1
            if targets_hit >= targets_needed:
                jump mai_finish_him
            with hpunch
            "You Hit! [targets_hit] / [targets_needed] Needed Hits Landed! "
            call mai_hunting
    
    if targets_hit >= targets_needed:
        jump mai_finish_him
    
    with vpunch
    "You WHIFFED! [targets_hit] / [targets_needed] Needed Hits Landed! "
    
    call mai_hunting
    
    return

label mai_finish_him:
    
    image mai_finished:
        "hunt/mai_head.png"
        xalign 0.5 yalign 0.5

    hide mai_finished with hpunch
    show mai_finished with pixellate

    return