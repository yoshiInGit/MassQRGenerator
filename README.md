# Mass QRcode Generator

## How to use

### 1.Write necessary information

All information you have to write is in order.json

~~~json:order.json
{
    "default":{
        "fileName"  : "qrCode",
        "data"      : "default text",
        "logoImg"   : "",
        "color"     : "black",
        "errorCorrection" : "H",
        "version"   : 12,
        "boxSize"   : 10,
        "border"    : 4
    },
    
    "order":[

    ]
}

~~~

#### STEP1. Overwrite default propety

Default propety is where common QRcode propety will be written.
Propeties which is not written in order will be same as default.
All propeties must be written in default.

ex)

~~~json:order.json
{
    "default":{
        "fileName"  : "wificode",
        "data"      : "default text",
        "logoImg"   : "logo.png",
        "color"     : "red",
        "errorCorrection" : "H",
        "version"   : 12,
        "boxSize"   : 10,
        "border"    : 4
    },
    
    "order":[

    ]
}

~~~

#### STEP2. Write ordres

In orders, you will write Qrcode information which you want.
A QRcode will be generated as much as it is written in order.
You only heve to write propeties which is different with default.

--Examples---

1. If you want 3 Qrcodes whose propety is same as default, order.json will be like this.

~~~json:order.json
{
    "default":{
        "fileName"  : "wificode",
        "data"      : "default text",
        "logoImg"   : "logo.png",
        "color"     : "red",
        "errorCorrection" : "H",
        "version"   : 12,
        "boxSize"   : 10,
        "border"    : 4
    },
    
    "order":[
        {}, {}, {}
    ]
}

~~~

1. If you want 3 Qrcodes whose propeties is same as defaul, but only data is different, order.json will be like this.

~~~json:order.json
{
    "default":{
        "fileName"  : "wificode",
        "data"      : "default text",
        "logoImg"   : "logo.png",
        "color"     : "red",
        "errorCorrection" : "H",
        "version"   : 12,
        "boxSize"   : 10,
        "border"    : 4
    },
    
    "order":[
        {
            "data":"text1"
        }, 
        {
            "data":"text2"
        }, 
        {
            "data":"text3"
        }
    ]
}

~~~

### 2.Execute generate_QRcodes.exe

Execute generate_QRcodes.exe to generate QRcodes.
you will get qrcode images in output folder.

note:

- When it generate qrcodes, all files in output folder will be deleted at first.

- So be sure to save data in output folder before you execute.
