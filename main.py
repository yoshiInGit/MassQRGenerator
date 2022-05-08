from scripts.order import Order
import shutil
import json

def main():
    delete_output()

    order = read_order()

    # generate_qr(order)

def delete_output():
    shutil.rmtree("output/")

def read_order():
    with open("order.js") as order_file:
        order_dict = json.load(order_file)
    
    return Order(order_dict=order_dict)
    


if __name__ == "__main__":
    main()