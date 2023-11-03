total = 0
while True:
    amount = input("Cat doriti sa depuneti? RON: ")

    if amount.isdigit():
        amount = int(amount)
        if amount == 0: break
        print("Ati depus " + str(amount) + " RON")
        total += amount
        print("Totalul dumneavoastra este de " + str(total) + " RON")
    else:
        print("Incercati din nou!")    