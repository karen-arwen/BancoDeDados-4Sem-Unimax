#Interface gráfica com tkinter para preencher campos de banco de dados, botões de inserir, excluir, atualizar e listar

import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import os
import sys
import ctypes
import platform


def conectar():
