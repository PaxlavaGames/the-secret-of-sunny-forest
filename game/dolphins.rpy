label dolphins:

    scene bg fish
    play sound dolphins
    pause 2
    p "Как здорово пахнет море: свободой и солью!"

    p "Смотри какое оно чистое! И дельфины!"
    show darina smile at left
    show polly smile right at right

    queue sound yey
    menu: 
        d "Вау! Никогда не видела дельфинов в открытом море. Выглядит просто волшебно!"
        
        "Да, очень красиво.  Хочется нарисовать пейзаж с дельфинами":
            d "Нарисовать не успеем, но сфотографируем"
            menu:
                "Сфотографировать дельфинов":
                    play sound photo
                    pause 0.5
                    show bg mobile fish
                
                    pause 2
    
                    hide bg mobile fish
        "Да, ладно, дельфины как дельфины, я видела и не такое":
            $ dr.down()
   
    scene bg sea sun

    p "Пойдем купаться! До заката еще далеко"

    play sound yey
    d "Да, да! Я так долго этого ждала"

    "Девочки переодеваются в купальники и забегают в воду" 

    jump sea