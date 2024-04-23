VOID_MANALEECH = {
    "rope belt": 25,
    "silencer claws": 25,
    "grimeleech wings": 5
}

STRIKE_CRITICALHIT = {
    "protective charm": 20,
    "sabretooth": 25,
    "vexclaw talon": 5
}

def getImbuimentPrice(imbuiment, prices) -> int:
    price = 0
    for item, amount in imbuiment.items():
        price += prices[item] * amount
    return price


x = [print("*"*i) for i in range(1,6)]