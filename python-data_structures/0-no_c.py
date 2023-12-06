def no_c(my_string):
    no_cstring=''
    for char in my_string:
        if char=='c' or char=='C':
            continue
        no_cstring= no_cstring+char
    
    
    
    
    
    return no_cstring