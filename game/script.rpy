# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define d = Character('Дарина',  who_bold=True, color="#ffdbeb")
define p = Character("[player_name]", who_bold=True, color="#feffbe") 
define n = Character('Незнакомец', color='#ffffff')
define k = Character('Кирилл', who_bold=True, color='#e7ddff')
define v = Character('[parrot_name]', who_bold=True, color='#c9ffd9')

#define v = Character('[parrot_name]', who_bold=True, color='#b40000')

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
    xalign 0.61
    yalign 0.45
    xzoom 0.4
    yzoom 0.4

transform transform_note:
    xalign 0.5
    yalign 0.5
    #xzoom 0.5
    #yzoom 0.5   

transform transform_room:
    xalign 0.5
    yalign 0.5
    #xzoom 0.5
    #yzoom 0.5       

init python:
    import copy

    NEUTRAL = 'NEUTRAL'
    GOOD = 'GOOD'
    BAD = 'BAD'

    relationship_imgs = {
        NEUTRAL: 'neutral.png',
        GOOD: 'good.png',
        BAD: 'bad.png'
    }

    class Relationship:

        def __init__(self, person, start_value=0, min_value=-2, max_value=2, character=None):
            self.person = person
            self.level = NEUTRAL
            self.min_value=min_value
            self.max_value=max_value
            self.character = character
            self.value=start_value
            self.observers = []
        
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if value >= self.min_value and value <= self.max_value:
                self._value = value
                self._change_level()

        def change(self, add_value):
            new_value = self.value + add_value
            self.value = new_value

        def notify(self, old_level, new_level):
            for observer in self.observers:
                observer.react(old_level, new_level)

        def up(self, number=1):
            old = copy.deepcopy(self)
            for i in range(number):
                self._up()
            self.notify(old, self)

        def _up(self):    
            self.value += 1
            self._change_level()

        def down(self, number=1):
            old = copy.deepcopy(self)
            if number:
                for i in range(number):
                    self._down()
            self.notify(old, self)

        def _down(self):
            self.value -= 1
            self._change_level()


        def _change_level(self):
            if self.value == 0:
                self.level = NEUTRAL
            elif self.value == self.max_value:
                self.level = GOOD
            elif self.value == self.min_value:
                self.level = BAD

        def __str__(self) -> str:
            return f'{self.person} - {self.level} - {self.value}'

    LIFE_IMG = 'life.png'
    MIND_IMG = 'mind.png'
    KIND_IMG = 'kind.png'
    MONEY_IMG = 'money.png'

    LIFE_IMG_MENU = 'lifesmall.png'
    MIND_IMG_MENU = 'mindsmall.png'
    KIND_IMG_MENU = 'kindsmall.png'
    MONEY_IMG_MENU = 'moneysmall.png'
  

    MAX_LIFE = 3
    
    class Characteristic:

        def __init__(self, name, desctiption, value, max_value=None, min_value=0, image=None):
            self.name = name
            self.description = desctiption
            self._value = value
            self.max_value = max_value
            self.min_value = min_value
            self.image = image

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if value < self.min_value:
                return
            if self.max_value and value > self.max_value:
                return
            self._value = value

        def __str__(self):
            return f'{self.name} {self.value}'

        def __ne__(self, other):
            return self._value != other._value

    class Hero:

        def __init__(self, character=None, life=MAX_LIFE, mind=0, kind=0, money=0):
            self.character=character
            self.life = Characteristic('life', 'жизнь', life, max_value=MAX_LIFE, min_value=0, image=LIFE_IMG)
            self.mind = Characteristic('mind', 'ум', mind, min_value=0, image=MIND_IMG)
            self.kind = Characteristic('kind', 'доброта', kind, min_value=0, image=KIND_IMG)
            self.money = Characteristic('money', 'монета', money, min_value=0, image=MONEY_IMG)
            self.observers = []

        def get(self, name):
            return getattr(self, name).value

        def __str__(self) -> str:
            return f'{self.life} {self.mind} {self.kind} {self.money}'

        def notify(self, old, new, kwargs):
            for observer in self.observers:
                observer.react(old, new, kwargs)

        def change(self, **kwargs):
            old = copy.deepcopy(self)
            for k,v in kwargs.items():
                characteristic = getattr(self, k)
                characteristic.value += v
            for observer in self.observers:
                self.notify(old, self, kwargs)

    class Notyfier:

        def react(self, old, new, kwargs):
            messages = []
            # Идем по тому что изменилось
            for k,v in kwargs.items():
                old_characteristic = getattr(old, k)
                new_characteristic = getattr(new, k)
                # Если характеристика поменялась
                if old_characteristic != new_characteristic:
                    # Уведомляем об этом
                    sign = '+' if v >=0 else '-'
                    new_message = f'{sign} {abs(v)} {old_characteristic.description} {{image={old_characteristic.image}}}'
                    messages.append(new_message)
                else:
                    # Было изменение но характеристика не поменялась (она может достигнуть максимума или минимума)
                    # Если достигнуто максимальное значение
                    if new_characteristic.value == new_characteristic.max_value:
                        messages.append(f'у вас уже максимум {new_characteristic.description} {{image={new_characteristic.image}}}')
            result_message = '\n'.join(messages)
            renpy.notify(result_message)

    class GetMoney:

        MONEY = 'money'

        def react(self, old, new, kwargs):
            if GetMoney.MONEY in kwargs:
                if kwargs[GetMoney.MONEY] > 0:
                    renpy.play('audio/money.mp3')

    class Death:

        def react(self, old, new, kwargs):
            if new.life.value == 0:
                renpy.jump('end_game')

    class RelationshipNotifier:

        def react(self, old, new):
            if new.level != old.level:
                # изменился статус
                message = f'Отношения с {new.person} изменились {{image={relationship_imgs[new.level]}}}'
            else:
                rel_diff = new.value - old.value
                if rel_diff == 0:
                    if new.value > 0:
                        sign = 'лучше'
                    else:
                        sign = 'хуже'
                else:
                    sign = 'лучше' if rel_diff > 0 else 'хуже'
                message = f'Отношения с {new.person} стали {sign}'
            renpy.show_screen("rnotify", message)

    def say_emotionally(relationship, message):
        emotionall_message = f'{{image={relationship_imgs[relationship.level]}}} {message}'
        renpy.say(relationship.character, emotionall_message)

# Игра начинается здесь:
label start:
    $ is_with_swimm= False
    # Отключение возврата по колесику
    $ config.rollback_enabled = False
    $ travel_skills_good= False
    # Характеристики
    $ h = Hero(p)
    $ notifier = Notyfier()
    $ h.observers.append(notifier)
    $ death = Death()
    $ h.observers.append(death)
    $ get_money = GetMoney()
    $ h.observers.append(get_money)
    # Отношения
    # Дарина
    $ dr = Relationship('Дариной', character=d)
    $ rn = RelationshipNotifier()
    $ dr.observers.append(rn)
    # Кирилл
    $ kr = Relationship('Кириллом', character=k)
    $ kr.observers.append(rn)

    $ is_use_timer = False

    hide screen lose_game
    show screen characteristics_mini
    $ darina_relationship_index = 0
    $ darina_relationship = "Neutral"

    # Тестовый режим DEBUG = True
    $ DEBUG =False
    
    if DEBUG:
        # Включение возврата по колесику
        $ config.rollback_enabled = True
        # Параметры тестового режима
        # Можно задать любые характеристики
        $ h.change(kind=999, mind=999, money=999)
        # Тестовые имена
        $ player_name = 'Polly'
        $ parrot_name = 'Popka'
        $ vr = Relationship(parrot_name)
        $ vr.observers.append(rn)
        # Доп переменные
        $ is_with_us_chameleon = True
        # К КАКОЙ МЕТКЕ ХОТИМ ПЕРЕЙТИ
        jump  bus
    

label start_game:

    jump bus
