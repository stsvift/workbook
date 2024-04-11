import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Алфавит:", self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)
    
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."

#Тесты
eng_alphabet = EngAlphabet()
eng_alphabet.print()

print("Число букв:", eng_alphabet.letters_num())
print("'F' английская буква?", eng_alphabet.is_en_letter('F'))
print("'Щ' английская буква?", eng_alphabet.is_en_letter('Щ'))
print("Пример текста:", EngAlphabet.example())

alphabet = Alphabet(lang='TestLang', letters=['a', 'b', 'c'])
alphabet.print()
print("Число букв:", alphabet.letters_num())