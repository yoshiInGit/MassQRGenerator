import os
from scripts.order import Order
import shutil
import json

from scripts.qr_generator import QRGenerator

def main():
    delete_output()

    order = read_order()

    generate_qr(order)

def delete_output():
    shutil.rmtree("output/")
    os.mkdir("output/")

def read_order():
    with open("order.json") as order_file:
        order_dict = json.load(order_file)
    
    return Order(order_dict=order_dict)
    
def generate_qr(order):
    generator = QRGenerator(order.default_props)

    for request in order.order:
        img = generator.generate(request = request)

        # decide file name
        if "fileName" in request:
            file_name = request["fileName"]
        else:
            file_name = order.default_props["fileName"]

        # if this file name is already exist
        if os.path.exists("./output/"+file_name+".png"):
            count = 1
            while os.path.exists("./output/"+file_name+"_"+str(count+1)+".png"):
                count += 1
            img.save("./output/" + file_name+"_"+str(count)+".png")
        else:
            img.save("./output/"+file_name+".png")

if __name__ == "__main__":
    main()