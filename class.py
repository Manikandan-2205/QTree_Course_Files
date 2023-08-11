class a:
    def __init__(self, txt_1, txt_2, txt_3):
        self.txt1 = txt_1
        self.txt2 = txt_2
        self.txt3 = txt_3


txt_1 = input("Enter your txt:")
txt_2 = input("Enter your txt:")
txt_3 = input("Enter your txt:")

obj = a(txt_1, txt_2, txt_3)
print(obj.txt1, obj.txt2, obj.txt3)
