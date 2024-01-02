label bus:
    scene bg bus

    show polly smile right at right

    $ PLAYER_DEFAULT_NAME = "Лиза"

    $ player_name = renpy.input("Как меня будут звать?", default=PLAYER_DEFAULT_NAME, allow="йцукенгшщзхъфывапролджэячсмитьбю-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = PLAYER_DEFAULT_NAME

    play music going
    
    "Две студентки на каникулах поехали отдохнуть на природе"

    show polly smile right at right

    "[player_name] сдала сессию на отлично, была любопытна и мечтала увидеть разные города и страны"

    hide polly smile right

    show darina smile at left

    "Дарина была рада, что она смогла уделить время отдыху. Девушка не только училась, но и подрабатывала рисованием портретов"

    hide darina smile at left

    show darina dissatisfied at left
    with Fade(1,1,1)

    play sound sad
    d "Мы уже трое суток добираемся, то на поезде, то на автобусе"
    p "Да, хочется поскорее вдохнуть чистый воздух без пыли"
    d "Нам потом еще идти несколько километров вдоль берега по каменистому пляжу с рюкзаком"
    jump rope