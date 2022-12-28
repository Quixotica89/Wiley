price = float(0)
size = input("What size coffe would you like small ,medium, or large?")
if size.lower() == "small":
   price = price + 2
if size.lower() == "medium":
    price = price + 3
if size.lower() == "large":
    price = price + 4    
# prices={'small':2,'medium':3,'large':4,'espresso':0.5,'coldpressed':1,'syrup':0.5}
type = input("Do you want brewed, espresso, or coldpressed?")
if type.lower() == "espresso":
    price = price + 0.5
if type.lower() == "coldpressed":
    price = price + 1    
syrup = input("Do you want flavoured syrup, yes or no?")
if syrup.lower() == "yes":
    flavour = input("Would you like hazelnut, caramel, or vanilla?")
    price = price + 0.5
else:
    flavour = "no flavoured"
print("You asked for a " + size + " " + type + " coffee with " + flavour + " syrup.")
print("Your coffee costs $" + str(price))
price = round((price * 1.15),2)
print("With a 15% tip, you should give $" + str(price))