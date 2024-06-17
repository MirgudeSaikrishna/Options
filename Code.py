def repl(budget, price):
    difference=budget/25-float(price)
    if difference<=0: return 1000000000
    else: return difference
def lots(bud,n,pric):
    net=bud
    i=0
    while bud>float(pric):
        bud=bud-(n*float(pric))
        i=i+1
    return (i-1)*n
budget=int(input("Enter budget: "))
nifty_price, banknifty_price, finnifty_price = input("Enter current prices ATM of 3 optionss(seperated by spaces)\nNifty,Banknifty,finnifty:").split()
nif_diff=repl(budget,nifty_price)
ban_diff= repl(budget,banknifty_price)
fin_diff= repl(budget,finnifty_price)
mini=min(nif_diff,ban_diff,fin_diff)
if mini== nif_diff:
    l=lots(budget,25,nifty_price)
    print("Nifty lot size: %d"%l)
    index=1
elif mini== ban_diff:
    l=lots(budget,15,banknifty_price)
    print("Banknifty lot size: %d"%l)
    index=2
else:
    l=lots(budget,40,finnifty_price)
    print("Finnifty lot size: %d"%l)
    index=3
current_price=float(input("Enter current price of indec(At 10:01 open):"))
match index:
    case 1:print("Target: %.2f\nStoploss: %.2f"%(current_price+67,current_price-36))
    case 2:print("Target: %.2f\nStoploss: %.2f"%(current_price+143,current_price-65))
    case 3:print("Target: %.2f\nStoploss: %.2f"%(current_price+64,current_price-32))
