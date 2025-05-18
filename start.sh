#!/bin/bash
echo "🔧 Instalando navegador Chromium..."
playwright install chromium
echo "🚀 Iniciando o bot..."
python main.py
