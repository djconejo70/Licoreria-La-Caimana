from licoreriaapp.precio_bcv import*

def total_carrito(request):
    totalbs=0
    total=0
    x=valorDolar()
    a=x[0]
    # print(a, type(a))
    if a!=0.0:
        mivar = (a.split(' ')[0])
        mivar=mivar.replace(",", ".")
        mivar1=float(mivar)
        mivar1=round(mivar1, 2)   
        # print(mivar1, type(mivar1))
    else:
        mivar1=0.00
        
    # if request.user.is_authenticated:
    #     for key,value in request.session["carrito"].items():
    #         total = total + float(value["subtotal"])
    #         totalbs=total* mivar1
    #         totalbs=round(totalbs,2)
            
    # else:
    #     totalbs=0.00
        
    return{"total_carrito":total, "totalbs":totalbs }
# , "totalbs":totalbs
    