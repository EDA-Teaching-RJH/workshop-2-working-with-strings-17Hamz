def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    clean_num = d.replace("£", "")
    return float(clean_num)

def percent_to_float(p):
    clean_num = p.replace("%", "")
    return float(clean_num) / 100 

main()
