import random
import math
'''
Írj eljárást, mely paraméterben kap 2 egész számot
ezen két szám közötti
páros számok összegét számolja ki az eljárás
'''
import random


def paros_osszeg(min:int, max:int):
    i:int=min
    osszeg:int=0
    while i<= max:
        if i%2==0:
            osszeg +=i
            #elégazás vége
        i+=1
        #ciklus vége

    ## viszatérési érték
    return osszeg #fügvény egy visszatérési érték, aminek van eredménye


 #Írj egy függvényt ami generál 10 db véletlen zámot -10 és 10 között. Számold meg hány negatív szám van közötte. A visszatérési érték a negatív számok


def negativ():
  db:int=0
  i:int=0
  while i<=20:
      szam: int = math.floor(random.random() * 21 -10)
      if szam <0:
          db +=1
      i+=1
  return db

def negativ2():
  db:int=0
  for i in range(0,20,1):
      szam: int = math.floor(random.random() * 21 -10)
      if szam <0:
          db +=1
      #i+=1
  return db


def paros_osszeg2(min:int, max:int):
    osszeg:int=0
    for i in range (min,max,1):
        if i%2==0:
            osszeg +=i
            #elégazás vége
        #ciklus vége
    ## viszatérési érték
    return osszeg #fügvény egy visszatérési érték, aminek van eredménye

#Írj fügvényt amely generél 10 db véletlen számo 12 és 33 között és vissza tér ezek összegével
def veletlen_szam():
    osszeg:int=0
    for i in range (0, 10, 1):
        szamok:int=math.floor(random.random()*(34-12)+12)
        osszeg += szamok
    return osszeg

#Írj fügvényt amely generél 8 db véletlen számot [20 és 50) között és vissza tér ezek közül a legnagyobb számmal
def veletlen2():
    legnagyobb_szam:int=0
    for i in range (0,8,1):
        szam:int=math.floor(random.random()*(50-20)+20)
        if szam>legnagyobb_szam:
            legnagyobb_szam =szam
    return legnagyobb_szam

#Kérjünk be 3 db egész számot a felhasználotól mekkora a számok átlaga?
def egesz_beker():
    osszeg:int=0
    for i in range(0,3,1):
        szam_be: int = int(input(f"Kérem az {i+1}. számot: "))
        osszeg += szam_be
    osszeg =osszeg / 3
    return osszeg

#Kérjünk be egész számokat a felh-tol amiog nullát nem add. Irjuk ki a számok átlagát
def nullas_szamig():
    osszeg:int=0
    i:int=0
    szam_be: int = int(input(f"Kérek az {i + 1} számot: "))
    while not (szam_be ==0):
        szam_be: int = int(input(f"Kérek az {i+1} számot: "))
        osszeg += szam_be
        i+=1
    atlag:int= osszeg /(i-1)
    return atlag






