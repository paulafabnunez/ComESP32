import tkinter as tk     # Para la interfaz grafica
from tkinter import ttk  # Para agregar mas estilos 
import socket
import threading
import time 

# --- Configuracion ---
IP_ESP32 = "192.168.20.12"
Puerto = 80 

# --- Clase de datos (para practicar) ---
class DatosSensor:
    def_init_(self, valor):
        self.valor = valor 



