#Zadanie1

def is_criticality_balanced():
   temperatura = 500
   neurony = 100
   if temperatura > 800000 and neurony < 500:
       return True
   else:
       return False

print(is_criticality_balanced())

#Zadanie2

def reactor_efficiency(voltage, current, theoretical_max_power):

   generated_power = voltagecurrent
   moc_procent = (generated_power/theoretical_max_power)100
   if moc_procent > 30:
       return("czarne")
   elif moc_procent <= 30 and moc_procent > 60:
       return("czerwony")
   elif moc_procent <= 60 and moc_procent > 80:
       return("pomarańczowy")
   else:
       return("zielony")

print(reactor_efficiency(230, 20, 500))

#Zadanie3

def fail_safe(temp, neutrony_produkowane_na_sekundę, prog):

   if tempneutrony_produkowane_na_sekundę < 0.9prog:
       return("LOW")
   elif tempneutrony_produkowane_na_sekundę > 0.1prog:
       return("NORMAL")

print(fail_safe(200,10,300))