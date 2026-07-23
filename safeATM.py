def numput(prompt, default=0, do=int,use=input):
  try:
    d = do(use(prompt))
  except:
    print(f"Non-numberic value - defaulting to {default}")
    d = default
  return d
import time, random
print("---😉 Secure the ATM! 😎---")
print("Welcome to 'Secure the ATM' game!")
print("Don't let attackers in!")
do = """
1. Add/change/delete rule 'Code_attempts_count'
2. Add/change/delete rule 'Max_money_tranication'
3. Add/change/delete rule 'Transicate_per_minute'
4. Try attacking by hackers & using by actual users it!
5. Show rules you made
6. Exit 
Anything else: Show this"""

rule = {"Transicate_per_minute": 1000, "Code_attempts_count": 60, "Max_money_tranication": 10000000}
def chgrl(nm, vl):
    global rule
    rule[nm] = vl
    print(f"You've been set rule {nm} for {vl}!")

def pin():
   print("WARNING: It will override current one")
   print("Current value:", rule.get('Code_attempts_count', "Not set"))
   chgrl('Code_attempts_count', numput("Set value! ", default=rule.get('Code_attempts_count', 20)))

def mmtrans():
   print("WARNING: It will override current one")
   print("Current value:", rule.get('Max_money_tranication', "Not set"))
   chgrl('Max_money_tranication', numput("Set value! ", default=rule.get('Max_money_tranication', 1000000)))

def tpm():
   print("WARNING: It will override current one")
   print("Current value:", rule.get('Transicate_per_minute', "Not set"))
   chgrl('Transicate_per_minute', numput("Set value! ", default=rule.get('Transicate_per_minute', 20)))

print(do)
while 1:
   x = numput("\nSelection (1~6): ")
   if x == 6:
      break
   elif x == 1:
      pin()
   elif x == 2:
     mmtrans()
   elif x == 3:
     tpm()
   elif x == 5:
     for m, y in rule.items():
        print(f"Rule: {m}, Value: {y}")
     print()
   elif x == 4:
      print("[INFO]:", f"Normal user accessing ... Name: {random.choice(["alice", "john", "pal", "alex", "steve", "max", "eric", "biff", "kipper"]) + str(random.randint(1000, 9999))}")
      print("Entering pin ...")
      time.sleep(1.5)
      pin_try = 5 if not random.randint(0, 5) else random.randint(1, 2)
      if pin_try == 5:
         print("User panicked! He forgot his pin and entered 5 times!")
      if rule.get('Code_attempts_count', 20) < pin_try:
         print("[ERROR]:", "Normal user cannot access using PIN code! Tries count:", pin_try)
         continue
      print("successful")
      time.sleep(0.4)
      dood = random.randint(1, random.randint(4, 10))
      print("User requests", dood, "transition")
      for ac in range(1, dood+1):
          a = random.randint(50, 200)
          print(f"Getting his money ${a} USD ...")
          time.sleep(0.9)
          if rule.get('Max_money_tranication', 1000000) < a:
             print("[ERROR]:", f"Normal user cannot get his money using money value ${a}!")
             continue
          if rule.get('Transicate_per_minute', 20) < ac:
             print("[ERROR]:", f"Normal user cannot get his money because he done {ac} transaction!")
             continue
      print("successful")
      time.sleep(2)
      print("[INFO]: Attacker 1 coming!")
      tried = random.randint(10, 50)
      print("Entering pin ... 7463", end="")
      for _ in "s"*tried:
           time.sleep(0.2)
           z = random.randint(1000, 9999)
           print(f", {z if not z == 2859 else 1628}", end="")
           
      print()
      if rule.get('Code_attempts_count', 20) < tried:
         print("Attacker cannot access using PIN code!")
         print("successfully protected money!")
      else:
         print("[ERROR]: Attacker scammed your money!")
         continue
      time.sleep(3)
      print("[INFO]:", f"Normal user accessing ... Name: {random.choice(["alice", "john", "pal", "alex", "steve", "max", "eric", "biff", "kipper"]) + str(random.randint(1000, 9999))}")
      print("Entering pin ...")
      time.sleep(1.5)
      pin_try = 5 if not random.randint(0, 5) else random.randint(1, 2)
      if pin_try == 5:
         print("User panicked! He forgot his pin and entered 5 times!")
      if rule.get('Code_attempts_count', 20) < pin_try:
         print("[ERROR]:", "Normal user cannot access using PIN code! Tries count:", pin_try)
         continue
      print("successful")
      time.sleep(0.4)
      dood = random.randint(1, random.randint(4, 10))
      print("User requests", dood, "transition")
      for ac in range(1, dood+1):
          a = random.randint(50, 200)
          print(f"Getting his money ${a} USD ...")
          time.sleep(0.9)
          if rule.get('Max_money_tranication', 1000000) < a:
             print("[ERROR]:", f"Normal user cannot get his money using money value ${a}!")
             continue
          if rule.get('Transicate_per_minute', 20) < ac:
             print("[ERROR]:", f"Normal user cannot get his money because he done {ac} transaction!")
             continue
      print("successful")
      time.sleep(random.randint(1, 4))
      print("[INFO]: Attacker 2 coming!")
      print("Entering pin ... 2859")
      time.sleep(1.2)
      print("success")
      x = random.randint(100000, 10000000)
      if rule.get('Max_money_tranication', 1000000) < x:
         print(f"Attacker cannot get money using ${x} amount!")
         print("successfully protected money!")
      else:
         print("[ERROR]: Attacker scammed your money!")
         continue
      time.sleep(2.5)
      print("[INFO]:", f"Normal user accessing ... Name: {random.choice(["alice", "john", "pal", "alex", "steve", "max", "eric", "biff", "kipper"]) + str(random.randint(1000, 9999))}")
      print("Entering pin ...")
      time.sleep(1.5)
      pin_try = 5 if not random.randint(0, 5) else random.randint(1, 2)
      if pin_try == 5:
         print("User panicked! He forgot his pin and entered 5 times!")
      if rule.get('Code_attempts_count', 20) < pin_try:
         print("[ERROR]:", "Normal user cannot access using PIN code! Tries count:", pin_try)
         continue
      print("successful")
      time.sleep(0.4)
      dood = random.randint(1, random.randint(4, 10))
      print("User requests", dood, "transition")
      for ac in range(1, dood+1):
          a = random.randint(50, 200)
          print(f"Getting his money ${a} USD ...")
          time.sleep(0.9)
          if rule.get('Max_money_tranication', 1000000) < a:
             print("[ERROR]:", f"Normal user cannot get his money using money value ${a}!")
             continue
          if rule.get('Transicate_per_minute', 1000) < ac:
             print("[ERROR]:", f"Normal user cannot get his money because he done {ac} transaction!")
             continue
      print("successful")
      time.sleep(2)
      print("[INFO]: Attacker 3 coming!")
      print("Entering pin ... 2859")
      time.sleep(0.92)
      print("success")
      cx = random.randint(16, 101)
      for l in range(1, cx):
         print(f"Getting ${random.randint(50, 200)} USD ...")
         time.sleep(0.7)
         if rule.get('Transicate_per_minute', 1000) < l:
            print(f"Attacker cannot transaction money repeated {l} times!")
            print("successfully protected money!")
            break
         else:
            print("success")
      print("[ERROR]: Attacker scammed your money!") if l == cx else None
            
   else:
      print(do)
print("Bye!")
