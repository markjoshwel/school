# Place order in restaurant: PlaceOrders.py
# Mark Joshwel - SXXXXXXXX (IM02/P12)
#
# 　　　　　　 ハ
# 　　　　 　 ,':|　　　　　　　　     　　　 ,.イ
# 　　　　　 ,::::ヽ‐-.､　　　　  　,,--.._／.::!
# 　　 　 　 l:::::::i::ﾑ　　　 　／.::::::::::/
# 　　 　 　 l:::::::.､::ﾑ　 　.／::::::::::::/
# 　　　　　 ヽ.:::::ヽ:::fヽﾑ,-､／;:-ｧ.:::::::／
# 　　　　　　 ＼::::::＞‐-<__/_ﾆ二::-‐''__;:'"
# 　　　　　 　 ／　,　 ./il　　￣｀''＜￣
#   　　　　　／　 ,.'　 /　lil　.ﾊ　　 ヽ
#   　　 　　//.　 /|__/ﾉ　 ∨l、lil　i 　 ヽ
# 　 　 　 /　　,ｰ'ﾞ|/　　　　V ｀ｰ-i-.　　∧
# 　　  ,.'ｨ .i/_＿＿　　　　＿＿ﾞ'ヽ、　　　:|
# 　　  |/ |　l 三三ﾐ　　　 三三三　 `　　 :.|
#         |./　　　　　　　　　　　  |. :l. |
#  　　　   / U　　　　　　　　 　 |　|l l:i.|
# 　　　    ヽ.　　　　ﾏ￣￣ ¨ ‐-､ U  |l　  .!
# 　　　　   V＞ ..._ !!________|---/i_,...!
# 　　　　   V ＼ﾊﾍ-__|./        \ﾊ!ノ､ﾙ､'ン
# 　　　　　　　　　　　/li |l工コヽﾊ
# 　　　　　　　 　 　 /　li l!工l/ \

prices = {
    "chicken": 8.50,
    "steak": 13.80,
    "fish": 9.80,
    "pasta": 9.50,
    "coffee": 2.50,
    "tea": 1.80,
    "water": 0.50,
}

choice = 0
orders = [0 for item in prices]
while choice != 3:
    choice = int(
        input(
            "-------------------\n"
            "1. Add order\n"
            "2. Summarize orders\n"
            "3. Quit\n"
            "-------------------\n"
            "Your choice? "
        )
    )

    if choice == 1:
        print(
            # 123456789
            "Item       Price\n"
            "----       -----"
        )
        for item, price in prices.items():
            print(f"{item.capitalize():<9} {price}")

        order = input("Your order? ").lower()
        if order not in prices:
            print(f"{order} is not available.")
            continue

        sets = int(input("How many sets? "))
        print(f"{sets} sets of {order} ordered.")
        orders[list(prices.keys()).index(order)] += sets

    elif choice == 2:
        print("Item       Quantity\n" "----       --------")
        total = 0.0
        for item, price, quantity in zip(prices.keys(), prices.values(), orders):
            total += price * quantity
            print(f"{item.capitalize():<9} {quantity}")
        print(f"Total cost = ${total:.2f}")

    elif choice != 3:
        print("Invalid choice.")
