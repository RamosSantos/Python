'''
                ### Script that generate a key KSA###
            Implentation of the algorithm by Felipe Ramos
    
    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
'''

def SendNumber(a):
    b=[0]*len(a)
    for i in range(len(a)):
        b[i]=int(a[i])#Distributes a letter to each position vector
    return b

def module11(b):
    mod=[11,10,9,8,7,6,5,4,3,2]
    aux=0
    for i in range(len(b)):
        result=b[i]*mod[i]#First char * last position in the vector
        aux+=result
    verificator=aux%11#Rules of module11
    verificator=11-verificator
    return print(verificator)

if __name__=='__main__':

    l=input("Digite:")
    l=SendNumber(l)
    module11(l)
    

    
