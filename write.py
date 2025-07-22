def updateLand_info(fileName, rent):
 file = open(fileName,"w")
 for key, value in rent.items():
      kitta_number = value["kitta_number"]
      city_district = value["city_district"]
      direction = value["direction"]
      area = value["area"]
      price = value["price"]
      availability = value["availability"]
      line =  kitta_number + ", " +city_district + ", " +direction+ ", "+ str(area) + ", " + str(price) + ", " + availability
      file.write(line)
      file.write("\n") 
