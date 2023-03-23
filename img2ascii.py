from PIL import Image
import torchvision

img = Image.open('test.png')

# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save("test1.png")

# 自定义灰度界限，大于这个值为白色，小于这个值为黑色
threshold = 90

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.png")


img = Image.open("test2.png")
print("原图大小：", img.size)
if img.size[0] > img.size[1]:
    squaresize = (img.size[1], img.size[1])
else:
    squaresize = (img.size[0], img.size[0])
# 这里的224就是正方形的大小
data1 = torchvision.transforms.CenterCrop(squaresize)(img)
print("裁剪后的大小:", data1.size)

# 这里的元组（224,224）是 背景的大小
# new_img = Image.new("RGB", (squaresize, squaresize))
# new_img.paste(data1)
data1.save('test3.png')


def transfer(infile, outfile):
    im = Image.open(infile)
    reim = im.resize((160, 160))  # 宽*高

    reim.save(outfile, dpi=(200.0, 200.0))  ##200.0,200.0分别为想要设定的dpi值


# 转大小
infil = "test3.png"
outfile = "test4.png"
transfer(infil, outfile)

image = Image.open("test4.png")
width, height = image.size

Counter = [[0]*width]*height
out = image.convert("L")
img_array = out.load()
for i in range(height):
    for j in range(width):
        if (img_array[j, i]==255):
            img_array[j, i] = 0
        else:
            img_array[j, i] = 1
        # print(img_array[i, j])


# or i in range(height):
#     col = ""
#     for j in range(width):
#         col = col + str(img_array[j, i])
#     print(col)

def to_ascii(x, y):
    draw = {0:img_array[2*y, 4*x], 1:img_array[2*y+1, 4*x], 2:img_array[2*y, 4*x+1], 3:img_array[2*y+1, 4*x+1], 4:img_array[2*y, 4*x+2], 5:img_array[2*y+1, 4*x+2], 6:img_array[2*y, 4*x+3], 7:img_array[2*y+1, 4*x+3]}
    code = draw[0] + draw[2]*2 + draw[4]*4 + draw[6]*8 + draw[1]*16 + draw[3]*32 + draw[5]*64 + draw[7]*128
    # print(draw, code, x, y)
    mang_wen = "⠀⠁⠂⠃⠄⠅⠆⠇⡀⡁⡂⡃⡄⡅⡆⡇⠈⠉⠊⠋⠌⠍⠎⠏⡈⡉⡊⡋⡌⡍⡎⡏⠐⠑⠒⠓⠔⠕⠖⠗⡐⡑⡒⡓⡔⡕⡖⡗⠘⠙⠚⠛⠜⠝⠞⠟⡘⡙⡚⡛⡜⡝⡞⡟⠠⠡⠢⠣⠤⠥⠦⠧⡠⡡⡢⡣⡤⡥⡦⡧⠨⠩⠪⠫⠬⠭⠮⠯⡨⡩⡪⡫⡬⡭⡮⡯⠰⠱⠲⠳⠴⠵⠶⠷⡰⡱⡲⡳⡴⡵⡶⡷⠸⠹⠺⠻⠼⠽⠾⠿⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⣀⣁⣂⣃⣄⣅⣆⣇⢈⢉⢊⢋⢌⢍⢎⢏⣈⣉⣊⣋⣌⣍⣎⣏⢐⢑⢒⢓⢔⢕⢖⢗⣐⣑⣒⣓⣔⣕⣖⣗⢘⢙⢚⢛⢜⢝⢞⢟⣘⣙⣚⣛⣜⣝⣞⣟⢠⢡⢢⢣⢤⢥⢦⢧⣠⣡⣢⣣⣤⣥⣦⣧⢨⢩⢪⢫⢬⢭⢮⢯⣨⣩⣪⣫⣬⣭⣮⣯⢰⢱⢲⢳⢴⢵⢶⢷⣰⣱⣲⣳⣴⣵⣶⣷⢸⢹⢺⢻⢼⢽⢾⢿⣸⣹⣺⣻⣼⣽⣾⣿"
    return mang_wen[code]





paintboard = [[0]*int(width/2)]*int(height/4)
for i in range(int(height/4)):
    for j in range(int(width/2)):
        paintboard[i][j] = to_ascii(i, j)

for i in range(int(height/4)):
    col = ""
    for j in range(int(width/2)):
        paintboard[i][j] = to_ascii(i, j)
        col = col + paintboard[i][j]
    print(col)

