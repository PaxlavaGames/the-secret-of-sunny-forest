# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define d = Character('Дарина', color="#ffffff")
define p = Character('Полли', color="#feffbe")
define n = Character('Незнакомец', color='#ffffff')
define k = Character('Кирилл', color='#ebe3ff')
define v = Character('Виря', color='#fff0cd')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#Transforms
transform upthetent:
    xalign 0
    yalign 0.5
    xzoom 0.5
    yzoom 0.5

transform chameleon_start:
    xalign 0.7
    yalign 0.5
    xzoom 0.5
    yzoom 0.5

transform chameleon_run:
    xalign 0.4
    yalign 0.0
    xzoom 0.2
    yzoom 0.2

transform chameleon_on_bag:
    xalign 0.65
    yalign 0.5
    xzoom 0.4
    yzoom 0.4

# Игра начинается здесь:
label start:

    play music go

    scene bg bus

    "Две студентки на каникулах поехали отдохнуть на природе"

    show polly smile right at right

    "Полли сдала сессию на отлично, была любопытна и мечтала увидеть разные города и страны"

    hide polly smile right

    show darina smile at left

    "Дарина так же была умна и рада, что она смогла уделить время отдыху. Девушка не только училась, но и подрабатывала рисованием портретов"

    hide darina smile at left

    show darina dissatisfied at left
    with Fade(1,1,1)

    play sound sad
    d "Мы уже трое суток добираемся, то на поезде, то на автобусе. А после этого, еще идти несколько километров вдоль берега по каменистому пляжу с рюкзаком"

    scene bg rock

    pause 1

    show polly smile right at right

    p "Уже почти пришли.  Видишь веревку, свисает с горы?"

    show darina smile at left

    d "Наконец-то. Надеюсь,что там не нужно быть альпинистом, чтобы залезть на верх?"

    p "Конечно, нет. Да, там тяжеловато, но подъем короткий"

    play sound yey
    p "Смотри какое чистое море! И дельфины!"


    scene bg fish

    show darina smile at left

    play sound yey
    d "Вау! Никогда не видела дельфинов в открытом море. Выглядит просто волшебно!"

    show polly smile right at right

    p "Да, очень красиво.  Хочется нарисовать пейзаж с дельфинами"

    d "Нарисовать не успеем, но сфоткаем"

    menu:
        
        "Сфоткать дельфинов":
            play sound photo
            pause 0.5
            show bg mobile fish
            
    pause 2
    
    hide bg mobile fish

    scene bg sea sun

    p "Пойдем купаться! До заката еще далеко, успеем поставить палатку"

    d "Да, да! Я так долго этого ждала"

    "Девочки переодеваются в купальники и забегают в воду"

    # Медленная
    play music relax

    scene bg sea sunny meduza

    show darina surprise swimsuit right at right

    play sound sad
    d "Тут водоросли и медузы!"

    show polly st swimsuit at left

    p "Ничего, водоросли полезные. А вот медузы мне тоже не нравятся. Какие-то из них даже жалятся"

    hide darina surprise swimsuit right at right

    show darina smile swimsuit right at right

    show polly smile swimsuit at left
    
    "Так проходит некоторое время. Солнце уже не так жарит, а девочки расслабленно лежат у берега в воде"

    scene bg see down

    show polly st swimsuit at left

    p "Пойдем ставить палатку?"
    show darina sly smile swimsuit right at right
    
    d "Хочу еще искупаться"

    menu:
        d "Ты иди посмотри что там наверху. А я приду позже"
        "Ладно, купайся пока. Пойду посмотрю, что там и как":
            play sound haha
            "Дарина хитро улыбается"
            "Полина переоделась в сухую одежду и пошла наверх, держась за веревку"
            "Вскоре ее догнала Дарина"
        "Ладно еще покупаемся и пойдем месте":
            d "Ладно, тогда еще 5 минут"
            "Девочки переоделись и пошли наверх"

    play music go

    scene bg rock

    "Девочки, держась за веревку, понимались сначала одна, потом вторая"

    play sound problem
    "На пути Полины возник большой камень"

    scene bg stone

    label stone:
        # TODO: выбора на время
        menu:
            "Облазить его слева":
                play sound success
                "Девочки удачно обошли камень"
            "Споткнуться":
                play sound fail
                "Полина подвернула ногу"
                #scene bg red
                #pause 1
                scene bg fon mistake
                pause 1
                scene bg stone
                jump stone
            "Облазить его справа":
                play sound fail
                "Полина ушибла бок"
                scene bg fon mistake 
                pause 1
                scene bg stone
                jump stone

    "Веревка закончилась и девочки пошли по тропинке"

    scene bg way

    "Тропинка стелилась между камней"

    show polly smile right at right

    p "Даринка, смотри, там, кажется, хамелеон!"

    play sound lick
    show chameleon at chameleon_start    
    with Dissolve(1)

    show darina smile at left

    d " О, точно, что же он здесь делает один? Сбежал от хозяина, наверное. Возьмем его с собой?"

    label chameleon:
         
        menu:
            "Он такой хорошенький, конечно, возьмем":
                p "Может быть, найдем его хозяина или оставим себе"
                "Взять на руки хамелеона и отнести наверх"
                play sound lick
                $ is_with_us_chameleon = True
                show chameleon at left:
                    yalign 0.7
                with move
                hide chameleon
                ""
            "Хамелион - красавчик, пусть еще погуляет":
                p "Может он свободолюбивый хамелеон"
                "Полюбоваться хамелеоном и идти дальше"
                play sound lick
                $ is_with_us_chameleon = False
                show chameleon at chameleon_run
                with move
                pause 1

    play music space
    scene bg top

    show polly smile right at right

    if is_with_us_chameleon:
        show chameleon at chameleon_on_bag

    play sound yey
    p "Какая красота!"

    show darina smile at left

    play sound yey
    d "Восхитительно!"

    hide polly smile right at right

    hide darina smile at left

    show polly st right at right

    show darina st left at left
    
    label tent:
        menu:
            d "Где же нам поставить палатку?"
            "На склоне":
                play sound fail
                "Вы скатитесь с горы в море"
                scene bg fon mistake
                pause 1
                scene bg top
                jump tent
            "На ровном месте":
                play sound success
                "Вам будет спать мягко и удобно"
            "У муравейника":
                play sound fail
                "Ночью вам будет не до сна"
                scene bg fon mistake
                pause 1
                scene bg top
                jump tent

    "Девочки выбрали место и поставили палатку"

    scene bg tent

    show darina standart left at left

    menu:
        d "что будем делать?"
        "Искать дрова":
            jump later
        "Приготовить покушать":
            jump later
        "Разложить вещи в палатке":
            jump later
        "Принести воду":
            jump later
    
    label later:
        "Остальное сделаем завтра, а то вечереет"
    
    if is_with_us_chameleon:

        "Девочки и хамелеон после долгой и трудной дороги быстро засыпают в палатке"

    else:

        "Девочки после долгой и трудной дороги быстро засыпают в палатке"

    scene bg tent night

    pause 2

    "А на поляне, тем временем, появляется странный гость"
    play sound secret

    show kirill siluette at right

    "Наступает утро"

    scene bg tent

    show polly dissatisfied right at right

    play sound sad
    p "Я плохо спала ночью, слышались какие-то звуки"

    show darina dissatisfied at center

    play sound sad
    d "А у меня болят ноги и спина"

    p "Дарина, кто - то ходит рядом, интересно кто, пойдем посмотрим"

    "Девочки видят на соседней поляне  мужчину в деловом костюме"

    show kirill left at upthetent

    p "Странная одежда для отдыха в палатке"

    d "Может, у него спортивок нет?"

    "Молодой человек подходит ближе"

    show kirill left at left:
        xzoom 1
        yzoom 1
    with move
    
    n "Привет, девчонки,я Кирилл"

    show darina standart right at center

    show polly st right at right

    p "Привет, ты контрабандист?"

    k "Как угадала?"

    hide darina standart right at center

    hide polly st right at right

    # hide kirill left at left

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

        "Кирилл посмотрел на хамелеона и взрогнул"

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
    "Девочки смотрят на Кирилла и видят, что с ним что-то не так"
    "Лицо Кирилла, как будто, на секунду застыло, и он чем-то задумался"

    p "Отдыхаешь или работаешь здесь, Кирилл?"

    show kirill wink at left
    
    k "И то и другое"

    d "Пойдемте купаться, Полина, Кирилл?"

    hide kirill wink at left

    show kirill st at left

    k "Нет, не пойду, не хочу обгореть, сейчас солнце сильно греет"

    menu:
        "Пойти купаться":
            k "Ладно, тогда позже увидимся"
            "Кирилл уходит плавной походкой, как будто на поляне нет не ни кустов, ни камней"

            hide kirill left
            if is_with_us_chameleon:
                "Девочки  делают небольшую площадку для хамелеона и спускаются к морю"
            else:
                "Девочки спускаются к морю"

        "Остаться на поляне":

            if is_with_us_chameleon:
                p "Давай немного перекусим, поиграем с хамелеоном, а потом пойдем купаться"                                          
            else:
                "Давай немного перекусим, а потом пойдем купаться"
            hide kirill left
            
            show darina standart left at left
            with move

            menu:
                "Что вы хотите съесть?"
                "{image=banana.png}":     
                    
                    "Банан"
                    show eat banana at truecenter
                                
                "{image=avocado.png}":    
                                
                    "Авокадо"
                    show eat avocado at truecenter

                "{image=papaya.png}":    
                    "Папайя"
                    show eat papaya at truecenter
            
            play sound eat

            pause 1

    scene bg sea sun

    "Девочки подходят к морю"

    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left

    "На камне лежит попугайчик"

    show popka on stone at right

    "Трепещет крылышками"
    "Видно, что попугаю сложно дышать"
    play sound problem

    label save_parrot:
        menu:
            "Спасти попугая":
                jump how_save_parrot
            "Оставить как есть попугая, и идти купаться":
                "Искупавшись, вернуться к попугаю"
                jump save_parrot
            "Не помогать попугаю":
                play sound fail
                "Высшие силы не довольны вашим выбором, и вы утонули, попробуйте выбрать другой вариант"
                show bg fon mistake
                pause 1
                show bg sea sun
                jump save_parrot

    label how_save_parrot:
        menu:
            "Дать попить из крышки питьевой воды":
                show polly swimsuit at center
                play sound drink
                with move
                pause 1
                "Попугай пришел в себя"
                show polly st swimsuit at left
            "Переложить себе на руки и прощупать крылышки":
                play sound fail
                "Попугай начал задыхаться и не выжил, попробуйте выбрать другой вариант"
                show bg fon mistake
                pause 1
                show bg sea sun
                jump how_save_parrot
            "Побрызгать на голову попугайчика воды":
                play sound fail
                "Попугайчик испугался и сошел с ума, попробуйте выбрать другой вариант"
                show bg fon mistake
                pause 1
                show bg sea sun
                jump how_save_parrot


    "Попугайчик, пошатываясь, встал на ноги"

    v "Привет, меня зовут Виря"

    show darina surprise swimsuit at left:
        xalign 0.2

    show polly surprise swimsuit at left

    play sound shock
    "Девочки удивленно распахнули глаза"
    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left

    play music important

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
    v "Так получилось, что я оказался здесь"

    play sound parrot
    v "Если бы вы не напоили меня, через некоторое время я растворился бы во времени и пространстве"

    play sound parrot
    v "Спасибо вам, девушки"

    #show popka new right at right

    p "Мы рады были помочь. А что случилось с твоим миром? Как ты оказался здесь?"

    v "Кто - то колдовством изгнал меня из моего мира и я оказался здесь"

    $ is_one_answer = False

    show darina st swimsuit at left:
        xalign 0.2

    show polly st swimsuit at left

    label parrot_world:
        if is_one_answer:
            menu:
                "Чем  мы можем помочь?":
                    play sound parrot
                    v "Мне необходима помощь в поиске портала в мой мир"
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
                    v "Поэтому меня изгнали,чтобы я не открыл правду правлению и народу"
                    
                    jump parrot_world
                "Почему ты оказался именно здесь?":
                    v "Думаю, что кто-то приближенный к власти захотел большего, полного господства"
                    play sound parrot
                    v "С помощью колдуна, меня отправили в ваш мир "
                    v "А здесь, у моря, находится переход. Если бы вы не напоили меня, я бы быстро погиб. И не смог бы найти изменников и помочь нашему миру"
                    p "Какой твой мир?"
                    play sound parrot
                    v "Наш мир очень красив: дикие джунгли, города, пасеки, горы, реки и моря"
                    v "В нем  живут птицы, хамелеоны и насекомые, других животных нет"
                    play sound parrot
                    v "Птицы разного вида и размера, некоторые обладают магией"
                    v "Но длительное пребывание в мире без магии сделает нас обычными птицами, не очень разумными"
                    jump parrot_world
                "Закончить опрос":

                    show popka at center

                    hide polly surprise swimsuit right at right

                    hide darina surprise swimsuit at left

                    show polly st swimsuit right at right

                    show darina st swimsuit at left

                    play sound yey
                    p "Множество миров ! Это так удивительно! Мы поможем тебе"
        else:
            menu:
                "Чем  мы можем помочь?":
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
                    v "Поэтому меня изгнали,чтобы я не открыл правду правлению и народу"
                    $ is_one_answer = True
                    jump parrot_world
                "Почему ты оказался именно здесь?":
                    play sound parrot
                    v "Думаю, что кто то приближенный к власти захотел большего, полного господства      "
                    v "С помощью колдуна, меня отправили в ваш мир "
                    play sound parrot
                    v "А здесь, у моря, находится переход. Если бы вы не напоили меня, я бы быстро погиб. И не смог бы найти изменников и помочь нашему миру"
                    p "Какой твой мир?"
                    v "Наш мир очень красив: дикие джунгли, города, пасеки, горы, реки и моря"
                    play sound parrot
                    v "В нем  живут птицы, хамелеоны и насекомые, других животных нет"
                    v "Птицы разного вида и размера, некоторые обладают магией"
                    play sound parrot
                    v "Но длительное пребывание в мире без магии сделает нас обычными птицами, не очень разумными"
                    $ is_one_answer = True
                    jump parrot_world

    play music main

    "Девочки были ошеломлены сказанным маленькой птицей"

    "Сначала даже показалось, что Виря  выдумал всю эту историю"

    "Но аргументированность и  логика беседы убедила их в обратном"

    return
