label rock:

    play music sea fadeout 1

    scene bg rock

    "Девочки, держась за веревку, поднимались сначала одна, потом вторая"
    d "Ощущение, что руки стали очень горячими, не привыкла я лазить по веревке, как бы не соскользнуть с нее"
    p "Держись крепче, и все будет ок"
    d "И почему ты нет лестницы?"
    p "Если бы были лесенки, то много людей смогли бы жить на горе"
    d "Так это 'естественный отбор' во всей красе?"
    p "Ага, похоже на то"
    play sound problem
    "Вдруг, [player_name] увидела большой камень"

    scene bg stone

    stop music fadeout 1

    $ is_made_error = False
    label stone:
        $ is_use_timer = True
        $ timez = 10
        $ time_range = 10
        $ marker = 'stone_no_choice'

        menu:
            "Облазить его слева":
                if not is_made_error:
                    $ h.change(mind=1, money=1)
                    "Ваши туристические навыки улучшились"
                    $ travel_skills_good= True
                else:
                    $ h.change(money=1)
                # queue sound successing
                queue sound success
                #play sound successing
                "Девочки удачно обошли камень"
                jump stone_success
            "Споткнуться":
                $ is_made_error = True
                $ h.change(life=-1)
                play sound fail
                $ travel_skills_good= False
                "[player_name] подвернула ногу"
                scene bg stone
                jump stone
            "Облазить его справа":
                $ is_made_error = True    
                $life = h.change(life=-1)       
                play sound fail
                $ travel_skills_good= False
                "[player_name] ушибла бок"
                scene bg stone
                jump stone

    label stone_no_choice:
        $ h.change(life=-1)
        $ travel_skills_good= False
        "[player_name] устала держаться за веревку и скатилась вниз. При этом ушибла коленку"
        "Придется подниматься снова"
        jump stone

    label stone_success:
        $ is_use_timer = False
        
        "Веревка закончилась и девочки пошли по тропинке"

    jump way