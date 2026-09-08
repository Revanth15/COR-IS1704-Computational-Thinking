combos = ((25.50,80,300,100), 
          (39.50,200,500,2000), 
          (59.50,300,1000,3000), 
          (79.50,400,1500,4000), 
          (109.50,800,2000,10000))

print("Please tell us your monthly usage requirements.")
outgoing_calls = int(input("What's the minimum outgoing calls (in mins) you need? "))
sms = int(input("What's the minimum number of SMS/MMS you need? "))
data = float(input("What's the minimum amount of data (in GB)) you need? "))

data_mb = data * 1024

for combo in combos:
    if outgoing_calls <= combo[1] and sms <= combo[2] and data_mb <= combo[3]:
        print("We recommend Combo ", (combos.index(combo) + 1))
        break
    else:
        print("Sorry! We don't have any plan that satisfies your requirements.")
        break