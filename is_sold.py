import tkinter as tk
from woocommerce import API

# Vinculación WooCommerce

v_url = 'XXXXXXXXXXXXXXX' # Your WordPress Link
v_consumer_key = 'ck_XXXXXXXXXXXXXXXXXXXX' # Your WooCommerce API Consumer Key
v_consumer_secret = 'cs_XXXXXXXXXXXXXXXXXXX' # Your WooCommerce API Consumer Secret Key


wcapi = API(
    url = v_url,
    consumer_key = v_consumer_key,
    consumer_secret = v_consumer_secret,
    wp_api = True,
    version = 'wc/v3'
)


#-------------------------------------------------------------------------
# Aspecto & Función
#-------------------------------------------------------------------------

root = tk.Tk()
root.geometry("470x350")
root.tk_setPalette("#ea91fa")
root.title('Window Title')

my_label = tk.Label(root)

my_label.place(x=0,y=0,relwidth=1,relheight=1,width=1,height=1)

miFrame = tk.Frame(root,padx=30,pady=10)
miFrame.pack()

nombreProd = tk.StringVar()
colorProd = tk.StringVar()
talleProd = tk.StringVar()

labelNombre= tk.Label(miFrame,text="Article Name: ",font=(14))
labelNombre.grid(row=0,column=0,pady=7)

labelColor= tk.Label(miFrame,text="Article Color: ",font=(14))
labelColor.grid(row=1,column=0,pady=7)

labelTalle= tk.Label(miFrame,text="Article Shape: ",font=(14))
labelTalle.grid(row=2,column=0,pady=7)

cuadroNombre= tk.Entry(miFrame,textvariable=nombreProd,bg="white",font=(14))
cuadroNombre.grid(row=0,column=1,pady=7)

cuadroColor= tk.Entry(miFrame,textvariable=colorProd,bg="white",font=(14))
cuadroColor.grid(row=1,column=1,pady=7)

cuadroTalle= tk.Entry(miFrame,textvariable=talleProd,bg="white",font=(14))
cuadroTalle.grid(row=2,column=1,pady=7)


def codigoBoton():
    pedidos = []
    product_name = nombreProd.get()
    product_color = colorProd.get()
    product_shape = talleProd.get()


    product_search = ""
    if (product_name!="") & (product_color!="") & (product_shape!=""): product_search = f"{product_name}+-+{product_color}%2C+{product_shape}"
    elif (product_name=="") & (product_color!="") & (product_shape!=""): product_search = f"{product_color}%2C+{product_shape}"
    elif (product_name!="") & (product_color=="") & (product_shape!=""): product_search = f"{product_name}+-+{product_shape}"

    if " " in product_search:
        product_search=product_search.replace(" ","+")
        
    print("\n")


    sold = ""
    try:
        orders = wcapi.get(f"orders?search={product_search}&per_page=100").json()
        
        for i in orders:
            if ("processing" in i["status"])|("order" in i["status"])|("aprobado" in i["status"]):
                sold = f"Order {i['id']} de {i['billing']['first_name']} {i ['billing']['last_name']}"
                pedidos.append(sold)
                
    except: print("#ERROR de programa o faltan datos. Consultar con Ciro.")
    print("----------------------------------------------")
    if sold=="": esta_vendido.config(text=f'[{product_name} - {product_color}, {product_shape}] - IS NOT sold',fg='green')
    else: esta_vendido.config(text=f'[{product_name} - {product_color}, {product_shape}] - Is Sold',fg='red')
    
    pedidos_vendidos.config(text=pedidos)
    
    
botonBuscar = tk.Button(root,text="Search",command=codigoBoton,bg="#fff")
botonBuscar.pack()

esta_vendido = tk.Label(root,text='',font=(14))
esta_vendido.pack()

pedidos_vendidos = tk.Label(root,text='',font=(11),wraplength=300)
pedidos_vendidos.pack()

root.mainloop()