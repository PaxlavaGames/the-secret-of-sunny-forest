label parrot:
    scene bg sea sun
    play music silentsea fadeout 3

    "Девочки подходят к морю"
    "Ветер ласково перебирает им волосы, а солнце тепло касается их лиц"
    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left
    
    "На камне лежит маленький попугайчик"


    show popka on stone at right
    # with irisin - появление из правого нижнего угла
    # with slideleft - сцена дублирует справа налево
    # with wipeleft - появление справа налево
    # with squares - появление из квадратов
    # with vpunch - всё трясется вниз-вверх
    # with hpunch - всё трясется вправо-влево
    # with zoomin - прикольная штука от маленького к большому
    # with Pixellate(time=1, steps=1) - делает всё пиксальныйм на какое то время
    # with ImageDissolve('popka on stone.png', 1) - какая то шляпа

    "Трепещет крылышками"
    "Видно, что попугайчик очень плохо себя чувствует"
    d "Откуда здесь попугайчик?"
    p "И что с ним такое?"
    play sound problem
    $ is_made_error = False

    label save_parrot:
        menu:
            " Помочь попугайчику (2 {image=[KIND_IMG_MENU]})":
                if h.get('kind') >= 2:
                    $ h.change(money=1, kind=2)
                    "Вы пытаетесь спасти попугая"
                    jump how_save_parrot
                else:
                    "у вас нет 2 доброты"
                    jump save_parrot
            "Спасти попугая (2 {image=[MONEY_IMG_MENU]})":
                if h.get('money') >= 2:
                    $ h.change(money=-2)
                    "Вы пытаетесь спасти попугая"
                    $ h.change(money=1, kind=2)
                    jump how_save_parrot
                else:
                    "у вас нет 2 монеты"
                    jump save_parrot                   
            "Оставить как есть попугая, и идти купаться":
                $ h.change(kind=-1)
                "Искупавшись, вернуться к попугаю"
                jump save_parrot
            "Не помогать попугаю":
                $ h.change(life=-1)
                play sound fail
                "Высшие силы не довольны вашим выбором, и вы утонули, попробуйте выбрать другой вариант"
                
                show  darina st swimsuit at left:
                    xalign 0.2
                show polly st swimsuit at left
                show popka on stone at right
                jump save_parrot

    label how_save_parrot:
        $ is_use_timer = True
        $ timez = 10
        $ time_range = 10
        $ marker = 'parrot_no'
        menu:
            "Дать попить из крышки питьевой воды (2 {image=[MIND_IMG_MENU]})":
                if h.get('mind') < 2:
                    "у вас не хватает ума"
                    jump how_save_parrot
                if not is_made_error: 
                    $ h.change(mind=1)  
                $ h.change(money=2)
                show polly swimsuit at center
                play sound drink
                with move
                pause 1
                "Попугай пришел в себя, начал вертеть головой"
                show polly st swimsuit at left
                jump parrot_success
            "Дать дорогое лекарство (2 {image=[MONEY_IMG_MENU]})":
                if h.get('money') < 2:
                    "У вас не хватает монет"
                    jump how_save_parrot
                if not is_made_error: 
                    $ h.change(mind=1)
                $ h.change(money=-2)
                show polly swimsuit at center
                play sound drink
                with move
                pause 1
                "Выпив последнюю каплю лекарства, попугай пришел в себя"
                show polly st swimsuit at left
                $ h.change(money=2)
                jump parrot_success
            "Переложить себе на руки и прощупать крылышки":
                play sound fail
                $ is_made_error = True
                $ h.change(life=-1)
                "Попугай начал задыхаться и не выжил, попробуйте выбрать другой вариант"
                show  darina st swimsuit at left:
                    xalign 0.2
                show polly st swimsuit at left
                show popka on stone at right
                jump how_save_parrot
            "Побрызгать на голову попугайчика воды":
                $ is_made_error = True
                play sound fail
                $ h.change(mind=-1)
                "Попугайчик испугался и сошел с ума, попробуйте выбрать другой вариант"
                show  darina st swimsuit at left:
                    xalign 0.2
                show polly st swimsuit at left
                show popka on stone at right
                             
                jump how_save_parrot

    label parrot_no:
            $ h.change(life=-1)
            "[player_name] не успела спасти попугайчика"
            "Вернитесь и попробуйте снова"
            
            jump how_save_parrot

            label parrot_success:
                queue sound success
                $ is_use_timer = False

    "Попугайчик, пошатываясь, встал на ноги"
    p "О, попугайчику стало лучше! Мы помогли ему!"
    $ PARROT_DEFAULT_NAME = "Виря"

    $ parrot_name = renpy.input ("Мое имя звучит на вашем языке, как...", default=PARROT_DEFAULT_NAME, allow="йцукенгшщзхъфывапролджэячсмитьбю-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
    
    $ parrot_name = parrot_name.strip()

    if parrot_name == "":
        $ parrot_name = PARROT_DEFAULT_NAME
    
    # Отношения с попугаем
    $ vr = Relationship(parrot_name, character=v)
    $ vr.observers.append(rn)
    $ vr.up(2)

    show darina surprise swimsuit at left:
        xalign 0.2

    show polly surprise swimsuit at left

    play sound shock
    
    "Девочки удивленно распахнули глаза"

    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left
    p "Говорящий попугай!!"
    # play music importanting
    # stop music fadeout 1
    play music mainsea

    pause 3

    v "Спасибо за помощь, мне нужна была местная пища или вода, чтобы зацепиться в этом мире"

    show darina surprise swimsuit at left:
        xalign 0.2

    show polly surprise swimsuit at left
    play sound shock
    d "В этом мире?"

    play sound parrot
    v "Да, я из другого мира"

  

    play sound parrot
    v "Если бы вы не напоили меня, через некоторое время я растворился бы во времени и пространстве"

    play sound parrot
    v "Спасибо вам, девушки"

    #show popka new right at right

    p "Мы рады были помочь. А что случилось с твоим миром? Как ты оказался здесь?"

    v "Кто-то применил заклинание, и я оказался здесь"
    v "Я понял, что я не своем мире, когда увидел людей и собак, у нас в мире нет людей и больших животных. Но я читал  о них в древних преданиях"
    $ is_one_answer = False

    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left

    label parrot_world:
        if is_one_answer:
            menu:
                "Чем мы можем помочь?":
                    play sound parrot
                    v "Мне необходима помощь в поиске портала в мой мир "
                    p "Портал, как его найти?"
                    play sound parrot
                    v "Портал - это круг из 108 камней. Когда в него заходишь, то он начинает светиться фиолетовым"
                    v "Нужно прикоснуться к некоторой комбинации камней и свечение станет зеленым"
                    play sound parrot
                    v "Затем произойдет переход в другой мир"
                    
                    jump parrot_world
                "Ты хочешь вернуться назад?":
                    play sound parrot
                    v "Да, мне нужно вернуться домой, иначе там разразится война"
                    p "Война между кем, ради чего?"
                    play sound parrot
                    v "Война между разными видами птиц"
                    v "Такие, как гарпии, вороны и другие птицы недовольны правлением клана волнистых"
                    v "Интриги последние 3 года. Я пытался найти заговорщиков"
                    play sound parrot
                    v "Поэтому меня изгнали, чтобы я не открыл правду имеющим власть и народу"
                    
                    jump parrot_world
                "Почему ты оказался именно здесь?":
                    play sound parrot
                    v "С помощью колдуна, меня отправили в ваш мир "
                    v "А здесь, у моря, находится переход. Если бы вы не напоили меня, я бы быстро погиб. И не смог бы найти изменников и помочь нашему миру"
                    p "Какой твой мир?"
                    play sound parrot
                    v "Наш мир очень красив: дикие джунгли, города, пасеки, горы, реки и моря"
                    v "В нем  живут птицы, хамелеоны и насекомые, других животных нет, некоторые из нас обладают магией"
                    play sound parrot
                    v "Но длительное пребывание в мире без магии сделает нас обычными птицами, не очень разумными"
                    jump parrot_world

                "Закончить опрос":

                    show popka at center

                    hide polly surprise swimsuit right at right

                    hide darina surprise swimsuit at left

                    show polly st swimsuit right at right

                    show darina st swimsuit at left

                    play sound yey

                    # stop music fadeout 4
                    play music silentsea fadeout 4
                    menu:
                        "Множество миров ! Это так удивительно! Мы поможем тебе":
                            $ vr.up()
                            jump manywords
                        "Оказывается, что сложно жить не только в нашем мире":
                            jump manywords
        else:
            menu:
                "Чем  мы можем помочь?":
                    $ h.change(kind=1)
                    $ vr.up()
                    play sound parrot
                    v "Мне необходима помощь в поиске портала в мой мир"
                    p "Портал, как его найти?"
                    v "Портал - это круг из 108 камней. Когда в него заходишь, то он начинает светиться фиолетовым"
                    play sound parrot
                    v "Нужно прикоснуться к некоторой комбинации камней и свечение станет зеленым"
                    v "Затем произойдет переход в другой мир"
                    $ is_one_answer = True
                    jump parrot_world
                "Ты хочешь вернуться назад?":
                    v "Да, мне нужно вернуться домой, иначе там разразится война"
                    p "Война между кем, ради чего?"
                    v "Война между разными видами птиц"
                    play sound parrot
                    v "Такие, как гарпии, вороны и другие птицы недовольны правлением клана волнистых"
                    v "Интриги последние 3 года. Я пытался найти заговорщиков"
                    play sound parrot
                    v "Поэтому меня изгнали, чтобы я не открыл правду имеющим власть и народу"
                    $ is_one_answer = True
                    jump parrot_world
                "Почему ты оказался именно здесь?":
                    $ h.change(mind=1)
                    play sound parrot
                    v "С помощью колдуна, меня отправили в ваш мир "
                    play sound parrot
                    v "А здесь, у моря, находится переход. Если бы вы не напоили меня, я бы быстро погиб. И не смог бы найти изменников и помочь нашему миру"
                    p "Какой твой мир?"
                    v "Наш мир очень красив: дикие джунгли, города, пасеки, горы, реки и моря"
                    play sound parrot
                    v "В нем  живут птицы, хамелеоны и насекомые, других животных нет, некоторые из нас обладают магией"
                    play sound parrot
                    v "Но длительное пребывание в мире без магии сделает нас обычными птицами, не очень разумными"
                    $ is_one_answer = True
                    jump parrot_world

label manywords:
    "Девочки были ошеломлены сказанным маленькой птицей"
    "В это время попугайчик поднял крыло и высыпал на камень части картины"

    v "Девушки, эта картина поможет нам найти портал, только при перемещении она порвалась"
    v "Помогите, пожалуйста, ее собрать"

    jump makepuzzle