from PIL import Image
import qrcode
import sys
import copy
from scripts.statics import QR_PROP_NAMES


class QRGenerator:
    def __init__(self, default_prop):
        self.default_prop = default_prop

    def generate(self, request):
        prop = copy.deepcopy(self.default_prop)

        # update prop to request prop if there are
        for prop_name in QR_PROP_NAMES:
            if prop_name in request:
                prop[prop_name] = request[prop_name]

        # convert error collection: str to qrcode.ERROR_CORRECT_?
        prop["errorCorrection"] = self._getErrorConection(prop["errorCorrection"])
        
        qr = qrcode.QRCode(
            version          = prop["version"],
            error_correction = prop["errorCorrection"],
            box_size         = prop["boxSize"],
            border           = prop["border"],
        )
        qr.add_data(prop["data"])
        qr.make()

        QRimg = qr.make_image(fill_color=prop["color"], back_color="white").convert('RGB')


        # logo = Image.open("../logoImg/"+prop["logoImg"])

        # # position of logo (center)
        # pos = (
        #     (QRimg.size[0] - logo.size[0]) // 2,
        #     (QRimg.size[1] - logo.size[1]) // 2,
        # )

        # QRimg.paste(logo, pos)

        return QRimg

        
    def _getErrorConection(self ,str):
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

        