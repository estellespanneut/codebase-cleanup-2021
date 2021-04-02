import os
from datetime import datetime
from pandas import read_csv

#FORMAT_USD FUNCTION

def format_usd(my_price):  
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
#ATTRIBUTION: Taken from code provided by Professor Rossetti

#PREVENT APPLICATION CODE FROM IMPORTING

if __name__ == "__main__":




    format_usd(10)
    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")

    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            if any(matching_products):
                selected_products.append(matching_products[0])
            else:
                print("OOPS, Couldn't find that product. Please try again.")

    checkout_at = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])
    tax_rate = .0875
    tax = subtotal*tax_rate
    total = subtotal + tax

    # PRINT RECEIPT

    print("---------")
    print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
    print("---------")
    for p in selected_products:
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
        #print("SELECTED PRODUCT: " + p["name"] + "   " + '${:.2f}'.format(p["price"]))

    print("---------")
    print("SUBTOTAL:", format_usd(subtotal))
    print("TAX:", format_usd(tax))
    print(f"TOTAL:", format_usd(total))
    print("---------")
    print("THANK YOU! PLEASE COME AGAIN SOON!")
    print("---------")

    # WRITE RECEIPT TO FILE

    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
            #receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + '${:.0f}'.format(p["price"]))

        receipt_file.write("\n---------")
        receipt_file.write(f"\nSUBTOTAL: {format_usd(subtotal)}")
        #receipt_file.write(f"\nSUBTOTAL: {subtotal}")
        receipt_file.write(f"\nTAX: {format_usd(tax)}")
        #receipt_file.write(f"\nTAX: {subtotal * 0.875}")
        receipt_file.write(f"\nTOTAL: {format_usd(total)}")
        #receipt_file.write(f"\nTOTAL: {((subtotal * 0.875) + subtotal)}")
        receipt_file.write("\n---------")
        receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
        receipt_file.write("\n---------")
