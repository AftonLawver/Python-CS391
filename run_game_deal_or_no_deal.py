import deal_or_no_deal
import random 

list_of_money_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200,300, 400, 500,
                        750, 1000, 5000, 10000, 25000,  50000, 75000, 100000, 
                        200000, 300000, 400000, 500000, 750000, 1000000]
list_of_suitcase_objects = []
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 1'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 2'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 3'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 4'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 5'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 6'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 7'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 8'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 9'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 10'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 11'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 12'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 13'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 14'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 15'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 16'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 17'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 18'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 19'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 20'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 21'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 22'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 23'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 24'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 25'))
list_of_suitcase_objects.append(deal_or_no_deal.Suitcase('Suitcase 26'))

for suitcase in list_of_suitcase_objects:
    amount = random.choice(list_of_money_amounts)
    suitcase.set_amount(amount)
    list_of_money_amounts.remove(amount)
print(list_of_money_amounts)

for suitcase in list_of_suitcase_objects:
    print("{}: ${}".format(suitcase.get_name(),suitcase.get_amount()))

'''
suitcase1 = deal_or_no_deal.Suitcase()
suitcase2 = deal_or_no_deal.Suitcase()
suitcase3 = deal_or_no_deal.Suitcase()
suitcase4 = deal_or_no_deal.Suitcase()
suitcase5 = deal_or_no_deal.Suitcase()
suitcase6 = deal_or_no_deal.Suitcase()
suitcase7 = deal_or_no_deal.Suitcase()
suitcase8 = deal_or_no_deal.Suitcase()
suitcase9 = deal_or_no_deal.Suitcase()
suitcase10 = deal_or_no_deal.Suitcase()
suitcase11 = deal_or_no_deal.Suitcase()
suitcase12 = deal_or_no_deal.Suitcase()
suitcase13 = deal_or_no_deal.Suitcase()
suitcase14 = deal_or_no_deal.Suitcase()
suitcase15 = deal_or_no_deal.Suitcase()
suitcase16 = deal_or_no_deal.Suitcase()
suitcase17 = deal_or_no_deal.Suitcase()
suitcase18 = deal_or_no_deal.Suitcase()
suitcase19 = deal_or_no_deal.Suitcase()
suitcase20 = deal_or_no_deal.Suitcase()
suitcase21 = deal_or_no_deal.Suitcase()
suitcase22 = deal_or_no_deal.Suitcase()
suitcase23 = deal_or_no_deal.Suitcase()
suitcase24 = deal_or_no_deal.Suitcase()
suitcase25 = deal_or_no_deal.Suitcase()
suitcase26 = deal_or_no_deal.Suitcase()

'''