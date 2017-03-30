#Break a string with a newline every x characters
#The program will never break a word in half
# By Aden Huen 

def linebreak(string,width):
    try:
        if type(string) == type("string") and type(width) == type(5):
            wstr = string.split()
            count = 0;
            for word in wstr:
                if len(word) <= width:
                    count+=1
                    
            if count == len(wstr):
                str = list(string)
                for i in range (width-1, len(str), width):
                    while str[i] != " ":
                       i-=1
                    str[i] = "\n"
                string = "".join(str)
                print(string)
                return None
            else:
                return("The line break length is too small.")
            
            
        else:
            return("Please enter valid arguments.")

    except Exeption:
        print("Error initiating...")
    
    
    
    
