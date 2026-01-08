with (
    open('dff.txt') as f1, 
    open('tred.txt') as f2,
    open('c11.txt') as f3 # and we can open more file's with this with
):
   
    print(f1.read())
    
    print(f2.read())
    
    print(f3.read())