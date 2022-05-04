import math
import numpy as np
import itertools

# -- 1 -- Sum of multiples of 3,5 below 1000:
# def sumY(x, y):
#     n = x // y
#     eqn = int(n*(2*y+(n-1)*y)/2)
#     return eqn
#
# def main():
#     sum3 = sumY(999,3)
#     sum5 = sumY(999,5)
#     sum15 = sumY(999,15)
#     print(sum3 + sum5 - sum15)
#
# main()

# -- 2 -- Sum of even numbers fibo:
# def fibo(n):
#     eqn = int((((1+(5)**0.5)/2)**n - ((1-(5)**0.5)/2)**n)/(5)**0.5)
#     return eqn
#
# def sumFibo(x):
#     total = 0
#     n = 1
#     while True:
#         n += 1
#         if fibo(n) > x:
#             break
#         elif fibo(n) % 2 == 0:
#             total += fibo(n)
#
#     print(total)
# sumFibo(4000000)

# -- 3 -- The largest prime factors of 600851475143:
# def prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
# def primeFactors(n):
#     p = False
#     for i in range(3,int(n**0.5)+1,2):
#         if (n % i == 0) and (prime(i)):
#             p = i
#     print(p)

# primeFactors(600851475143)

# -- 4 -- Largest palindrome product made of two 3-digit numbers:
# def palindrome(n):
#     n = str(n)
#     if n == n[::-1]:
#         return True
#     else:
#         return False
#
# def main():
#     l = []
#     for i in range(999,0,-1):
#         for j in range(999,0,-1):
#             if palindrome(i*j):
#                 l.append(i*j)
#     print(max(l))
# main()

# -- 5 -- Smallest multiple from 1 to 20
# list 1-20 by the multiples of primes
# find the least number of primes to get divided by numbers from 1-20

# -- 6 -- Sum square difference of the first 100 natural numbers
# def sum2(n):
#     eqn = int(n*(n+1)*(2*n+1)/6)
#     return eqn
#
# def sum1(n):
#     eqn = int((n*(n+1)/2)**2)
#     return eqn
#
# def main():
#     ans = sum1(100) - sum2(100)
#     print(ans)
#
# main()

# -- 7 --
# def prime(n):
#     num = 1
#     a = 3
#     while True:
#         for i in range(2,int(a**0.5)+1):
#             if a % i == 0:
#                 break
#         else:
#             num += 1
#
#         if num == n:
#             print(a)
#             break
#         a += 2
#
# prime(10001)

# -- 8 -- Largest product in a series 13
# l = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
#
# def find(l):
#     prodList = []
#     for i in range(len(l)-13):
#         prod = 1
#         for j in range(13):
#             prod *= int(l[j+i])
#         prodList.append(prod)
#     print(max(prodList))
#
# find(l)

# -- 9 -- a + b + c = 1000
# for a in range(1,1000):
#     for b in range(1,1000):
#         c = (a**2 + b**2)**0.5
#         if c.is_integer() and (a + b + c == 1000):
#             print(int(a*b*c))
#             break

# -- 10 -- Sum of primes below 2000000
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
# def main():
#     sumP = 0
#     for i in range(2,2000000):
#         if prime(i):
#             sumP += i
#     print(sumP)
# main()

# -- 12 -- Highly divisible triangular number：
# def divisor(n):
#     l = 0
#     if n % 2 != 0:
#         return l
#     for i in range(1,int(n**0.5)+1):
#         if n % i == 0:
#             l += 2
#     return l
#
# n = 1
# while True:
#     if divisor(int(0.5*n*(n+1))) > 500:
#         print(int(0.5*n*(n+1)))
#         break
#
#     n += 1

# -- 13 -- Large sum:
# l = [37107287533902102798797998220837590246510135740250,
#      46376937677490009712648124896970078050417018260538,
#      74324986199524741059474233309513058123726617309629,
#      91942213363574161572522430563301811072406154908250,
#      23067588207539346171171980310421047513778063246676,
#      89261670696623633820136378418383684178734361726757,
#      28112879812849979408065481931592621691275889832738,
#      44274228917432520321923589422876796487670272189318,
#      47451445736001306439091167216856844588711603153276,
#      70386486105843025439939619828917593665686757934951,
#      62176457141856560629502157223196586755079324193331,
#      64906352462741904929101432445813822663347944758178,
#      92575867718337217661963751590579239728245598838407,
#      58203565325359399008402633568948830189458628227828,
#      80181199384826282014278194139940567587151170094390,
#      35398664372827112653829987240784473053190104293586,
#      86515506006295864861532075273371959191420517255829,
#      71693888707715466499115593487603532921714970056938,
#      54370070576826684624621495650076471787294438377604,
#      53282654108756828443191190634694037855217779295145,
#      36123272525000296071075082563815656710885258350721,
#      45876576172410976447339110607218265236877223636045,
#      17423706905851860660448207621209813287860733969412,
#      81142660418086830619328460811191061556940512689692,
#      51934325451728388641918047049293215058642563049483,
#      62467221648435076201727918039944693004732956340691,
#      15732444386908125794514089057706229429197107928209,
#      55037687525678773091862540744969844508330393682126,
#      18336384825330154686196124348767681297534375946515,
#      80386287592878490201521685554828717201219257766954,
#      78182833757993103614740356856449095527097864797581,
#      16726320100436897842553539920931837441497806860984,
#      48403098129077791799088218795327364475675590848030,
#      87086987551392711854517078544161852424320693150332,
#      59959406895756536782107074926966537676326235447210,
#      69793950679652694742597709739166693763042633987085,
#      41052684708299085211399427365734116182760315001271,
#      65378607361501080857009149939512557028198746004375,
#      35829035317434717326932123578154982629742552737307,
#      94953759765105305946966067683156574377167401875275,
#      88902802571733229619176668713819931811048770190271,
#      25267680276078003013678680992525463401061632866526,
#      36270218540497705585629946580636237993140746255962,
#      24074486908231174977792365466257246923322810917141,
#      91430288197103288597806669760892938638285025333403,
#      34413065578016127815921815005561868836468420090470,
#      23053081172816430487623791969842487255036638784583,
#      11487696932154902810424020138335124462181441773470,
#      63783299490636259666498587618221225225512486764533,
#      67720186971698544312419572409913959008952310058822,
#      95548255300263520781532296796249481641953868218774,
#      76085327132285723110424803456124867697064507995236,
#      37774242535411291684276865538926205024910326572967,
#      23701913275725675285653248258265463092207058596522,
#      29798860272258331913126375147341994889534765745501,
#      18495701454879288984856827726077713721403798879715,
#      38298203783031473527721580348144513491373226651381,
#      34829543829199918180278916522431027392251122869539,
#      40957953066405232632538044100059654939159879593635,
#      29746152185502371307642255121183693803580388584903,
#      41698116222072977186158236678424689157993532961922,
#      62467957194401269043877107275048102390895523597457,
#      23189706772547915061505504953922979530901129967519,
#      86188088225875314529584099251203829009407770775672,
#      11306739708304724483816533873502340845647058077308,
#      82959174767140363198008187129011875491310547126581,
#      97623331044818386269515456334926366572897563400500,
#      42846280183517070527831839425882145521227251250327,
#      55121603546981200581762165212827652751691296897789,
#      32238195734329339946437501907836945765883352399886,
#      75506164965184775180738168837861091527357929701337,
#      62177842752192623401942399639168044983993173312731,
#      32924185707147349566916674687634660915035914677504,
#      99518671430235219628894890102423325116913619626622,
#      73267460800591547471830798392868535206946944540724,
#      76841822524674417161514036427982273348055556214818,
#      97142617910342598647204516893989422179826088076852,
#      87783646182799346313767754307809363333018982642090,
#      10848802521674670883215120185883543223812876952786,
#      71329612474782464538636993009049310363619763878039,
#      62184073572399794223406235393808339651327408011116,
#      66627891981488087797941876876144230030984490851411,
#      60661826293682836764744779239180335110989069790714,
#      85786944089552990653640447425576083659976645795096,
#      66024396409905389607120198219976047599490197230297,
#      64913982680032973156037120041377903785566085089252,
#      16730939319872750275468906903707539413042652315011,
#      94809377245048795150954100921645863754710598436791,
#      78639167021187492431995700641917969777599028300699,
#      15368713711936614952811305876380278410754449733078,
#      40789923115535562561142322423255033685442488917353,
#      44889911501440648020369068063960672322193204149535,
#      41503128880339536053299340368006977710650566631954,
#      81234880673210146739058568557934581403627822703280,
#      82616570773948327592232845941706525094512325230608,
#      22918802058777319719839450180888072429661980811197,
#      77158542502016545090413245809786882778948721859617,
#      72107838435069186155435662884062257473692284509516,
#      20849603980134001723930671666823555245252804609722,
#      53503534226472524250874054075591789781264330331690]
# all = str(sum(l))
# print(all[0:10])

# -- 14 -- Longest Collatz sequence: 1000000
# def collatz(n):
#     if n == 1:
#         return n
#     elif n % 2 == 0:
#         n /= 2
#     else:
#         n = 3*n + 1
#     return n
#
# l = []
# num = []
#
# for i in range(100000,1000001):
#     count = 2
#     num.append(i)
#     while True:
#         if collatz(i) == 1:
#             l.append(count)
#             break
#         else:
#             i = collatz(i)
#             count += 1
# print(num[l.index(max(l))])

# -- 16 -- Power digit sum:
# def power2(n):
#     ans = 1
#     for i in range(1,n+1):
#         ans *= 2
#     return str(ans)
#
# def main():
#     sum = 0
#     for i in range(len(power2(1000))):
#         sum += int(power2(1000)[i])
#     print(sum)
#
# main()

# -- 20 -- Factorial digit sum:
# def fact(n):
#     ans = 1
#     for i in range(1,n+1):
#         ans *= i
#     return(ans)
#
# num = fact(100)
# l = []
# for i in range(len(str(num))):
#     l.append(int(str(num)[i]))
# print(sum(l))

# -- 21 -- Amicable numbers:
# def d(n):
#     sum = 0
#     l = []
#     for i in range(1,n):
#         if n % i == 0:
#             sum += i
#     return sum
#
# def main():
#     l = []
#     l2 = []
#     sum = 0
#     for i in range(1,10000):
#         l.append(d(i))
#         l2.append(d(l[i-1]))
#         if l2[i-1] == i and l2[i-1] != l[i-1]:
#             sum += i
#
#     print(sum)
#
# main()
