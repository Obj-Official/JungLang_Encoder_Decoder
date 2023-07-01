#Encode class to encode message
class EncodeMsg:
    #initializer
    def __init__(self, msg):
       self.NumberOfCharacter =  len(msg) 
       self.currentCharIndex = 0
       self.msg = msg
       self.encodedmsg = ""
       self.numDigit = 0
       
    #The method that ecodes the message written in normal English
    def processEncode(self):
       while self.currentCharIndex < self.NumberOfCharacter:
           numchar = str(self.msg[self.currentCharIndex].isdigit())
           if self.msg[self.currentCharIndex] == "a" :
               self.encodedmsg = self.encodedmsg + "1"
           elif self.msg[self.currentCharIndex] == "e" :
               self.encodedmsg = self.encodedmsg + "2"
           elif self.msg[self.currentCharIndex] == "i" :
               self.encodedmsg = self.encodedmsg + "3"
           elif self.msg[self.currentCharIndex] == "o" :
               self.encodedmsg = self.encodedmsg + "4"
           elif self.msg[self.currentCharIndex] == "u" :
               self.encodedmsg = self.encodedmsg + "5"
           elif self.msg[self.currentCharIndex] == " " :
               self.encodedmsg = self.encodedmsg + " "
           elif numchar == "True":
               x=""
               while numchar == str(self.msg[self.currentCharIndex].isdigit()): 
                   numStr = self.msg[self.currentCharIndex]
                   x = x + numStr
                   self.numDigit = int(x)
                   self.currentCharIndex += 1
                   if self.currentCharIndex == self.NumberOfCharacter:
                       break               
               numcode = ""
               for i in range (0, self.numDigit):
                   numcode = numcode + "%"
               self.encodedmsg = self.encodedmsg + numcode
               self.currentCharIndex -= 1
           else :
               self.encodedmsg = self.encodedmsg + self.msg[self.currentCharIndex] + "a"
           self.currentCharIndex += 1
       return self.encodedmsg

#Decode class to decode an encoded message        
class DecodeMsg:
    def __init__(self, msg):
       self.NumberOfCharacter = len(msg)
       self.currentCharIndex = 0
       self.msg = msg
       self.decodedmsg = ""
       
     #The method that decodes the encoded message and outputs normal English
    def processDecode(self):
        while self.currentCharIndex < self.NumberOfCharacter:
            if self.msg[self.currentCharIndex] == "1" :
               self.decodedmsg = self.decodedmsg + "a"
            elif self.msg[self.currentCharIndex] == "2" :
               self.decodedmsg = self.decodedmsg + "e"
            elif self.msg[self.currentCharIndex] == "3" :
               self.decodedmsg = self.decodedmsg + "i"
            elif self.msg[self.currentCharIndex] == "4" :
               self.decodedmsg = self.decodedmsg + "o"
            elif self.msg[self.currentCharIndex] == "5" :
               self.decodedmsg = self.decodedmsg + "u"
            elif self.msg[self.currentCharIndex] == " " :
               self.decodedmsg = self.decodedmsg + " "
            elif self.msg[self.currentCharIndex] == "%":
               numberr = 0               
               while self.msg[self.currentCharIndex] == "%" :
                   numberr += 1
                   self.currentCharIndex += 1 
                   if self.currentCharIndex == self.NumberOfCharacter:
                       break
               self.decodedmsg = self.decodedmsg + str(numberr)
               self.currentCharIndex -= 1
            elif self.msg[self.currentCharIndex] == "a" :
               self.decodedmsg = self.decodedmsg + self.msg[self.currentCharIndex - 1]
            self.currentCharIndex += 1 
        return self.decodedmsg

#main funtion, for testing this module  in the console         
def main():
    print("Choose operation")
    operationn = input("Enter 1 to encode or 2 to decode: ")
    msg = input("Enter a message: ")
    messagex = ""
    if operationn == "1" :
        messagex = EncodeMsg(msg)
        print(messagex.processEncode())
    elif operationn == "2":
        messagex = DecodeMsg(msg)
        print(messagex.processDecode())
    
#main()#main function call
