label sea:

    play sound water

    # Медленная
    play music relaxing

    scene bg sea sunny meduza

    show darina surprise swimsuit right at right
    #добавить переменную про маску
    menu:
        d "Будешь плавать в маске?"
        "{image=swimm.png}": 
            "Да" 
            show polly swimm swimsuit at left
            $ is_with_swimm = True
        "Плавать без маски":
            $ h.change(life=-1)
            "В глаза попала соленая вода и теперь их жжет"
            show polly smile swimsuit at left 
            $ is_with_swimm = False   

    play sound shock
    menu:
        d "Тут водоросли и медузы!"
        # "Мы же не в бассейне, конечно, тут водоросли":
        #     "Отношения с Дариной стали хуже"
        #     # отн к Д -
        "Ничего, водоросли полезные":
            p "А вот медузы мне тоже не нравятся. Какие-то из них даже жалятся"
            
            # Либо плохие либо нейтральные
            # $ renpy.notify(darina_relationship)
            if dr.level == BAD:
                # d "Нифига они не полезные"
                $ say_emotionally(dr, "Ничего они не полезные!")
            else:
                $ say_emotionally(dr, "Да, водоросли вкусные и я пробывала маски на их основе - кожа потом просто супер!")
            # отн к Д +

    hide darina surprise swimsuit right at right

    show darina smile swimsuit right at right

    show polly smile swimsuit at left
    
    "Так проходит некоторое время. Солнце уже не так жарит, а девочки расслабленно лежат у берега в прохладной морской воде, рассматривают камешки и ракушки"

    scene bg see down

    show polly st swimsuit at left

    p "Пойдем ставить палатку?"
    show darina sly smile swimsuit right at right
    
    d "Хочу еще искупаться"

    menu:
        d "Ты иди посмотри что там наверху. А я приду позже"
        "Ладно, купайся пока. Пойду посмотрю, что там и как":
            $ h.change(kind=1)
            play sound haha
            "Дарина хитро улыбается"
            "[player_name] переоделась в сухую одежду и пошла наверх, держась за веревку"
            "Вскоре ее догнала Дарина"
        "А палатку ночью сама будешь ставить?":
            $ h.change(mind=1)
            d "Ладно, тогда еще 5 минут"
            "Девочки переоделись и пошли наверх"

    jump rock