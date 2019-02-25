test = '2018/10/08 01:06:01 45234921 a34 [INFO Client 16116] @From <Ö*FG*Ö> Sukret: Hi, I would like to buy your Domination Twine Stygian Vise listed for 22 chaos in Delve (stash tab "~b/o 22 chaos"; position: left 1, top 3)'

test.split('@')
my_list = test.split('@')
message = my_list[1]

new_list = message.split()
name = new_list[2]

second_split = message.split('your ')
message_one = second_split[1]

third_split = message_one.split(' listed')

item_name = third_split[0]

fourth_split = message_one.split('for')

message_two = fourth_split[1]

message_two.split('in')

fifth_split= message_two.split('in')
price = fifth_split[0]

location_raw = fifth_split[1]
step1 = location_raw.split('tab')
location_raw = step1[1]
loc_step2 = location_raw.split(')')
loc_step3 = loc_step2[0]
loc_step4 = loc_step3.split('"')
loc_step5 = loc_step4[1]
loc_step6 = loc_step4[2]
loc_step7 = loc_step5 + loc_step6


print(f'Name: {name}\nItem: {item_name}\nTab: {loc_step7}\nPrice: {price}')

#Expected output:
#Name: Sukret:
#Item: Domination Twine Stygian Vise
#Tab: ~b/o 22 chaos; position: left 1, top 3
#Price:  22 chaos 
