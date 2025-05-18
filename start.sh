#!/bin/bash
echo "Instalando navegadores do Playwright..."
playwright install chromium
echo "Iniciando o bot..."
python main.py
