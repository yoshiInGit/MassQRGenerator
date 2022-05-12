from scripts.statics import QR_PROP_NAMES
import sys

class Order:
    def __init__(self, order_dict):
        self.default_props = order_dict["default"]
        self.order         = order_dict["order"]
        
        # check if necessary info is written
        for key in QR_PROP_NAMES:
            if key in self.default_props:
                None
            else:
                print(f'Error: No prop {key} in default', file=sys.stderr)
                sys.exit(1)
    

