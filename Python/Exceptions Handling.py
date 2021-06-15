#Exceptions Handling
import sys
def main():
    try:
        print('hi')
        x=15/0
        x=int(y)
    #except ZeroDivisionError:
        #print("dont divide by zero")
    except:
        print(f"unkwnoun error {sys.exc_info()[1]}") 
    else:
        print('good job')   
    def func1():            
        if False:
            x=1120/0.0
        else:
            raise TypeError('again dividing by floating zero')
    try:
        func1()
    except TypeError as e:
        print(f'some error raise {e}')       
    

main()        
