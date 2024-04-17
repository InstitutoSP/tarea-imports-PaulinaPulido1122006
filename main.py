
import funciones as fn

ope = fn.menu()

if ope == "S":
       n1=int (input("Ingrese primer numero:  "))
       n2=int(input("Ingrese segundo numero:  "))
       fn.suma(n1,n2)
      
elif ope == "R":
       n1=int (input("Ingrese primer numero:  "))
       n2=int(input("Ingrese segundo numero:  "))
       fn.resta(n1,n2)
elif ope == "M":
       n1=int (input("Ingrese primer numero:  "))
       n2=int(input("Ingrese segundo numero:  "))
       fn.multi(n1,n2)
elif ope == "D":
       n1=int (input("Ingrese primer numero:  "))
       n2=int(input("Ingrese segundo numero:  "))
       fn.div(n1,n2)
elif ope == "E":
       print("programa finalizado")
else:
        print("invalido, intente de nuevo")
        fn.menu()

fn.menu()


