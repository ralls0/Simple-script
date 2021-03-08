hex24 = input("Insert HEX color 0x")
red = hex24[0:2]
green = hex24[2:4]
blue = hex24[4:6]
print("0x",red, green, blue)
rgb565 = (((int(red, 16) & 0xf8)<<8) + ((int(green, 16) & 0xfc)<<3)+(int(blue, 16)>>3))

print(hex(rgb565))
