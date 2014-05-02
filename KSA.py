def KSA(key):
    
    j=0
    s=list(range(256))
    for i in range(256):
        j=(j+s[i]+ord(key[i%len(key)]))%256
        s[i],s[j]=s[j],s[i]
    return s
 

       

if __name__=="__main__":
    key=input("Input your key: ")
    print(KSA(key))
    
    


    
