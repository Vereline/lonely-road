label act_0_street:

    scene bg_street_rainy:
        zoom 0.68

    "It’s raining hard."
    "Big raindrops crash asphalt and nail dust, which was flying in the air, to the ground."
    "Low two-storey houses, colored in some sort of grey color, are standing around me."
    "On each window of the houses shutters were attached, which now, during the rain, were securely closed with the hecks."
    "There is no soul in the street. I’m going through the street and I can’t understand how did I appear here? I’ve gone somewhere, but where -I don’t remember."  
    " . . ."
    "Pigeons are hiding under the peak of the one close and unremarkable bar in order to be saved from heavy rain."
    "Letters on the bar sign lost their colours and became almost invisible, but if you look attentively, you’ll see a bar name: \“Lonely road\”. "
    "Hmpf… it’s worth to visit this place. Anyway, I’ve got no umbrella and I don’t want to soak and catch cold after the rain."  
    " . . ."
    
    hide screen bg_street_rainy
    jump act_1

label act_4_street:
    
    scene bg_street:
        zoom 0.68

    "It's still raining outside, though not as strong as before."
    "Directly at the entrance to the bar there are two police cars, they put me in one of them. "
    "Slamming the car door, the police quickly began to assemble and get into the car."
    "There was only one of them left on the porch, elderly, with a notebook in his hands, and talked leisurely to the girl."
    "She no longer waved her hands and did not throw out hundreds of phrases by one stream, but simply stood with an unflappable air, leaning against the door jamb and responding monosyllabically to the interlocutor's questions, and answered as if she were not the first time:"

    kira "{b}Yes …{/b}"

    policeman "{b}...{/b}"

    kira "{b}Yes …{/b}"

    policeman "{b}...{/b}"

    kira "{b}Yeah, that’s him...{/b}"

    "The police car started off and took me to the darkness…"
    
    hide screen bg_street
    jump end_game
