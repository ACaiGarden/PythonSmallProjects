from PIL import Image

class Picture():
    def __init__(self):
        pass

    def get_char(self,r, g, b, alpha = 256):
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

        length = len(ascii_char)
        gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        gary_char = int((gary / alpha) * length)
        return ascii_char[gary_char]

    def drew(self, pic_path, width = 200, height = 100):
        try:
            im = Image.open(pic_path)
            im = im.resize((width, height), Image.NEAREST)

            txt = ""
            for i in range(height):
                for j in range(width):
                    txt += self.get_char(*im.getpixel((j, i)))
                txt += "\n"

            save_name = '.\\' + self.get_file_name(pic_path) + '_t.txt'
            with open(save_name, 'w') as f:
                f.write(txt)
        except:
            print('找不到目标文件')
            exit()

    def get_file_name(self, pic_path):
        pic_name = pic_path.split('/')[-1].split('.')[0]
        return pic_name

if __name__ == '__main__':
    P = Picture()
    P.drew('E:\\a.jpg', 200, 100)
    #print(P.get_file_name('E:\\a.jpg'))