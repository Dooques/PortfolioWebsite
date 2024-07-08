import csv
import pandas as pd


class Morse:
    def __init__(self):
        self.alphabet = []
        self.morse_code = []
        with open('files/morse.csv', newline='') as csv_file:
            morse = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in morse:
                entry = ', '.join(row).split(',')
                self.alphabet.append(entry[0])
                self.morse_code.append(entry[1])
        self.morse_alphabet = pd.DataFrame({'alphabet': self.alphabet, 'morse_code': self.morse_code})

    def convert_string(self, to_convert):
        string_type = self.check_type(to_convert[0])
        convert_split = to_convert.split(" ")
        if string_type == "alphabet":
            result = self.to_morse(convert_split)
        else:
            result = self.from_morse(convert_split)
        return result

    def check_type(self, item):
        if item in self.morse_alphabet.morse_code.values:
            return "morse"
        else:
            return "alphabet"

    def to_morse(self, convert_list):
        morse_list = []
        word_list = [word + " " for word in convert_list[:-1]]
        word_list.append(convert_list[-1])
        for word in word_list:
            for char in word:
                char_cap = char.capitalize()
                if char_cap in self.morse_alphabet.alphabet.values:
                    char_entry = self.morse_alphabet.loc[self.morse_alphabet.alphabet == char_cap]
                    morse_list.append(char_entry.morse_code.values[0])
            if " " in word and word != convert_list[-1:]:
                morse_list.append("/")
        result = " ".join(morse_list)
        return result

    def from_morse(self, convert_list):
        alphabet_string = []
        for character in convert_list:
            if character == '/':
                alphabet_string.append(' ')
            else:
                char_entry = self.morse_alphabet.loc[self.morse_alphabet.morse_code == character].values
                alphabet_string.append(char_entry[0][0])
        result = "".join(alphabet_string)
        return result
