class ENDE:
    def __init__(self, filename, filename_2):
        self.filename_main = filename
        self.filename_ende = filename_2
        self.code = 13
        self.charcode = {
            'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8,
            'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16,
            'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24,
            'Y' : 25, 'Z' : 26
            }
    
        # print('keys', self.charcode.keys())
        # print('values', self.charcode.values())
        # print('items', self.charcode.items())

    
    def ende(self):
        file_ = open (f"{self.filename_main}", 'r+')
        ende_file = open (f"{self.filename_ende}.txt", 'w+')
        file_data = file_.read()
        word = file_data  
        # print(word)
        for letter in word:
            letter = letter.upper()
            if letter in self.charcode:
                # print(self.charcode[letter])
                letter_code = self.charcode[letter]
                if letter_code <= 13:
                    encode_letter = letter_code + self.code
                    if encode_letter in self.charcode.values():
                        for key, value in self.charcode.items():
                            if value == encode_letter:
                                # print('checking encoded', key, value)
                                ende_file.write(key)
                
                elif letter_code > 13:
                    encode_letter = letter_code - self.code
                    if encode_letter in self.charcode.values():
                        for key, value in self.charcode.items():
                            if value == encode_letter:
                                # print('checking encoded', key, value)
                                ende_file.write(key)
            else:
                ende_file.write(letter)
                
    
    def encode(self):
        file_ = open (f"{self.filename_main}.txt", 'r+')
        ende_file = open (f"{self.filename_ende}.txt", 'w+')
        file_data = file_.read()
        word = file_data  
        print(word)
        for letter in word:
            if letter == ' ':
                ende_file.write(letter)
            elif letter == '.':
                ende_file.write(letter)
            elif letter == ',': 
                ende_file.write(letter)
            elif letter == '?':
                ende_file.write(letter)
            elif letter == '-':
                ende_file.write(letter)
            elif letter == '0':
                ende_file.write(letter)
            elif letter == '1':
                ende_file.write(letter)
            elif letter == '2':
                ende_file.write(letter)
            elif letter == '3':
                ende_file.write(letter)
            elif letter == '4':
                ende_file.write(letter)
            elif letter == '5':
                ende_file.write(letter)
            elif letter == '6':
                ende_file.write(letter)
            elif letter == '7':
                ende_file.write(letter)
            elif letter == '8':
                ende_file.write(letter)
            elif letter == '9':
                ende_file.write(letter) 
            else:
                
                letter = letter.upper()
                if letter in self.charcode:
                    print(self.charcode[letter])
                    letter_code = self.charcode[letter]
                    if letter_code <= 13:
                        encode_letter = letter_code + self.code
                        if encode_letter in self.charcode.values():
                            for key, value in self.charcode.items():
                                if value == encode_letter:
                                    print('checking encoded', key, value)
                                    ende_file.write(key)
                    
                    elif letter_code > 13:
                        encode_letter = letter_code - self.code
                        if encode_letter in self.charcode.values():
                            for key, value in self.charcode.items():
                                if value == encode_letter:
                                    print('checking encoded', key, value)
                                    ende_file.write(key)
                        
    
    
    def decode(self):
        file_ = open (f"{self.filename_main}.txt", 'r+')
        ende_file = open (f"{self.filename_ende}.txt", 'w+')
        file_data = file_.read()
        word = file_data
        print(word)
        for letter in word:
            if letter == ' ':
                ende_file.write(letter)
            elif letter == '.':
                ende_file.write(letter)
            elif letter == ',': 
                ende_file.write(letter)
            elif letter == '?':
                ende_file.write(letter)
            elif letter == '-':
                ende_file.write(letter)
            elif letter == '0':
                ende_file.write(letter)
            elif letter == "1":
                ende_file.write(letter)
            elif letter == '2':
                ende_file.write(letter)
            elif letter == '3':
                ende_file.write(letter)
            elif letter == '4':
                ende_file.write(letter)
            elif letter == '5':
                ende_file.write(letter)
            elif letter == '6':
                ende_file.write(letter)
            elif letter == '7':
                ende_file.write(letter)
            elif letter == '8':
                ende_file.write(letter)
            elif letter == '9':
                ende_file.write(letter) 
            else:
                letter = letter.upper()
                if letter in self.charcode:
                    print(self.charcode[letter])
                    letter_code = self.charcode[letter]
                    if letter_code > 13:
                        encode_letter = letter_code - self.code
                        if encode_letter in self.charcode.values():
                            for key, value in self.charcode.items():
                                if value == encode_letter:
                                    print('checking decoded', key, value)
                                    ende_file.write(key)
                    
                    elif letter_code <= 13:
                        encode_letter = letter_code + self.code
                        if encode_letter in self.charcode.values():
                            for key, value in self.charcode.items():
                                if value == encode_letter:
                                    print('checking decoded', key, value)
                                    ende_file.write(key)
                        
                        
ende = ENDE('output 3 file', 'output 4 file')
# # ende.encode()
# ende.decode()
