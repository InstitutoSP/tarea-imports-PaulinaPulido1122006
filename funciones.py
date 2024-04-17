#Funciones Calculadora
def menu():
  print("-----------------------------------------------------------------")
  print("ingrese S para sumar")
  print("Ingrese R para restar")
  print("Ingrese M para multiplicar")
  print("Ingrese D para dividir")
  print("Ingrese E para tereminar el programa")
  op=input("Ingrese una letra:  ")
  operacion=op.upper()
  print("-----------------------------------------------------------------")
  return operacion

def suma(n1,n2):

        rs=n1+n2
        print("el resultado es",rs)
        menu()
def resta(n1,n2):
        rs=n1-n2
        print("el resultado es ",rs)
        menu()

def multi(n1,n2):
        rs=(n1*n2)
        print("el resultado es ",rs)
        menu()

def div(n1,n2):
        if n2==0:
          print("no se puede dividr por cero, intente de nuevo")
          menu()
        rs=n1/n2
        print("el resultado es ",rs)

        menu()

#Funciones listas
