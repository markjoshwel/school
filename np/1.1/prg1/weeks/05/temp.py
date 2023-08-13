prices = [["kopi", 0.4], ["teh", 0.4], ["milo", 0.5], ["soft drinks", 1.20]]
path = ""
file = open("pricesa.txt", "w")
drink1, price1 = prices[0]
drink2, price2 = prices[1]
drink3, price3 = prices[2]
drink4, price4 = prices[3]
# import code; code.interact(local=locals())
file.write("{}: ${}\n".format(drink1, price1))
file.write("{}: ${}\n".format(drink2, price2))
file.write("{}: ${}\n".format(drink3, price3))
file.write("{}: ${}\n".format(drink4, price4))
file.close()
