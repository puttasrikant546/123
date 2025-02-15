# welcome my  luxiries car shorrom :
menu =  {
    'tatapunch': 613000,
   'hyundaicreta' : 2200000,
   'marutifronx' : 1300000,
   'mahindra  thar' :1700000,
   'Audi' :  4400000,
   'BMW': 7400000,
   'Honda' : 6300000,
   'landrover=' : 10000000,
   'Kia' : 1100000,
   'ferrari': 30000000,
   'lambargini' : 300000000, 
}

print("Welcome my srikant  super luxiriues car and drive  the future :")
print("check the menu  available the car in  shorrom but out  of menu no available :")
print(f"you have take with loan or  give money directly price will be reduced then your wish  ")
print("tatapunch = 613000\nhyundaicreta = 2200000\nmahindra  thar = 1300000\nAudi = 4400000\nBMW = 7400000\nHonda = 6300000\nLandrover =1000000\nKia= 1100000\nferrari = 3000000:")
# if order two cars then price will be reduced   5 lakhs all  are   available  luxiries cars
order_total  = 0 
item_1 =  input("Enter a name of the  car  you want to order the car = ") 
if item_1  in menu: 
  order_total  +=  menu[item_1] 
  print(f"your item{item_1}  has  been added your order ") 
  order_total  = input("do you have take the car loan or direct case? ")
  print(f"your car warante for three year any problem come free service available didn't pay you :")
else: 
 print(f"order item {item_1}is not available yet !: ")
another_order = input("Do you want  add  another  car? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter a name of the second itom car which you want  ")
    if item_2 in menu:
     order_total =  menu[item_2]
    print(f"your item {item_2} has been added your order ")
    print(f"your car warante  is three year any problem come again for free service ")
else:
  print("order second item{item_2} is not avalaible :")

 










 

