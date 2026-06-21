from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear productos
producto1 = Producto("Hamburguesa", 5.50)
producto2 = Producto("Jugo Natural", 2.00)

# Crear clientes
cliente1 = Cliente("María Pérez", "0991234567")
cliente2 = Cliente("Juan López", "0987654321")

# Crear restaurante
restaurante = Restaurante()

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("=== PRODUCTOS DISPONIBLES ===")
restaurante.mostrar_productos()

print("\n=== CLIENTES REGISTRADOS ===")
restaurante.mostrar_clientes()
