from itertools import count
import os
from scripts.order import Order
import shutil
import json
import copy
import qrcode
import sys
from scripts.statics import QR_PROP_NAMES
from PIL import Image

def main():
    delete_output()

    order = read_order()

    for request in order.requests:
        props = make_props(request=request, default_props=order.default_props)
        qr_img = generate_qr_img(props=props)

        # If it has to paste logo
        if(props["logoImg"]!=""):
            logo_img = Image.open("logoImg/"+props["logoImg"])
            qr_img = paste_logo(qr_img=qr_img, logo_img=logo_img)

        to_save_file_path = decide_file_path(props["fileName"])
        qr_img.save(to_save_file_path)   


def delete_output():
    shutil.rmtree("output/")
    os.mkdir("output/")

def read_order():
    with open("order.json") as order_file:
        order_dict = json.load(order_file)
    
    return Order(order_dict=order_dict)

def make_props(request, default_props):
    props = copy.deepcopy(default_props)

    for prop_name in QR_PROP_NAMES:
        if prop_name in request:
            props[prop_name] = request[prop_name]

    return props
 
def generate_qr_img(props):
    errorCorrection = _getErrorCorrection(props["errorCorrection"])
    qr = qrcode.QRCode(
        version          = props["version"],
        error_correction = errorCorrection,
        box_size         = props["boxSize"],
        border           = props["border"],
    )
    qr.add_data(props["data"])
    qr.make()
    qrImg = qr.make_image(fill_color=props["color"], back_color="white").convert('RGB')

    return qrImg

def paste_logo(qr_img, logo_img):
    maxLogoSize = qr_img.width // 4

    if logo_img.width > maxLogoSize:
        print("before:"+str(logo_img.width))
        logo_img = logo_img.resize((maxLogoSize, maxLogoSize))
        print("after:"+str(logo_img.width))

    pos = (
             (qr_img.size[0] - logo_img.size[0]) // 2,
             (qr_img.size[1] - logo_img.size[1]) // 2,
    )
    qr_img.paste(logo_img, pos)

    return qr_img

def decide_file_path(request_file_name):
    qr_file_path = "./output/" + request_file_name + ".png"

    count = 1
    while os.path.exists(qr_file_path):
        count += 1
        qr_file_path = "./output/" + request_file_name + "_"+ str(count) + ".png"

    return qr_file_path


def _getErrorCorrection(str):
    if(str=="L"):
        return qrcode.ERROR_CORRECT_L
    if(str=="M"):
        return qrcode.ERROR_CORRECT_M
    if(str=="Q"):
        return qrcode.ERROR_CORRECT_Q
    if(str=="H"):
        return qrcode.ERROR_CORRECT_H

    # no matches
    print(f'Error:{str} is bad request for error correction', file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()