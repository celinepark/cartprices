import sys
import json

"""
Takes in a filename as input (JSON)
Returns the parsed file as a list
"""
def parseFiles(fileName):
    with open(fileName) as fileData:
        data = json.load(fileData)
        return data


def main():
    cartFile = sys.argv[1]
    pricesFile = sys.argv[2]
    
    cartList = parseFiles(cartFile)
    pricesList = parseFiles(pricesFile)
    
    totalPrice = 0

    for item in cartList:
        basePrice = 0
        artistMarkup = item["artist-markup"]
        artistMarkup = artistMarkup/100
        quantity = item["quantity"]

        for price in pricesList:
            # If the price listing is for the same product type

            if item["product-type"] == price["product-type"]:

                # Dictionary {"colour": ["white", "dark"]}
                itemOpts = item["options"]
                priceOpts = price["options"]
        
                isItem = True

                for opt in priceOpts:
                    if itemOpts[opt] not in priceOpts[opt]:
                        isItem = False
                        break
                
                if isItem == True:
                    basePrice = price["base-price"]
                    break
        itemPrice = (basePrice + int(round(basePrice * artistMarkup))) * quantity
        totalPrice += itemPrice
    print(totalPrice, "\n")

# run cart.py "cart-ex-1.json" "prices-ex-1.json"



if __name__ == '__main__':
    main()
