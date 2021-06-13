import matplotlib.pyplot as plt

v = 140000          # ventas
u = 7000            # unidades vendidas
pu = 20             # precio por unidad
cv = 56000          # costos variables
cf = 44000          # costos fijos
ga = 16000          # gastos adicionales (pj: interes, impuestos)
pe = (ga+cf)/(1-cv/v)    # punto de equilibrio

v=v/1000
u=u/1000
cv=cv/1000
cf=cf/1000
ga=ga/1000
pem = pe/1000       # punto de equilibro sobre mil

# ****** anotaciones ******
# plt.plot(dominio de X, rango de Y)

plt.plot([0,u], [0, v], 'b-', label="ventas totales")
plt.plot([0,u], [cf,cv+cf], 'r-', label="costos variables")
plt.plot([0,u], [cf, cf], 'g-', label="costos fijos")

plt.annotate('punto de equilibrio', xy=(pem/pu, pem), xytext=(pem/pu*.3, pem*1.2), arrowprops=dict(facecolor='black', shrink=0.1))
plt.text(0, pem*.9, f'${pe:,.1f} pesos')
plt.text(pem/pu*1.03, 0, f'{pe/pu:,.1f} unidades')
plt.plot(pem/pu, pem, 'ok')
plt.plot([0,pem/pu], [pem,pem], 'k--')
plt.plot([pem/pu,pem/pu], [0,pem], 'k--')

plt.title('Planteamiento de utilidades')
plt.ylabel('miles de pesos')
plt.xlabel('miles de unidades')

plt.legend()
plt.savefig('plot.png')
plt.show()
