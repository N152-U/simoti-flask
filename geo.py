import psycopg2
import requests
import time
class BaseDatos:
    def __init__(self):
        self.connection = psycopg2.connect(
                host = "10.11.11.207",
                user = "postgres_dev",
                password = "Dt1c-s4cm3x_p0stgr3s14_d3v",
                database = "test",
                port="5430"
            )
        print("Conexión Exitosa")
    def updateOne(self,consulta):
        self.cursor = self.connection.cursor()
        self.sql = consulta
        self.cursor.execute(self.sql)
        self.connection.commit()
        self.cursor.close()
    def qwerysAll(self,consulta):
        self.cursor = self.connection.cursor()
        self.sql = consulta
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.cursor.close()
        return self.rows
db=BaseDatos()
#tablas a modificar
tablas=["hist2019","hist2020","hist2021","fugas2018","fugas2019"]
llaves=["KuTECA4h9SUsiJFxDmiAaVeINZdsPhm3HnpPUAU7QWw","jFIUgihf3yVuRK7uVL2ts8HF36hXFS6ZbxylNOeNU-8","QMoMpDNd1O_bWe1MOUR4pOQDhwzRaJVXvHhqKDs7a60",
        "j2WXHqb8PHn4RemAEbhN4ewLTf_mgEtQEDJD4ziJOzU","DFVyj4xKrsfL38GCWoOI5WpLof8zgFf2VnDDi4JQHJw","QrsKhR6FipQyELaPajZ4rk3Zm7APOBAo8etc_9wEoPw",
        "S4-migd4GYKMt7K089N3xXBy0SGdmvnawifdkuQfqbY","UT-IcQmIX-2PpXqIL-Hkw5VOVPOeXqB0AsC09FCx098","EMqo6Y5v06dJOvBudEEuqEzuuk6FyMUy0XGUBN3uVwQ",
        "f2JCXZUrBcA_9l7hiqOQwjrHkIdJZeA3Z1lFas7NFds","GNqMABHorni2FSED6hw0-ssrhQ5vZ5hj8iNvY3Faqm8","nidL1T2KpxBsmIKmmgnE6CBcQ7nbU6T5tymDxbDtNnA",
        "5JNas6mpa61r2o2AOL2rtoPPjpvum2WDOD-3T-oWwcs","5no467kaiJkhbQU3EldJ3pTN_fJGRprKpOBE2n0cPLI","TmnNg6sZ4fywAJG25H9o9UYsvdBfFAnoqF_WljTJQSc",
        "-H7C2LgkT4ggzW_V2MjDsYqiPFjoqKiHD0hAm4qpObg","8l0EjPepQHYU_KdkYniobTjlQGbdzcKsckPhjOU8gZQ","eRGfgpQhIdAQZruWpFEhBxTy7JD5EIWdrx9q8Jd830U",
        "4lftYJ00m9GbwTYtJy_bHSsIyGWrWCcug1wtr_Kc4C0","jOsIkGWEMVRYeN474L7fHGlRjXYoPd0ix8ovhpHsTE4","8w17pVu4eC6mqIIWHcKFJcOScTPeQ55nT_Bag3ZCLNA",
        "RuRNrLtd0Iq54QqFTHPnnPyPTVd7_PIQndhfIWYg1MY","Bt05mKEHHe292vCIbMfduXcQru2JAWJxUFvIfY1F9is","yV5o1weIHSYIBl921Iowxts4YYVstUlCPmu-DajQ0ns",
        "f4mw-cbxnQCyMw3icfB7lVgaFlC4UjHYGWRQEPib87g","5P7BivMGu4THrP6t1zfohcixdvzH3sxX9A0d948_Ihc","NsXt41tv1tbNHIA9B4mLEKbUUajPiuUgOtt03EKuuf8",
        "RuDXW49RchuR_u-25Pfv_uy3Dl9F1izzIWBKDtFhxiQ","1vbtZiiDVXHMt2QpiXKWEss_aIE6Ioz_3ixShHhYu6A","BzDqzhpTHzgabalRBqZ5B-r1hXkkEQILzTlpPbu98eU",
        "lzUXv-fxHZOYnHw4SIpDH2PFGY_GxSvNa8Iz3zoK_5k","1aM071IfK84G7v761k4UzP3qFIdOhDz4rnpkL8YU7fg","pv9ELJNJYXEQoh3WLYbDXBUlDxEvJxlKF0L7RVRJkfk",
        "-Rim6HIh4tMWQl19FyIpj66svKuOTwkmmRH6JgY0JOc","NGDng20ahjtLnpnHUDGdfp8M_G4k0G5t3vLLOSlTPOk","LRi5R1izBebuDCyy-IQXNAoy4PsL9Tcr2J-CNehOdF0",
        "Uk5dNixacLmXq_PD3ZKkUA7rSWGMHtyVtRgIgF-MTb8","g-nx0fGBEw0kQQttYj1YrrpxO3vzRSjI6NLHfmw-EcE"]
db=BaseDatos()
campos=["FOLIO","ALCALDIA","DIRECCION","LATITUD","LONGITUD"]
def Postal(ide):#Da formato de codigo postal
  numeracion=""
  ceros=""
  for x in range(5-len(format(ide))):
    ceros=ceros+"0"
  numeracion=ceros+format(ide)
  return numeracion
def coords3(direccion,key):
    url3=f"https://geocode.search.hereapi.com/v1/geocode?q={direccion}&limit=4&apiKey={key}"
    print(direccion)
    response=requests.get(url3)
    print(response)
    try:
        if response.status_code==200:
            data=response.json()
            cartesiano=data.get("items")
            print(cartesiano)
            cartesiano=cartesiano[0].get("position")
            latitud=cartesiano.get("lat")
            longitud=cartesiano.get("lng")
            return [latitud,longitud],0
        elif response.status_code==429:
            return ["ERR","ERR"],1
        else:
            return ["ERR","ERR"],2
    except:
        return ["ERR","ERR"],2
  #-----------------------------------------------------------------------------
def direccionTune(Direction,Pais="Mexico"):
    calle=Direction.split(",")
    Alcaldia=calle[3].strip(" ").split(" ")
    Alcaldia="+".join(Alcaldia)
    cp=Postal(calle[2].strip(" "))
    col=calle[1].strip(" ").split(" ")
    col="+".join(col)
    calle=calle[0].strip(" ").split(" ")
    temp=[]
    for x in range(len(calle)):#calle y numero
        if not (calle[x]=="#" or "#" in calle[x] or calle[x]=='' or "INT." in calle[x] or"(" in calle[x]):
            temp.append(calle[x].strip(" "))
        elif "#" in calle[x] and not calle[x]=="#" :
            aux=calle[x].strip(" ").split("#")
            temp.append(aux[1])
        elif "INT." in calle[x]:
            break
        else:
            pass
    calle="+".join(temp)
    nDire=calle+"+"+col+"+"+cp+"+"+Alcaldia.replace(" ","+")+"+"+Pais
    return nDire
# cp=Postal(Perdidos[0][3])
# test=direccionTune(cp,Perdidos[0][2],Perdidos[0][1])
# print(test + "")
  #-----------------------------------------------------------------------------
def Omar(key):
    rev=[]
    cont=0
    useKey=0
    control=0
    while control<len(tablas):
        Perdidos=db.qwerysAll(F"select {campos[0]},{campos[1]},{campos[2]} FROM {tablas[control]} where {campos[3]} IS NULL AND {campos[4]} IS NULL")
        while len(Perdidos) >0 :
            direccion=direccionTune(Perdidos[0][2])
            Morsa,err=coords3(direccion,key[useKey])
            print(f"key: {Perdidos[0][0]}")
            if err==0:
                print(str(Morsa[0])+" "+str(Morsa[1]) + " coords")
                db.updateOne(f"""update hist2019 set latitud = {Morsa[0]} , longitud = {Morsa[1]}  where folio='{str(Perdidos[0][0])}' """ )
                print(f"corrio la consulta en {Perdidos[0][0]}")
                Perdidos.pop(0)#saca de la lista los ya buscados
                cont=cont+1
                print(str(cont)+ " consultas realizadas")
            elif err==1:
                print("--------------------------------------------------------------------------------------")
                print("cambio de llave...")
                time.sleep(1)
                useKey+=1
            else:
                rev.append(Perdidos[0])
                Perdidos.pop(0)
                print(rev)
            print("-------------------------------------------------------------------------------------------------------")
        control+=1
        print("cambio de tabla")
        time.sleep(1)
Omar(llaves)
#00 es colonia, 01 s alcaldia , 03 CP ,02 calle
#
##para generar nuevas llaves en pacog7870@gmail.com Pass: Gerte1234
#j82177887@gmail.com:           2E&sDVezTQpb
#pruebasimollu1@outlook.com:    nO1pS_s88zoE
#pruebasimollu2@outlook.com:    -Q`C^5lw41G4
#pruebasimollu3@outlook.com :   0MQi4}M5j^61
# <Response [401]>