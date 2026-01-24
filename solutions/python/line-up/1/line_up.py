ORDINAL_ENDINGS = {
    1: "st",
    2: "nd",
    3: "rd",
}
def ordinal(n):
    if n % 100 not in (11, 12, 13):
        ending = ORDINAL_ENDINGS.get(n % 10, "th")
    else:
        ending = "th"
    return f"{n}{ending}"

def line_up(name, n):
    return f"{name}, you are the {ordinal(n)} customer we serve today. Thank you!"
