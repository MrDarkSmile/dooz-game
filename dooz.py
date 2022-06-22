from random import randint
from colorama import Fore , init
from os import system
init()
home = [i for i in range(1,10)]
me = Fore.GREEN+"×"+Fore.WHITE
bot = Fore.RED+"#"+Fore.WHITE


table = f"""
{home[0]}  |  {home[1]}  |  {home[2]}
{home[3]}  |  {home[4]}  |  {home[5]}
{home[6]}  |  {home[7]}  |  {home[8]}
"""
print(table)


def setx():
  while True:
    x = int(input("enter your block : "))
    if x in home:
      return x
    else:
      print("please choose order blocks")

def sety():
  while True:
    y = randint(1,9)
    if y in home:
      return y


def set_table():
  global table
  table = f"""\r
{home[0]}  |  {home[1]}  |  {home[2]}
{home[3]}  |  {home[4]}  |  {home[5]}
{home[6]}  |  {home[7]}  |  {home[8]}
"""



def score():
  for i in range(0,3):
    if home[i] == home[i+3] and home[i] == home[i+6]:
      if home[i] == me:
        return [True , "You"]
      elif home[i] == bot:
        return [True , "Bot"]
  
  for i in [0,3,6]:
    if home[i] == home[i+1] and home[i] == home[i+2]:
      if home[i] == me:
        return[True , "You"]
      elif home[i] == bot:
        return[True , "Bot"]
    
    
  if (home[0]==home[4] and home[4]==home[8]) or (home[2]==home[4] and home[4]==home[6]):
    if home[4] == me:
      return [True , "You"]
    elif home[4] == bot:
      return [True , "Bot"]
  
  return [False]
  
  

def clear():
  try:
    system("clear")
  except:
    system("cls")

while True:
  x = setx()
  home[x-1] = me
  set_table()
  win = score()
  if win[0] == True:
    print(win[1]+" Win")
    break
  y = sety()
  home[y-1] = bot
  set_table()
  clear()
  print(table)
  win = score()
  if win[0] == True:
    print(win[1]+" Win")
    break