label rope:
    scene bg rock

    play music sea fadeout 2 # вроде норм

    pause 3

    show polly smile right at right

    menu:
        "Уже почти пришли.  Видишь веревку, свисает с горы? Нам как раз туда":
            $ dr.up()
        "Даринка, мы же путешествуем, и дорога - это тоже часть приключения":
            $ dr.down()
            show darina dissatisfied at left
            d "Ладно, просто я устала, и рюкзак тяжелый"
            show darina surprise at left
            play sound shock
            d "Веревка?"
    
    show darina smile at left

    d "Надеюсь, что там не нужно быть альпинистом, чтобы залезть на верх?"

    p "Конечно, нет. Да, там тяжеловато, но подъем короткий"
       
    jump dolphins