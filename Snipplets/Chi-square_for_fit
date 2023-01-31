def simple_chisquare (array, expected_value):
    x2 = 0
    deg_freedom = len(array) - 1
    for i in range(0,len(array)):
        
        x2 += ((array[i] - expected_value)**2)/expected_value
        
    return x2, deg_freedom

chi, deg = simple_chisquare (array, expected_value)

print ("Chi square = {0}   and   'degrees of freedon' = {1}".format(chi,deg))
