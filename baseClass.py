from typing import Type


class KeyboardBase:

    def __init__(self,keyboard:list) -> None:
        self.val_to_index={keyboard[i]:i for i in range(len(keyboard))}
        self.index_to_val=keyboard

    def get_val(self,index):
        return self.index_to_val[index]
    
    def get_index(self,val):
        return self.val_to_index[val]
    
    def val_exists(self,val):
        return val in self.val_to_index

    def translate(self,text:str,to_keyboard)->str:
        if not isinstance(to_keyboard,KeyboardBase):
            raise TypeError()
        newstring=""
        for s in text:
            if self.val_exists(s):
                ind =self.get_index(s)
                newstring+=to_keyboard.get_val(ind)
            else:
                newstring+=s
        return newstring
        
    

class HebrewKeyboard(KeyboardBase):

    def __init__(self) -> None:
        keyboard=["/","'","ק","ר","א","ט","ו","ן","ם","פ","]","[","ש","ד","ג","כ","ע","י","ח","ל","ך","ף",",","ז","ס","ב","ה","נ","מ","צ","ת","ץ","."]
        super().__init__(keyboard)


class EnglishKeyboard(KeyboardBase):

    def __init__(self) -> None:
        keyboard=["q","w","e","r","t","y","u","i","o","p","[","]","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","/",]
        super().__init__(keyboard)

hebrew=HebrewKeyboard()
english=EnglishKeyboard()
print(hebrew.translate("דאןךך 'םרלד?",english))
