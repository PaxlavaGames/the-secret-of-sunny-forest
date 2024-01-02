label note:
    
    show popka on stone at center 
    show polly st swimsuit right at right

    show darina st swimsuit at left

    v "На обороте картины мы найдем рецепт зелья"
    v "Оно откроет нам глаза на магию в вашем мире, и  мы увидим портал"
    # убрать здесь пазл
    hide popka at center   
    show bg sea      
    show room at transform_room

    $ k.hide()

    menu:
        
        "Перевернуть картину и посмотреть, что на обороте сейчас":
            hide room at transform_room
            show note at transform_note
            
            $ vr.up()
            show polly st swimsuit right at right
            show darina st swimsuit at left
            p "О, тут действительно что-то есть, но не понимаю, что написано"
            v "Да, это на нашем языке, сейчас переведу"
            v "Здесь сказано, что для зелья необходимо собрать 5 ингредиентов:"
            $ h.change(money=1)
            queue sound success
            v "{color=#dcc600}Семена подсолнуха,{/color}{color=#f00} лепестки мака,{/color} {color=#00ff00} листья гладиолуса,{/color} {color=#a4a4a4} каменную пыль,{/color}{color=#00d3eb} голубые трубчатые водоросли{/color}"
            p "Как много компонентов!"
            d "Я видела недалеко от палатки поляну с цветами, думаю, найдем там что-то для зелья"
            #добавить переменную про маску
            if is_with_swimm:
                p "А я видела голубые водоросли, когда плавала в маске, мы справимся!!"
            else:
                p "Надо было плавать в маске, тогда бы я разглядела все дно. Не знаю, справимся ли мы"
                $ down.up()
        "Давай потом посмотрим, мы спешим": 
            $ vr.down()      
            hide room at transform_room 
    hide note at transform_note 

    jump end_story