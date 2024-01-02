label dolphins:

    scene bg fish
    play sound dolphins
    pause 2
    p "Как здорово пахнет море: свободой и солью!"

    p "Смотри какая вода чистая! И дельфины!"
    show darina smile at left
    show polly smile right at right

    queue sound yey
    menu: 
        d "Вау! Никогда не видела дельфинов в открытом море. Интересно, насколько близко они могут доплыть до берега?"
        
        "Да, выглядит просто чудесно.  Хочется нарисовать пейзаж с дельфинами":
            d "Нарисовать не успеем, но сфотографируем обязательно"
            menu:
                "Сфотографировать дельфинов":
                    play sound photo
                    pause 0.5
                    show bg mobile fish
                    d "Ученые выяснили, что дельфины интеллектуально соизмеримы с человеком и даже умнее нас"
                    p "Ага, хорошо было бы с ними пообщаться на философские темы"
                    play sound haha
                    show polly laugh right at right
                    show darina laugh at left  
                    d "Да, обсудить с ними Ницше и Канта"
                    p "Думаю дельфинам было бы интересно поговорить с философами о рыбьем бытие"
                    play sound haha                            
                    pause 2
                    #hide bg mobile fish
        "Да, ладно, дельфины как дельфины, я видела и не такое в своих трипах":
            $ dr.down()
            show darina dissatisfied at left
            d "Не возможно войти в одну реку дважды - известная народная мудрость"
            p "Зато можно пойти искупаться в море"

   
    scene bg sea sun
    show darina st left at left
    d "Пойдем купаться! До заката еще далеко"

    play sound yey
    show polly smile right at right
    p "Да, да! Я так долго этого ждала"

    "Девочки переодеваются в купальники и забегают в воду" 

    jump sea