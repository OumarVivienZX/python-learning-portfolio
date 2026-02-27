def table_de_multplication(n,min=1,max=10):

    result = 0
    if min > max :
        print("❌ERREUR❌")
        return
    for i in range (min , max+1 ) : 
     print (f" {n} × {i} = {n*i} ")


table_de_multplication(5,max=20)