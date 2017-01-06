# ==========================================================
# Inteligencia Artificial. Tercer curso. 
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Entregable grupo 2. 
# Primera entrega 
# ===========================================================


# Escribir el código Python de las funciones que se piden en el
# espacio que se indica en cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN (aquellas funciones con un nombre distinto al que se pide en el
# ejercicio NO se corregirán).

# ESTE ENTREGABLE SUPONE 0.75 PUNTOS DE LA NOTA TOTAL 

# *****************************************************************************
# HONESTIDAD ACADÉMICA Y COPIAS: la realización de los ejercicios es un
# trabajo personal, por lo que deben completarse por cada estudiante de manera
# individual.  La discusión con los compañeros y el intercambio de información 
# DE CARÁCTER GENERAL con los compañeros se permite, pero NO AL NIVEL DE
# CÓDIGO. Igualmente el remitir código de terceros, obtenido a través
# de la red o cualquier otro medio, se considerará plagio. 

# Cualquier plagio o compartición de código que se detecte significará
# automáticamente la calificación de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados, independientemente de otras medidas de carácter 
# DISCIPLINARIO que se pudieran tomar. Por tanto a estos alumnos NO se les 
# conservará, para futuras convocatorias, ninguna nota que hubiesen obtenido
# hasta el momento. 
# *****************************************************************************


# ------------------------
# DESCRIPCIÓN DEL PROBLEMA
# ------------------------

# En este ejercicio, se trata de realizar funciones que tratan con "sopas de
# letras", entendiendo como tal un juego consistente en una cuadrícula con
# letras, en la que hay que buscar la ocurrencia de determinadas palabras,
# palabras que se proporcionan al jugador, pero no su localización en la 
# cuadrícula. Las palabras están en secuencias consecutivas de casillas de la
# cuadrícula, bien en horizontal, vertical o diagonal, y además se pueden leer
# en cualquier sentido. 
# Por ejemplo, lo que sigue es una sopa de letras de tamaño 15x15, en la que
# hay que buscar las palabras "ejercicio","inteligencia","artificial","python"
# y "entregable": 

# kbhypmfxtrdqrcq
# inteligencialat
# altaqrehurjxajh
# reavmjdwnwzwlal
# tipigfxomrydxce
# nbbhcrhkmjslblo
# tooicicrejebbyt
# nszdhnftwiwafez
# uofkwjqihngpplw
# dnhxncujtefxviu
# kxithejerrnjyye
# ctubygrtueadxuc
# fupcgpnozhhnjjt
# nzxehejgdzycvod
# ngxdipqwyowqfqf

# La resolución de esta sopa de letras sería la siguiente (poniendo en blanco
# las casillas donde no ocurren las palabras):

#               
# inteligencia   
#  l             
#   a            
#    i          e
#     c        l 
#   oicicreje b  
# n     f    a   
#  o     i  g    
#   h     te     
#    t    rr     
#     y  t  a    
#      pn        
#      e         
#               

# Supondremos que la sopa de letras sólo contiene letras del alfabeto
# en minúsculas (excluyendo la "ñ")

# En lo que sigue, nombraremos a las distintas casillas de una sopa de letras
# mediante sus coordenadas (fila,columna), empezando a contar en el cero. Para
# describir la ocurrencia de una palabra en una sopa de letras, daremos la
# casilla en la que comienza la palabra, y la dirección hacia la que se
# lee. Estos sentidos los designaremos como pares (x,y) que representan a 
# los puntos cardinales, según la siguiente correspondencia:
# Norte: (-1,0), Sur: (1,0), Este: (0,1), Oeste: (0,-1),
# Noroeste: (-1,-1), Noreste: (-1,1), Sureste: (1,1) y Suroeste: (1,-1). 

# Por ejemplo, en la sopa de letras anterior la palabra "ejercicio" empieza y
# la posición (6,10) y se lee hacia el (0,-1) (oeste). La palabra "artificial"
# empieza en (11,10) y se lee hacia el (-1,-1) (noroeste).

# En python, representaremos una sopa de letras mediante la lista de sus
# filas, y cada fila mediante un string. Por ejemplo, la sopa de letras
# anterior se representa con la siguiente lista:

# >>> sopa0=['kbhypmfxtrdqrcq', 'inteligencialat', 'altaqrehurjxajh',
#            'reavmjdwnwzwlal', 'tipigfxomrydxce', 'nbbhcrhkmjslblo', 
#            'tooicicrejebbyt', 'nszdhnftwiwafez', 'uofkwjqihngpplw', 
#            'dnhxncujtefxviu', 'kxithejerrnjyye', 'ctubygrtueadxuc', 
#            'fupcgpnozhhnjjt', 'nzxehejgdzycvod', 'ngxdipqwyowqfqf']


# ========
# SE PIDE:
# ========

# -----------------------------------------------------------------------------
# EJERCICIO (1)

# Definir un procedimiento 

# imprime_sopa(sopa)

# que recibiendo como entrada una sopa de letras, la imprime por pantalla, cada
# fila en una línea. Por ejemplo:

# >>> imprime_sopa(sopa0)
# kbhypmfxtrdqrcq
# inteligencialat
# altaqrehurjxajh
# reavmjdwnwzwlal
# tipigfxomrydxce
# nbbhcrhkmjslblo
# tooicicrejebbyt
# nszdhnftwiwafez
# uofkwjqihngpplw
# dnhxncujtefxviu
# kxithejerrnjyye
# ctubygrtueadxuc
# fupcgpnozhhnjjt
# nzxehejgdzycvod
# ngxdipqwyowqfqf











# -----------------------------------------------------------------------------
# EJERCICIO (2)
# Definir una función 

# comprueba_palabra(palabra,sopa,orx,ory,dirx,diry)

# que recibiendo como entrada un string con una palabra, una sopa de letras
# (representada como lista de strings), y cuatro números orx, ory, dirx,diry
# (representando (orx,ory) una posición en la sopa, y (dirx,diry) una
# dirección), entonces devuelve True si la palabra está en la sopa de letras,
# comenzando en la posición (orx,ory) y leída en la dirección (dirx,diry), y
# False en caso contrario.  

# Por ejemplo:

# >>> comprueba_palabra("python",sopa0,5,8,-1,0)
# False
# >>> comprueba_palabra("artificial",sopa0,11,10,1,1)
# False
# >>> comprueba_palabra("ejercicio",sopa0,6,10,0,1)
# False
# >>> comprueba_palabra("ejercicio",sopa0,6,10,0,-1)
# True
# >>> comprueba_palabra("entregable",sopa0,13, 5,-1, 1)
# True
# -----------------------------------------------------------------------------















# -----------------------------------------------------------------------------
# EJERCICIO (3)

# Usando la anterior, definir una función 

# resuelve_sopa_de_letras(sopa,palabras)

# que recibiendo como entrada una sopa de letras, y una lista de palabras,
# devuelve un diccionario en el que las claves serán las palabras de la lista
# que se encuantran en la sopa, y su valor asociado, un par con la posición de
# comienzo de la palabra y la dirección en la que se lee esa palabra en la
# sopa. Nótese que podría haber palabras en la lista de palabras que no se
# encuentren en la sopa, y en ese caso no hay que incuirlas en el diccionario.

# Por ejemplo:

# >>> resuelve_sopa_de_letras(sopa0,["ejercicio","tortilla","inteligencia","artificial",
#                                 "python","pupitre","entregable"])
# {'artificial': ((11, 10), (-1, -1)), 
#  'inteligencia': ((1, 0), (0, 1)), 
#  'ejercicio': ((6, 10), (0, -1)), 
#  'python': ((12, 5), (-1, -1)), 
#  'entregable': ((13, 5), (-1, 1))}

# NOTA: Se valorará que el código de esta función sea compacto, sin excesiva
# distinción de casos. 
# -----------------------------------------------------------------------------









# -----------------------------------------------------------------------------
# EJERCICIO (4)

# Usando la anterior, definir una función 

# imprime_sopa_resuelta(sopa,palabras)

# que recibiendo como entrada una sopa de letras y una lista de palabras en
# las que algunas de ellas se encuentran en la sopa, imprime por pantalla la 
# misma sopa pero en la que sólo aparecen las palabras encontradas (el resto
# de letras se sustituyen por un espacio en blanco).

# Por ejemplo:


# >>> imprime_sopa_resuelta(sopa0,["ejercicio","tortilla","inteligencia","artificial",
#                                "python","pupitre","entregable"])

#               
# inteligencia   
#  l             
#   a            
#    i          e
#     c        l 
#   oicicreje b  
# n     f    a   
#  o     i  g    
#   h     te     
#    t    rr     
#     y  t  a    
#      pn        
#      e         
#               
# -----------------------------------------------------------------------------












# -----------------------------------------------------------------------------
# EJERCICIO (5)
#
# genera_sopa_de_letras(d,n,palabras)

# que recibe dos números d y n, y una lista de palabras, y devuelve una sopa
# de letras (una lista de strings), de dimensiones d x d, en la que están
# colocadas n palabras de la lista de palabras (escogidas aleatoriamente). El
# resto de casillas de la sopa se rellenan con letras del alfabeto, escogidas
# aleatoriamente.  

# Por ejemplo:

# >>> sopa01=genera_sopa_de_letras(15,5,["ejercicio","tortilla","inteligencia","artificial",
#                                 "python","pupitre","entregable"])
# >>> imprime_sopa(sopa01)
# weoahjiwoncqoua
# gbihsxlkxwbnqal
# nwwjafbwosazktu
# iguhuelftarjwdd
# keaxuxiwnitncyw
# lohbxspqrciceey
# ttortillanfenzv
# jpokmwcvzeictsy
# bfyhgafhegcgrel
# cbltqauueiieeyr
# tmiihuxpulamgmp
# zyrrgokedeldaav
# oscvjznqytvdbjy
# vwqexmuylnqelep
# emocijzstiebexj


# NOTA: será necesario importar la librería ramdom. Los métodos random.sample
# y radom.randint pueden ser de utilidad. Además, también puede ser de
# utilidad la función chr. 











# --------------------------------------------------------

# Lo que sigue son algunas ejemplos de uso de las funciones anteriores, para
# generación y resolución de sopas de letras:

# Ejemplo 1
# =========

palabras1=["lugar","mancha","quiero","acordarme","tiempo","hidalgo","lanza",
           "astillero","adarga","antigua","rocin","flaco","galgo","corredor",
           "duelos","quebrantos","sabados","lentejas","viernes","palomino",
           "añadidura","domingos","hacienda","velludo","pantunflos"]


# >>> sopa1=genera_sopa_de_letras(30,15,palabras1)

# >>> imprime_sopa(sopa1)
# ijzecdlifflpvzxvbkmxvdlndlkmlg
# emdynoqnqnefaemxwteweuratdiype
# qfoiwrrtmuuwabjhkzpetqxflpisoe
# jfjeyoqpksenzcpdkitlemtjftaelz
# ragkyvlgdmgfafhtionnfztjqqgnxq
# msiizyiqkukkwslxgorgskkajbtrmx
# fqmxtznmomqblqflubcgpqiqqzdeoj
# dywtoxhqdtaiozafwecjgilhehgihy
# ouquzpvrcevdkgqhmnbgkndgzhkvth
# fobvjzvgxhdvjstnbgtaofmsrxhtav
# panjqaexkfawqhuyqfdjzbnhukqrsc
# wveirhvzbqetoiebyanlijybakfhcn
# zedsmezlugzrxsxkrylimxddjfdpbb
# jlfiuonjeurbhmrgcektcsqrbdxwfu
# slttdglbikavixahhawrdouwgamfcz
# tuajsgwacvgcdazcscuulfrhsdcexy
# ldnfyishpiuqaskeentbmazsykllix
# gozrvacxcnlbltzxqarudidañaqwdf
# bwpiplhrpklpgiesfswibskmepseux
# bukphsceagttolpthgbqnjmbqjnavo
# tlhlffcqolrullsejneoccsmmpuqoy
# hrhdkssrivwdcepuqmlojnnvmmjofj
# dbbkzaghlhxfqrwamjrtdopaycmunm
# unorsszdrantsotklrceppkssmjheh
# jmizhornhktcwocsebamgjjkdzwinx
# eysgdlanzacnnegdziewdvsykvquyt
# ybnjrezgnnybwzoizitnkkshdbbnrx
# zhcpnuazpkqwdredtkvqikghbrtpdf
# guvfldtlpytqfmyjbfmazhgsupncxv
# yfbupantunflosjakhpihsmthbhqgw

# >>> imprime_sopa_resuelta(sopa1,palabras1)

#
#                              
#                            s  
#                            e  
#                  o         n  
#                 g          r  
#                l           e  
#               a            i  
#              g             v  
#  o                 a          
#   n               d           
#  v i             an           
#  e  m           r  i          
#  l   o    r h  g    c         
#  l    l   a i a      o        
#  u     a  g da        r       
#  d      p u as                
#  o        l lt   arudidaña    
#             gi                
#             ol                
#              l      c         
#              e     o          
#              r    r  o        
#      s       o   r  p         
#      o          e  m          
#      lanza     d  e           
#      e        o  i            
#      u       r  t             
#      d                        
#     pantunflos                


# Ejemplo 2
# =========


palabras2=["peloton","fusilamiento","coronel","aureliano","buendia","recordar",
           "aquella","remota","padre","conocer","hielo","macondo","aldea","barro",
           "cañabrava","construidas","orilla","diafanas","precipitaban","lecho",
           "piedras","pulidas","blancas","enormes","huevos","prehistoricos"]


# >>> sopa2=genera_sopa_de_letras(40,17,palabras2)
# >>> imprime_sopa(sopa2)
# sketxoccmuqhwacazkcvmeaeiodmspwbclqgamnf
# juwiyqmbqpyygxxzvhekphgpksbbxiplsmruxwhk
# ltmodxceiebdhsxkukpazemrnwfgbcpfothfqegi
# plqorzvstzorwrctaiknrfjzlvcqlhlhkbsbvmew
# pojwuoxupgbomdhugzcidbgyeiosmsdmzppfhkcf
# zfwoigyeduoxicyjvjddaovmtcyoowqyybxcgnlg
# ykxyjwtxkazpodcqfdbrjshdbtfcbhqmqfllkwtk
# eplpryzbsvbnktvmqfrtbhhhxdipsqmmodavagvt
# ypoymhnpviiuzznagogvhjdxfrbcvgolltotbbew
# nmyohiufzenybhaeictqazccoayorkhnfmmdlqgv
# icgqnqbvwmblvkzuiahdslgtzuolyzuoawirfpdv
# cgkofoncdkwfcazcimkenqszdbnduyrqkibvsyte
# ugpplutncwwvtomonvasdiarbimsezfboalyjeea
# asyaitanyqtemflalvqlhyxcxzpocbxfecbeqgkw
# vokmwillnfeobxrfvyfeiwwmihrccqfyhlswrlrh
# tllpylwkhdrzhpcpqlroisfcloxkhfuzvqdtoupl
# tigedqkrfggaockiepdgpyuupmdvitcdzbnghiaa
# vibuxxseptvvguebzthzseifdkjjctntqkejkpgi
# iinymkmmnytypwvllowbthtxomfenjyczgdzwuuj
# krucseihyipgcncahfdfwhqrbdastimzcotnypqn
# lgtgkprgkybzcaonccrupvdvauikumyaexgeswuf
# qcebvbtiplhyomvrttwlfhftbyjxatomerjcjmit
# ddcjqzczbqkcnjwmiqfvdzzqdsussznyjzbkdayx
# vticzetaweyhodzhslotvnsffwiuzymzulkrtvvr
# omyxyfrkobmzctyqjyleyvglkvqijfvcqyrgcrdt
# zjmwuaodkompezaaqjcassanafaidcxaaazkysjv
# prprigzdakaqruacakspschelailmabtphygdyen
# lcbgipdixpkfrqrlwmlbjaeypesqiahtlufrmrsa
# ihbfcfpawxyauurcaoedwarwakaymcnlxdemtyaz
# ylimzmcgpxrrznkzriadqdhdlnfikfiyqazhklnr
# lncogjizpilzaxhqxjvzsqmxehjudlaxvsvedxue
# odnocamsllckolgnsadilupdiioasperjpdemwtv
# igdjzjpcamkwhaodgejtoovenppnhoqnzfafraxk
# hkjhiqzldsphbcqwwpizwbafzqnvcdjmocmtgumq
# uelbhphmjslmocrosvisnpfirukvdorwzroousyr
# fmnugbtnznoecwurkbnmnargdiajlkiofyonrsaf
# toutumdkguaywgavlguktmijgnlozlooieccixwh
# hltsuodovlblbojksslndfsldkefzjcezbswuwlq
# sldterylxsxqqsjjqgwkooyredhucmieasdsfvpp
# nihegjhhzhueqaiwwilxnqugnhrbbxgkfpldpwec
# >>> imprime_sopa_resuelta(sopa2,palabras2)
#                                        
#                                        
#                                        
#                                        
#                      b       s          
#                     a       o           
#             o      r       c            
#              t    r       i             
#               n  o       r    o         
#                e        o      n        
#                 i      t        a       
#                  m    s          i      
#                   a  i            l     
#                    lh              e    
#            o       ei               r   
#             h     r  s               u  
#              c   p    u               a 
#               e        f                
#                l                        
                                        
#             c o                         
#             o  r            atomer      
#             n   i                       
#      e      o    l                      
#       r     c     l                     
#        d    e      a sanafaid           
#         a   r a     s                   
#          p   q       a                  
#             u         r               a 
#            r           d             l  
#           l             e    l      d   
# odnocam  l      sadilup  i    e    e    
#         a                 p    n  a     
#                       a         o       
#                        i         r      
#                         d         o     
#                          n         c    
#                           e             
#                            u            
#                             b           
#




# Ejemplo 3
# =========


# palabras3=["año","onofre","bouvila","barcelona","ciudad","fiebre","renovacion",
#            "ciudad","situada","valle","montañas","cadena","costera","interior",
#            "anfiteatro","templado","altibajos","cielos","claros","luminosos",
#            "nubes","blancas","presion","atmosferica","lluvia","traicionera",
#            "torrencial","opinion","dominante","fundacion","fenicios","historia",
#            "colonia","cartago","aliada","probado","elefantes","anibal","detuvieron",
#            "beber","triscar","riberas","terreno","accidentado","diezmarian",
#            "maravillados","colmillos","orejas","trompa","proboscis","asombro",
#            "compartido","comentarios","ulteriores"]    


# >>> sopa3=genera_sopa_de_letras(60,25,palabras3)
# >>> imprime_sopa(sopa3)
# ebgyntlzcrloszjhjipyskabftbqkroqyhyahdcihhluzgzstqruepksfime
# frurnrsxolmlibfmxxjxsefrjfvqlefzpajqnrrgogjlewmwbnqjbviqhrgx
# rpksjdzryjicyiuwfvcwayadailadicpolrhulwpaqqzzspmltmfprvmqldo
# bcbvyjensgklrddnrrrzchmteblrywsorjmlsuqoxpuhjwqafuzynyfaellx
# dgpijjzodfuwhzvlkezzezfpjmdntokxfilxxxwtoibkvyfgdhdxgisgrbbw
# judsanpnkskirdxxptjqlaubzkmymipixouyoxsqdxilbiloqainyxxmojtf
# covsnjhiucitchfoxjtamfwgoqnpzrjvxdcvwjsqifjgjqqwfctkztzntryk
# gasaihtntuemfzytlxqcixnoxkqclnkivlqpqqkjayifxfuddjogfczayogy
# imcwfnfimmzxxppwkzrlmipvonorjbreadmvixnvdicnmdxmsjwxuhmefshj
# rkyhicbjqwklejffyfsuiblcmobgcnduhvwwbzfkojmepbjhfyqwdqdecyyl
# lvuzhakashegfshahqgskfmgkfmjpbbakqpqgqqsjyvgojqrhafhbrjrxpww
# radzonghcghmujfacpdmsqmpurtwjyajulsmijspffffjfxkamumbkfxigxe
# ldyobmncedrudqrjkqjvtmvzvpdyocapxnaaqskjebzmimsrawauvoxcssez
# zoxygpwnvxtlcwvfrjqebpjrztklojrumwaqodacxqhdalhfmvdjhbcqefsu
# ncfvznaejcdtbwhzverojucdytvicwkcxocxcskkorprhwpjymgexyzxwcou
# ztlxlvipvqgerkqnidwsnedxuimulmbnonrnyvthsraamingjsdsvhzzcohh
# herfteeqwcsrlejpluenjefgvirlrrhqtfstwgrcevxroewgmtpbbdfdnluf
# onqeytsjncjizkzvazkkkyrkarbhrpxtjwqreehsiacypkfkorvvcjttmdcg
# mwnzthzzzahodyorombbormrromcceymlnrlotilkxeklksewzsijsyhjklt
# mtudmspumdbrxxhcbbjqmzhneqwtkdgwoicveolqchopbiicndzdqejgafss
# rclplkzxmedeockhanahcphcytrjiqwhnsaqnacjcrjxfehskiscznagkmhy
# vuoyazkspnoszjitatsafintmrbnrosxrlbpdsbyzwffgsehfzcbphwoffbt
# pttfyuehjaxciakoztebocwoevdjrjowrtwosepsdsvlxjlrzxwiwzrlpibk
# wkvdwyoiopkpsgudoxgjgbdtrnstmgxxznsbdikgeqdqmewjtmueostajdyt
# klbtpalnjroalkkxnwsvconfdqfepqrexvuxuzrkfygaajoyxraczsqyadip
# wexrvdwjchdñvaodphjkckncpvmrafjiqwdbpmmmuxstdwknuuixrjufuwbo
# ndadywrctjyopidhlchwkywzhkocmbhnelpaecuoqodueuecdqvnemnnpqlp
# nxukppefczjevxriawtjodajvefikwxhjmneusgikyzxhyiuxfrmxsuzujsp
# cqauyimhmfwylfgjvdkwskuogaieplcuoxkuyrceujclybucevcfmafolbxs
# alaoqmzqevpyeatnxjduniyzismlgncnvlplmxvvgpalbkghisrtgnimmxhx
# qckqcpxysbzblfluzjxyugqntcyoltlpzszzjiklwizlvvacnwnghbvvxidt
# shlyhtsdmmmfozrpbvfmdbjzfndsztiyfsvinlwoccefusvkbbhyldobuvpc
# ddvmwhehlmtihvhckbdsqnnvnzqghvkvwdvjrxjnsektsuvhqwksuyxvllcc
# ytnpsfretlvrtsshorklqbdzbzmfxcyskstknwebcoaepujlalbpwqdniblw
# ubebzssvykwwfubjknsdrvvppwzodtimkyoavrdfwdptdhzhqpssvgrmitdo
# ghfnhotdepimeukcrdgcjhrjlwpzrwdghqnwrucjyczbglzenhioqrapfvad
# qpespysaoqywwkodbbsobxfgpegjfwqotgfoyegajmypoqlmskwfehujtoei
# qqiwukjkremzhgxcyngjeuasqwgixmcstttgrnmwbzeckjdiezmariangwge
# hvdvwajwxcuxxujqovbgaguglbujjtffdridaikjbwepvensegcsqapahwjb
# vioulpfeekitayktymsaupczactlrksyshdpthcdeysiebyodbkcmeepqfih
# atfiwqasrulyutjmtkpmxvncubsashwamcejcpwjxicjflaymzjfjxhzezdw
# ntvhjzplhmmkjvuhfmdauesxeoissmzlactlxastwwyeawzorbmosaixqwst
# oqqpcajznwaqpihcphbfraeppccvyntudkwnznretmimwxqnoxrwresyvmre
# vsnzeylfuvfeaheloooaytdlibxkjiieotlzyluedlxynqxhytiejcsbhqpi
# daibfarslxbeyinybumfyyiosprpovinpvecqeugppwitoyoeqquqeuqtqvn
# jiveerenwtmtokkufqvgsyndhghefjvldnjresspjlcqkdrbyxunmxxahnfl
# qcidhymktnjeryythonunedxoanwckmtfqshlaahioiteeuekbhyweiedlvm
# vzwqoqfxodwytzcpkmiirlfukkrnqdyxskpzanbychmjbyagifesrfqylbtd
# nkikjwscxkdsygttgxzahfvrglxuyawvswbalrddgovhpgpegvwizyunkaze
# rydpvpaverkbdjflbscpbluwbnovralmhtiuqriberaskyvwqvukbdwgzzpy
# uhtjpwdnetbdaqqlovcwtbewhyztooakunwmezcaqvaikrxulovtsjpoksju
# laygjlvynlxvbdgtixptqszpmzmcsfwlollqiyauvcfsfzrlqnrzemmnxxeg
# nhibrdominantetlvyzcaudwahwgqroldegnjqvrshioqmqwfsmbadlewvzy
# srxdwlxyzxqpntxpchvaltchcxpcjeocxokggmhqdupypslbngcbqsivrung
# shfrvrtzkrqdszrxbxfsokvnekblcckcnimudgvovcqrwxyznjcqgqrupbdu
# ofkmijumkaztdrvruybbhcrabveqooyvftdpgbrpouiojcddzvnruyuhmepx
# fzuvrlenzwqjbluminososazypdzsjbjvmqonvsquzxxxtwmhbbrcllqxbfa
# lijygitxuoottvvlnsgecsqcttudvvravozpqlfsbrmcfiwgsyvfuyphfeea
# ulrdafbpdmcseytoseotyfszvuqcnvwvvzvekbfdbikrsugbbajnhmtorrar
# jxzqcrsuaaawyylvsbnzwfhirbwclhinkgljbkdzgsyfkmvyxckwemaqnorx
# >>> imprime_sopa_resuelta(sopa3,palabras3)
#                                                            
#         o                                                   
#        r              adaila                                
#       e                                                     
#      j                                                      
#     a                                                       
#    s                                                        
#                                                            
#                                                            
#                                                            
#                                                            
#                               a                             
#            u                   p             m              
#            l                    m           a               
#            t       o             o        pr                
#            e        n             r      ra                 
#            r         e             t    ev                  
#          c i          r                si     f             
#          a o           r              il       e            
#          d r            e            ol         n           
#          e e             t          na           i          
#          n s                        d             c         
#          a                         o               i        
#                                  ns       d         o       
#            a                      u        a         s      
#            ñ                       b        d               
#            o               c        e        u              
#                            i         s        i             
#                            e               l   c     a      
#                            l              a           i     
#                            o             i             v    
#                            s            c               u   
#                                        n                 l  
#                                       e                   l 
#                                      r                      
#                                     r                       
#                                    o                        
#                c                  t           diezmarian    
#                 o            t                              
#                  m          r                               
#                   p        a                                
#                    a      i                    orbmosa      
#                     r    c                                  
#                      t  i                   n               
#                       io                     o              
#                       nd                      r             
#                      e  o                      e            
#                     r                           i           
#                    a               a             v          
#                                   i  riberas      u         
#                                  n                 t        
#                                 o                   e       
#      dominante                 l                     d      
#                               o                             
#                              c                           b  
#                                                          e  
#              luminosos                                   b  
#                                                          e  
#                                                          r  
#                                                            
#
