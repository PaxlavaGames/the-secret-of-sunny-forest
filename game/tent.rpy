label tent:

    scene bg tent
    show darina st left at left
    show polly st right at right
    d "А палатка не промокнет под дождем?"
    p "Нет, если тент и стенки палатки не будут соприкасаться друг с другом во время дождя"
    d "Да, проснуться в луже, представляю какое это удовольствие!"
    show darina dissatisfied at left
    p "Мы поставили палатку на хорошем месте, думаю, что все будет хорошо"
    p "Если конечно не начнется сильный ветер"
    d "Я столько сил потратила на вбивание колышков, сомневаюсь, что их легко будет достать обратно из земли"
    p "Ага, ты постаралась на славу, пока их вколачивала. Так кряхтела и стучала, что я думала, сюда из соседнего хутора придут"
    show polly wink right at right


    stop music fadeout 1

    show darina st left at left

    label what_will_do:
        menu:
            d "Что будем делать?"
            
            "Посидим у костра и поиграем на варгане {image=vargan.png}":
                show polly st right at right
                play music vargan fadeout 1
                d "[player_name], где ты научилась играть на варгане?"
                p "Научил друг из трипа по Индии"
                d "Как его зовут?"
                p "Его зовут Херриш, а мы называли его Херри. Возможно, скоро мы его увидим, он обещал приехать"
                d "Как там в Индии?"
                p "Очень жарко, звонко и благоухает. Коровы там священное животное, поэтому они ходят где хотят"
                p "Индийцы работают рикшами на велосипедах, продают и готовят еду прямо на улицах, а в храмах танцуют"
                p "Вообще, море впечатлений, потом подробнее расскажу тебе"
                d "У меня спина замерзла, пойдем в палатку?"
                p "Да, давай"
                $ dr.up()
                jump later
            "Приготовить покушать (1 {image=[KIND_IMG_MENU]})":
                if h.get('kind') < 1:
                    "Не хватает доброты"
                    jump what_will_do
                $ h.change(life=1)
                "Аромат гречи с грибами и тушенкой наполнили поляну домашним уютом"
                show polly smile right at right
                p "Какая вкуснятина!"
                d "Да, это еще рецепт моей бабушки, у нее был свой ресторан, пока не началась перестройка"
                show polly st right at right
                p "Перестройка затронула многих, у моих соседей тогда случилась и вовсе скверная история"
                d "Что за история?"
                p "Давай потом расскажу, это не сказка на ночь..."
                p "Хочу уже улечься в теплый уютный спальник"
                d "Да, а то завтра встанем поздно "
                jump later
            "Разложить вещи в палатке (1 {image=[MIND_IMG_MENU]})":
                if h.get('mind') < 1:
                    "Не хватает ума"
                    jump what_will_do
                $ h.change(life=1)
                "Спать будет тепло и удобно"
                show polly smile right at right
                p "Как хорошо ты все распределила в палатке, стало уютно и ничего не будет мешать "
                d "Да, мне тоже нравится, что бы все было на своем месте"
                p "Надеюсь, что этого порядка хватит не только на одну ночку со мной..."
                show darina surprise at left
                d "..."
                p "Я часто переворачиваюсь во сне"
                show darina smile at left
                d "Ничего страшного, я тоже не подарок"
                jump later
            "Принести воду (1 {image=[MONEY_IMG_MENU]})":
                if h.get('money') < 1:
                    "Не хватает успеха"
                    jump what_will_do
                $ h.change(money=-1, life=1)
                show polly st right at right
                p "Утром будет чем умыться"
                d "Да, вода нам точно пригодится"
                jump later
    
    label later:
        p "Остальное сделаем завтра, сейчас уже совсем темно становится"
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
        d "А у меня болят ступни ног и спина"
        "И, что предлагаешь, весь день в палатке провести?": 
            $ dr.down()
        "Это нормально после долгого пути, потерпи, скоро пройдет":
            $ dr.up()

    if dr.level == BAD:
        $ say_emotionally(dr, "Зачем я с тобой вообще поехала?!")
        show darina evil at center
        p "Затем, что ты хотела  попробовать как жить без удобств!"
        show polly evil right at right
        show darina dissatisfied at center
        show polly dissatisfied right at right
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
    d "..."
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
            k "Вы тут недавно? Не видел вас вчера "
            p "Мы пришли сюда уже под вечер, тебя тоже не заметили"
            d "Где твоя палатка?"
            k "Отсюда ее не видно, она за холмом"

        "А мы с незнакомцами не говорим":
            $ kr.down()
            k "Вы уже говорите, следовательно, я уже не являюсь 'незнакомцем'"
            p  "Хм..."

    show polly st right at right

    show darina st right at center

    p "Ты контрабандист?"

    "Кирилл и нервно засмеялся"

    k "Как угадала?"

    hide darina st right at center

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
            d "Все тайное рано или поздно становится явным..."
            p "Ладно, мы же пошутили, не будь букой"
            k "Ок, прощаю вам ваши инсинуации в мой адрес. Я сегодня великодушный"
        "Отдыхаешь или работаешь здесь, Кирилл?":
            show kirill wink at left
            k "И то и другое"  
            p "Как интересно! Расскажешь подробности?"
            d "А ты здесь один или с друзьями или подругой?"
            k "Сколько вопросов! Я один, и у меня здесь важное дело, связанное с моей семьей, подробности пока и сам не все знаю"
            menu:
                k "А вы надолго приехали?"
                "Как получится, каникулы до сентября":
                    p "Так, что мы будем отдыхать и купаться сколько захотим"
                "Пока не знаем":
                    p "Вдруг, нам здесь не понравится"
                    d "А мне уже тут нравится"
                    p "Ты еще недавно жаловалась, что устала"
                    d "Уже отдохнула"
    
   

    hide kirill wink at left

    show kirill st at left

    # TODO: Проверить отношения с Кириллов
    
    "Пойдем купаться, [player_name], Кирилл?"
    if kr.level == GOOD:
        $ say_emotionally(kr, "Да, через 30 минут догоню вас")  
    elif kr.level == BAD:
        $ say_emotionally(kr, "У меня есть дела поважнее, чем с вами купаться!")
    else:
        $ say_emotionally(kr, "Нет, не пойду, сейчас солнце сильно греет")
     
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
                        p "Как же здесь красиво и приятно находится!"
                                    
                    "{image=avocado.png}":                                   
                        "свежий авокадо"
                        $ h.change(mind=1)
                        show eat avocado at truecenter
                        p "Чувствую, что готова поразмыслить над смыслом бытия"

                    "{image=papaya.png}":    
                        "Ароматная папайя"
                        $ h.change(life=1)
                        show eat papaya at truecenter
                        p "Чувствую, что готова на подвиги"
                play sound eat

                pause 1             
        
    jump parrot