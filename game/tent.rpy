label tent:

    scene bg tent

    stop music fadeout 1

    show darina standart left at left

    label what_will_do:
        menu:
            d "Что будем делать?"
            "Посидим у костра и поиграем на варгане {image=vargan.png}":
                
                play music vargan fadeout 1
                d "[player_name], где ты так научилась играть на варгане?"
                p "Научил друг из путешествия по Индии"
                d "Как его зовут?"
                p "Его зовут Херриш, а мы называли его Херри. Возможно, скоро мы его увидим, он обещал приехать"
                p "У меня спина замерзла, пойдем в палатку?"
                d "Да, давай"
                $ dr.up()
                jump later
            "Приготовить покушать (1 {image=[KIND_IMG_MENU]})":
                if h.get('kind') < 1:
                    "Не хватает доброты"
                    jump what_will_do
                $ h.change(life=1)
                "Аромат гречи с грибами и тушенкой наполнили поляну домашним уютом"
                jump later
            "Разложить вещи в палатке (1 {image=[MIND_IMG_MENU]})":
                if h.get('mind') < 1:
                    "Не хватает ума"
                    jump what_will_do
                $ h.change(life=1)
                "Спать будет тепло и уютно"
                jump later
            "Принести воду (1 {image=[MONEY_IMG_MENU]})":
                if h.get('money') < 1:
                    "Не хватает успеха"
                    jump what_will_do
                $ h.change(money=-1, life=1)
                "Утром будет чем умыться"
                jump later
    
    label later:
        "Остальное сделаем завтра, а то вечереет"
        stop music fadeout 1
    
    if is_with_us_chameleon:
        "Девочки и хамелеон после долгой и трудной дороги быстро засыпают в палатке"
    else:
        "Девочки после долгой и трудной дороги быстро засыпают в палатке"

    scene bg tent night

    pause 2

    "А на поляне, тем временем, появляется странный гость"
    queue sound steps
    queue sound secret

    show kirill siluette at right

    "Наступает утро"

    scene bg tent
    play music forest fadeout 1

    show polly dissatisfied right at right

    play sound sad
    p "Я плохо спала ночью, слышались какие-то звуки"

    show darina dissatisfied at center

    play sound sad
    menu:
        d "А у меня болят ноги и спина"
        "И, что предлагаешь, весь день в палатке провести?": 
            $ dr.down()
        "Это нормально после долгого пути, потерпи, скоро пройдет":
            $ dr.up()

    if dr.level == BAD:
        $ say_emotionally(dr, "Зачем я с тобой вообще поехала!")
    elif dr.level == GOOD:
        $ say_emotionally(dr, "Сделаешь мне массаж?")
        p "Конечно, давай, ложись"
        show darina smile at left
        with Fade(1,1,1)
    else:
        $ say_emotionally(dr, "Угу")

    p "Дарина, кто - то ходит рядом, интересно кто, пойдем посмотрим"
    
    show darina dissatisfied at center

    "Девочки видят на соседней поляне  мужчину в деловом костюме"

    show kirill left at upthetent

    p "Странная одежда для отдыха в палатке"

    d "Может, у него спортивок нет?"

    "Молодой человек подходит ближе"

    show kirill left at left:
        xzoom 1
        yzoom 1
    with move
    
    menu: 
        n "Привет, девчонки, я Кирилл"

        "Привет, я [player_name], а это Дарина":
            $ kr.up()

        "А мы с незнакомцами не говорим":
            $ kr.down()

    show polly st right at right

    show darina standart right at center

    p "Ты контрабандист?"

    "Кирилл и нервно засмеялся"

    k "Как угадала?"

    hide darina standart right at center

    hide polly st right at right

    show darina laugh right at center

    show polly laugh right at right

    show kirill laugh at left
    with move

    show darina laugh right at right:
        xalign 0.8
    with move

    play sound haha
    "Ахахаха..."
    
    if is_with_us_chameleon:

        play sound lick
        show chameleon at chameleon_on_bag:
            xalign 0.35
        with Dissolve(2)

        p "Кирилл, смотри, кого мы нашли вчера на тропинке. Знаешь чей он?"

        "Кирилл посмотрел на хамелеона и вздрогнул"

        hide kirill laugh at left

        show kirill dissatisfied at left

        k "Нет, не знаю, чей он"

        play sound lick
        hide chameleon
        with Dissolve(2)

    else:
        p "Кирилл, видел на тропинке хамелеона?"
 
        hide kirill laugh at left

        show kirill dissatisfied at left

        k "Нет, не видел ни хамелеона, ни его хозяев"
    
    show polly standart right at right

    show kirill st at left

    show darina standart right at center
    with move
    
    play sound hm
    
    "Лицо Кирилла, как будто, на секунду застыло, и он чем-то задумался"    

    menu:
        "Девочки смотрят на Кирилла и видят, что с ним что-то не так"
        "Какой-то ты подозрительный, Кирилл, что ты скрываешь?":
            $ kr.down()
            k "Так, я и выложил вам все мои секреты"
        "Отдыхаешь или работаешь здесь, Кирилл?":
            show kirill wink at left
            k "И то и другое"  
            menu:
                k "А вы надолго приехали?"
                "Как получится, каникулы до сентября":
                    p "Так, что мы будем отдыхать и купаться сколько захотим"
                "Пока не знаем":
                    p "Вдруг, нам здесь не понравится"
    
   

    hide kirill wink at left

    show kirill st at left

    # TODO: Проверить отношения с Кириллов
    
    "Пойдемте купаться, [player_name], Кирилл?"
    if kr.level == GOOD:
        $ say_emotionally(kr, "Да, минут через 30 догоню вас")  
    elif kr.level == BAD:
        $ say_emotionally(kr, "У меня есть дела поважнее, чем с вами купаться!")
    else:
        $ say_emotionally(kr, "Нет, не пойду, не хочу обгореть, сейчас солнце сильно греет")
     
    k "Ладно, тогда позже увидимся"
    "Кирилл уходит плавной походкой, как будто на поляне нет не ни кустов, ни камней"

    hide kirill left


    menu:
        "Пойти купаться":
            #k "Ладно, тогда позже увидимся"
            #"Кирилл уходит плавной походкой, как будто на поляне нет не ни кустов, ни камней"

            #hide kirill left
            if is_with_us_chameleon:
                "Девочки  делают небольшую площадку для хамелеона и спускаются к морю"
            else:
                "Девочки спускаются к морю"

        "Остаться на поляне":

            if is_with_us_chameleon:
                p "Давай немного перекусим, поиграем с хамелеоном, а потом пойдем купаться"                                          
            else:
                "Давай немного перекусим, а потом пойдем купаться"
            #hide kirill left
            
            show darina standart left at left
            with move

            label tent_eating:
                menu:
                    "Что вы хотите съесть?"
                    "{image=banana.png}":                        
                        "Спелый банан" 
                        $ h.change(kind=1)
                        show eat banana at truecenter
                                    
                    "{image=avocado.png}":                                   
                        "свежий авокадо"
                        $ h.change(mind=1)
                        show eat avocado at truecenter

                    "{image=papaya.png}":    
                        "Ароматная папайя"
                        $ h.change(life=1)
                        show eat papaya at truecenter
                
                play sound eat

                pause 1             
        
    jump parrot