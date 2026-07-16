def numput(prompt, default=0, do=int,use=input):
  try:
    d = do(use(prompt))
  except:
    print(f"Non-numberic value - defaulting to {default}")
    d = default
  return d
import time
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

rule = {}
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
      print("[INFO]:", "Normal user accessing ...")
      print("Entering pin ...")
      time.sleep(1.5)
      if rule.get('Code_attempts_count', 20) < 1:
         print("[ERROR]:", "Normal user cannot access using PIN code!")
         continue
      print("successful")
      time.sleep(0.4)
      print("Getting his money $100 USD ...")
      time.sleep(0.9)
      if rule.get('Max_money_tranication', 1000000) < 100:
         print("[ERROR]:", "Normal user cannot get his money using money value $100!")
         continue
      if rule.get('Transicate_per_minute', 20) < 1:
         print("[ERROR]:", "Normal user cannot get his money because he done 1 transaction!")
         continue
      print("successful")
      time.sleep(2)
      print("[INFO]: Attacker 1 coming!")
      print("Entering pin ... 7463", end="")
      for z in [1111, 1234, 5715, 9999, 3846, 1027, 2836, 9876, 2319]:
           time.sleep(0.2)
           print(f", {z}", end="")
           
      print()
      if rule.get('Code_attempts_count', 20) < 10:
         print("Attacker cannot access using PIN code!")
         print("successfully protected money!")
      else:
         print("[ERROR]: Attacker scammed your money!")
         continue
      time.sleep(3)
      print("[INFO]: Attacker 2 coming!")
      print("Entering pin ... 2859")
      time.sleep(1.2)
      print("success")
      if rule.get('Max_money_tranication', 1000000) < 100000:
         print("Attacker cannot get money using $100000 amount!")
         print("successfully protected money!")
      else:
         print("[ERROR]: Attacker scammed your money!")
         continue
      time.sleep(2.5)
      print("[INFO]: Attacker 3 coming!")
      print("Entering pin ... 2859")
      time.sleep(0.92)
      print("success")
      for l in range(1, 16):
         print("Getting $100 USD ...")
         time.sleep(0.7)
         if rule.get('Transicate_per_minute', 20) < l:
            print(f"Attacker cannot transaction money repeated {l} times!")
            print("successfully protected money!")
            break
         else:
            print("success")
      print("[ERROR]: Attacker scammed your money!") if l == 15 else None
            
   else:
      print(do)
print("Bye!")
