import json

data={
    "State":"Capital",
    "Delhi":"Delhi",
    "Gujrat":"Ahmedabad",
    "Telangana":"Hyderabad",
    "Maharashtra":"Mumbai",
    "Rajasthan":"Jaipur",
    "Karnataka":"Banglore",
    "Tamilnadu":"Chennai"
}

with open ("C:\\Users\\ankit chandak\\Documents\\Data\\DS301222\\python\\Assignments\\capital.json","w") as file:

 json.dump(data,file)