'''This code generates a QR code image file with the given data 
(URL in this example) and saves it as a PNG file with the specified filename. 
You can adjust the parameters (e.g. version, error_correction, box_size, border) 
to customize the QR code generation.'''

import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == '__main__':
    data = "https://www.example.com"
    filename = "qr_code.png"
    generate_qr_code(data, filename)
