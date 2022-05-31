# -- 30 -- Digit fifth powers:
# def digitPower(n):
#     sum = 0
#     for i in range(len(str(n))):
#         sum += int(str(n)[i])**5
#     return sum
#
# def main():
#     sum = 0
#     for i in range(10,1000000):
#         if i == digitPower(i):
#             print(i)
#             sum += i
#     print(sum)
#
# main()

# -- 32 -- Pandigital products:
# def div(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             a, b = i, int(n/i)
#             combine = str(a) + str(b) + str(n)
#             if sorted(combine) == ['1','2','3','4','5','6','7','8','9']:
#                 return True
#         else:
#             continue
#
# def main():
#     sum = 0
#     for i in range(10,100000):
#         if div(i):
#             print(i)
#             sum += i
#     print(sum)
#
# main()

# -- 33 -- Digit cancelling functions:
# def cancelling(a,b):
#     a, b = str(a), str(b)
#     for i in a:
#         if i in b:
#             a= a.replace(i,'',1)
#             b = b.replace(i,'',1)
#     return a,b
#
# prod = 1
# for i in range(11,100):
#     for j in range(10,i):
#         x, y = cancelling(j,i)
#         try :
#             x, y = int(x), int(y)
#         except:
#             continue
#
#         if y == 0:
#             continue
#         elif x == j or y == i or str(i)[-1] == '0' or str(j)[-1] == '0':
#             continue
#         elif x/y == j/i:
#             prod *= x/y
# print(prod)

# -- 34 -- Digit factorials:
# def fact(n):
#     return 1 if (n==1 or n==0) else n * fact(n - 1);
#
# def same(n):
#     sum = 0
#     for i in range(len(str(n))):
#         sum += fact(int(str(n)[i]))
#     if sum == n:
#         return True
#
# sum = 0
# for i in range(10,50000):
#     if same(i):
#         sum += i
# print(sum)

# -- 35 -- Circular primes:
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#
#     for i in range(3,int(n**0.5)+2, 2):
#         if n % i == 0 or n % 2 == 0:
#             return False
#     else:
#         return True
#
#
# def cycle(n):
#     n = str(n)
#
#     for i in range(len(n)):
#         num = int(n[i:] + n[:i])
#         if not prime(num):
#             return
#
#     return True
#
# def main():
#     l = []
#     all = 0
#
#     for i in range(2,1000000):
#         if prime(i):
#             l.append(i)
#
#     for i in range(len(l)):
#         if cycle(l[i]) is True:
#            all += 1
#
#     print(all)
#
# main()

# -- 36 -- Double-base palindrome:
# def palindrome(n):
#     if n == n[::-1]:
#         return True
#     else:
#         return False
#
# def main():
#     sum = 0
#     for i in range(1,1000000):
#         if palindrome(str(i)) and palindrome(bin(i)[2:]):
#             sum += i
#     print(sum)
#
# main()

# -- 37 -- Truncatable primes:
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#
#     for i in range(3,int(n**0.5)+2, 2):
#         if n % i == 0 or n % 2 == 0:
#             return False
#     else:
#         return True
#
# def trunc(n):
#     l = []
#     for i in range(len(str(n))):
#         l.append(int(str(n)[i:]))
#         l.append(int(str(n)[:i+1]))
#
#     for i in range(len(l)):
#         if not prime(l[i]):
#             return False
#     else:
#         return True
#
# def main():
#     sum = 0
#     count = 0
#     for i in range(10,10000000):
#         if prime(i):
#             if trunc(i):
#                 sum += i
#                 count += 1
#         if count == 11:
#             print(sum)
#             break
#
# main()

# -- 39 -- Integer right triangles:
# p = []
# count = []
#
# for a in range(1,500):
#     for b in range(1,500):
#         c = (a**2 + b**2)**0.5
#         if int(c) == c and a+b+c <= 1000:
#             if a+b+c not in p:
#                 p.append(a+b+c)
#                 count.append(1)
#             else:
#                 count[p.index(a+b+c)] += 1
#
# print(p[count.index(max(count))])

# -- 40 -- Champernowne's constant:
# def constant():
#     num = ''
#     for i in range(1, 200000):
#         num += str(i)
#     return num
#
# def main():
#     num = constant()
#     n = 1
#     ans = 1
#     while n != 1000000:
#         ans *= int(num[n - 1])
#         n *= 10
#     print(ans)

# -- 41 -- Pandigital prime: 123456789
#
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#
#     for i in range(3,int(n**0.5)+2, 2):
#         if n % i == 0 or n % 2 == 0:
#             return False
#     else:
#         return True
#
# def pand():
#     l = []
#     new = []
#
#     for a in range(1,10):
#         n = ''
#         for b in range(1,a+1):
#             n += str(b)
#         l += [int(''.join(i)) for i in itertools.permutations(n, a)]
#
#     for i in l:
#         if prime(i):
#             new.append(i)
#     print(max(new))
#
# pand()

# -- 42 -- Coded triangle numbers:
# x = ["A","ABILITY","ABLE","ABOUT","ABOVE","ABSENCE","ABSOLUTELY","ACADEMIC","ACCEPT","ACCESS","ACCIDENT","ACCOMPANY","ACCORDING","ACCOUNT","ACHIEVE","ACHIEVEMENT","ACID","ACQUIRE","ACROSS","ACT","ACTION","ACTIVE","ACTIVITY","ACTUAL","ACTUALLY","ADD","ADDITION","ADDITIONAL","ADDRESS","ADMINISTRATION","ADMIT","ADOPT","ADULT","ADVANCE","ADVANTAGE","ADVICE","ADVISE","AFFAIR","AFFECT","AFFORD","AFRAID","AFTER","AFTERNOON","AFTERWARDS","AGAIN","AGAINST","AGE","AGENCY","AGENT","AGO","AGREE","AGREEMENT","AHEAD","AID","AIM","AIR","AIRCRAFT","ALL","ALLOW","ALMOST","ALONE","ALONG","ALREADY","ALRIGHT","ALSO","ALTERNATIVE","ALTHOUGH","ALWAYS","AMONG","AMONGST","AMOUNT","AN","ANALYSIS","ANCIENT","AND","ANIMAL","ANNOUNCE","ANNUAL","ANOTHER","ANSWER","ANY","ANYBODY","ANYONE","ANYTHING","ANYWAY","APART","APPARENT","APPARENTLY","APPEAL","APPEAR","APPEARANCE","APPLICATION","APPLY","APPOINT","APPOINTMENT","APPROACH","APPROPRIATE","APPROVE","AREA","ARGUE","ARGUMENT","ARISE","ARM","ARMY","AROUND","ARRANGE","ARRANGEMENT","ARRIVE","ART","ARTICLE","ARTIST","AS","ASK","ASPECT","ASSEMBLY","ASSESS","ASSESSMENT","ASSET","ASSOCIATE","ASSOCIATION","ASSUME","ASSUMPTION","AT","ATMOSPHERE","ATTACH","ATTACK","ATTEMPT","ATTEND","ATTENTION","ATTITUDE","ATTRACT","ATTRACTIVE","AUDIENCE","AUTHOR","AUTHORITY","AVAILABLE","AVERAGE","AVOID","AWARD","AWARE","AWAY","AYE","BABY","BACK","BACKGROUND","BAD","BAG","BALANCE","BALL","BAND","BANK","BAR","BASE","BASIC","BASIS","BATTLE","BE","BEAR","BEAT","BEAUTIFUL","BECAUSE","BECOME","BED","BEDROOM","BEFORE","BEGIN","BEGINNING","BEHAVIOUR","BEHIND","BELIEF","BELIEVE","BELONG","BELOW","BENEATH","BENEFIT","BESIDE","BEST","BETTER","BETWEEN","BEYOND","BIG","BILL","BIND","BIRD","BIRTH","BIT","BLACK","BLOCK","BLOOD","BLOODY","BLOW","BLUE","BOARD","BOAT","BODY","BONE","BOOK","BORDER","BOTH","BOTTLE","BOTTOM","BOX","BOY","BRAIN","BRANCH","BREAK","BREATH","BRIDGE","BRIEF","BRIGHT","BRING","BROAD","BROTHER","BUDGET","BUILD","BUILDING","BURN","BUS","BUSINESS","BUSY","BUT","BUY","BY","CABINET","CALL","CAMPAIGN","CAN","CANDIDATE","CAPABLE","CAPACITY","CAPITAL","CAR","CARD","CARE","CAREER","CAREFUL","CAREFULLY","CARRY","CASE","CASH","CAT","CATCH","CATEGORY","CAUSE","CELL","CENTRAL","CENTRE","CENTURY","CERTAIN","CERTAINLY","CHAIN","CHAIR","CHAIRMAN","CHALLENGE","CHANCE","CHANGE","CHANNEL","CHAPTER","CHARACTER","CHARACTERISTIC","CHARGE","CHEAP","CHECK","CHEMICAL","CHIEF","CHILD","CHOICE","CHOOSE","CHURCH","CIRCLE","CIRCUMSTANCE","CITIZEN","CITY","CIVIL","CLAIM","CLASS","CLEAN","CLEAR","CLEARLY","CLIENT","CLIMB","CLOSE","CLOSELY","CLOTHES","CLUB","COAL","CODE","COFFEE","COLD","COLLEAGUE","COLLECT","COLLECTION","COLLEGE","COLOUR","COMBINATION","COMBINE","COME","COMMENT","COMMERCIAL","COMMISSION","COMMIT","COMMITMENT","COMMITTEE","COMMON","COMMUNICATION","COMMUNITY","COMPANY","COMPARE","COMPARISON","COMPETITION","COMPLETE","COMPLETELY","COMPLEX","COMPONENT","COMPUTER","CONCENTRATE","CONCENTRATION","CONCEPT","CONCERN","CONCERNED","CONCLUDE","CONCLUSION","CONDITION","CONDUCT","CONFERENCE","CONFIDENCE","CONFIRM","CONFLICT","CONGRESS","CONNECT","CONNECTION","CONSEQUENCE","CONSERVATIVE","CONSIDER","CONSIDERABLE","CONSIDERATION","CONSIST","CONSTANT","CONSTRUCTION","CONSUMER","CONTACT","CONTAIN","CONTENT","CONTEXT","CONTINUE","CONTRACT","CONTRAST","CONTRIBUTE","CONTRIBUTION","CONTROL","CONVENTION","CONVERSATION","COPY","CORNER","CORPORATE","CORRECT","COS","COST","COULD","COUNCIL","COUNT","COUNTRY","COUNTY","COUPLE","COURSE","COURT","COVER","CREATE","CREATION","CREDIT","CRIME","CRIMINAL","CRISIS","CRITERION","CRITICAL","CRITICISM","CROSS","CROWD","CRY","CULTURAL","CULTURE","CUP","CURRENT","CURRENTLY","CURRICULUM","CUSTOMER","CUT","DAMAGE","DANGER","DANGEROUS","DARK","DATA","DATE","DAUGHTER","DAY","DEAD","DEAL","DEATH","DEBATE","DEBT","DECADE","DECIDE","DECISION","DECLARE","DEEP","DEFENCE","DEFENDANT","DEFINE","DEFINITION","DEGREE","DELIVER","DEMAND","DEMOCRATIC","DEMONSTRATE","DENY","DEPARTMENT","DEPEND","DEPUTY","DERIVE","DESCRIBE","DESCRIPTION","DESIGN","DESIRE","DESK","DESPITE","DESTROY","DETAIL","DETAILED","DETERMINE","DEVELOP","DEVELOPMENT","DEVICE","DIE","DIFFERENCE","DIFFERENT","DIFFICULT","DIFFICULTY","DINNER","DIRECT","DIRECTION","DIRECTLY","DIRECTOR","DISAPPEAR","DISCIPLINE","DISCOVER","DISCUSS","DISCUSSION","DISEASE","DISPLAY","DISTANCE","DISTINCTION","DISTRIBUTION","DISTRICT","DIVIDE","DIVISION","DO","DOCTOR","DOCUMENT","DOG","DOMESTIC","DOOR","DOUBLE","DOUBT","DOWN","DRAW","DRAWING","DREAM","DRESS","DRINK","DRIVE","DRIVER","DROP","DRUG","DRY","DUE","DURING","DUTY","EACH","EAR","EARLY","EARN","EARTH","EASILY","EAST","EASY","EAT","ECONOMIC","ECONOMY","EDGE","EDITOR","EDUCATION","EDUCATIONAL","EFFECT","EFFECTIVE","EFFECTIVELY","EFFORT","EGG","EITHER","ELDERLY","ELECTION","ELEMENT","ELSE","ELSEWHERE","EMERGE","EMPHASIS","EMPLOY","EMPLOYEE","EMPLOYER","EMPLOYMENT","EMPTY","ENABLE","ENCOURAGE","END","ENEMY","ENERGY","ENGINE","ENGINEERING","ENJOY","ENOUGH","ENSURE","ENTER","ENTERPRISE","ENTIRE","ENTIRELY","ENTITLE","ENTRY","ENVIRONMENT","ENVIRONMENTAL","EQUAL","EQUALLY","EQUIPMENT","ERROR","ESCAPE","ESPECIALLY","ESSENTIAL","ESTABLISH","ESTABLISHMENT","ESTATE","ESTIMATE","EVEN","EVENING","EVENT","EVENTUALLY","EVER","EVERY","EVERYBODY","EVERYONE","EVERYTHING","EVIDENCE","EXACTLY","EXAMINATION","EXAMINE","EXAMPLE","EXCELLENT","EXCEPT","EXCHANGE","EXECUTIVE","EXERCISE","EXHIBITION","EXIST","EXISTENCE","EXISTING","EXPECT","EXPECTATION","EXPENDITURE","EXPENSE","EXPENSIVE","EXPERIENCE","EXPERIMENT","EXPERT","EXPLAIN","EXPLANATION","EXPLORE","EXPRESS","EXPRESSION","EXTEND","EXTENT","EXTERNAL","EXTRA","EXTREMELY","EYE","FACE","FACILITY","FACT","FACTOR","FACTORY","FAIL","FAILURE","FAIR","FAIRLY","FAITH","FALL","FAMILIAR","FAMILY","FAMOUS","FAR","FARM","FARMER","FASHION","FAST","FATHER","FAVOUR","FEAR","FEATURE","FEE","FEEL","FEELING","FEMALE","FEW","FIELD","FIGHT","FIGURE","FILE","FILL","FILM","FINAL","FINALLY","FINANCE","FINANCIAL","FIND","FINDING","FINE","FINGER","FINISH","FIRE","FIRM","FIRST","FISH","FIT","FIX","FLAT","FLIGHT","FLOOR","FLOW","FLOWER","FLY","FOCUS","FOLLOW","FOLLOWING","FOOD","FOOT","FOOTBALL","FOR","FORCE","FOREIGN","FOREST","FORGET","FORM","FORMAL","FORMER","FORWARD","FOUNDATION","FREE","FREEDOM","FREQUENTLY","FRESH","FRIEND","FROM","FRONT","FRUIT","FUEL","FULL","FULLY","FUNCTION","FUND","FUNNY","FURTHER","FUTURE","GAIN","GAME","GARDEN","GAS","GATE","GATHER","GENERAL","GENERALLY","GENERATE","GENERATION","GENTLEMAN","GET","GIRL","GIVE","GLASS","GO","GOAL","GOD","GOLD","GOOD","GOVERNMENT","GRANT","GREAT","GREEN","GREY","GROUND","GROUP","GROW","GROWING","GROWTH","GUEST","GUIDE","GUN","HAIR","HALF","HALL","HAND","HANDLE","HANG","HAPPEN","HAPPY","HARD","HARDLY","HATE","HAVE","HE","HEAD","HEALTH","HEAR","HEART","HEAT","HEAVY","HELL","HELP","HENCE","HER","HERE","HERSELF","HIDE","HIGH","HIGHLY","HILL","HIM","HIMSELF","HIS","HISTORICAL","HISTORY","HIT","HOLD","HOLE","HOLIDAY","HOME","HOPE","HORSE","HOSPITAL","HOT","HOTEL","HOUR","HOUSE","HOUSEHOLD","HOUSING","HOW","HOWEVER","HUGE","HUMAN","HURT","HUSBAND","I","IDEA","IDENTIFY","IF","IGNORE","ILLUSTRATE","IMAGE","IMAGINE","IMMEDIATE","IMMEDIATELY","IMPACT","IMPLICATION","IMPLY","IMPORTANCE","IMPORTANT","IMPOSE","IMPOSSIBLE","IMPRESSION","IMPROVE","IMPROVEMENT","IN","INCIDENT","INCLUDE","INCLUDING","INCOME","INCREASE","INCREASED","INCREASINGLY","INDEED","INDEPENDENT","INDEX","INDICATE","INDIVIDUAL","INDUSTRIAL","INDUSTRY","INFLUENCE","INFORM","INFORMATION","INITIAL","INITIATIVE","INJURY","INSIDE","INSIST","INSTANCE","INSTEAD","INSTITUTE","INSTITUTION","INSTRUCTION","INSTRUMENT","INSURANCE","INTEND","INTENTION","INTEREST","INTERESTED","INTERESTING","INTERNAL","INTERNATIONAL","INTERPRETATION","INTERVIEW","INTO","INTRODUCE","INTRODUCTION","INVESTIGATE","INVESTIGATION","INVESTMENT","INVITE","INVOLVE","IRON","IS","ISLAND","ISSUE","IT","ITEM","ITS","ITSELF","JOB","JOIN","JOINT","JOURNEY","JUDGE","JUMP","JUST","JUSTICE","KEEP","KEY","KID","KILL","KIND","KING","KITCHEN","KNEE","KNOW","KNOWLEDGE","LABOUR","LACK","LADY","LAND","LANGUAGE","LARGE","LARGELY","LAST","LATE","LATER","LATTER","LAUGH","LAUNCH","LAW","LAWYER","LAY","LEAD","LEADER","LEADERSHIP","LEADING","LEAF","LEAGUE","LEAN","LEARN","LEAST","LEAVE","LEFT","LEG","LEGAL","LEGISLATION","LENGTH","LESS","LET","LETTER","LEVEL","LIABILITY","LIBERAL","LIBRARY","LIE","LIFE","LIFT","LIGHT","LIKE","LIKELY","LIMIT","LIMITED","LINE","LINK","LIP","LIST","LISTEN","LITERATURE","LITTLE","LIVE","LIVING","LOAN","LOCAL","LOCATION","LONG","LOOK","LORD","LOSE","LOSS","LOT","LOVE","LOVELY","LOW","LUNCH","MACHINE","MAGAZINE","MAIN","MAINLY","MAINTAIN","MAJOR","MAJORITY","MAKE","MALE","MAN","MANAGE","MANAGEMENT","MANAGER","MANNER","MANY","MAP","MARK","MARKET","MARRIAGE","MARRIED","MARRY","MASS","MASTER","MATCH","MATERIAL","MATTER","MAY","MAYBE","ME","MEAL","MEAN","MEANING","MEANS","MEANWHILE","MEASURE","MECHANISM","MEDIA","MEDICAL","MEET","MEETING","MEMBER","MEMBERSHIP","MEMORY","MENTAL","MENTION","MERELY","MESSAGE","METAL","METHOD","MIDDLE","MIGHT","MILE","MILITARY","MILK","MIND","MINE","MINISTER","MINISTRY","MINUTE","MISS","MISTAKE","MODEL","MODERN","MODULE","MOMENT","MONEY","MONTH","MORE","MORNING","MOST","MOTHER","MOTION","MOTOR","MOUNTAIN","MOUTH","MOVE","MOVEMENT","MUCH","MURDER","MUSEUM","MUSIC","MUST","MY","MYSELF","NAME","NARROW","NATION","NATIONAL","NATURAL","NATURE","NEAR","NEARLY","NECESSARILY","NECESSARY","NECK","NEED","NEGOTIATION","NEIGHBOUR","NEITHER","NETWORK","NEVER","NEVERTHELESS","NEW","NEWS","NEWSPAPER","NEXT","NICE","NIGHT","NO","NOBODY","NOD","NOISE","NONE","NOR","NORMAL","NORMALLY","NORTH","NORTHERN","NOSE","NOT","NOTE","NOTHING","NOTICE","NOTION","NOW","NUCLEAR","NUMBER","NURSE","OBJECT","OBJECTIVE","OBSERVATION","OBSERVE","OBTAIN","OBVIOUS","OBVIOUSLY","OCCASION","OCCUR","ODD","OF","OFF","OFFENCE","OFFER","OFFICE","OFFICER","OFFICIAL","OFTEN","OIL","OKAY","OLD","ON","ONCE","ONE","ONLY","ONTO","OPEN","OPERATE","OPERATION","OPINION","OPPORTUNITY","OPPOSITION","OPTION","OR","ORDER","ORDINARY","ORGANISATION","ORGANISE","ORGANIZATION","ORIGIN","ORIGINAL","OTHER","OTHERWISE","OUGHT","OUR","OURSELVES","OUT","OUTCOME","OUTPUT","OUTSIDE","OVER","OVERALL","OWN","OWNER","PACKAGE","PAGE","PAIN","PAINT","PAINTING","PAIR","PANEL","PAPER","PARENT","PARK","PARLIAMENT","PART","PARTICULAR","PARTICULARLY","PARTLY","PARTNER","PARTY","PASS","PASSAGE","PAST","PATH","PATIENT","PATTERN","PAY","PAYMENT","PEACE","PENSION","PEOPLE","PER","PERCENT","PERFECT","PERFORM","PERFORMANCE","PERHAPS","PERIOD","PERMANENT","PERSON","PERSONAL","PERSUADE","PHASE","PHONE","PHOTOGRAPH","PHYSICAL","PICK","PICTURE","PIECE","PLACE","PLAN","PLANNING","PLANT","PLASTIC","PLATE","PLAY","PLAYER","PLEASE","PLEASURE","PLENTY","PLUS","POCKET","POINT","POLICE","POLICY","POLITICAL","POLITICS","POOL","POOR","POPULAR","POPULATION","POSITION","POSITIVE","POSSIBILITY","POSSIBLE","POSSIBLY","POST","POTENTIAL","POUND","POWER","POWERFUL","PRACTICAL","PRACTICE","PREFER","PREPARE","PRESENCE","PRESENT","PRESIDENT","PRESS","PRESSURE","PRETTY","PREVENT","PREVIOUS","PREVIOUSLY","PRICE","PRIMARY","PRIME","PRINCIPLE","PRIORITY","PRISON","PRISONER","PRIVATE","PROBABLY","PROBLEM","PROCEDURE","PROCESS","PRODUCE","PRODUCT","PRODUCTION","PROFESSIONAL","PROFIT","PROGRAM","PROGRAMME","PROGRESS","PROJECT","PROMISE","PROMOTE","PROPER","PROPERLY","PROPERTY","PROPORTION","PROPOSE","PROPOSAL","PROSPECT","PROTECT","PROTECTION","PROVE","PROVIDE","PROVIDED","PROVISION","PUB","PUBLIC","PUBLICATION","PUBLISH","PULL","PUPIL","PURPOSE","PUSH","PUT","QUALITY","QUARTER","QUESTION","QUICK","QUICKLY","QUIET","QUITE","RACE","RADIO","RAILWAY","RAIN","RAISE","RANGE","RAPIDLY","RARE","RATE","RATHER","REACH","REACTION","READ","READER","READING","READY","REAL","REALISE","REALITY","REALIZE","REALLY","REASON","REASONABLE","RECALL","RECEIVE","RECENT","RECENTLY","RECOGNISE","RECOGNITION","RECOGNIZE","RECOMMEND","RECORD","RECOVER","RED","REDUCE","REDUCTION","REFER","REFERENCE","REFLECT","REFORM","REFUSE","REGARD","REGION","REGIONAL","REGULAR","REGULATION","REJECT","RELATE","RELATION","RELATIONSHIP","RELATIVE","RELATIVELY","RELEASE","RELEVANT","RELIEF","RELIGION","RELIGIOUS","RELY","REMAIN","REMEMBER","REMIND","REMOVE","REPEAT","REPLACE","REPLY","REPORT","REPRESENT","REPRESENTATION","REPRESENTATIVE","REQUEST","REQUIRE","REQUIREMENT","RESEARCH","RESOURCE","RESPECT","RESPOND","RESPONSE","RESPONSIBILITY","RESPONSIBLE","REST","RESTAURANT","RESULT","RETAIN","RETURN","REVEAL","REVENUE","REVIEW","REVOLUTION","RICH","RIDE","RIGHT","RING","RISE","RISK","RIVER","ROAD","ROCK","ROLE","ROLL","ROOF","ROOM","ROUND","ROUTE","ROW","ROYAL","RULE","RUN","RURAL","SAFE","SAFETY","SALE","SAME","SAMPLE","SATISFY","SAVE","SAY","SCALE","SCENE","SCHEME","SCHOOL","SCIENCE","SCIENTIFIC","SCIENTIST","SCORE","SCREEN","SEA","SEARCH","SEASON","SEAT","SECOND","SECONDARY","SECRETARY","SECTION","SECTOR","SECURE","SECURITY","SEE","SEEK","SEEM","SELECT","SELECTION","SELL","SEND","SENIOR","SENSE","SENTENCE","SEPARATE","SEQUENCE","SERIES","SERIOUS","SERIOUSLY","SERVANT","SERVE","SERVICE","SESSION","SET","SETTLE","SETTLEMENT","SEVERAL","SEVERE","SEX","SEXUAL","SHAKE","SHALL","SHAPE","SHARE","SHE","SHEET","SHIP","SHOE","SHOOT","SHOP","SHORT","SHOT","SHOULD","SHOULDER","SHOUT","SHOW","SHUT","SIDE","SIGHT","SIGN","SIGNAL","SIGNIFICANCE","SIGNIFICANT","SILENCE","SIMILAR","SIMPLE","SIMPLY","SINCE","SING","SINGLE","SIR","SISTER","SIT","SITE","SITUATION","SIZE","SKILL","SKIN","SKY","SLEEP","SLIGHTLY","SLIP","SLOW","SLOWLY","SMALL","SMILE","SO","SOCIAL","SOCIETY","SOFT","SOFTWARE","SOIL","SOLDIER","SOLICITOR","SOLUTION","SOME","SOMEBODY","SOMEONE","SOMETHING","SOMETIMES","SOMEWHAT","SOMEWHERE","SON","SONG","SOON","SORRY","SORT","SOUND","SOURCE","SOUTH","SOUTHERN","SPACE","SPEAK","SPEAKER","SPECIAL","SPECIES","SPECIFIC","SPEECH","SPEED","SPEND","SPIRIT","SPORT","SPOT","SPREAD","SPRING","STAFF","STAGE","STAND","STANDARD","STAR","START","STATE","STATEMENT","STATION","STATUS","STAY","STEAL","STEP","STICK","STILL","STOCK","STONE","STOP","STORE","STORY","STRAIGHT","STRANGE","STRATEGY","STREET","STRENGTH","STRIKE","STRONG","STRONGLY","STRUCTURE","STUDENT","STUDIO","STUDY","STUFF","STYLE","SUBJECT","SUBSTANTIAL","SUCCEED","SUCCESS","SUCCESSFUL","SUCH","SUDDENLY","SUFFER","SUFFICIENT","SUGGEST","SUGGESTION","SUITABLE","SUM","SUMMER","SUN","SUPPLY","SUPPORT","SUPPOSE","SURE","SURELY","SURFACE","SURPRISE","SURROUND","SURVEY","SURVIVE","SWITCH","SYSTEM","TABLE","TAKE","TALK","TALL","TAPE","TARGET","TASK","TAX","TEA","TEACH","TEACHER","TEACHING","TEAM","TEAR","TECHNICAL","TECHNIQUE","TECHNOLOGY","TELEPHONE","TELEVISION","TELL","TEMPERATURE","TEND","TERM","TERMS","TERRIBLE","TEST","TEXT","THAN","THANK","THANKS","THAT","THE","THEATRE","THEIR","THEM","THEME","THEMSELVES","THEN","THEORY","THERE","THEREFORE","THESE","THEY","THIN","THING","THINK","THIS","THOSE","THOUGH","THOUGHT","THREAT","THREATEN","THROUGH","THROUGHOUT","THROW","THUS","TICKET","TIME","TINY","TITLE","TO","TODAY","TOGETHER","TOMORROW","TONE","TONIGHT","TOO","TOOL","TOOTH","TOP","TOTAL","TOTALLY","TOUCH","TOUR","TOWARDS","TOWN","TRACK","TRADE","TRADITION","TRADITIONAL","TRAFFIC","TRAIN","TRAINING","TRANSFER","TRANSPORT","TRAVEL","TREAT","TREATMENT","TREATY","TREE","TREND","TRIAL","TRIP","TROOP","TROUBLE","TRUE","TRUST","TRUTH","TRY","TURN","TWICE","TYPE","TYPICAL","UNABLE","UNDER","UNDERSTAND","UNDERSTANDING","UNDERTAKE","UNEMPLOYMENT","UNFORTUNATELY","UNION","UNIT","UNITED","UNIVERSITY","UNLESS","UNLIKELY","UNTIL","UP","UPON","UPPER","URBAN","US","USE","USED","USEFUL","USER","USUAL","USUALLY","VALUE","VARIATION","VARIETY","VARIOUS","VARY","VAST","VEHICLE","VERSION","VERY","VIA","VICTIM","VICTORY","VIDEO","VIEW","VILLAGE","VIOLENCE","VISION","VISIT","VISITOR","VITAL","VOICE","VOLUME","VOTE","WAGE","WAIT","WALK","WALL","WANT","WAR","WARM","WARN","WASH","WATCH","WATER","WAVE","WAY","WE","WEAK","WEAPON","WEAR","WEATHER","WEEK","WEEKEND","WEIGHT","WELCOME","WELFARE","WELL","WEST","WESTERN","WHAT","WHATEVER","WHEN","WHERE","WHEREAS","WHETHER","WHICH","WHILE","WHILST","WHITE","WHO","WHOLE","WHOM","WHOSE","WHY","WIDE","WIDELY","WIFE","WILD","WILL","WIN","WIND","WINDOW","WINE","WING","WINNER","WINTER","WISH","WITH","WITHDRAW","WITHIN","WITHOUT","WOMAN","WONDER","WONDERFUL","WOOD","WORD","WORK","WORKER","WORKING","WORKS","WORLD","WORRY","WORTH","WOULD","WRITE","WRITER","WRITING","WRONG","YARD","YEAH","YEAR","YES","YESTERDAY","YET","YOU","YOUNG","YOUR","YOURSELF","YOUTH"]
# y = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,'I': 9,'J': 10,'K': 11,'L': 12,'M': 13,'N': 14,'O': 15,'P': 16,'Q': 17,'R': 18,'S': 19,'T': 20,'U': 21,'V': 22,'W': 23,'X': 24,'Y': 25,'Z': 26}
#
# def tri():
#     l = []
#     for i in range(1, 100):
#         l.append(0.5*i*(i+1))
#     return l
#
# def main():
#     l = tri()
#     count = 0
#     for word in x:
#         sum = 0
#         for letter in word:
#             sum += int(y[letter])
#         if sum in l:
#             count += 1
#     print(count)
#
# main()

# -- 43 -- Sub-string divisibility:
# def pand():
#     l = []
#     new = []
#     n = '0123456789'
#     l += [int(''.join(i)) for i in itertools.permutations(n, 10) if i[0] != '0']
#     return l
#
# def check(num):
#     p = [2,3,5,7,11,13,17]
#     for i in range(1,len(str(num))-2):
#         if int(str(num)[i:i+3]) % p[i-1] != 0:
#             return False
#     else:
#         return True
#
# def main():
#     l = pand()
#     sum = 0
#     for i in range(len(l)):
#         if check(l[i]):
#             sum += l[i]
#     print(sum)
#
# main()

# -- 44 -- Pentagon numbers:
# def pentagon(n):
#     if (1+(24*n+1)**0.5) % 6 == 0:
#         return True
#     else:
#         return False
#
# for i in range(1,100000):
#     for j in range(1,i):
#         a = i*(3*i-1)/2
#         b = j*(3*j-1)/2
#         if pentagon(a+b) and pentagon(a-b):
#             print(a-b)
#             break

# -- 45 -- Triangular, pentagonal, and hexagonal:
# a = 100000
# t = [n*(n+1)/2 for n in range(2,a+2)]
#
# for i in range(0,100000):
#     if (1+(1+24*t[i])**0.5) % 6 == 0 and (1+(1+8*t[i])**0.5) % 4 == 0:
#         print(t[i])

# -- 48 -- Self powers: 1 - 1000
# def eqn(n):
#     return n**n
#
# def sumP(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += eqn(i)
#     return sum
#
# def main():
#     num = sumP(1000)
#     print(str(num)[-10:])
#
# main()

# -- 49 -- Prime permutations:
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#
#     for i in range(3,int(n**0.5)+2, 2):
#         if n % i == 0 or n % 2 == 0:
#             return False
#     else:
#         return True
#
# for i in range(1000,10000):
#     if sorted(str(i)) == sorted(str(i+3330)) == sorted(str(i+6660)):
#         if prime(i) and prime(i+3330) and prime(i+6660):
#             print(str(i)+str(i+3330)+str(i+6660))

# -- 52 -- Permutated multiples:
# for i in range(10,10000000):
#     if sorted(str(i)) == sorted(str(i*2)) == sorted(str(i*3)) == sorted(str(i*4)) == sorted(str(i*5)) == sorted(str(i*6)):
#         print(i)
#         break

# -- 53 -- Combinatoric selections:
# def nCr(n,r):
#     f = math.factorial
#     return f(n)/(f(r)*f(n-r))
#
# def main():
#     count = 0
#     for i in range(1,101):
#         for j in range(1,i+1):
#             if nCr(i,j) > 1000000:
#                 count += 1
#                 print(nCr(i,j))
#     print(count)
#
# main()

# -- 55 -- Lychrel numbers:
# def lyc(n):
#     for i in range(50):
#         num = n + int(str(n)[::-1])
#         if num == int(str(num)[::-1]):
#             return False
#         n = num
#     else:
#         return True
#
# count = 0
# for i in range(1,10001):
#     if lyc(i):
#         print(i)
#         count += 1
# print(count)

# -- 56 -- Powerful digit sum
# def cal(a,b):
#     return a**b
#
# def sumNum(n):
#     sum = 0
#     for i in range(len(n)):
#         sum += int(n[i])
#     return sum
#
# l = []
# for a in range(1,100):
#     for b in range(1,100):
#         l.append(sumNum(str(cal(a,b))))
# print(max(l))


# -- 97 -- Large non-Mersenne prime:
# def main():
#     print(((28433*(2**7830457))+1)%10000000000)
