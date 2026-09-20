meter = float(input("请输入长度（米）："))

cm = 100
mm = 1000
inch = 39
foot = 3.2

cent = meter * cm
mill = meter * mm
inche = meter * inch
foote = meter * foot

print("你输入的长度是：", meter, "米")
print("换算成厘米：", cent)
print("换算成毫米：", mill)
print("换算成英寸：", inch)
print("换算成英尺：", foot)