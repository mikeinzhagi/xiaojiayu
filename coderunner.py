import os
input_dir = "E:\QR_code.txt"
name = os.path.join(input_dir).split(".")[0]
suffix = os.path.join(input_dir).split(".")[1]
onepass = name + "_1pass." + suffix
f = open(onepass,"a+")
