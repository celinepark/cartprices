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


"""
Takes in two command-line arguments, referring to two JSON files
Then calculates each item's price using the following metric:
    (base_price + round(base_price * artist_markup in cents)) * quantity where artist_markup is a percentage
Finally, it prints the total cart price to the command line followed by a newline character
"""
def main():

    # Error Handling for Command Line Arguments
    if len(sys.argv) != 3:
        print("Usage: cart.py [Cart JSON File] [Base Prices JSON File]")
        sys.exit("Please make sure to include the cart and base prices JSON files as command-line arguments")

    # Save arguments as variables
    cartFile = sys.argv[1]
    pricesFile = sys.argv[2]
    
    # Use helper function parseFiles to read the JSON files into Python lists
    cartList = parseFiles(cartFile)
    pricesList = parseFiles(pricesFile)

    # Begin with a total cart price of $0 
    totalPrice = 0

    # Loop through all items in the cart
    for item in cartList:

        # Set up variables to calculate price
        basePrice = 0
        artistMarkup = item["artist-markup"]
        # Dividing by 100 to make it a float since it's currently a whole-number percentage
        artistMarkup = artistMarkup/100 
        quantity = item["quantity"]

        # Find the base price by looping through the base prices file
        for price in pricesList:

            # If the price listing is for the same product type
            if item["product-type"] == price["product-type"]:

                # Create dictionaries for the options
                itemOpts = item["options"]
                priceOpts = price["options"]
        
                # Boolean that indicates whether the item matches the base price
                isItem = True

                for opt in priceOpts:
                    # Check each option for matches
                    if itemOpts[opt] not in priceOpts[opt]:
                        # If any options do not match, break out of loop
                        isItem = False
                        break
                
                if isItem == True:
                    # If we have found the base price that the item matches to,
                    # appropriately set basePrice, then break out of loop
                    basePrice = price["base-price"]
                    break

        # Calculate item price            
        itemPrice = (basePrice + int(round(basePrice * artistMarkup))) * quantity
        
        # Add item price to the total cart price
        totalPrice += itemPrice

    # Print total price with a newline character following it
    print(totalPrice, "\n")



if __name__ == '__main__':
    main()

