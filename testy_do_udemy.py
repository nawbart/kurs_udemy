'''stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

res = list(map(lambda i: True if i['indeks'] == 'mWIG40' else False, stocks))


num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

res = list(map(lambda i, j: i%j, num1, num2))
print(res)


fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
def gen(list):
    for el in fnames:
        if el.endswith('.txt'):
            yield el


print(list(gen(fnames)))


def enum(lista):
    a = 0
    for i in lista:
        yield (a, i)
        a += 1


print(list(enum(['TEN', 'CDR', 'BBT'])))



days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']

def dayname(day):
    yield days[day-1]
    yield days[day]
    yield days[day+1]

for pair in dayname(0):
    print(pair)



omega = {(i,j) for i in range(1,7) for j in range(1,7) }
d = len(omega)
ten = {para for para in omega if para[0] + para[1] > 10}
t = len(ten)
res = t/d



print(f'P-stwo: {round(res,2)}')


desc = "Playway: Playway to producent gier komputerowych."
low = desc.lower()

out = low.replace(':',"").replace('.','')

split = out.split()

re = {slowo for slowo in split}

d = len(re)
print(d)


omega = {(i,j) for i in range(1,7) for j in range(1,7)}
o = len(omega)
p = {a for a in omega if (a[0]**2 + a[1]**2) >= 45  }
p_p = len(p)
res = round(p_p/o, 2)
print('P-stwo:', res)


omega = {(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)}
o = len(omega)
pr = {i for i in omega if((i[0] + i[1] + i[2]) % 7 == 0)}
p = len(pr)
probality = round(p/o,2)
print('P-stwo:', probality)


omega = {
    (x, y, z)
    for x in range(1, 7)
    for y in range(1, 7)
    for z in range(1, 7)
}
a = {(x, y, z) for x, y, z in omega if (x**2 + y**2 + z**2) % 3 == 0}
prob = round(len(a) / len(omega), 4)
print(f'P-stwo: {prob}')



#  A – w każdym rzucie wypadnie nieparzysta liczba oczek
omega = {
    (x, y, z)
    for x in range(1, 7)
    for y in range(1, 7)
    for z in range(1, 7)
}
a = {(x, y, z) for x, y, z in omega if (x % 2 & y % 2 & z % 2) != 0}
prob = round(len(a) / len(omega), 4)
print(f'P-stwo: {prob}')



tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]

res = [round(i * (1+tax),2) for i in net_price]
print(res)


pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

res = [round(pv * (1+i)**n, 2) for i in rate]
print(res)




pv = 1000
pv1 = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

res1 = [round(pv * (1+i)**n, 2) for i in rate]

res = [round(i - pv1, 2) for i in res1]

print(res)



data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
res = [[k,v] for k,v in data.items()]
print(res)

res = {k: k**2 for k in range(1,8) }
print(res)


stocks = ['Playway', 'CD Projekt', 'Boombit']
res = {k: len(k) for k in stocks }
print(res)


stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
res = {v: k for k,v in stocks.items() }
print(res)



stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

res = {k: v for k,v in stocks.items() if v > 100}
print(res)


a = [{k: k**j for k in range(1,10)} for j in range(1,4)]
print(a)




indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']

a = { i:{p: None for p in properties} for i in indeks }
print(a)


indeks = ['WIG20', 'mWIG40', 'sWIG80']
a = {i: indeks[i] for i in range(len(indeks))}

print(a)

import calendar

print (calendar.calendar(2020))

import calendar
print (calendar.month(2020, 6))



import datetime

a = datetime.date(2020,6,1)
b = datetime.date(2020,7,18)
print(b-a)


import re


string = 'Python 3.8'
match = re.findall('\d', string)
print(match)


import re
string = '!@#$%^&45wc'
match = re.findall('\w', string)
print(match)


import re


raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"

match = re.findall('[\w\.-]+@[\w\.-]+', raw_text)
print(match)


import re
text = 'Programowanie w języku Python - od A do Z'

match = re.split('\s+', text)
print(match)


import string
print(string.ascii_letters)


import collections
from collections import Counter


items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

print(collections.Counter(items))


import math

def sigmoid(x):
    fx = 1 / (1 + math.exp(-x))
    return fx


import random

random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
print(random.choice(items))


import random

random.seed(15)
random.shuffle(items)
print(items)
*
resu = []

items = ['python', 'java', 'sql', 'c++', 'c']
res = []
res = [random.choice(items) for it in items if it not in res]
print(res)
*




import pickle

ids = ['001', '003', '011']

with open('data.pickle', 'wb') as f:
   pickle.dump(ids, f)



y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

def accuracy(l1, l2):
   a = len(y_pred)

   res = []
   for i in range(a):
      if y_pred[i] == y_true[i]:
       res.append(1)
   b = len(res)
   acc = round(b / a, 4)

   return acc


a = accuracy(y_pred,y_true)
print(a)



def mse(l1, l2):
   a = len(l1)
   min_pow = [(l1[i]-l2[i])**2 for i in range(a)]
   suma = sum(min_pow)
   res = round(suma/a,3)
   return res


y_pred = [10.2, 10.4, 10.8, 11.0]
y_true = [10, 10.5, 11.2, 10.4]


r = mse(y_true, y_pred)
print(r)




def relu(x):
   return max(0, x)

a = relu(4)
print(a)


items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def flatten(lista):
   res = []
   for i in lista:
      for j in i:
         res.append(j)
   return res

a = flatten(items)
print(a)



def transfer_zeros(lista):
   res = []
   for el in lista:
      if el == 0:
         continue
      else:
         res.append(el)

   for i in range((len(lista)- len(res))):
      res.append(0)

   return res

a = transfer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2])
print(a)



def euclidean_distance(l1,l2):
   min_pow = []
   a = len(l1)
   for i in range(a):
      min_pow.append((l2[i] - l1[i])**2)
   suma = sum(min_pow)
   res = suma**(1/2)

   return res

q = euclidean_distance([0, 3], [4, 0])
print(q)



def arange(start, stop, step=1):
   res = []
   for i in range(start, stop, step):
      res.append(i)
   return res



a = arange(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


b = arange(0, 10, 2)
#[0, 2, 4, 6, 8]
print(a)
print(b)


def concat(l1,l2):
   r = len(l1)
   res = [l1[i] + l2[i] for i in range(r)]
   return res





l1 = [[1], [2]]
l2 = [[3], [4]]
a = concat(l1, l2)
print(a)

#[[1, 3], [2, 4]]



def identity(x):

   res = []

   for row in range(0,x):
      temp = []
      for col in range(0,x):
         if row == col:
            temp.append(1)
         else:
            temp.append(0)
      res.append(temp)

   return res


a = identity(3)
print(a)
#[[1, 0, 0], [0, 1, 0], [0, 0, 1]]



def fill_value(w, h, text):

   res = []

   for row in range(0,w):
      temp = []
      for col in range(0,h):
            temp.append(text)
      res.append(temp)

   return res

a = fill_value(2,6,123)
print(a)




def trace(lista):

   res = []
   for row in lista:
      for col in row:
         if row == col:
            res.append(row[col])
         else:
            continue


   return res

a = trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])
print(a)



def trace(lista):

   res =[]
   id = 0
   for row in lista:
         res.append(row[id])
         id +=1
   tr = sum(res)

   return tr

a = trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])
print(a)



def transpose(lista):
   trans = []
   id = 0
   d = len(lista[0])

   for i in range(d):
      res = []
      for row in lista:
         res.append(row[id])
      trans.append(res)
      id += 1

   return trans

a = transpose([[1, 2, 3], [4, 5, 6]])
print(a)
#[[1, 4], [2, 5], [3, 6]]
b = transpose([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
c = transpose([[1, 2], [3, 4], [5, 6]])
print(c)




def max_prob(lista):
   res = []

   id = 0
   for i in lista:
      maks = [max(i)]
      res.append(maks)

   return res



a = max_prob([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]])
print(a)
# [[0.4], [0.9]]

b = max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])
print(b)
# [[0.4], [0.7]]

c = max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.4, 0.3, 0.3]])
print(c)
# [[0.4], [0.7], [0.4]]




def detect_class(lista):
   r = []
   m = []
   res = []
   d = len(lista)
   for i in range(d):
      maks = max(lista[i])
      m.append(maks)

   for i in lista:
      r = []
      for j in i:
         if j in m:
            r.append(1)
         else:
            r.append(0)
      res.append(r)

   return res

a = detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])
print(a)
# [[0, 1, 0, 0], [0, 0, 1, 0]]



def dot_product(l1,l2):
   r = [a*b for a,b in zip(l1,l2)]
   res = sum(r)

   return res


a = dot_product([1, 2], [5, 2])
print(a)



def count_none(lista):
   id = 0
   for i in lista:
      if i == None:
         id += 1
      else:
         continue
   return id


a = count_none([1, None, None, 5, None, 2])
print(a)


def top_n(lista, x):
   res = []
   y = 0
   while y < x:
         m = max(lista)
         res.append(m)
         lista.remove(m)
         y += 1

   return res

# [10, 9, 8]
a = top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3)
print(a)


#f = open("playway.txt", 'r')
#f.close() #1 z opcji

with open("playway.txt", 'r') as moj_plik: # 2 sposob na zamkniecie
    linie = moj_plik.read().splitlines()
    zamkniecia_dni = []
    for idx, linia in enumerate(linie):
        if idx > 0:
            zamkniecia_dni.append(int(linia.split(',')[-2]))

d = len(zamkniecia_dni)
s = sum(zamkniecia_dni)
srednia_zamk_dni = s/d
print(srednia_zamk_dni)
print(type(linie))
print(linie)


lista_WIG = []

with open("indeksy.txt", 'r') as moj_plik:
    for idx, l in enumerate(moj_plik):
        if idx > 0:
            linia = moj_plik.readline()
            if linia.startswith('WIG'):
                lista_WIG.append(linia.strip())
                #lista_WIG.append(linia.replace('\n',''))

print(lista_WIG)

'''






























































































