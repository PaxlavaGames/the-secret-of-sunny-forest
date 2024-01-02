label end_story:

      show bg sea sun

      "Сложно было поверить, что [parrot_name] может говорить так рассудительно, и что он не выдумал всю эту историю"

      "Но в воздухе уже повеяло невероятной тайной..."
    
      show polly smile swimsuit right at right
       
      hide  polly st swimsuit right at right
      hide darina st swimsuit at left
      hide popka at center 
      #show bg autors
      show bg fon mistake
      play music going
      menu:
            "Конец 1-ой части":
                  jump credits

label credits:
      show paintinig shadow at left with zoomin:
            yalign 0.5 xalign 0.2
      "{color=#dcc600}Design{/color}, {color=#00d3eb}Game Design{/color}, {color=#00ff00}Narrative Design{/color} - {b}Polina{/b}"
      show comp shadow at right with squares:
            yalign 0.5 xalign 0.8
      "{color=#ff00ff}Development{/color}, {color=#00f7ff}Sound{/color} - {b}Leonid (Random Coder){/b}"
      
      "{color=#00f7ff}Звук и музыка{/color} - {a=https://freesound.org/}freesound.org{/a} и Wondershare Filmora 11"
      # "Wondershare Filmora 11"
      show paintinig shadow at left with move:
            yalign 0.5
      show comp shadow at right with move:
            yalign 0.5
      show popka new at truecenter with vpunch
      "Производство {b}{color=#00f7ff}Random Coder{/color}{/b}"
      "До новых встреч!"

      hide paintinig shadow at left 
      hide comp shadow at right 
      hide popka new at truecenter 

      menu:
            "Играть снова":
                  jump start
            "Выход":
                  return