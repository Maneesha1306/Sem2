import string
class passwd_validator:
    def __init__(self,passwd):
        self.passwd=passwd
    def length(self):
        if len(self.passwd)>=8:
            return True
        else:
            return False
    def upper(self):
        for i in self.passwd:
            if i.isupper():
                return True
        else:
            return False
    def lower(self):
        for i in self.passwd:
            if i.islower():
                return True
        else:
            return False
    def digit(self):
        for i in self.passwd:
            if i.isdigit():
                return True
        else:
            return False
    def sp_charc(self):
        for i in self.passwd:
            if i in string.punctuation:
                return True
        else:
            return False
    def validate(self):
        if self.length() and self.digit() and self.lower() and self.upper() and self.sp_charc():
            print("The passwd is valid")
        else:
            print("The passwd is not valid")

password=input("Enter password:")
p=passwd_validator(password)
p.validate()

#2
class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.sentenceList=[]

    def split_into_sentences(self):
        punctuation = ['.', '!', '?']
        sentence = ""
        for char in self.text:
            sentence += char
            if char in punctuation:
                self.sentenceList.append(sentence.strip())
                sentence = ""
        if sentence.strip():  # Add any remaining text as a sentence
            self.sentenceList.append(sentence.strip())
        for i in self.sentenceList:
            print(i)

    def process_sentences(self):
        for sentence in self.sentenceList:
            word_count = len(sentence.split())
            print("Sentence:",sentence,", Word Count:",word_count)

text = "Hello! How are you? I am fine. Let's learn NLP."
p = TextProcessor(text)
p.split_into_sentences()
p.process_sentences()

