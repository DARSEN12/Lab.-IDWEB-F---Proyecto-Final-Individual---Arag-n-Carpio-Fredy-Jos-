#!C:/Python311/python.exe
# ↑ Ajusta la ruta según la versión de Python instalada en tu PC

import cgi
import html

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
descripcion = form.getvalue("descripcion", "")
cantidad = form.getvalue("cantidad", "")
metodo_pago = form.getvalue("metodo_pago", "")
otros_detalles = form.getvalue("otros_detalles", "")

print("<html><head><title>Pedido Recibido</title></head><body>")
print("<h1>Pedido Registrado</h1>")
print(f"<p><strong>Descripción:</strong> {html.escape(descripcion)}</p>")
print(f"<p><strong>Monto:</strong> S/ {html.escape(cantidad)}</p>")
print(f"<p><strong>Método de Pago:</strong> {html.escape(metodo_pago)}</p>")

if metodo_pago == "Otros":
    print(f"<p><strong>Detalles:</strong> {html.escape(otros_detalles)}</p>")

# 🔒 Aquí más adelante puedes conectar a base de datos (ejemplo con SQLite o MySQL)
# import sqlite3
# conn = sqlite3.connect("pedidos.db")
# conn.execute("INSERT INTO pedidos (descripcion, cantidad, metodo_pago) VALUES (?, ?, ?)",
#              (descripcion, cantidad, metodo_pago))
# conn.commit()

print("<a href='../pedido.html'>⬅ Volver al formulario</a>")
print("</body></html>")