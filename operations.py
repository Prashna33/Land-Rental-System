def properties(rented):
        print("\t")
        print("| {:<14} | {:<31} | {:<10} | {:<9} | {:<6} | {:<15}  |".format( "kitta_number", "city", "direction", "anna", "Rupees", "availability"))
        print()
        for key,value in rented.items():
            print()
            kitta_number = value["kitta_number"]
            city_district = value["city_district"]
            direction = value["direction"]
            area = value["area"]
            price = value["price"]
            avaibility = value["availability"]
            print("| {:<14} | {:<31} | {:<10} | {:<9} | {:<6} | {:<15}  |".format(kitta_number, city_district, direction, area, price, avaibility))
        print(" ")


def rentedLand(rented,customerName):
        totalPrice=0
        rentedLand=[]
        userChoice= "q" 
        
        while True:
            try:
                properties(rented)
                if (rented["101"]["availability"].lower() == "not available" and rented["102"]["availability"].lower() == "not available" and rented["103"]["availability"].lower() == "not available"):
                    print("Property cannot be rented")
                    break
                userChoice = input("Enter the kitta number you want to rent or 'q' to quit: ")
                
                if userChoice.lower() == "q" or userChoice.lower == "quit":
                    break
                
                if userChoice not in rented:
                    print("Invalid input!")
                    continue
                
                if(rented[userChoice]["availability"].lower() == "not available"):
                    print("The land is not available to rent")
                    continue
                rentDuration_month = int(input("Enter for how many months you want to rent the land: "))
                
                price = int((rented[userChoice]["price"]))
                
                totalPrice = totalPrice + (price  * rentDuration_month)
                
                rentedLand.append({
                    "Customer name": customerName,
                    "kitta_number": rented[userChoice]["kitta_number"],
                    "city_district": rented[userChoice]["city_district"],
                    "direction": rented[userChoice]["direction"],
                    "anna": rented[userChoice]["area"],
                    "price": rented[userChoice]["price"],
                    "availability": rented[userChoice]["availability"]
                })
                    
                rented[userChoice]["availability"] = "Not Available"
                moreLand = input("Do you want to add more lands to rent? (y/n): ")
                if moreLand.lower() == "n":
                    break
            except Exception as error:
                break
        if(rentedLand == []):
            print("Sorry we do not have any land available to rent out")
        else:
            bill= customerName + "Rented land.txt"
            file= open(bill,"a")
            file.write("\n\n")
            file.write("------------------------------------------------------------------------------------------\n")
            file.write(" Properties Nepal\n")
            file.write("\n\n")
            file.write(" Bill\n")
            file.write("-----------------------------------------------------------------------------------------\n\n")
            file.write(" Customer Name:" ,customerName)
            file.write("*------------------------------------------------------------------------------------------\n")
            file.write("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number","City/District", "Direction", "Area", "Price (NPR)"))
            file.write("------------------------------------------------------------------------------------------\n")
            for value in rentedLand:
                file.write("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15}|\n".format(value["kitta_number"], value["city_district"], value["direction"], value["anna"],str(value["price"])))
            file.write("------------------------------------------------------------------------------------------\n")
            file.write(" Total: {} NPR\n".format(totalPrice))
            file.write("------------------------------------------------------------------------------------------\n")
            print("\n\n------------------------------------------------------------------------------------------\n")
            print(" Land Properties Nepal\n")
            print(" Bill\n")
            print(" \n\n")
            print(" Customer Name: {}\n".format(customerName))
            print(" \n\n")
            print("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number","City/District", "Direction", "Area", "Price (NPR)"))
            print("------------------------------------------------------------------------------------------\n")
            for key in rentedLand:
                    print("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15} |".format(key["kitta_number"],key["city_district"], key["direction"], key["anna"], str(key["price"])))
            print("\n------------------------------------------------------------------------------------------\n")
            print(" Total: ", totalPrice )
            print("\n------------------------------------------------------------------------------------------\n")
                    

def returnedLand(rented,customerName):
        totalPrice=0
        rentedLand=[]

        Current_month = 0
        return_time = 0
        while True:
            properties(rented)
            userChoice = input("Enter the number of the kita  you are returning or 'q' to exit: ")
            if userChoice.lower() == "q" or userChoice.lower == "exit":
                break
            
            if(rented["101"]["availability"].lower() == "available" and rented["102"]["availability"].lower() == "available" and rented["103"]["availability"].lower() == "available"):
                print("All the lands have benn returned")
                break
            
            if userChoice not in rented:
                print("Invalid input!")
                continue
            
            Current_month = int(input("Enter for how many months you have rented the land:"))
            return_time = int(input("Enter when you should have returned the land: "))



            if(rented[userChoice]["availability"].lower() == "available"):
                print("The land is not in our list!")
                continue
          
            rentedLand.append({
                "Customer name":customerName,
                "kitta_number" :rented[userChoice]["kitta_number"],
                "city_district": rented[userChoice]["city_district"],
                "direction": rented[userChoice]["direction"],
                "anna": rented[userChoice]["area"],
                "price": rented[userChoice]["price"],
                "availability": rented[userChoice]["availability"]
            })
                
            rented[userChoice]["availability"] = "Available"
            moreland= input("Do you want to return more ?(y/n): ")
            if moreland.lower()=="n":
                break
            
        if(rentedLand == []):
            print("You have not rented any land!")
        else:
            invoice= customerName + " Returned land.txt"
            if(Current_month and return_time != 0):
                if(return_time >= Current_month):
                    totalPrice = totalPrice + int((rented[userChoice]["price"])) * Current_month
                    file= open(invoice,"a")
                    file.write("\n\n")
                    file.write("------------------------------------------------------------------------------------------\n")
                    file.write(" Poperties Nepal \n")
                    file.write(" Bill\n")
                    file.write("\n\n")
                    file.write("\n\n")
                    file.write(" Customer Name: {}\n\n".format(customerName))
                    file.write("\n\n")
                    file.write("\n\n")
                    file.write("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number", "City/District", "Direction", "Area", "Price (NPR)"))
                    file.write("------------------------------------------------------------------------------------------\n")
                    for value in rentedLand:
                        file.write("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15}\n".format(value["kitta_number"], value["city_district"], value["direction"], value["anna"],str(value["price"])))
                    file.write("\n")
                    file.write("\n")
                    file.write(" Total: "+ (totalPrice))
                    print("\n\n------------------------------------------------------------------------------------------\n")
                    print(" Land Properties Nepal \n")

                    print(" Bill\n")
                    print(" Customer Name:" , customerName)
                    print("------------------------------------------------------------------------------------------\n")
                    print("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number","City/District", "Direction", "Area", "Price (NPR)"))
                    for value in rentedLand:
                        print("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15}|".format(value["kitta_number"], value["city_district"], value["direction"], value["anna"],str(value["price"])))
                    print("\n------------------------------------------------------------------------------------------ \n")
                    print(" Total: ", totalPrice)
                else :
                    totalPrice = (totalPrice + int((rented[userChoice]["price"])) * Current_month) + 0.3* int((rented[userChoice]["price"]))
                    file= open(invoice,"a")
                    file.write("\n\n")
                    file.write(" \n")
                    file.write(" Land Propeties Nepal\n")
                    file.write(" Bill\n")
                    file.write("\n\n")
                    file.write("\n\n")
                    file.write(" Customer Name: {}\n\n".format(customerName))
                    file.write("\n")
                    file.write("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number","City/District", "Direction", "Area", "Price (NPR)"))
                    file.write("\n")
                    for value in rentedLand:
                        file.write("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15}|\n".format(value["kitta_number"], value["city_district"], value["direction"], value["anna"],str(value["price"])))
                    file.write("------------------------------------------------------------------------------------------\n")
                    file.write(" Total: {} NPR\n".format(totalPrice))
                    file.write("The payment charge has been added to extra 30% " +" fine of original price for delay of payment\n")
                    file.write("------------------------------------------------------------------------------------------\n")
                    print("\n\n------------------------------------------------------------------------------------------\n")
                    print(" Land Properties Nepal\n")
                    print(" Bill\n")
                    print("\n\n")
                    print("\n\n")
                    print(" Customer Name: {}\n".format(customerName))
                    print(" \n")
                    print("{:<15} | {:<20} | {:<15} | {:<10} | {:<15}\n".format("Kitta Number","City/District", "Direction", "Area", "Price (NPR)"))
                    print("------------------------------------------------------------------------------------------\n")
                    for value in rentedLand:
                        print("| {:<13} | {:<20} | {:<15} | {:<10} | {:<15}|".format(value["kitta_number"], value["city_district"], value["direction"], value["anna"],str(value["price"])))
                    print("\n")
                    print(" Total: ", totalPrice)
                    print("The payment charge has been added to extra 30% " +" fine of original price for delay of payment")
                    print("\n-----------------------------------------------------------------------------------------------")
