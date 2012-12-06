'''
Created on Nov 23, 2012
@author: SC
'''
def main():
    s=r'''\
    salam halet khobe
    manam\n khobam
    kojaE?!
    che mikoni?!
    '''
    print(s);
    a, b ,c = 0 , 1 , 5
    
    if a<b :
        print('a({}) is less than b({}) and c is {} '.format(a,b,c))
    else:
        print('b({}) less than a({})')
        
    v='c is grather than b' if c>b  else 'b is grattest'
    print(v)
    print('hi' if a < c else 'bye' )
    s='this is a string'
    for i, l in enumerate(s) :
        if l=='s': print('is in {}'.format(i))
    
    x=5
    print('{:05b}'.format(x))
    list=[1,2,3,4,5]
    list[:] = range(100)
    print(list[0:100])
    fibonachi()
    fact()
    
    

#fibonachi
def fibonachi():
    print ('fibonachi')
    a , b = 0 , 1
    while b<50:
        print(b)
        a,b=b,a+b
    print('end of fibonachi')
    print()
#fact
def fact():
    m, s= 5, 1
    n=m
    while n>0:
        s=n*s
        n=n-1
    print('fact of {} is {}'.format(m,s))

if __name__== "__main__": main()


