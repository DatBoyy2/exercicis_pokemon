i=Objeto1={
    
    "Nombre":"PokeBall",
    "Precio":200

}

a=objeto2={

    "Nombre":"SuperBall",
    "Precio":600

}

h=objeto3={

    "Nombre":"UltraBall",
    "Precio":800

}

j=objeto4={

    "Nombre":"Pocion",
    "Precio":300

}

m=objeto5={

    "Nombre":"Superpocion",
    "Precio":700

}

n=objeto6={

    "Nombre":"UltraPocion",
    "Precio":1500

}

s=objeto7={

    "Nombre":"Max. Pocion",
    "Precio":2500

}

q=objeto8={

    "Nombre":"Restaurar Todo",
    "Precio":3000

}

w=objeto9={

    "Nombre":"Antidoto",
    "Precio":200

}

t=objeto10={

    "Nombre":"Antiparaliz.",
    "Precio":200

}

l=objeto11={

    "Nombre":"Despertar",
    "Precio":200

}

p=objeto12={

    "Nombre":"Antiquema.",
    "Precio":200

}

o=objeto13={

    "Nombre":"anticongel.",
    "Precio":200

}

k=objeto14={

    "Nombre":"Cura Total",
    "Precio":600

}

print("Bienvenido a la tienda...")
print("1:")
print(i)
print("2:")
print(a)
print("3:")
print(h)
print("4:")
print(j)
print("5:")
print(m)
print("6:")
print(n)
print("7:")
print(s)
print("8:")
print(q)
print("9:")
print(w)
print("10:")
print(t)
print("11:")
print(l)
print("12:")
print(p)
print("13:")
print(o)
print("14:")
print(k)
print("15: Nada")
x=input("Que quieres comprar(Selecciona numero del producto)??")

if x=="1":
    print("Has seleccionado:")
    print(i["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(i*n1)
    print("tu cuenta es de"+res1)
