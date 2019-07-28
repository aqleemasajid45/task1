class CharacterCount:
    str1=''
    def function1(self,a):
        if type(a)==str:
            self.str1=a
           
        else:
            print("invalid input")
    def function2(self):
        return len(self.str1)
    
    
str2= "hello world"   
obj=CharacterCount()
obj.function1(str2)
print(obj.function2())
            
 
