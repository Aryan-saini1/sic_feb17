total_land=80
segments=5
land_per_segment=total_land/segments
#tomato 30% give 10 tonnes per acre and 70% gives 12 tonnes per acre at cost 7 per kg
#1 ton=1000kg
tomato_sp=(0.3*16*10+0.7*16*12)*1000*7
potato_sp=16*10*1000*20
cabbage_sp=16*14*1000*24
sunflowers_sp=16*0.7*1000*200
sugarcane_sp=16*45*4000
total_sales=tomato_sp+potato_sp+cabbage_sp+sunflowers_sp+sugarcane_sp
print(f"%-20s ={total_sales}"%("Total Sales"))
#after 11 months farmer won't have sugarcane as it is not chemical free
total_sales_chemfree=tomato_sp+potato_sp+cabbage_sp+sunflowers_sp
print(f"%-20s ={total_sales_chemfree}"%("Total Sales after chemical free production"))