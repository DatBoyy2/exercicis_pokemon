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

#1er objeto

if x=="1":
    print("Has seleccionado:")
    print(i["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(i["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="1":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#2do objeto

if x=="2":
    print("Has seleccionado:")
    print(a["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(a["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="2":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#3er objeto

if x=="3":
    print("Has seleccionado:")
    print(h["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(h["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="3":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#4to objeto

if x=="4":
    print("Has seleccionado:")
    print(j["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(a["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="4":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#5to objeto

if x=="5":
    print("Has seleccionado:")
    print(m["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(m["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="5":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#6to objeto

if x=="6":
    print("Has seleccionado:")
    print(n["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(n["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="6":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#7 objeto

if x=="7":
    print("Has seleccionado:")
    print(s["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(s["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="7":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#8 objeto

if x=="8":
    print("Has seleccionado:")
    print(q["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(q["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="8":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#9 objeto

if x=="9":
    print("Has seleccionado:")
    print(w["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(w["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="9":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#10 objeto

if x=="10":
    print("Has seleccionado:")
    print(t["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(t["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="10":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#11 objeto

if x=="11":
    print("Has seleccionado:")
    print(l["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(l["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="11":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#12 objeto

if x=="12":
    print("Has seleccionado:")
    print(p["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(p["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="12":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#13 objeto

if x=="13":
    print("Has seleccionado:")
    print(o["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(o["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="13":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="14":
            print("Has seleccionado")
            print(k["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(k["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")

#14 objeto

if x=="14":
    print("Has seleccionado:")
    print(k["Nombre"])
    n1=int(input("Que cantidad quieres?"))
    res1=(k["Precio"]*n1)
    print("tu cuenta es de:")
    print(res1)
    p2=input("Quieres algo mas(S/N)?")
    if p2=="S":
        x2=input("Que otro objeto quieres?")
        if x2=="14":
            print("ya has comprado este articulo, total de la cuenta:")
            print(res1)
            print("muchas gracias por comprar!!")
        if x2=="1":
            print("Has seleccionado")
            print(i["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(i["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="3":
            print("Has seleccionado")
            print(h["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(h["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="4":
            print("Has seleccionado")
            print(j["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(j["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="5":
            print("Has seleccionado")
            print(m["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(m["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="6":
            print("Has seleccionado")
            print(n["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(n["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="7":
            print("Has seleccionado")
            print(s["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(s["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="8":
            print("Has seleccionado")
            print(q["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(q["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="9":
            print("Has seleccionado")
            print(w["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(w["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="10":
            print("Has seleccionado")
            print(t["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(t["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="11":
            print("Has seleccionado")
            print(l["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(l["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="12":
            print("Has seleccionado")
            print(p["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(p["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="13":
            print("Has seleccionado")
            print(o["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(o["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
        if x2=="2":
            print("Has seleccionado")
            print(a["Nombre"])
            na=int(input("Que cantidad quieres?"))
            res2=(res1+(a["Precio"]*na))
            print("tu cuenta ahora es de:")
            print(res2)
            print("Muchas gracias por comprar!")
    if p2=="N":
        print("Muchas gracias por comprar!!")







