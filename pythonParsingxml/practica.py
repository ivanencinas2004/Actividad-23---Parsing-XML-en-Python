from bs4 import BeautifulSoup


print('PRUEBA EN pYTHON')

with open ('CatalogoProductos.xml','r') as f:
    data=f.read()
#print(data)

Bs_data=BeautifulSoup(data,'xml')
#print(Bs_data)
desc=Bs_data.find_all('Descripcion')
#print(descripcion)


for tag in Bs_data.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = "9.95"

print(Bs_data.prettify())