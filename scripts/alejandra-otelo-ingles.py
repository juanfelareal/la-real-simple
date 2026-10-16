#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La traduccion al ingles de la landing de Alejandra Otelo.

Cada entrada es el texto en espanol tal como esta en la pagina y su version en
ingles. El script incrusta el diccionario en assets/alejandra-otelo.html, dentro
de un <script type="application/json" id="ingles">, y el JS de la pagina lo usa
para cambiar de idioma sin recargar.

Al cambiar un texto en espanol hay que cambiar tambien su llave aqui: el script
avisa de las llaves que ya no aparecen en la pagina.

    python3 scripts/alejandra-otelo-ingles.py
"""

# --------------------------------------------------------------- barra y hero
TEXTOS = {
"Alejandra Otelo — Ceremonias simbólicas de boda. Ir al inicio":
  "Alejandra Otelo — Symbolic wedding ceremonies. Back to top",
"Alejandra Otelo — Ceremonias simbólicas de boda":
  "Alejandra Otelo — Symbolic wedding ceremonies",
"La mirada": "The approach",
"Formación": "Background",
"Ceremonias": "Ceremonies",
"Cómo trabajo": "How I work",
"Voces": "Voices",
"Conversemos": "Let's talk",

"Una ceremonia que no podría pertenecerle a": "A ceremony that could belong to",
"nadie más": "no one else",
"Construyo cada ceremonia a partir de su historia, de sus vínculos y de lo que significa para ustedes decidir casarse. La escribo y la diseño desde cero.":
  "I build every ceremony out of your story, your bonds and what deciding to marry means to you. I write it and design it from scratch.",
"Conversemos sobre su boda": "Let's talk about your wedding",
"Primera asesoría conmigo, sin costo.": "Your first consultation with me is free.",

# ------------------------------------------------------------------ manifiesto
"Quizás ya saben que quieren una boda simbólica. O quizás simplemente saben que quieren una ceremonia distinta a la tradicional. No hace falta tener claro todavía qué hacer, qué decir o qué tradiciones quieren conservar.":
  "Maybe you already know you want a symbolic wedding. Or maybe you just know you want a ceremony that isn't the traditional one. You don't need to have worked out yet what to do, what to say or which traditions you want to keep.",
"Para mí, la pregunta importante es otra": "For me, the question that matters is a different one",
"¿Qué tendría que pasar para que ese momento represente algo verdadero para ustedes?":
  "What would have to happen for that moment to mean something true to you?",

# -------------------------------------------------------------------- partida
"Antes de escribir, necesito": "Before I write, I need to",
"conocerlos": "know you",
"Cuando converso con una pareja, quiero conocer su historia, pero también entender cómo es su relación, qué los une, qué admiran el uno del otro y qué han aprendido a construir juntos.":
  "When I sit down with a couple, I want to know their story, but also to understand what their relationship is like, what binds them, what they admire in one another and what they have learnt to build together.",
"Alejandra Otelo — Bucaramanga, Colombia": "Alejandra Otelo — Bucaramanga, Colombia",

# ------------------------------------------------------------------ para quien
"Escucho con atención, cuestiono y encuentro sentido en los detalles":
  "I listen closely, I question, and I find meaning in the details",
"Después viene una parte menos visible: ordenar lo que escuché, encontrar conexiones e interpretar lo que cada historia revela sobre su manera de amar.":
  "Then comes a less visible part: ordering what I heard, finding the connections, and interpreting what each story reveals about the way you love.",
"El arte también es una manera de contar su historia": "Art is another way of telling your story",
"Me interesa explorar materiales, técnicas artísticas y procesos hechos a mano para crear símbolos que representen algo verdadero de cada pareja. Me gusta pensar que esos objetos pueden encontrar un lugar en sus hogares y, con los años, seguir recordándoles lo que decidieron construir juntos.":
  "I like exploring materials, artistic techniques and hand-made processes to create symbols that stand for something true about each couple. I like to think those objects can find a place in your home and, years from now, go on reminding you of what you decided to build together.",
"Antes de conocerlos como pareja, quiero conocerlos como individuos":
  "Before I know you as a couple, I want to know you as individuals",
"Cada uno llega a la relación con su propia historia, sus experiencias, sus valores y su manera de entender el amor. Por eso, parte de mi proceso consiste en conversar con cada uno por separado. Me interesa conocer quiénes son individualmente para comprender mejor lo que han elegido construir juntos.":
  "Each of you comes to the relationship with your own story, your own experiences, your own values and your own way of understanding love. That's why part of my process is talking with each of you separately. I want to know who you are on your own, so I can better understand what you have chosen to build together.",
"No parto de una visión determinada": "I don't start from a fixed view",
"Para algunas parejas, Dios ocupa un lugar importante en su historia. Otras entienden la espiritualidad de otra manera, y algunas no se identifican con ninguna de esas creencias. Me interesa conocer cómo ven el mundo, en qué creen y qué sentido le dan al compromiso que están haciendo.":
  "For some couples God holds an important place in their story. Others understand spirituality differently, and some don't identify with any of those beliefs. I want to know how you see the world, what you believe, and what meaning you give to the commitment you are making.",
"Todo lo que sucede debe tener sentido": "Everything that happens has to mean something",
"Cada palabra, cada símbolo y cada momento de la ceremonia tiene una razón de ser. Me gusta preguntarme por qué hacemos las cosas y qué significan para quienes las viven. Así, lo que construimos juntos tiene una intención que va más allá de lo estético o de la costumbre.":
  "Every word, every symbol and every moment of the ceremony has a reason to be there. I like to ask myself why we do things and what they mean to the people living them. That way, what we build together carries an intention that goes beyond the aesthetic or the customary.",

# ------------------------------------------------------------------- formacion
"Mi manera de hacer este trabajo viene de lugares distintos":
  "My way of doing this work comes from different places",
"Filosofía, Derecho y Dirección de Arte.": "Philosophy, Law and Art Direction.",
"Soy filósofa y abogada de la Universidad de los Andes y cursé un Máster en Dirección de Arte en ELISAVA, Escuela de Diseño e Ingeniería de Barcelona. Con el tiempo entendí que las tres cosas estaban presentes en mi manera de construir una ceremonia. Esa mezcla terminó dándome una manera muy particular de trabajar: escuchar, interpretar, escribir y encontrar una forma para lo que cada pareja quiere expresar.":
  "I am a philosopher and a lawyer from Universidad de los Andes, and I hold a Master's in Art Direction from ELISAVA, the Barcelona School of Design and Engineering. Over time I realised all three were present in the way I build a ceremony. That mix ended up giving me a very particular way of working: listening, interpreting, writing, and finding a form for what each couple wants to express.",
"Filosofía": "Philosophy",
"Aparece en las preguntas y en la forma de pensar una unión.":
  "It shows in the questions, and in how I think about a union.",
"Derecho": "Law",
"Aparece en el rigor con el lenguaje y con la estructura.":
  "It shows in the rigour with language and structure.",
"Dirección de arte": "Art direction",
"Aparece cuando una idea necesita convertirse en un objeto, un gesto o una experiencia.":
  "It shows when an idea needs to become an object, a gesture or an experience.",

# ------------------------------------------------------------------ ceremonias
"La historia viene primero. El símbolo aparece": "The story comes first. The symbol comes",
"después": "after",
"No empiezo escogiendo un ritual. Primero necesito entender qué queremos expresar; después buscamos la forma que mejor pueda contener esa idea. A veces usamos un símbolo que ya existe y le damos un sentido propio a partir de su historia; otras veces diseñamos algo nuevo. Puede ser un objeto, una acción o una pieza creada especialmente para ese momento y, cuando hace falta, también trabajo con artistas o artesanos para materializarla. Lo importante es que el gesto no llegue antes que la intención. No se trata de escoger un símbolo entre un listado.":
  "I don't begin by choosing a ritual. First I need to understand what we want to express; then we look for the form that can best hold that idea. Sometimes we take a symbol that already exists and give it a meaning of your own, drawn from your story; other times we design something new. It can be an object, an action or a piece created especially for that moment — and when it's needed, I also work with artists and craftspeople to make it real. What matters is that the gesture never arrives before the intention. It isn't about picking a symbol from a list.",
"Cada tarjeta abre la información del símbolo.": "Each card opens the story of its symbol.",
"VER INFORMACIÓN": "SEE DETAILS",
"Algunas historias han tomado esta forma": "Some stories have taken this shape",
"Ver todas las ceremonias": "See every ceremony",

# --------------------------------------------------------------- como trabajo
"¿Cómo trabajo?": "How do I work?",
"Cada ceremonia parte de conversaciones con ustedes y de un proceso de escucha, escritura y diseño. No trabajo sobre un guion ya escrito ni necesitan llegar sabiendo cómo quieren que sea la ceremonia.":
  "Every ceremony starts from conversations with you and from a process of listening, writing and design. I don't work from a script that's already written, and you don't need to arrive knowing what you want the ceremony to be.",
"Primero necesito entender.": "First I need to understand.",
"Después empiezo a construir.": "Then I start to build.",
"La ceremonia dura alrededor de 45 a 50 minutos, pero el trabajo empieza mucho antes.":
  "The ceremony lasts around 45 to 50 minutes, but the work begins long before.",
"Por eso acompaño un número limitado de fechas.":
  "That's why I take on a limited number of dates.",
"En nuestra primera asesoría les cuento con detalle cómo funciona el proceso y qué pueden esperar de él.":
  "In our first consultation I'll walk you through exactly how the process works and what you can expect from it.",

# ----------------------------------------------------------------- testimonios
"Lo que dicen las": "In their own",
"parejas": "words",
"Cuando decidimos casarnos lo único claro que teníamos era que nos casara Alejandra. La encontré con la ilusión de tener un matrimonio emotivo, diferente, que enalteciera nuestro amor, y efectivamente lo hizo posible. Alejandra nació con un don, que lo describo como el de conectar; no sé si será por ser mujer, filósofa, abogada, madre, o quizás simplemente por lograr transmitir todas esas cosas bonitas que habitan en su corazón a través de las palabras.":
  "When we decided to get married, the only thing we were sure of was that we wanted Alejandra to marry us. I found her hoping for a wedding that would be moving, different, a wedding that would lift our love up — and she made exactly that possible. Alejandra was born with a gift, and I'd describe it as the gift of connecting; I don't know whether it comes from being a woman, a philosopher, a lawyer, a mother, or simply from being able to put all the beautiful things that live in her heart into words.",
"Alejandra conectó a todos nuestros invitados con nuestro amor, y al escuchar cómo nos describía a Alejandro y a mí, me hizo sentir escuchada, más enamorada y conmovida por la decisión que habíamos tomado. Si piensan que su amor merece ser celebrado de una forma especial, no duden en que ella lo hará posible: te escucha, los celebra y conecta de una manera demasiado hermosa y auténtica. Si la vida me permite renovar mis votos, no dudaría en tenerla de nuevo como nuestra oficiante.":
  "Alejandra connected every one of our guests to our love, and hearing the way she described Alejandro and me made me feel heard, more in love, and moved by the decision we had made. If you believe your love deserves to be celebrated in a special way, have no doubt that she will make it happen: she listens to you, she celebrates you, and she connects in a way that is beautiful and genuinely her own. If life lets me renew my vows, I wouldn't hesitate to have her as our officiant again.",
"Johanna y Alejandro": "Johanna and Alejandro",
"Ceremonia del nido": "The nest ceremony",
"Alejandra fue una de esas casualidades afortunadas que terminan siendo parte esencial de la historia. La conocimos inicialmente a través de Casa Terma, buscando un lugar especial para celebrar nuestra boda, y descubrimos que además ella misma oficiaba ceremonias.":
  "Alejandra was one of those lucky coincidences that end up becoming an essential part of the story. We first came across her through Casa Terma, while looking for a special place to hold our wedding, and then discovered that she also officiated ceremonies herself.",
"El proceso consistió en unas entrevistas individuales con cada uno de nosotros y luego un encuentro conjunto, dedicando tiempo a conocer nuestras historias, nuestros valores y el significado que queríamos darle a nuestra unión. Gracias a ese proceso, la ceremonia fue completamente personalizada y auténtica.":
  "The process was made up of individual interviews with each of us and then a joint meeting, taking the time to get to know our stories, our values and the meaning we wanted to give our union. Thanks to that process, the ceremony was completely personal and completely ours.",
"Fue una celebración íntima, pero nunca pequeña: estuvo llena de detalles, emociones y momentos significativos. Alejandra construyó un discurso cuidadoso, profundamente conectado con nuestra historia, que logró emocionarnos a nosotros y a todos los presentes. Cada palabra reflejaba quiénes somos y lo que representaba ese día para nuestra familia y amigos. Salimos con el corazón llenísimo de amor.":
  "It was an intimate celebration, but never a small one: it was full of detail, emotion and moments that mattered. Alejandra built a careful piece of writing, deeply connected to our story, that moved us and everyone there. Every word reflected who we are and what that day meant to our family and friends. We walked out with our hearts completely full.",
"@20mlopez": "@20mlopez",
"Ceremonia en Casa Terma": "Ceremony at Casa Terma",
"Las palabras se quedan cortas para describir lo maravilloso que fue estar acompañados por Alejandra en el proceso, porque no fue solo un día: fueron meses en los que, a través de reuniones programadas, le hacíamos conocedora de nuestra historia, de los momentos que nos definen como pareja y del recorrido que por siete años hemos realizado tomados de la mano.":
  "Words fall short of describing how wonderful it was to have Alejandra with us through the process, because it wasn't just one day: it was months in which, meeting after meeting, we let her into our story, into the moments that define us as a couple and into the seven years we've walked hand in hand.",
"Aleja no solo tomó cada fragmento para hilar de inicio a fin la ceremonia, sino que rompió cualquier estereotipo que pudiese presentarse por la unión de dos personas del mismo sexo: resaltó de una manera tan conmovedora cada aspecto positivo de nuestros seres que, para el final, conmovió a todos los asistentes, incluidos nosotros.":
  "Aleja didn't just take every fragment and thread the ceremony together from beginning to end — she broke through any stereotype that might come with the union of two people of the same sex: she brought out every good thing in us so movingly that, by the end, everyone there was in tears, ourselves included.",
"Siempre estaremos agradecidos con el cielo por el maravilloso don que tienes. Sin duda, este proceso no hubiese sido igual de especial sin tu compañía. Gracias por ser nuestra oficiante y nuestra amiga.":
  "We will always be grateful to the heavens for the wonderful gift you have. This process would not have been nearly as special without you. Thank you for being our officiant and our friend.",
"@dcamilov": "@dcamilov",
"Siete años juntos": "Seven years together",
"Al principio no sabíamos dónde encontrar a una persona que oficiara una boda hecha a nuestra medida y con nuestros gustos. Mi esposa encontró a Alejandra por redes sociales y desde ese momento terminamos de encajar todas las piezas que nos faltaban para planear nuestra ceremonia.":
  "At first we had no idea where to find someone who would officiate a wedding made to our measure and to our taste. My wife found Alejandra on social media, and from that moment every missing piece of our ceremony fell into place.",
"Alejandra hizo un excelente trabajo conociéndonos y adaptando nuestras historias e intereses para construir un ritual especialmente significativo. Esperamos seguir contando con ella para futuros rituales familiares.":
  "Alejandra did an excellent job of getting to know us and weaving our stories and interests into a ritual that meant a great deal. We hope to have her with us for future family rituals.",
"@juanalberto1995": "@juanalberto1995",
"Ceremonia simbólica": "Symbolic ceremony",
"Leer completo": "Read in full",
"Leer menos": "Read less",
"@evelinduran01": "@evelinduran01",
"Ceremonia del móvil de grullas": "The crane mobile ceremony",
"Cuando Jhon y yo decidimos casarnos teníamos una sola cosa clara, al principio: queríamos una ceremonia que conectara con los nuestros. Desde esa premisa tuve la casualidad y la fortuna de encontrarme a Aleja en redes, y de que alguien muy cercano, nuestro fotógrafo y amigo, nos recomendara su gran talento y su trabajo.":
  "When Jhon and I decided to get married we only had one thing clear, at first: we wanted a ceremony that would connect with our people. From that starting point I had the chance and the good fortune of coming across Aleja on social media, and of having someone very close to us \u2014 our photographer and friend \u2014 recommend her talent and her work.",
"Cuando empezamos toda la preparación de la boda, Aleja nos dio esa confianza y esa seguridad de crear el momento más inolvidable de nuestra historia con Jhon. Ella hizo magia con nuestra historia y la transmitió a nuestra familia y amigos de una manera cálida, abrazando con tranquilidad cada palabra y cada una de nuestras perspectivas para construir una ceremonia mágica. Todo fluyó y todo salió perfecto.":
  "Once we started getting the wedding ready, Aleja gave us the confidence and the certainty that we would create the most unforgettable moment of our story with Jhon. She worked magic with our story and passed it on to our family and friends with real warmth, holding every word and every one of our perspectives calmly to build a magical ceremony. Everything flowed and everything came out perfectly.",
"Aleja es sin duda una oficiante talentosa, que transmite calma y conecta con todos. Si buscan de verdad vivir un momento diferente al tradicional, emocionante, emotivo, inolvidable y que deje una huella para siempre, Aleja es la persona perfecta. Además, Aleja es una gran maestra: no solo te crea un momento mágico, sino que sin darte cuenta aprendes un montón de ella, de su calma, de su serenidad, de su sabiduría y de su amor. Mil gracias, Aleja, porque nuestra boda fue más hermosa de lo imaginado. Tuviste en cuenta cada detalle.":
  "Aleja is without doubt a gifted officiant, one who radiates calm and connects with everyone. If you genuinely want to live something other than the traditional \u2014 moving, heartfelt, unforgettable, something that leaves a mark for good \u2014 Aleja is the right person. And Aleja is a great teacher too: she doesn't only create a magical moment for you, you also learn an enormous amount from her without realising it \u2014 from her calm, her serenity, her wisdom and her love. Thank you so much, Aleja, because our wedding was more beautiful than we had imagined. You thought of every single detail.",

"@angiemurillo0311": "@angiemurillo0311",
"Para nosotras fue una experiencia que siempre hemos definido como mágica. Nuestro matrimonio implicaba algo un poco más complejo de lo normal; sin embargo, nuestra conexión con Aleja permitió que ese momento representara todo lo que somos.":
  "For us it was an experience we have always described as magical. Our marriage involved something a little more complex than usual; even so, our connection with Aleja meant that the moment came to stand for everything we are.",
"Aleja nos acompañó en cada momento y construyó un espacio en el que conectamos desde el amor y la espiritualidad, con ella y con cada una de las personas que estuvo presente. Sin duda alguna, fue la oportunidad en la cual el amor ganó por encima de todo. Gracias infinitas, Aleja, por haber logrado que nuestra esencia estuviera en cada detalle y que ese momento continúe grabado en nuestra mente y nuestro corazón.":
  "Aleja was with us at every step and built a space where we connected through love and spirituality \u2014 with her and with every person who was there. It was, without any doubt, the occasion on which love won above everything else. Endless thanks, Aleja, for making sure our essence was in every detail, and that the moment stays engraved in our minds and our hearts.",

"@pililanegrita": "@pililanegrita",
"Fue la mejor decisión. Siempre quisimos algo diferente, íntimo y especial; no queríamos una ceremonia y ya. Ale se tomó el tiempo de conocernos como personas y de conocer nuestra historia, de saber qué nos había enamorado, y acompañarnos a literalmente crear un espacio sagrado que respetara esa unión fue maravilloso. Siempre vamos a estar agradecidos por ese proceso y por ese momento tan hermoso.":
  "It was the best decision. We always wanted something different, intimate and special; we didn't want just a ceremony and that was that. Ale took the time to get to know us as people and to know our story, to find out what had made us fall in love \u2014 and having her walk us through literally creating a sacred space that honoured that union was wonderful. We will always be grateful for that process and for a moment that beautiful.",

"@violeta_____vio": "@violeta_____vio",
"Nuestro proceso con Ale fue maravilloso: ella nos ayudó a construir un momento único que recordaremos para siempre. Queríamos celebrar con nuestra familia colombiana lo que significó apostar por un proyecto común, y deseábamos que fuera la confirmación de la red que somos. ¡Y así fue! Gracias, Ale, por todo tu trabajo, por tu escucha sincera, por tus palabras y por tu guía.":
  "Our process with Ale was wonderful: she helped us build a moment we will remember for the rest of our lives. We wanted to celebrate with our Colombian family what it meant to commit to something together, and we wanted it to confirm the network that we are. And that is exactly what it was. Thank you, Ale, for all your work, for listening so honestly, for your words and for your guidance.",

"@mafesabe": "@mafesabe",
"Describir con palabras la lluvia de sentimientos y emociones vividas es definitivamente tarea de Aleja. Sin embargo, honrando su inmensa dedicación y la fortuna de haberla conocido, aquí vamos.":
  "Putting into words the downpour of feelings and emotions we lived is definitely Aleja's job, not mine. Still, in honour of her immense dedication and of how lucky we were to meet her, here goes.",
"Una boda simbólica, a grandes rasgos, es personalizar la boda a tu antojo; pero hacerlo dirigido por Aleja es llevarlo al siguiente nivel. Es su don, su pasión. Se siente desde el momento cero: cuando interiorizas lo que realmente quieres y no tienes idea de cómo decirlo, ella se conecta y lo ejecuta. Hace lo imposible posible, porque su idea no es vender un servicio de oficiante; es sin duda el paquete completo, premium, VIP, ajustado a ti y a tu pareja.":
  "A symbolic wedding, broadly speaking, means tailoring the wedding exactly to your liking; but doing it led by Aleja takes it to another level. It is her gift, her passion. You feel it from moment zero: when you work out what you really want and have no idea how to say it, she tunes in and makes it happen. She makes the impossible possible, because her idea isn't to sell you an officiant's service; it is, without doubt, the complete package \u2014 premium, VIP, fitted to you and your partner.",
"Lo especial no tiene valor monetario, ni mucho menos las lágrimas de alegría que inevitablemente saldrán escuchando cómo una persona puede describirte y describir tu relación como si llevara años de conocer el detrás de cámaras de tu vida. Aleja no es simplemente una oficiante de bodas: Aleja es una amiga indispensable en el día más soñado.":
  "What is special has no price tag, and still less do the tears of joy that will inevitably come as you listen to someone describe you and describe your relationship as though she had spent years knowing the behind-the-scenes of your life. Aleja isn't simply a wedding officiant: Aleja is an indispensable friend on the day you have dreamed of most.",
"Sin dar más spoiler: háganse un favor y cásense con Aleja. Prometo que lo agradecerán y no se arrepentirán.":
  "Without giving away any more: do yourselves a favour and get married with Aleja. I promise you will be grateful, and you will not regret it.",

"Las flechas llevan a los demás testimonios.": "The arrows take you to the other testimonials.",

# --------------------------------------------------------------- conversaciones
"También pueden conocerme un poco más": "You can also get to know me a little more",
"Hay conversaciones que cuentan partes de mi trabajo que no caben en esta página. Si quieren escucharme con más tiempo, aquí pueden encontrar cuatro espacios distintos en los que he hablado de las ceremonias, de mi manera de trabajar y de las parejas que he acompañado.":
  "There are conversations that tell parts of my work this page can't hold. If you'd like to hear me at greater length, here are four places where I've talked about the ceremonies, the way I work, and the couples I've walked alongside.",
"Televisión regional": "Regional television",
"Entrevista en televisión regional": "Interview on regional television",
"Una conversación sobre mi trabajo como oficiante y mi manera de entender las ceremonias simbólicas.":
  "A conversation about my work as an officiant and the way I understand symbolic ceremonies.",
"Ver entrevista": "Watch the interview",
"Conversación": "Conversation",
"Conversación en podcast": "A podcast conversation",
"Una entrevista en formato podcast para conocer con más calma cómo pienso y construyo una ceremonia.":
  "A podcast interview, with the time to go into how I think and how I build a ceremony.",
"Ver conversación": "Watch the conversation",
"Entrevista": "Interview",
"Una novia que casé me entrevista": "A bride I married interviews me",
"Una conversación especialmente cercana: una de las novias que acompañé cambia de lugar y esta vez es ella quien me hace las preguntas.":
  "A particularly close conversation: one of the brides I worked with swaps places, and this time she's the one asking the questions.",
"Escuchar episodio": "Listen to the episode",
"Video": "Video",
"Conversación con la primera pareja que casé": "A conversation with the first couple I married",
"Una mirada hacia el inicio de este trabajo, conversando con la primera pareja cuya ceremonia tuve la oportunidad de crear y oficiar.":
  "A look back at the beginning of this work, in conversation with the first couple whose ceremony I had the chance to create and officiate.",

# ---------------------------------------------------------------------- faq
"Algunas preguntas antes de conversar": "A few questions before we talk",
"¿Con cuánto tiempo deberíamos reservar?": "How far in advance should we book?",
"Como trabajo con un número limitado de fechas, lo ideal es escribirme tan pronto tengan definido el día de la boda. No necesitan tener clara la ceremonia para hacerlo. Al principio basta con confirmar disponibilidad y saber que quieren construirla de una manera propia.":
  "Because I take on a limited number of dates, it's best to write to me as soon as you've settled on the wedding day. You don't need to have the ceremony worked out to do that. At the start it's enough to check availability and to know you want to build it in your own way.",
"¿Viajas para oficiar bodas fuera de Bucaramanga?": "Do you travel to officiate weddings outside Bucaramanga?",
"Sí. Viajo a otras ciudades de Colombia y también a otros países. Si su boda es fuera de Bucaramanga, revisamos la logística necesaria y los viáticos correspondientes según el destino.":
  "Yes. I travel to other cities in Colombia and to other countries as well. If your wedding is outside Bucaramanga, we go over the logistics involved and the travel costs for that destination.",
"¿Haces ceremonias bilingües en español e inglés?": "Do you do bilingual ceremonies in Spanish and English?",
"Sí. Puedo construir y oficiar la ceremonia en español e inglés. Junto con ustedes definimos cómo integrar ambos idiomas para que la ceremonia tenga ritmo y pueda ser vivida de manera natural tanto por ustedes como por sus invitados.":
  "Yes. I can build and officiate the ceremony in Spanish and English. Together we decide how to weave both languages in, so the ceremony keeps its rhythm and feels natural to you and to your guests alike.",
"¿Te encargas de toda la boda o solamente de la ceremonia?": "Do you handle the whole wedding or only the ceremony?",
"¿Cuánto tiempo tenemos que disponer para construir la ceremonia?": "How much time do we need to set aside to build the ceremony?",
"Como punto de partida tendremos al menos tres encuentros de aproximadamente dos horas cada uno, aunque algunas ceremonias necesitan más. Pero el proceso no ocurre solamente durante nuestras reuniones: ustedes también son cocreadores de la ceremonia, así que necesitan disponer de tiempo y apertura para pensar, conversar, escribir y ayudarnos a materializar algunos de los detalles que vayamos imaginando juntos. No tienen que llegar con las respuestas. Sí con disposición para involucrarse.":
  "As a starting point we'll have at least three meetings of around two hours each, though some ceremonies need more. But the process doesn't only happen in our meetings: you are co-creators of the ceremony too, so you'll need time and openness to think, talk, write and help us bring to life some of the details we imagine together. You don't have to arrive with the answers. You do have to arrive willing to get involved.",
"¿Nos acompañas con los votos, la música y otros detalles de la ceremonia?": "Will you help us with the vows, the music and other details of the ceremony?",
"Sí. Todo eso hace parte de mi trabajo. Durante los meses previos tendremos un grupo de WhatsApp en el que estaré disponible para acompañarlos con los votos, la música, las participaciones y cualquier otra decisión que haga parte de la ceremonia. Pueden escribirme cuando aparezca una pregunta, una idea o algo que quieran mostrarme. No tenemos que esperar hasta la siguiente reunión para hablarlo.":
  "Yes. All of that is part of my work. In the months beforehand we'll have a WhatsApp group where I'll be there to help you with the vows, the music, the readings and any other decision that belongs to the ceremony. You can write to me whenever a question, an idea or something you want to show me comes up. We don't have to wait until the next meeting to talk it through.",
"Sabemos que queremos una boda simbólica, pero todavía no sabemos cómo queremos que sea. ¿Tenemos que tenerlo claro antes de contactarte?":
  "We know we want a symbolic wedding, but we don't yet know what we want it to be like. Do we need to have that clear before contacting you?",
"No. No espero que lleguen con la ceremonia resuelta. Pueden saber algunas cosas que quieren, otras que definitivamente no quieren y tener todavía muchas preguntas. Parte del proceso consiste justamente en descubrir juntos qué tiene sentido para ustedes.":
  "No. I don't expect you to arrive with the ceremony already solved. You may know some things you want, others you definitely don't want, and still have plenty of questions. Part of the process is precisely discovering together what makes sense for you.",
"¿La ceremonia puede hablar de Dios sin ser una ceremonia religiosa?": "Can the ceremony speak of God without being a religious ceremony?",
"Sí. Si Dios hace parte de su manera de entender la relación y quieren nombrarlo, podemos hacerlo sin necesidad de convertir la ceremonia en una ceremonia religiosa tradicional. También trabajo con parejas que viven la espiritualidad de otra forma o para quienes ese lenguaje no hace parte de su historia. La ceremonia se construye desde las creencias de ustedes, no desde una visión impuesta por mí.":
  "Yes. If God is part of how you understand your relationship and you want to name that, we can do it without turning the ceremony into a traditional religious service. I also work with couples who live their spirituality differently, or for whom that language isn't part of their story. The ceremony is built from your beliefs, not from a view I impose.",
"¿Una ceremonia simbólica tiene validez legal?": "Is a symbolic ceremony legally binding?",
"No, y no pretende tenerla. Es un acto de palabra, presencia y sentido: lo que sostiene el vínculo ahí es lo que se dicen el uno al otro delante de quienes los acompañan. El trámite legal se hace por lo civil, antes o después. Muchas de las parejas que acompaño hacen las dos cosas.":
  "No, and it isn't meant to be. It is an act of words, presence and meaning: what holds the bond there is what you say to one another in front of the people with you. The legal side is done civilly, before or after. Many of the couples I work with do both.",
"¿Cuánto dura la ceremonia?": "How long does the ceremony last?",
"Generalmente entre 45 y 50 minutos. Puede variar un poco dependiendo de los votos, las participaciones y de lo que hayamos construido para ese día.":
  "Usually between 45 and 50 minutes. It can vary a little depending on the vows, the readings and whatever we've built for that day.",

# -------------------------------------------------------------------- cierre
"Conversemos sobre su": "Let's talk about your",
"boda": "wedding",
"La primera asesoría conmigo no tiene costo. No necesitan llegar sabiendo cómo debería ser la ceremonia, cuál será el símbolo o qué van a decir en sus votos. Quiero conocerlos, escuchar qué están imaginando y contarles con detalle cómo trabajo.":
  "Your first consultation with me is free. You don't need to arrive knowing what the ceremony should be, what the symbol will be or what you'll say in your vows. I want to get to know you, hear what you're imagining and tell you in detail how I work.",
"Al agendar, les pediré la fecha y el lugar de la boda para revisar disponibilidad antes de nuestra videollamada.":
  "When you book, I'll ask for the date and place of the wedding so I can check availability before our video call.",
"Agendar una videollamada": "Book a video call",

# ----------------------------------------------------------------------- pie
"El acompañamiento": "The work",
"Ver y preguntar": "See and ask",
"Lo que dicen las parejas": "What couples say",
"Conversaciones y entrevistas": "Conversations and interviews",
"Preguntas frecuentes": "Frequently asked questions",
"Ceremonias simbólicas de boda · Filosofía, Derecho y Dirección de Arte":
  "Symbolic wedding ceremonies · Philosophy, Law and Art Direction",
"Bucaramanga, Colombia": "Bucaramanga, Colombia",
"Menú": "Menu",
"· Bucaramanga, Colombia": "· Bucaramanga, Colombia",
}

# ------------------------------------------------------- la pregunta de Casa Terma
TEXTOS["En mi rol como oficiante me encargo específicamente de crear y dirigir la ceremonia simbólica. Si quieren casarse en Santander, también está Casa Terma, mi proyecto de eventos y una casa que reúne muchos de los valores con los que entiendo y trabajo las bodas. Cuando la boda se realiza allí, además de crear y oficiar la ceremonia, puedo asumir la dirección creativa del evento completo junto a mi equipo. Fuera de Casa Terma, mi trabajo se concentra exclusivamente en la ceremonia."] = \
  "In my role as an officiant I take care specifically of creating and leading the symbolic ceremony. If you'd like to marry in Santander, there is also Casa Terma, my events project and a house that gathers many of the values I understand and work weddings with. When the wedding takes place there, as well as creating and officiating the ceremony I can take on the creative direction of the whole event together with my team. Outside Casa Terma, my work is devoted exclusively to the ceremony."

# -------------------------------------------------- las fichas de los simbolos
TEXTOS.update({
"Qué representa": "What it represents",
"Técnica": "Technique",

"El ojo turco tejido con cristales": "The evil eye woven with crystals",
"Roberto y Daniela": "Roberto and Daniela",
"Representa la intención de proteger la relación y el hogar que están construyendo, dejando entrar lo positivo y manteniendo fuera aquello que pueda alejarlos de su esencia. El espejo en el centro suma una idea importante: mirar hacia adentro, actuar con honestidad y cultivar la introspección como una forma de cuidar tanto el amor propio como la relación. Dentro del tejido quedan incorporados además cinco valores que para ellos sostienen su vínculo: lealtad, fortaleza, protección, serenidad y amor.":
  "It represents the intention to protect the relationship and the home they are building, letting in what is good and keeping out whatever might pull them away from who they are. The mirror at the centre adds an important idea: looking inward, acting honestly and cultivating self-reflection as a way of caring for both self-love and the relationship. Woven into the piece are five values that, for them, hold their bond together: loyalty, strength, protection, serenity and love.",
"Tejido hecho a mano con espejo central e incrustación de cristales.":
  "Hand-woven piece with a central mirror and inlaid crystals.",

"El rompecabezas familiar": "The family jigsaw",
"Astrid y Manuel": "Astrid and Manuel",
"Representa una relación que se ha ido construyendo pieza a pieza. Cada experiencia, recuerdo, persona y sueño compartido forma parte de una imagen mayor: la familia que han creado juntos y que seguirá transformándose con el tiempo. El símbolo también conecta directamente con su historia, porque el rompecabezas estuvo presente en la pedida de mano y vuelve en la ceremonia como una continuación de ese momento. No representa algo terminado, sino una construcción constante entre dos personas que conservan su individualidad mientras crean una vida en común.":
  "It represents a relationship that has been built piece by piece. Every experience, memory, person and shared dream is part of a larger picture: the family they have created together and that will keep changing over time. The symbol also connects directly to their story, because the jigsaw was there at the proposal and returns in the ceremony as a continuation of that moment. It doesn't stand for something finished, but for a constant building between two people who keep their own selves while making a life in common.",
"Pintura hecha a mano, dividida en piezas de rompecabezas.":
  "Hand-painted artwork, cut into jigsaw pieces.",

"El jardín zen en forma de yin-yang": "The zen garden shaped as a yin-yang",
"Marlyn y Arturo": "Marlyn and Arturo",
"Representa el hogar y la familia que han cultivado juntos como su propio edén: un espacio construido desde la paz, el equilibrio y la consciencia. El yin-yang habla de sus diferencias —razón y emoción, reflexión y acción— y de cómo, sin perder su individualidad, han aprendido a complementarse. Dentro de ese jardín aparecen también los frutos de su relación: las transformaciones que han provocado el uno en el otro, sus recuerdos, el amor por sus perros y, especialmente, Emma, representada por el bonsái como el fruto más importante de su unión.":
  "It represents the home and family they have cultivated together as an Eden of their own: a space built on peace, balance and awareness. The yin-yang speaks of their differences — reason and emotion, reflection and action — and of how, without losing who they each are, they have learnt to complement one another. Inside that garden are the fruits of their relationship too: the changes they have brought about in each other, their memories, their love for their dogs and, above all, Emma, represented by the bonsai as the most important fruit of their union.",
"Jardín zen diseñado e impreso en 3D, en forma de yin-yang, intervenido con arenas de diferentes colores, figuras personalizadas y un bonsái central.":
  "A zen garden designed and 3D-printed in the shape of a yin-yang, filled with coloured sands, custom figures and a bonsai at its centre.",

"El nido": "The nest",
"Alejandro y Johanna": "Alejandro and Johanna",
"Representa la historia que Johanna y Alejandro han construido durante casi ocho años, etapa por etapa. Cada una de sus ocho piezas guarda un capítulo distinto —la unión, el cambio, el hogar, el presente, las turbulencias, los viajes, la aceptación y los sueños—, y al ensamblarlas hacen visible todo lo que han aprendido, atravesado y creado juntos. Las grullas suman los deseos de quienes los acompañan y convierten el nido en un símbolo de lo ya construido y de todo lo que todavía puede seguir creciendo dentro de él.":
  "It represents the story Johanna and Alejandro have built over almost eight years, stage by stage. Each of its eight pieces holds a different chapter — union, change, home, the present, turbulence, travel, acceptance and dreams — and in assembling them they make visible everything they have learnt, come through and created together. The cranes add the wishes of the people there with them, turning the nest into a symbol both of what has been built and of all that can still grow inside it.",
"Nido compuesto por ocho piezas ensambladas durante la ceremonia e intervenido con grullas de origami intencionadas previamente por los invitados.":
  "A nest of eight pieces assembled during the ceremony, hung with origami cranes the guests had each made a wish on beforehand.",

"El globo viajero": "The travelling balloon",
"Carolina y Jhonatan": "Carolina and Jhonatan",
"Representa la relación de Carolina y Jhonatan como un viaje compartido. El globo habla de una vida en movimiento, de su amor por conocer el mundo y de la idea de que el hogar no depende de un lugar específico, sino de estar juntos. El equipaje simboliza aquello que han decidido llevar siempre con ellos: los valores que han sostenido su relación y que quieren conservar como guía en lo que viene —el amor, la complicidad y el crecimiento, la admiración y el orgullo, y el cuidado en lo cotidiano.":
  "It represents Carolina and Jhonatan's relationship as a shared journey. The balloon speaks of a life in motion, of their love of seeing the world, and of the idea that home doesn't depend on a particular place but on being together. The luggage stands for what they have decided to carry with them always: the values that have held their relationship up and that they want to keep as a guide for what comes next — love, closeness and growth, admiration and pride, and care in everyday things.",
"Globo aerostático con mapamundi tejido por la mamá del novio, intervenido con cuatro saquitos que contienen piedras asociadas a los valores centrales de la relación.":
  "A hot-air balloon with a world map woven by the groom's mother, hung with four small pouches holding stones tied to the relationship's core values.",

"El árbol de los sueños": "The tree of dreams",
"Harold y Felipe": "Harold and Felipe",
"Representa todo lo que Harold y Felipe ya han cultivado juntos y todo lo que todavía sueñan construir. Sus frutos hablan de los aprendizajes, logros, recuerdos y transformaciones que han cosechado como pareja, mientras sus ramas guardan las metas y sueños hacia los que quieren seguir creciendo.":
  "It represents everything Harold and Felipe have already grown together and everything they still dream of building. Its fruit speaks of the lessons, achievements, memories and changes they have harvested as a couple, while its branches hold the goals and dreams they want to keep growing towards.",
"Árbol de alambres hecho a mano sobre una matera personalizada impresa en 3D, intervenido con corazones de madera que representan sus frutos y sueños.":
  "A hand-made wire tree in a custom 3D-printed pot, hung with wooden hearts standing for their fruit and their dreams.",

"El castillo de LEGO y la coronación": "The LEGO castle and the crowning",
"Juan Camilo y Estefany": "Juan Camilo and Estefany",
"Representa todo lo que han construido juntos, pieza a pieza, y al mismo tiempo honra el juego, la imaginación y a sus niños interiores. Al terminar el castillo y coronarse mutuamente, celebran el mundo que han creado como pareja y la elección de seguir construyéndolo juntos.":
  "It represents everything they have built together, brick by brick, while honouring play, imagination and the children they still carry inside. As they finish the castle and crown one another, they celebrate the world they have created as a couple and their choice to keep building it together.",
"Construcción en LEGO finalizada durante la ceremonia y coronación mutua.":
  "A LEGO build completed during the ceremony, followed by crowning one another.",

"El lazo tejido con cristales": "The cord woven with crystals",
"Franchesco y Miguel": "Franchesco and Miguel",
"Representa una reflexión sobre lo que realmente significa unirse al otro: no dejar de ser uno mismo, sino entrelazar dos historias, aprendizajes y formas de habitar la vida para construir algo nuevo en común. Los cristales reúnen los valores que quieren mantener como guía en esa construcción: amor, familia, prosperidad, salud, sabiduría y aventura.":
  "It represents a reflection on what joining another person really means: not ceasing to be yourself, but interweaving two stories, two sets of lessons and two ways of inhabiting life in order to build something new in common. The crystals gather the values they want as a guide in that building: love, family, prosperity, health, wisdom and adventure.",
"Tejido hecho a mano, intervenido durante la ceremonia con seis cristales suspendidos, cada uno asociado a un valor de la relación.":
  "A hand-woven cord, hung during the ceremony with six crystals, each tied to one value of the relationship.",

"La composición musical": "The musical composition",
"Juan y Diana": "Juan and Diana",
"Representa la relación como una obra que han ido creando juntos a lo largo de los años. Cada uno aporta su propio ritmo, su sonido y su individualidad, y de esa diferencia nace una melodía compartida que incluye momentos altos y bajos, aprendizajes, recuerdos, sueños y transformaciones. El pentagrama simboliza ese recorrido: una historia que no ha sido lineal, pero que ha encontrado armonía en la manera en que ambos se escuchan, se adaptan y siguen componiendo su vida en común.":
  "It represents the relationship as a work they have been composing together over the years. Each brings their own rhythm, their own sound and their own self, and out of that difference comes a shared melody with its highs and lows, its lessons, memories, dreams and changes. The stave stands for that journey: a story that has not been linear, but that has found its harmony in the way they listen to each other, adapt, and keep composing their life in common.",
"Pintura hecha a mano sobre lienzo, con un pentagrama curvo que la pareja completa durante la ceremonia incorporando las notas musicales que representan su historia.":
  "A hand-painted canvas with a curving stave that the couple completes during the ceremony, adding the notes that stand for their story.",

"La pintura de los siete colores": "The painting of seven colours",
"Effy y Daniel": "Effy and Daniel",
"Representa las cualidades y decisiones que Daniel y Effy quieren llevar a esta nueva etapa: creatividad, transformación, profundidad, raíces, amor, magia, alegría y esperanza. Cada color conserva un significado propio, pero al encontrarse en una misma obra simboliza también la manera en que ellos han aprendido a crecer con libertad, aportar desde su individualidad y crear algo nuevo juntos.":
  "It represents the qualities and choices Daniel and Effy want to carry into this new stage: creativity, transformation, depth, roots, love, magic, joy and hope. Each colour keeps a meaning of its own, but meeting in a single work they also stand for the way the two of them have learnt to grow freely, to contribute as themselves and to create something new together.",
"Pintura realizada durante la ceremonia con siete colores de cera previamente transformados con fuego y mezclados libremente por la pareja sobre una misma obra.":
  "A painting made during the ceremony in seven wax colours, melted beforehand with fire and then blended freely by the couple onto a single work.",

"El camello": "The camel",
"Pilar y Marco": "Pilar and Marco",
"Representa el camino que han recorrido juntos y la forma en que han aprendido a vivirlo: con curiosidad, resistencia y serenidad. El camello recoge su espíritu viajero y explorador, su capacidad de adaptarse a los cambios, las distancias y la vida como migrantes, y también la tranquilidad con la que han aprendido a resolver las dificultades desde el diálogo y el respeto. Es un símbolo de una relación que no se queda quieta, que avanza, se transforma y sigue eligiendo la aventura compartida.":
  "It represents the road they have travelled together and the way they have learnt to travel it: with curiosity, endurance and calm. The camel holds their travelling, exploring spirit, their ability to adapt to change, to distance and to life as migrants, and also the composure with which they have learnt to work through difficulty by talking and by respecting one another. It is the symbol of a relationship that doesn't stand still, that moves forward, changes, and keeps choosing the shared adventure.",
"Escultura modelada a mano en arcilla por la pareja, intervenida con color durante la ceremonia y sometida después a dos quemas para convertirse en una pieza cerámica permanente.":
  "A sculpture modelled by hand in clay by the couple, coloured during the ceremony and then fired twice to become a permanent ceramic piece.",

"El móvil de grullas en origami": "The origami crane mobile",
"Evelin y Jhon": "Evelin and Jhon",
"Representa el hogar que Jhon y Evelin han construido y los principios que quieren heredarle a Salomé. El móvil habla de una familia que se sostiene en equilibrio, donde cada parte tiene un lugar y aporta al conjunto. Las grullas simbolizan protección, esperanza y buenos deseos, mientras cada color representa uno de los valores que quieren dejarle como guía para su vida.":
  "It represents the home Jhon and Evelin have built and the principles they want to pass on to Salomé. The mobile speaks of a family held in balance, where every part has its place and adds to the whole. The cranes stand for protection, hope and good wishes, while each colour stands for one of the values they want to leave her as a guide for her life.",
"Móvil de grullas elaborado en origami y ensamblado por la pareja durante la ceremonia.":
  "A mobile of origami cranes, folded beforehand and assembled by the couple during the ceremony.",

"Las banderas del orgullo": "The pride flags",
"Camilo y Harold": "Camilo and Harold",
"Representan la decisión de Harold y Camilo de hacer visible su amor, su identidad y la vida que han construido juntos. Al izarlas sobre su barco, no solo honran los principios y valores que orientan su relación, sino también la libertad de amarse abiertamente, con verdad, dignidad y orgullo. Son una forma de afirmar que este vínculo ha sido elegido, sostenido y defendido con valentía, y que merece navegar el mundo sin esconderse.":
  "They represent Harold and Camilo's decision to make their love, their identity and the life they have built together visible. Raising them over their boat, they honour not only the principles and values that guide their relationship but also the freedom to love each other openly, with truth, dignity and pride. They are a way of affirming that this bond has been chosen, held and defended with courage, and that it deserves to sail the world without hiding.",
"Banderas hechas a mano por los novios e izadas durante la ceremonia sobre un barco que representa su relación.":
  "Flags made by hand by the couple and raised during the ceremony over a boat standing for their relationship.",

"El álbum de su historia": "The album of their story",
"Daniela y Néstor": "Daniela and Néstor",
"Representa los trece años de vida que Daniela y Néstor han construido juntos: canciones, viajes, arquitectura, proyectos, fotografías, conversaciones, dificultades y pequeños momentos que terminaron formando una historia compartida. Durante la ceremonia, ese álbum se completa con un último gesto: retratarse mutuamente y luego juntos, como una forma de guardar también quiénes son hoy y seguir mirándose con atención, curiosidad y admiración mientras continúan cambiando.":
  "It represents the thirteen years of life Daniela and Néstor have built together: songs, journeys, architecture, projects, photographs, conversations, difficulties and small moments that ended up forming a shared story. During the ceremony that album is completed with one last gesture: photographing each other and then the two of them together, as a way of keeping who they are today and of going on looking at one another with attention, curiosity and admiration as they keep changing.",
"Álbum fotográfico construido a partir de su historia, completado durante la ceremonia con retratos tomados por ellos mismos: uno de cada uno y uno final juntos.":
  "A photo album built from their story, completed during the ceremony with portraits they took themselves: one of each of them and a final one together.",

"El Scrabble": "The Scrabble board",
"Kenzo y María Luisa": "Kenzo and María Luisa",
"Representa el juego como una parte esencial de su relación y, al mismo tiempo, convierte sus votos en algo tangible. Las palabras que eligen durante la ceremonia resumen los compromisos que quieren cuidar en su vida juntos y quedan como un recordatorio visible de aquello que decidieron construir y sostener como pareja.":
  "It represents play as an essential part of their relationship and, at the same time, turns their vows into something you can hold. The words they choose during the ceremony sum up the promises they want to look after in their life together, and remain as a visible reminder of what they decided to build and sustain as a couple.",
"Composición con fichas de Scrabble sobre tablero, ensamblada durante la ceremonia y convertida después en un cuadro para su casa.":
  "A composition of Scrabble tiles on the board, laid out during the ceremony and later framed for their home.",
})

# ------------------------------- textos alternativos y etiquetas de accesibilidad
TEXTOS.update({
"Abrir menú": "Open menu",
"Cerrar menú": "Close menu",
"Cerrar": "Close",
"Secciones": "Sections",
"Los pilares de mi manera de trabajar": "The pillars of the way I work",
"1 de 4": "1 of 4",
"2 de 4": "2 of 4",
"3 de 4": "3 of 4",
"4 de 4": "4 of 4",
"Ver ficha 1": "See card 1",
"Ver ficha 2": "See card 2",
"Ver ficha 3": "See card 3",
"Ver ficha 4": "See card 4",
"Ficha anterior": "Previous card",
"Ficha siguiente": "Next card",
"Detalles de ceremonias": "Details from ceremonies",
"Símbolos creados para otras ceremonias. Las flechas los recorren.":
  "Symbols created for other ceremonies. The arrows move through them.",
"Símbolos anteriores": "Previous symbols",
"Símbolos siguientes": "Next symbols",
"Testimonio anterior": "Previous testimonial",
"Testimonio siguiente": "Next testimonial",
"Testimonios de parejas": "Testimonials from couples",
"Fotografía ampliada": "Enlarged photograph",

"Alejandra Otelo oficiando una ceremonia simbólica al aire libre frente a los novios.":
  "Alejandra Otelo officiating an outdoor symbolic ceremony in front of the couple.",
"Retrato de Alejandra Otelo.": "Portrait of Alejandra Otelo.",
"Alejandra Otelo oficiando junto a un arco de flores, con el valle de fondo.":
  "Alejandra Otelo officiating beside an arch of flowers, with the valley behind her.",
"Corazones de madera con palabras escritas a mano, en las manos de la pareja.":
  "Wooden hearts with hand-written words, held by the couple.",
"Aro de fibra con las argollas colgando sobre una tabla grabada con los nombres.":
  "A woven hoop with the rings hanging over a board engraved with their names.",
"Un nido de ramas con las argollas dentro, rodeado de flores.":
  "A nest of branches with the rings inside, surrounded by flowers.",
"Los novios con coronas de papel dorado, riéndose.":
  "The couple wearing gold paper crowns, laughing.",
"Salida de la ceremonia entre humo de colores.":
  "Leaving the ceremony through coloured smoke.",
"Alejandra caminando hacia la ceremonia.": "Alejandra walking towards the ceremony.",
"Ojo turco tejido en macramé con un espejo al centro, colgado durante la ceremonia de Roberto y Daniela.":
  "An evil eye woven in macramé with a mirror at its centre, hung during Roberto and Daniela's ceremony.",
"Astrid y Manuel completando el rompecabezas pintado a mano durante su ceremonia.":
  "Astrid and Manuel completing the hand-painted jigsaw during their ceremony.",
"Jardín zen en forma de yin-yang con un bonsái al centro, en la ceremonia de Marlyn y Arturo.":
  "A yin-yang zen garden with a bonsai at its centre, at Marlyn and Arturo's ceremony.",
"Johanna y Alejandro ensamblando el nido de ocho piezas durante su ceremonia.":
  "Johanna and Alejandro assembling the eight-piece nest during their ceremony.",
"Globo aerostático con un mapamundi tejido, colgado durante la ceremonia de Carolina y Jhonatan.":
  "A hot-air balloon with a woven world map, hung during Carolina and Jhonatan's ceremony.",
"Árbol de alambre con corazones de madera colgando de sus ramas, en la ceremonia de Harold y Felipe.":
  "A wire tree with wooden hearts hanging from its branches, at Harold and Felipe's ceremony.",
"Las manos de la pareja colocando la última pieza del castillo de LEGO durante su ceremonia.":
  "The couple's hands placing the last brick of the LEGO castle during their ceremony.",
"Franchesco y Miguel unidos por el lazo tejido a mano, junto a Alejandra, al final de su ceremonia.":
  "Franchesco and Miguel joined by the hand-woven cord, beside Alejandra, at the end of their ceremony.",
"Juan y Diana completando con notas musicales el pentagrama pintado para su ceremonia.":
  "Juan and Diana adding the musical notes to the stave painted for their ceremony.",
"Las siete velas de colores y los retratos de familia dispuestos para la ceremonia de Effy y Daniel.":
  "The seven coloured candles and the family portraits laid out for Effy and Daniel's ceremony.",
"Pilar y Marco pintando el camello de arcilla que modelaron para su ceremonia.":
  "Pilar and Marco painting the clay camel they modelled for their ceremony.",
"Móvil de grullas de origami ensamblado por Evelin y Jhon durante su ceremonia.":
  "The origami crane mobile assembled by Evelin and Jhon during their ceremony.",
"Camilo y Harold frente al barco con las banderas que izaron durante su ceremonia.":
  "Camilo and Harold in front of the boat with the flags they raised during their ceremony.",
"Daniela y Néstor mostrando los retratos instantáneos que tomaron para cerrar su álbum.":
  "Daniela and Néstor holding up the instant portraits they took to close their album.",
"Tablero de Scrabble con las palabras que Kenzo y María Luisa eligieron durante su ceremonia.":
  "The Scrabble board with the words Kenzo and María Luisa chose during their ceremony.",
"Ceremonia simbólica en una terraza con vista a la montaña.":
  "A symbolic ceremony on a terrace looking out over the mountains.",
"Dos novios sentados frente a Alejandra bajo un arco floral con vista a la montaña.":
  "Two grooms seated in front of Alejandra beneath a floral arch with a mountain view.",
"Ceremonia al aire libre con los invitados entre plumas de pampa.":
  "An outdoor ceremony with the guests among pampas grass.",
"Ceremonia en un bosque de pinos bajo un arco de gypsophila.":
  "A ceremony in a pine forest beneath an arch of gypsophila.",
"La novia leyendo sus votos al novio en un bosque de pinos.":
  "The bride reading her vows to the groom in a pine forest.",
"Dos novias saliendo de la ceremonia entre pétalos.":
  "Two brides leaving the ceremony through falling petals.",
"Los novios soltando un globo al final de la ceremonia.":
  "The couple releasing a balloon at the end of the ceremony.",
"Las manos de la pareja atando el lazo tejido durante la ceremonia.":
  "The couple's hands tying the woven cord during their ceremony.",
"Alejandra con los novios bajo un arco de rosas blancas y rosadas.":
  "Alejandra with the couple beneath an arch of white and pink roses.",
"Los novios besándose al final de la ceremonia.":
  "The couple kissing at the end of the ceremony.",
"La ceremonia al aire libre, con los invitados al borde del cañón.":
  "The outdoor ceremony, with the guests at the edge of the canyon.",
"La pintura del árbol sobre el caballete, al final de la ceremonia.":
  "The painting of the tree on its easel, at the end of the ceremony.",
"Alejandra oficiando junto al atril con la pieza tejida, frente a un telón de hojas.":
  "Alejandra officiating beside the lectern with the woven piece, against a backdrop of leaves.",
"La novia leyendo sus votos con el micrófono en la mano.":
  "The bride reading her vows with the microphone in her hand.",
"Los novios preparando el café de su ritual sobre la mesa blanca.":
  "The couple brewing the coffee for their ritual on the white table.",
"Los novios y Alejandra entre el humo de colores al final de la ceremonia.":
  "The couple and Alejandra among the coloured smoke at the end of the ceremony.",
"Los libros de votos junto a las figuras pintadas y las flores.":
  "The vow books beside the painted figures and the flowers.",
"Alejandra en una ceremonia frente al mar.": "Alejandra at a ceremony by the sea.",
"Alejandra Otelo oficiando una ceremonia con la ciudad de fondo.":
  "Alejandra Otelo officiating a ceremony with the city behind her.",
})

# ------------------------------------------ los mensajes que se abren en WhatsApp
WHATSAPP = {
"Hola Alejandra, vimos su página y queremos agendar la primera asesoría.":
  "Hi Alejandra, we saw your website and we'd like to book the first consultation.",
"Hola Alejandra, queremos agendar la primera asesoría para hablar de nuestra ceremonia.":
  "Hi Alejandra, we'd like to book the first consultation to talk about our ceremony.",
"Hola Alejandra, queremos agendar la primera asesoría. Nuestra boda sería el: ":
  "Hi Alejandra, we'd like to book the first consultation. Our wedding would be on: ",
"Hola Alejandra, queremos más información sobre las ceremonias simbólicas.":
  "Hi Alejandra, we'd like more information about the symbolic ceremonies.",
"Hola Alejandra, queremos agendar la primera asesoría.":
  "Hi Alejandra, we'd like to book the first consultation.",
}

# ------------------------------------------------------- titulo y descripciones
CABEZA = {
"titulo": ("Alejandra Otelo — Ceremonias simbólicas de boda",
           "Alejandra Otelo — Symbolic wedding ceremonies"),
"descripcion": ("Construyo cada ceremonia a partir de su historia, de sus vínculos y de lo que significa para ustedes decidir casarse. La escribo y la diseño desde cero. Bucaramanga y toda Colombia.",
                "I build every ceremony out of your story, your bonds and what deciding to marry means to you. I write it and design it from scratch. Bucaramanga and all of Colombia."),
"og": ("Una ceremonia que no podría pertenecerle a nadie más.",
       "A ceremony that could belong to no one else."),
}

TEXTOS["Idioma"] = "Language"
TEXTOS["Página en inglés"] = "Page in English"
TEXTOS["Página en español"] = "Page in Spanish"


# ============================================================ incrustar en la pagina

import io, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGINA = os.path.join(RAIZ, 'assets', 'alejandra-otelo.html')

DICCIONARIO = ('<script type="application/json" id="ingles">\n%s\n</script>\n'
               % json.dumps({'textos': TEXTOS, 'whatsapp': WHATSAPP, 'cabeza': CABEZA},
                            ensure_ascii=False, separators=(',', ':'), sort_keys=True))


def main():
    s = io.open(PAGINA, encoding='utf-8').read()
    nuevo = re.sub(r'<script type="application/json" id="ingles">.*?</script>\n',
                   '', s, flags=re.S)
    if nuevo == s and 'id="ingles"' in s:
        sys.exit('no se pudo quitar el diccionario viejo')
    ancla = '<script>\n/* Alejandra Otelo — interacciones mínimas */'
    if ancla not in nuevo:
        sys.exit('no se encontro donde poner el diccionario')
    nuevo = nuevo.replace(ancla, DICCIONARIO + ancla, 1)
    io.open(PAGINA, 'w', encoding='utf-8').write(nuevo)
    print('diccionario incrustado: %d textos, %.1f kB'
          % (len(TEXTOS), len(DICCIONARIO) / 1024.0))


if __name__ == '__main__':
    main()
