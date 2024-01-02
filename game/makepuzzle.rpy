label makepuzzle:

    scene bg sea sun
    play music relaxing
    # stop music fadeout 3
    # play music sea fadeout 3

    python:
        k = Puzzle()
        k.set_sensitive(False)
        k.show()
    
    "Добро пожаловать в мини-игру! Нажимайте на части, чтобы вращать их"
    "Перетащите части друг на друга, чтобы переключиться. Удачи!!!"
    

label quick_continue:
    
    while True:

        python:
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()
            
            k.set_sensitive(False)
        if event == "win":
            jump win

label win:

    # play music sea fadeout 3
    show polly smile swimsuit right at right

    show darina smile swimsuit at left

    $ h.change(money=1)
    play sound success
    play music silentsea
    d "УРА! У нас получилось!!"

    p "Какой красивый портрет!"

    jump note

    
