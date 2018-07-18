label act_1_bar:
    "А внутри он совсем ничего, правда, и здесь никого нет."
    "В подвальном помещении стоят несколько круглых деревянных столиков, обшарпанных и потрепанных временем, затертых тряпками до блеска."
    "В дальнем конце помещения, где-то в темноте стоит старый, но все еще рабочий музыкальный автомат. Он мигает своими уцелевшими лампочками и зовёт опустить в него монетку и насладиться джазом."
    "За барной стойкой стоит полусонный бармен, уже, видимо, по инерции протирающий до блеска и без того чистую и блестящую стойку."
    "Рядом висит на подставке старенький телевизор, вещающий что-то о новостях за неделю. За барменом на полках стоят уже открытые и опустошенные наполовину различные напитки."
    "Где-то вдалеке играет тихая и спокойная музыка, явно приглашая гостей задержаться, посидеть и пропустить еще стакашку чего-нибудь крепкого и согревающего." 

    me "{b}Добрый день, мне стакашку тёмного.{/b}" 

    "Бармен смотрит на меня исподлобья, затем быстро прячется  за стойку. Спустя минуту поднимается  уже с большим бокалом, наполненным до краев." 

    bartender "{b}С вас 4.50.{/b}" 

    "Я сижу и пробую на вкус содержимое бокала. На первый взгляд, ничего примечательного, однако спустя мгновение по телу разливается тепло." 
    ". . ."
    "Я сижу и думаю о чем-то, о чем-то далеком. Вдруг слышу:"

    bartender "{b}Ну что, как погодка? Сильный дождь?{/b}"

    menu is_it_raining:
        "{b}Да так, льёт ещё.{/b}":
            me "{b}Да так, льёт ещё.{/b}"
            bartender "{b}А ведь погода, все-таки, штука странная. Сегодня по прогнозу ни облачка, а на деле…{/b}"
        "{b}. . .{/b}":
            me "{b}. . .{/b}"
            "Бармен посмотрел на меня, будто хотел что-то услышать, однако, так и не получив ответа, быстро отвернулся и стал щёлкать каналы по телевизору." 

    "Прощелкав все каналы и не найдя ничего интересного, бармен снова обратился ко мне:"
    bartender "{b}От, слухи ходят, так ходят. Поговаривают, девочку нашли, на путях, всю порезанную, аж жуть… Как вспомнишь, так вздрогнешь, такое зрелище не каждому дано выдержать… Я вот не видел, правда… А ты слыхал?{/b}"
    me "{b}Да нет, впервые слышу. А что ещё говорят?{/b}"
    bartender "{b}Да вот, убийцу ищут, все никак не найдут. А у нас городок маленький, все знают друг друга в лицо. Значит, этот убийца - один из нас?{/b}"
    me "{b}Это точно.{/b}" 

    jump act_2

label act_2_bar:
    "Я так сижу долго и все думаю, как меня вдруг резко разбудил стук двери."
    "В бар зашла девушка, вся мокрая, запыхавшаяся от бега  и чем-то жутко недовольная."
    "Она быстро подбежала к стойке, вскарабкалась на высокий стул и плюхнулась, вздохнув с облегчением."
    "Девушка была одета в черное пальто, под которым виднелись красная юбка-шотландка и белая рубашка, промокшая насквозь и прилипшая к телу."
    "На ногах у девушки были уже посеревшие от дождя и грязи некогда белые гольфы и черные туфли, похожие на школьные ботиночки первоклашек."
    # ". . ."
    "На соседний стул незнакомка поставила свой маленький портфельчик, с которого ручьями стекала вода, а затем навесила на него своё пальто, которое было бы неплохо выжать."
    "Посидев с минуту, девушка наконец обратилась к бармену:"

    show kira_dafault:
        xalign 0.5 yalign 1 xzoom 0.3 yzoom 0.3

    kira "{b}Мне бы чаю горячего.{/b}"

    "Бармен подошел и без слов налил чашку горячего чая, приложив рядом полагающуюся бесплатную маленькую шоколадку."
    "Девушка мигом отпила горячий напиток, поставила кружку и прикрыла глаза, явно о чем-то думая."
    ". . ."
    "Так мы сидели около получаса. Наконец она открыла глаза, повернула ко мне голову и сказала:"  

    kira "{b}Привет! Ну и погодка сегодня!{/b}"

    "Потом обвела меня взглядом и неожиданно спросила:" 

    kira "{b}Неужели за мной так интересно наблюдать?{/b}"   

    "Я поперхнулся от удивления."
    "Только сейчас заметил, что все это время пристально наблюдал за ней."
    "Мне стало слегка неловко. Я было уже начал отворачиваться в другую сторону, как услышал:"
    
    kira "{b}А ведь это местечко ничего такое, интересненькое. Кстати, меня Кира зовут.{/b}"

    $ Kira_name = 'Kira'

    python:
        name_question = "What is your name?"
        me = renpy.input(name_question)
        me = me.strip()

        if not me:
                me = "Me"

    kira "{b}Приятно познакомиться!{/b}"

    me "{b}Взаимно.{/b}"

    kira "{b}Как жизнь?{/b}"

    menu how_do_you_do:
        "{b}Норм.{/b}":
            me "{b}Норм.{/b}"
            kira "{b}Ну, норм, так норм, чего сказать тут ещё?{/b}"
        
        "{b}Да ничего, перебиваюсь потихоньку.{/b}":
            me "{b}Да ничего, перебиваюсь потихоньку.{/b}"
            kira "{b}Хехе, неплохо, неплохо, жизнь медленно течет в этом городке, и мы стараемся не отставать от неё.{/b}" 

        "{b}Все плохо.{/b}":
            me "{b}Все плохо.{/b}"
            kira "{b}Нууууу, всегда в самой плохой ситуации надо находить что-то хорошее, не стоит так себя угнетать.{/b}" 

    "Кира отхлебнула еще глоток чая и распаковала шоколадку."
    "Достав из кармана юбки маленький перочинный ножик, она ловко разделила сладкое угощение на две части."

    kira "{b}Угощайся!{/b}"

    "Мои глаза пристально наблюдали за перочинным ножиком. Он такой маленький и удобный, спорю на что угодно, его можно везде запросто пронести, настолько он незаметен."
    "Кира спрятала свой ножичек в карман, а я машинально, глядя на нее, засунул свою руку в карман брюк."
    "Нащупываю что-то холодное, металлическое. Неужели тоже ножик?"
    "Это нечто было настолько ржавым, скользким и неприятным, что я немедленно одернул руку и положил ее на барную стойку."
    "На лбу проступил пот. Странно, что это со мной? {b}Что в кармане?{/b}"

    "От Киры это не укрылось."
    "Она быстро обвела меня взглядом и о чем-то призадумалась."
    "Видимо, решив немного меня отвлечь и заполнить неловкое молчание, она начала говорить:"

    kira "{b}Ух, ну и железка у вас, такая шумная, такая громкая!{/b}"

    "Я прислушался к шуму снаружи и услышал постукивание колес электропоезда и скрип старых составов на железной дороге, что неподалёку."
    
    me "{b}Ну да, есть такое. Вообще, железная дорога - это единственное место, которое хоть чем-то интересно в этом старом скучном городе.{/b}"
    
    kira "{b}Хм, я уверена, что есть ещё замечательные места! Вот, когда бежала мимо, краем глаза заприметила парк с фонтаном. Надо бы наведаться туда, когда дождь кончится.{/b}"
    
    "{i}Меня резко забила дрожь. В голове всплыли образы старого леса, заросших тропинок, старого фонтана, который едва-едва выпускает струйки мутно-зеленой вонючей воды, маленькая девочка, бегущая домой по парку наперерез.{/i}"
    "{i}Я сижу на лавочке и думаю о чем-то… Неважно, о чем. {/i}"
    
    kira "{b}Эй, ты окей?{/b}"

    me "{b}Да, все в порядке, просто задумался.{/b}"

    kira "{b}Ну, тогда ладно. Да и вообще, не такой уже и скучный город, я уверена, в нем есть жизнь!{/b}"

    "Ее экспрессия начинает мне надоедать."
    "Моя новая собеседница открыла свежий номер газеты и, уставившись куда-то на странице, спросила:"
    
    kira "{b}Я в этом городе совсем недавно. Как жизнь, что в городе происходит?{/b}"

    me "{b}Да так, ничего особенного, городок маленький, ничего и не происходит.{/b}"

    kira "{b}А разве ты не читал про убийство некой девочки на железнодорожных путях?{/b}"

    me "{b}Да и там ничего интересного, ну, подумаешь, подкинули труп на пути.{/b}"

    "{i}Никаких газет,  я, разумеется, не читал, лишь так, озвучил слухи, чтобы она от меня отстала.{/i}"

    kira "{b}Ух ты, ничего себе, а ведь такое не каждый день происходит! И, что, как в настоящих детективах, и свидетелей не нашлось?{/b}"
    
    me "{b}Да что-то типа того.{/b}"

    kira "{b}И убийцу уже нашли?{/b}"

    me "{b}Да нет ещё, если бы нашли, то написали бы.{/b}"

    kira "{b}О боже, зря ты это сказал, теперь мне страшно выходить на улицу!{/b}"

    "Девушка была экспрессивная, много и быстро болтала и ещё активно жестикулировала. Ну и болтунья!"

    kira "{b}А ещё что расскажешь? Мне так интересно!{/b}"

    me "{b}… Ээээ, а что?{/b}"

    kira "{b}А как девочку зовут?{/b}"

    me "{b}Не знаю.{/b}"

    kira "{b}О, а она школьница была, знаешь?{/b}"

    me "{b}Не знаю.{/b}"

    kira "{b}А в каком классе она учится? А сколько ей лет?{/b}"

    me "{b}Да не знаю я!{/b}"

    kira "{b}Хм, ну и ладно. Больно и хотелось узнать.{/b}"

    "Кира демонстративно отвернулась, надула щеки, как у хомяка, и стала недовольно смотреть в потолок."

    "{i}. . .{/i}"
    "{i}...Девочка подбежала к фонтану и сбавила темп. Дальше она просто шла, восстанавливая дыхание.{/i}"
    "{i}По щекам текут слезы, брови нахмурены, губы сжаты, щеки надуты  и ручки сжаты в кулачки, а за спиной новый красный рюкзачок, почему-то старательно вывалянный в грязи.{/i}"
    "{i}Теперь я понимаю, почему она шла недовольная...{/i}"

    kira "{b}А вот представляешь, кого я сегодня увидела! Вашего мэра! Как мне известно, он личность скрытая, из дому не выходит почти.  А сегодня вот взял и вышел. Раздал множество интервью, пообщался с народом…{/b}"
    kira "{b}...{/b}"
    
    "Я стал потихоньку зевать, уставая от ее болтовни, и засунул руки в карманы, чтобы не завалиться в сон."

    kira "{b}...{/b}"
    kira "{b}… ведь полиция обязана искать преступника, а не шастать по домам и расспрашивать, у кого какие планы…{/b}"
    kira "{b}...{/b}"
    
    "До меня доходили только обрывки ее фраз, я уже давно перестал слушать и воспринимать ее монолог."
    
    kira "{b}...{/b}"
    kira "{b}…а ведь налоги, которые вы платите, уходят им на оборудование, а они и не пользуются, все ходят вручную...{/b}"
    kira "{b}...{/b}"
    kira "{b}…а у одного из них есть забавный песель по кличке Чаппи, хороший сосед, однако…{/b}"
    kira "{b}...{/b}"

    "Она все говорила и говорила."

    kira "{b}Так  где, говоришь?{/b}"

    "Я встрепенулся."

    me "{b}Что где?{/b}"

    kira "{b}Эй, ты что, меня не слушаешь?{/b}"

    me "{b}Эээээ, да я все слушал, слушал, просто думаю. Скажи ещё раз, о чем ты спросила?{/b}"

    kira "{b}Где же убили девочку?{/b}"

    "Резкий вопрос выбил меня из колеи. Так что там по слухам говорили? Надо что-то придумать..."

    me "{b}…{/b}"

    kira "{b}Ну?{/b}"

    menu location_of_nurderer:
        "{b}На берегу реки.{/b}":
            pass
        "{b}В лесу.{/b}":
            pass
        "{b}На заброшенном складе.{/b}":
            pass
        "{b}На железнодорожных путях.{/b}":
            pass
        "{b}Где-то в подворотне.{/b}":
            pass

    kira "{b}Да ладно, не дури! Сам понимаешь, что это не логично. Но где?{/b}"

    "Что-то щелкнуло у меня в голове."

    "{i}...Девочка, минув фонтан, шла все менее и менее уверенно.{/i}"
    "{i}Кажется, она сейчас заплачет. Увидев меня, девочка подбежала и спросила что-то про салфетки.{/i}"
    "{i}А я все сижу на лавочке и думаю о чем-то… Неважно, о чем, или важно? Хотя... {/i}"

    me "{b}В парке, на центральной аллее, за крайней правой скамейкой.{/b}"

    kira "{b}Аааааа, так вот оно что! Логично, логично, а главное, как хорошо сходится!{/b}"
    kira "{b}Только это... откуда ты это знаешь? В газете про это не написано!{/b}"

    "Я напрягся."

    me "{b}Да так… Эмммм… Слухи тут ходят.{/b}"

    kira "{b}Слухи? Какие слухи?{/b}"
    
    me "{b}Да так, слышал.{/b}"

    "Но уже ничего говорить не хотелось. Девушка испытывала меня взглядом, явно раскусив меня. Я явно сболтнул лишнего."

    kira "{b}Да что ты говоришь?)){/b}"

    me "{b}Так, девушка, перестаньте меня нервировать!{/b}"

    "Вдруг она неожиданно придвинулась ко мне и резко закричала:"

    kira "{b}РУКИ ВВЕРХ!{/b}"

    "От неожиданности подскочил на стуле и резко вынул руки из карманов."
    "Этих резких движений было достаточно, чтобы из карманов штанов вывалился маленький перочинный ножик, уже тупой и с пятнами засохшей крови."

    kira "{b}Теперь паззл весь сложился.{/b}"

    jump act_3

label act_3_bar:
    
    "Она жестом поманила кого-то за окном, и в бар вбежали сразу четверо полицейских, окружили, нацепили наручники и пригнули к столу."

    kira "{b}Ага, вот и преступничек попался. Я сразу поняла, что это ты: уж больно хорошо картину преступления знаешь.{/b}"
    kira "{b}Согласись, я тебя здорово уболтала! Это мой личный приём, никогда с такими, как ты, осечек не давал, когда человек еще находится в прострации после преступления, его проще всего вывести на чистую воду именно так!{/b}"

    kira "{b}Ведь никаких газет не выходило, да и слухов не было. Вот, посмотри! Кукла!{/b}"

    "Она развернула газету и показала мне внутренний разворот. Там были только абсолютно чистые, но мокрые листы."

    kira "{b}Девочку-то нашли всего час назад! Ну и картина налицо: девочка на путях, с ножевыми…{/b}"

    "Кира еще раз осмотрела меня. Теперь новым, ликующим взглядом. Не знаю, как это описать, но я начал ее бояться, по-настоящему бояться."    

    kira "{b}Эй, только ты учти, что я все записала, видишь?{/b}"

    "Девушка взяла в руки пальто и повернула ко мне свой портфельчик другой стороной. Из маленького кармашка, надежно спрятанного от моих глаз, торчал портативный диктофон."

    kira "{b}Ну что, Алекс, заскучал? Долго мы тут болтали?{/b}"

    bartender "{b}Да ничего, ничего, я уже было подумал, что ты его не уломаешь. Проспорил двадцатку, однако!{/b}"

    kira "{b}Ах, да, совсем забыла, познакомься - это Алекс, свой человек. Как раз подкинул тебе пару слухов, подготовил к нашей беседе, так сказать.{/b}"

    "Она подошла к стулу, на котором я сидел, нагнулась под барную стойку и, немного пошарив в темноте, достала мой старый перочинный ножик."

    kira "{b}А вот и ножик! Смотрите, на нем кровь!{/b}"
    kira "{b}Ууу, какой хороший образец. Настоящий швейцарский ножик, проржавел немного, правда, но выглядит действительно неплохо. Сажайте его, ребятки.{/b}"  

    jump act_4
