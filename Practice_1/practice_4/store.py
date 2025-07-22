def read_from_database():
    prodocts = []
    try:
        
        with open("store_database.csv", "r") as f:
            d= f.read()
        product_list = d.strip().split("\n")
        
        for i in range(len(product_list)):
            info = product_list[i].split(',')
            prodocts.append({"id":info[0],"name":info[1],"count":info[2],"price":info[3]})
        return prodocts 
    except Exception as e:
        print(e)
        prodocts = []
        return prodocts
    
def add(id,name,count,price):
    with open("store_database.csv","a") as f:
            f.write(f"{id},{name},{count},{price}\n")
            f.close 
def search(user_data,result):
    try:
        user_base = user_data.split(" ")
        output = ""
    
        for user in user_base:
            for data in result:
                if data["id"] == user:
                    output+=data["id"]+"  |  "+data["name"]+"  |  "+data["count"]+"  |  "+data["price"]
                    break
            else:
                print("not found")
    except Exception as e:
        print(e)
    return output.strip().split("\n") 
def remove_database(user_data,result):
    try:
        user_base = user_data.split(" ")
        output = ""
    
        for user in user_base:
            for data in result:
                if data["id"] == user:
                    result.remove(data)
                    
                    break
            with open("store_database.csv","w") as f:
                for data in result:
                    f.write(f"{data["id"]},{data["name"]},{data["count"]},{data["price"]}\n")   
    except Exception as e:
        print(e)
def buy_store(user_data, result, user_count):
    try:
        user_base = user_data.split(" ")
        output = 0

        for user in user_base:
            for data in result:
                if data["id"] == user:
                    
                    count = user_count
                    price = data["price"].strip("[").strip().strip("]")
                    price2 = int(price)
                    data2 = data["count"].strip("[").strip().strip("]")
                    data3 = int(data2)
                    data4 = data3 - count

                    if data4 >= 0:
                        print("found")
                        remove_database(user_data, result)
                        with open("store_database.csv", "a") as f:
                            f.write(f"{data['id']},{data['name']},{data4},{price2}\n")
                        output += price2 * count
                        name=data["name"]
                        id=data['id']
                        print(f"Id: {id}")
                        print(f"Name: {name}")
                        print(f"Count: {count}")
                        print(f"Price : {price2}")
                        print(f"Total cost: {output}")
                    else:
                        print("not enough stock")
                    break

            else:
                print("not found")


    except Exception as e:
        print(e)

while True:
    result = read_from_database()
    print("""
1=> Add form database
2=> Remove from database
3=> Search from database
4=> Buying from the store
5=> The store is closing now
    """)    
    c=input("Choose a request: ") 
    if c=="1":  
        id = input("Enter An Id:").strip()
        name=input("Enter An Name:").strip()
        count = input("Enter An Count:").strip()
        price = input("Enter An Price:").strip()
        add(id,name,count,price)
    elif c=="2":
        user_data=input("Enter An Id: ")    
        print(remove_database(user_data,result))

    elif c=="4":
        
            user_data=input("Enter An Id: ")
            user_count=int(input("Enter An Count: "))
            print(buy_store(user_data,result,user_count))
    elif c=="3":
        user_data=input("Enter An Id: ")  
        print(search(user_data,result))
    elif c=="5":
        print("Good bye")
        break
    else:
        print("Not found")