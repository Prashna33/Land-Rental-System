def readLand(file_name):
    landRentals = {} 
    with open(file_name, "r") as file: 
        for line in file:
            value = line.strip().split(", ")
            kitta_number = value[0]
            city_district = value[1]
            direction = value[2]
            area = int(value[3])
            price = int(value[4])
            availability = value[5] 

            landRentals[kitta_number] = {
            "kitta_number": kitta_number,
            "city_district": city_district,
            "direction": direction,
            "area": area,
            "price": price,
            "availability": availability
            }
    return landRentals
