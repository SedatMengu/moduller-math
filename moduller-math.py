# modül nedir ? çok kullanılan fonksiyonların bir araya geldiği paketlere modül denir.

import math                         # matematik işlemlerine ait moduldür. modülü komple çağırmak için kullanılır.

sonuc = math.factorial(5)
sonuc2 = math.sqrt(81)
sonuc3 = math.fabs(-65)

print(sonuc)                        # / 120 
print(sonuc2)                       # / 9
print(sonuc3)                       # / 65 


# eğer bütün modül yerine sadece bir veya birden fonksiynu yüklemek istersek

from math import factorial , sqrt

#eğer sadece bir fonksiyonu çağırdıysak fonksiyon kullanımı şu şekildedir.

sonuc4 = factorial(3)              
print(sonuc4)                        # / 6

# modülü değilde bütün fonksiyonları çağırmak istersek : 

from math import *

# modülü komple import etmediğimiz için math. kısmını kullanmadık.

sonuc5 = sqrt(64)
print(sonuc5)                       # / 8

# kendi fonksiyonlarımızı hazırlayıp bir modül yapabiliriz. ,(javascript ekler gibi ekliyoruz)
# uzun modül isimlerinden kurtulmak için 

import modul-math as m        # modül ismini bu şekilde kısaltabiliriz.
import modul-math             # modül ismini kısaltmadan bu şekilde de bırakabiliriz.

sonuc6=m.cember_cevresi(6)
print(sonuc6)                       # / 37.68

# 1  - math.acos() fonksiyonu     :
# 2  - math.acosh() fonksiyonu    :
# 3  - math.asin() fonksiyonu     :
# 4  - math.asinh() fonksiyonu    :
# 5  - math.atan() fonksiyonu     :
# 6  - math.atan2() fonksiyonu    :
# 7  - math.atanh() fonksiyonu    :
# 8  - math.ceil() fonksiyonu     :
# 9  - math.comb() fonksiyonu     :
# 10 - math.copysign() fonksiyonu :
# 11 - math.cos fonksiyonu        :
# 12 - math.cosh() fonksiyonu     :
# 13 - math.degrees() fonksiyonu  :
# 14 - math.dist() fonksiyonu     :
# 15 - math.erf fonksiyonu        :
# 16 - math.erfc fonksiyonu       :
# 17 - math.exp fonksiyonu        :
# 18 - math.expm1 fonksiyonu      :
# 19 - math.fabs fonksiyonu       :
# 20 - math.factorial fonksiyonu  :
# 21 - math.floor fonksiyonu      :
# 22 - math.fmod fonksiyonu       :
# 23 - math.frexp fonksiyonu      :
# 24 - math.fsum fonksiyonu       :
# 25 - math.gamma fonksiyonu      :
# 26 - math.gcd fonksiyonu        :
# 27 - math.hypot fonksiyonu      :
# 28 - math.isclose fonksiyonu    :
# 29 - math.isfinite fonksiyonu   :
# 30 - math.isinf fonksiyonu      :
# 31 - math.isnan fonksiyonu      :
# 32 - math.isqrt fonksiyonu      :
# 33 - math.lcm fonksiyonu        :
# 34 - math.ldexp fonksiyonu      :
# 35 - math.lgamma fonksiyonu     :
# 36 - math.log fonksiyonu        :
# 37 - math.log10 fonksiyonu      :
# 38 - math.log1p fonksiyonu      :
# 39 - math.log2 fonksiyonu       :
# 40 - math.modf fonksiyonu       :
# 41 - math.nextafter fonksiyonu  :
# 42 - math.perm fonksiyonu       :
# 43 - math.pow fonksiyonu        :
# 44 - math.prod fonksiyonu       :
# 45 - math.radians fonksiyonu    :
# 46 - math.remainder fonksiyonu  :
# 47 - math.sin fonksiyonu        :
# 48 - math.sinh fonksiyonu       :
# 49 - math.sqrt fonksiyonu       :
# 50 - math.tan fonksiyonu        :
# 51 - math.tanh fonksiyonu       :
# 52 - math.trunc fonksiyonu      :
# 53 - math.ulp fonksiyonu        :