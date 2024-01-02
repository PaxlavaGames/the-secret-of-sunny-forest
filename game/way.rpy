label way:

    scene bg way

    "Тропинка стелилась между камней"
    p "Эти камни так нависают над нами, что кажется, что мы оказались в древнем каменном городе"
    d "У этого города есть на нас таинственные планы..."

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
                $ h.change(mind=1)
                p "Может быть, найдем его хозяина или оставим себе"
                "Взять на руки хамелеона и отнести наверх"
                d "Хамелеон такой прохладный и приятный на ощупь, и такой легкий, как котенок"
                play sound lick
                $ is_with_us_chameleon = True
                show chameleon at left:
                    yalign 0.7
                with move
                hide chameleon
                pause 1
            "Хамелеон - красавчик, пусть еще погуляет":
                $ h.change(kind=1)
                p "Может он свободолюбивый хамелеон"
                "Полюбоваться хамелеоном и идти дальше"
                play sound lick
                $ is_with_us_chameleon = False
                show chameleon at chameleon_run
                with move
                pause 1

    jump space