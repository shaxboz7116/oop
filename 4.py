class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def reader(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                print("Fayl ma'lumotlari:")
                print(data)
        except FileNotFoundError:
            print("Fayl topilmadi!")

file_obj = FileReader("example.txt")

file_obj.reader()