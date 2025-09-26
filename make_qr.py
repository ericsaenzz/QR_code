import qrcode

# Website URL
website_url = "https://ericchang.realscout.com/homesearch/map?zoom=12&geo_type=zipcode&geo_id=92630"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Save QR code image
img = qr.make_image(fill_color="black", back_color="white")
img_filename = "website_qr.png"
img.save(img_filename)

print(f"✅ QR code saved as {img_filename}")
