label act_1_bar:

    scene bg_bar:
        zoom 0.68

    "So, it’s not so bad inside, but there is nobody."
    "There are staying several round and shabby wooden tables, ragged to shine."
    "In the far corner, somewhere in the dark an old, but still working jukebox is playing. It flashes with its survived light bulbs and calls to push a small coin into it to enjoy the jazz."
    "A half-asleep bartender stands behind the bar and, apparently, blanches by inertia already clean and shiny stand."
    "Nearby hangs an old tv, telling some news of the week. Behind the bartender, on shelves, there are placed already opened and half emptied different drinks."
    "Somewhere far away plays calm and quiet music, obviously inviting guests to stay, sit down and take one more glass of something strong and warming." 

    me "{b}Good evening, a glass of dark, please.{/b}" 

    "The bartender watches at me sullenly, then quickly hides under the rack. A minute later he raises with a big glass, filled up to the edges." 

    bartender "{b}It’s 4.50{/b}" 

    "I’m sitting and tasting the contents of the glass. On the first view, nothing remarkable, but after a moment a strong heat is spilling through the body." 
    ". . ."
    "I’m sitting and thinking about something, something far. Suddenly, I hear:"

    bartender "{b}So, how’s the weather? Is it raining hard?{/b}"

    menu is_it_raining:
        "{b}Well, yea, it’s raining hard.{/b}":
            me "{b}Well, yea, it’s raining hard.{/b}"
            bartender "{b}Heck, the weather is a strange thing. Today the forecast promised neither the clouds here, but in real…{/b}"
        "{b}. . .{/b}":
            me "{b}. . .{/b}"
            "The bartender looked at me, waiting for me to answer something. However, he didn’t get any response, quickly turned around and started switching tv channels." 

    "Switched all available tv channels and didn’t find anything interesting, the bartender again contacted me:"
    bartender "{b}Look, rumours go, so go. They say, that the girl was found at the railroad, she was totally cut, that’s awkward. As you remember, you shudder, such a spectacle is not given to everyone… Sincerely speaking, I didn’t see it. Did you hear that?{/b}"
    me "{b}Well, nope, I hear this thing the first time. What else do people say?{/b}"
    bartender "{b}As far as I know, they look for the murderer, but they can’t find him. Well, we live in a small town, where everyone knows each other in person. That means this murderer is one of us?{/b}"
    me "{b}That’s the point.{/b}" 

    jump act_2

label act_2_bar:
    "So, I was sitting and thinking for a long time, as suddenly I was abruptly woke up by a knock on the door."
    "The girl entered the bar, she was completely wet, out of breath and terribly dissatisfied with something."
    "She quickly ran to the rack, climbed on a high chair and flopped on it, sighing with relief."
    "The girl was wearing a black coat, under which a red Scottish skirt and white shirt were seen, a shirt was soaked through and adhered to the body."
    "At the feet of the girl were already greyed cause of rain and dirt somewhen white knee-highs and black shoes looked similar to school boots of first-formers."
    # ". . ."
    "On the next chair, stranger put her small bag, from which water streamed down, and then hang on it her coat, which would be nice to be squeezed."
    "After sitting for a minute, the girl finally applied to the bartender:"

    show kira_dafault:
        xalign 0.5 yalign 1 xzoom 0.3 yzoom 0.3 ypos 0.2

    kira "{b}Would you give me a cup of hot tea?{/b}"

    "The bartender came to her and silently poured a cup of hot tea and put obligatory free small chocolate bar near the cup."
    "The girl instantly took a hot drink, put a cup and closed eyes, thinking about something."
    ". . ."
    "We were sitting for about half an hour this way. Suddenly she opened her eyes, turned her head to me and said:"  

    kira "{b}Oh, hi! What a strange weather today!{/b}"

    "Then she looked me around and asked unexpectedly:" 

    kira "{b}Is it such interesting to watch me?{/b}"   

    "I choked with surprise."
    "Only now I noticed that all this time I stared at her."
    "I felt slightly uncomfortable.  I was already turning away the other way, as I heard:"
    
    kira "{b}And this place seems to be soooo… interesting. By the way, my name is Kira.{/b}"

    $ Kira_name = _('Kira')

    python:
        name_question = _("What is your name?")
        me = renpy.input(name_question)
        me = me.strip()

        if not me:
                me = _("Me")

    "I introduced myself."

    kira "{b}Nice to meet you!{/b}"

    me "{b}And you.{/b}"

    kira "{b}How do you do?{/b}"

    menu how_do_you_do:
        "{b}Fine.{/b}":
            me "{b}Fine.{/b}"
            kira "{b}Well, fine means fine, what else can I say?{/b}"
        
        "{b}Well, I’m not bad, just trying to live here.{/b}":
            me "{b}Well, I’m not bad, just trying to live here.{/b}"
            kira "{b}Hehe, not bad, not bad, life just slowly flows in this town, and we’re trying not to get behind it.{/b}" 

        "{b}It can’t be worse.{/b}":
            me "{b}It can’t be worse.{/b}"
            kira "{b}Well, it worth to look for something good in every terrible situation, you don’t have to depress yourself.{/b}" 

    "Kira drank one more sip of tea and unpacked a small chocolate bar."
    "She got from skirts’ pocket small Swedish pen knife and skillfully shared sweet treat into two pieces."

    kira "{b}Treat yourself!{/b}"

    "My eyes stared at her penknife. It’s so small and comfortable, I bet on anything, it can be carried everywhere without fail, so it is invisible."
    "Kira hid her small knife in pocket, and I mechanically, looking at her, shove hand in the pants pocket."
    "I feel something cold and metallic. Is it really also a knife?"
    "It was so rusty, slippery and unpleasant, that I instantly pulled my hand and put in on the bar counter."
    "My forehead just sweated. It’s strange, what’s wrong with me? {b} What’s in the pocket?{/b}"

    "It did not hide from Kira."
    "She quickly looked me around again and thought about something."
    "Apparently, having decided to distract me a little and fill an embarrassing silence, she began to talk:"

    kira "{b}Uh, well, your rail is extremely noisy and super loud!{/b}"

    "I listened to the noise outside and heard the tapping of the electric train's wheels and the creaking of old trains on the railway which is nearby."
    
    me "{b}Well, yes, there is. In general, the railway is the only place, which is at least something interesting in this old boring town.{/b}"
    
    kira "{b}Hey, I’m pretty sure, that there are lots of remarkable places! Here, when I ran past old square, I noticed by the eye park with a fountain. I’m thinking about visiting that place when the rain stops.{/b}"
    
    "{i}I sharply scored a shiver. Some images surfaced in my head, there were images of the ugly old forest, overgrown paths, old fountain, which hardly released jets of dark-green stinking water, a small girl, running home across the park.{/i}"
    "{i}I’m sitting on the bench and thinking about something…No matter, about what.{/i}"
    
    kira "{b}Hey! Are you alright?{/b}"

    me "{b}Yeah, I’m fine, just thinking.{/b}"

    kira "{b}Well, okay. And in general, this town is not so boring, as you think, I’m sure, it has a life!{/b}"

    "Her expression started to annoy me."
    "My new companion opened a recent newspaper and being stared somewhere on the page, asked me:"
    
    kira "{b}I came to this town quite recently. How is life, what is happening in the town?{/b}"

    me "{b}Well, nothing special, our town is small, and nothing happens.{/b}"

    kira "{b}Haven’t you read about the murder of a girl on the railway tracks?{/b}"

    me "{b}And there is nothing interesting, well, you think, somebody threw the body on the way.{/b}"

    "{i}I didn’t read any newspapers, of course, so I just announced some rumours that she would leave me alone.{/i}"

    kira "{b}Wow, wow, but this doesn’t happen every day! And, as in real detectives, there were no witnesses?{/b}"
    
    me "{b}It seems to be something like that.{/b}"

    kira "{b}Is the murderer already found?{/b}"

    me "{b}Definitely no, if police had found that guy, they would have written about this in the newspaper.{/b}"

    kira "{b}Oh no, you shouldn’t have said it, now I'm afraid to go out!{/b}"

    "The girl was expressive, talked a lot and quickly and gesticulated actively. What a chatterbox!"

    kira "{b}What else can you tell me, I am so interested!{/b}"

    me "{b}… Emmm, what?{/b}"

    kira "{b}What’s her name?{/b}"

    me "{b}I don’t know.{/b}"

    kira "{b}Oh, don’t you know, whether she was a pupil or not?{/b}"

    me "{b}I don’t know!{/b}"

    kira "{b}And in which class was she studying? How old was she?{/b}"

    me "{b}The hell I know!{/b}"

    kira "{b}Hmm, well, okay. I wouldn’t like to know too much, anyway.{/b}"

    "Kira defiantly turned away, puffed out her cheeks like a hamster, and began to look at the ceiling with displeasure."

    "{i}. . .{/i}"
    "{i}...The girl ran to the fountain and lowered tempo. Then she simply walked, restoring breathing.{/i}"
    "{i}Tears are flowing down her cheeks, her brows have frowned, his lips are compressed, her cheeks are inflated and her hands are clenched into fists, and behind her back is a new red rucksack, for some reason diligently piled in the mud.{/i}"
    "{i}Now I see, why she was disappointed…{/i}"

    kira "{b}Can you imagine, whom did I meet today? Your mayor! As I know, he is a hidden person, he does not get out almost from home.  And today he took it and went out. He gave a lot of interviews, talked with the people ...{/b}"
    kira "{b}...{/b}"
    
    "I began to yawn, tired of her chatter, and put my hands in my pockets, so as not to fall asleep."

    kira "{b}...{/b}"
    kira "{b}… because the police must look for a criminal, but not to look through their homes and ask who has any plans…{/b}"
    kira "{b}...{/b}"
    
    "Only snatches of her phrases reached me, I had long ceased to listen and perceive her monologue."
    
    kira "{b}...{/b}"
    kira "{b}… but the taxes that you pay go to them for equipment, and they don’t use it, still walking by hand...{/b}"
    kira "{b}...{/b}"
    kira "{b}… and one of them has a funny doggie called Chappi, he’s a good neighbour, however…{/b}"
    kira "{b}...{/b}"

    "She kept talking and talking."

    kira "{b}...{/b}"
    kira "{b}So where did you say?{/b}"

    "I cheered up."

    me "{b}What where?{/b}"

    kira "{b}Hey, aren’t you listening to me?{/b}"

    me "{b}Eeeem, I was listening, of course, just thinking. Tell me one more time, what did you asked me about?{/b}"

    kira "{b}Where was the girl killed?{/b}"

    "The sharp question knocked me out of the rut. So what's rumoured to be said? I Need to come up with something..."

    me "{b}…{/b}"

    kira "{b}So?{/b}"

    menu location_of_nurderer:
        "{b}On the river coast.{/b}":
            pass
        "{b}In the forest.{/b}":
            pass
        "{b}In the abandoned warehouse.{/b}":
            pass
        "{b}At the railway station.{/b}":
            pass
        "{b}Somewhere in the doorway.{/b}":
            pass

    kira "{b}Come on, don’t be silly! You may see by yourself, that that’s not logical. But where?{/b}"

    "Something clicked in my head."

    "{i}...The girl, passing the fountain, walked less and less confidently.{/i}"
    "{i}It seems that she’s going to cry right now. Seeing me, the girl ran up and asked something about napkins.{/i}"
    "{i}And I’m sitting on the bench and thinking about something… It doesn’t matter, about what, or does it matter? Although...{/i}"

    me "{b}In the park, on the central avenue, behind the extreme right bench.{/b}"

    kira "{b}Aааааа, so that's it! Logical, logical, and most importantly, how well it converges!{/b}"
    kira "{b}Just one more thing... How did you know that? The newspaper does not say this!{/b}"

    "I strained."

    me "{b}Err... Ummm... the rumours are here{/b}"

    kira "{b}Rumours? What kind of rumours?{/b}"
    
    me "{b}Well, I heard it.{/b}"

    "But I didn’t want to say anything. The girl tested me with a look, obviously having bitten me. I obviously blurted out too much."

    kira "{b}What are you talking about?)){/b}"

    me "{b}Well, girl, stop annoying me!{/b}"

    "Suddenly she moved closer to me and screamed sharply:"

    kira "{b}FREEZE!{/b}"

    "I jumped in surprise on the chair and sharply took my hands out of my pockets."
    "These sharp movements were enough to make a small penknife fall from the pockets of my trousers, already blunt and stained with dried blood."

    kira "{b}Now the puzzle is done.{/b}"

    jump act_3

label act_3_bar:
    
    "She beckoned to someone outside the window, and four policemen ran into the bar at once, surrounded, cuffed and bent to the table."

    kira "{b}Yeah, that's the criminal got caught. I immediately realized that it was you: well, the picture is obvious: the girl is on the road, with a knife.{/b}"
    kira "{b}Agree, I have a great talk! This is my personal reception, never with someone like you, did not give a misfire, when a person is still in prostration after a crime, it's easiest to bring it out in clean water exactly!{/b}"

    kira "{b}Because there were no newspapers, and there were no rumours. Here, look! A doll!{/b}"

    "She launched a newspaper and showed me an internal turn. There were only absolutely clean, but wet sheets."

    kira "{b}The girl was found just an hour ago! Well, the picture is obvious: the girl is on the road, with knife injuries…{/b}"

    "Kira examined me once more. Now a new, gleeful look. I do not know how to describe it, but I began to be afraid of it, really afraid."    

    kira "{b}Hey, only you remember that I recorded everything, you see?{/b}"

    "The girl took up her coat and turned her briefcase to me with the other side. From a small pocket, securely hidden from my eyes, protruded a portable recorder."

    kira "{b}Well, Alex, bored? How long did we chat here?{/b}"

    bartender "{b}Oh, nothing, nothing, I already thought that you would not break him down. I've lost the twenty, however!{/b}"

    kira "{b}Ah, yes, I completely forgot, meet this guy - it's Alex, our man. He just threw you a couple of rumours and prepared for our conversation, so to speak.{/b}"

    "She came to the chair, on which I had sat, bent down under the bar and, a little fumbling in the dark, took out my old penknife."

    kira "{b}And here’s a knife! Look, there is blood on it!{/b}"
    kira "{b}Ugh, what a good thing. This Swiss knife, rusted a little, though, but it looks really good. Get him, guys.{/b}"  

    jump act_4
