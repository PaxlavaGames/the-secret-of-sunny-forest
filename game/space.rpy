label space:

    # play music spaceing
    play music sea fadeout 1
    scene bg top

    show polly smile right at right

    if is_with_us_chameleon:
        show chameleon at chameleon_on_bag

    p "Какая красота!"

    show darina smile at left

    play sound yey
    p "Восхитительно!"
    d "Если, что падать будет очень далеко..."

    hide polly smile right at right

    hide darina smile at left

    show polly st right at right

    show darina st left at left
    
    $ is_made_error = False
    label where_tent:
        $ is_use_timer = True
        $ timez = 4
        $ time_range = 4
        $ marker = 'no_tent'
        menu:
            d "Где же нам поставить палатку?"
            "На склоне":
                $ is_made_error = True
                play sound fail
                "Вы скатитесь с горы в море"
                $ h.change(life=-1)
                scene bg top
                jump where_tent
            "На ровном месте":
                if not is_made_error:
                    $ h.change(mind=1, money=1)
                else:
                    $ h.change(money=1)
                play sound success
                "Вам будет спать мягко и удобно"
                jump tent_success
            "У муравейника":
                $ is_made_error = True
                play sound fail
                "Ночью вам будет не до сна"
                $ h.change(life=-1)
                scene bg top
                jump where_tent
            "На тропах лесных зверей":
                $ is_made_error = True
                play sound fail
                "Ночью вам будет не до сна"
                $ h.change(life=-1)
                scene bg top
                jump where_tent

    label no_tent:
        $ h.change(life=-1)
        "[player_name] споткнулась о камень"
        
        jump tent_success

    label tent_success:
        $ is_use_timer = False            

    "Наконец, девочки выбрали место и поставили палатку"

    jump tent