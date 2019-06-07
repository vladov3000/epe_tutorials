gal_to_litre = 3.78541178
mile_to_km = 1.609344

def convert_mileage(mpg):
    '''Converts miles per gallon to liters per 100 km'''
    if mpg<=0:
        raise ValueError
    else:
        litres_per_100_km = 100 / mpg / mile_to_km * gal_to_litre
    return round(litres_per_100_km,2)

if __name__ == "__main__":
    inp=input("Mileage in MPG:")
    while inp!='q':
        try:
            print("Mileage in L/100km:",convert_mileage(float(inp)))
        except ValueError:
            print("Invalid Input")
        inp=input("Mileage in MPG:")
