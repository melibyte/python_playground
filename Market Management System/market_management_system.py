
print(" Add Product (1)\n Delete Product (2)\n Sell Products (3)")


products = {"778899": {"Name of product": "Green Pepper",
                      "1 kg Price": 20,
                      "Stock Quantity": 100},
           
           "667788": {"Name of product": "Cucumber",
                     "1 kg Price": 15,
                     "Stock Quantity": 500 },

           "556677": {"Name of product": "Lemon",
                     "1 kg Price": 10,
                     "Stock Quantity": 200 },

           "445566": {"Name of product": "Parsley",
                       "1 kg Price": 16,
                       "Stock Quantity": 200 },

           "334455": {"Name of product": "Courgette",
                    "1 kg Price": 15,
                    "Stock Quantity": 100},

           "223344": {"Name of product": "Eggplant",
                       "1 kg Price": 23,
                       "Stock Quantity": 150},

           "112233": {"Name of product": "Tomatoes",
                       "1 kg Price": 17,
                       "Stock Quantity": 200 },

           "221100": {"Name of product": "Red Pepper",
                      "1 kg Price": 16,
                     "Stock Quantity": 200 },

           "332211": {"Name of product": "Peach",
                       "1 kg Price": 22,
                       "Stock Quantity": 250 },

           "443322": {"Name of product": "Strawberry",
                     "1 kg Price": 13,
                     "Stock Quantity": 18 },

           "554433": {"Name of product": "Banana",
                    "1 kg Price": 14,
                    "Stock Quantity": 500 },

           "665544": {"Name of product": "Cherry",
                      "1 kg Price": 10,
                      "Stock Quantity": 300 },

           "776655": {"Name of product": "Apple",
                     "1 kg Price": 15,
                     "Stock Quantity": 400 },

           "887766": {"Name of product": "Grape",
                     "1 kg Price": 15,
                     "Stock Quantity": 170 },

           "998877": {"Name of product": "Kiwi",
                    "1 kg Price": 20,
                    "Stock Quantity": 300}}


def calc_price(quantity,kg_price):
        
    if quantity.isdigit() == False:
        return -1
        
    else:
        result = int(quantity) * int(kg_price)
        return result

while True:
    
    question = input("\nSelect the action you want to do: ")

    if question == "1":
        barcode = input("Enter the barcode you want to add: ")
        name_of_product = input("Enter product name: ")
        price = int(input("Ürün fiyatı giriniz: "))
        kg = int(input("How many kilograms of products are in stock?: "))
        value = {"Name of product": name_of_product,
                 "1 kg Price": price,
                 "Stock Quantity": kg}
        
        products[barcode] = value
        
        print(products)

    elif question == "2":
        barcode =input("Type the barcode of the product you want to delete: ")
        value = products.pop(barcode)
        print(products)
        
    elif question == "3":
        
        print(" --Available Products-- \n Green Pepper(778899)\n Cucumber(667788)\n Lemon(556677)\n Parsley(445566)\n Courgette(334455)\n \
Eggplant(223344)\n Tomatoes(112233)\n Red Pepper(221100)\n Peach(332211)\n Strawberry(443322)\n \
Banana(554433)\n Cherry(665544)\n Apple(776655)\n Grape(887766)\n Kiwi(998877)")
        
        result = 0

        while True:
            
            try:

                question = input("\nEnter Product Barcode: ")
                        
                if question == "Finish":
                    print(f"The safe is closing.Shopping Price: {result} TL")
                    break
               
                kg_price = products[question]["1 kg Price"]

                quantity = input("How many kilograms do you want to buy?: ")
                
                stok_miktarı = products[question]["Stock Quantity"]
                
                if int(quantity) > stok_miktarı:
                    print("Not enough stock.")
                
                else:
                    
                    calc = calc_price(quantity,kg_price)

                    if calc == -1:
                        print("You must not enter a negative value.")
                        break

                    else:
                        result = int(result) + calc
                        print(f"Shopping Price: {result} TL")

            except KeyError:
                
                print("Error.Please try again.")





