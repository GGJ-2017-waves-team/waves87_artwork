label start:

    image bg battle_bg = "battle_bg.jpg"

    image fujitsu_target:
        "hunt/fujitsu_head.png"

    $ targets_needed = 5

label fujitsu_begin_hunt:
    
    $ shots_fired = 0
    $ targets_hit = 0

    call fujitsu_hunting

label fujitsu_finished_him:
    return
    
label fujitsu_hunting:
    
    $ import random
    $ xposi = random.randint(340, 940)
    $ yposi = random.randint(100, 420)

    transform fujitsu_moving_target:
        ypos yposi - 50
        linear 3.0 xpos 2000
        xpos -300

    scene bg battle_bg
    show fujitsu_target at fujitsu_moving_target
    $ position = At(ImageReference("fujitsu_target"), fujitsu_moving_target)
    show expression position

    $ ui.imagebutton("hunt/fist.png", "hunt/fist_hover.png", 
        clicked = ui.returns("fired"), xpos= xposi, ypos = yposi)
    $ fired_gun = ui.interact()
    

    show expression position
    if position.xpos > xposi - 50:
        if position.xpos < xposi + 50:
            $ targets_hit = targets_hit + 1
            if targets_hit >= targets_needed:
                jump fujitsu_finish_him
            with hpunch
            "You Hit! [targets_hit] / [targets_needed] Needed Hits Landed! "
            call fujitsu_hunting
    
    if targets_hit >= targets_needed:
        jump fujitsu_finish_him
    
    with vpunch
    "You WHIFFED! [targets_hit] / [targets_needed] Needed Hits Landed! "
    
    call fujitsu_hunting
    
    return

label fujitsu_finish_him:
    
    image fujitsu_finished:
        "hunt/fujitsu_head.png"
        xalign 0.5 yalign 0.5

    hide fujitsu_finished with hpunch
    show fujitsu_finished with pixellate

    return