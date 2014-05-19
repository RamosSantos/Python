def SendNumber(a):
    b=[0]*len(a)
    for i in range(10):
        b[i]=int(a[i])
    return b

def module11(b):
    mod=[11,10,9,8,7,6,5,4,3,2]
    aux=0
    for i in range(10):
        result=b[i]*mod[i]
        aux+=result
    verificator=aux%11
    verificator=11-verificator
    return print(verificator)

if __name__=='__main__':

    l=input("Digite:")
    l=SendNumber(l)
    module11(l)
    

    
