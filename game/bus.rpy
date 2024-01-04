label bus:
    scene bg bus

    show polly smile right at right

    $ PLAYER_DEFAULT_NAME = _("Лиза")

    $ player_name = renpy.input(_("Как меня будут звать?"), default=PLAYER_DEFAULT_NAME, allow="йцукенгшщзхъфывапролджэячсмитьбю-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = PLAYER_DEFAULT_NAME

    play music going
    
    "Две студентки на каникулах поехали отдохнуть на природе"

    show polly smile right at right

    "[player_name] сдала сессию на отлично, была любопытна и мечтала увидеть разные города и страны. Даже, когда  [player_name] была маленькой девочкой, она не выходила из дома без своего любимого оранжевого рюкзачка"

    hide polly smile right

    show darina smile at left

    "Дарина была рада, что она смогла уделить время отдыху. Девушка не только училась, но и подрабатывала рисованием портретов. Мечтала стать более обеспеченной, что бы рисовать то, что требует ее душа "

    hide darina smile at left

    show darina dissatisfied at left
    with Fade(1,1,1)

    play sound sad
    d "Мы уже трое суток добираемся, уже использовали разные виды транспорта: и поезд, и автобус...и до сих пор в дороге..."
    d "Хочется заняться уже чем-то полезным"
    p "Ага, и поскорее вдохнуть чистый воздух без пыли"
    d "Да, подышим... "
    d "...пока будем преодолевать несколько километров вдоль каменистого побережья с рюкзаком..."
    jump rope