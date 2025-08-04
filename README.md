# 🤖 Bot de Telegram Ultra Simple

Bot de Telegram creado con Python y la librería `requests` para consultas de DNI, familiares, MinSeg y boletos.

## 📋 Comandos Disponibles

- `/start` - Mensaje de bienvenida
- `/ping` - Probar si el bot responde
- `/me` - Información del usuario
- `/buscar [nombre]` - Buscar DNI por nombre completo
- `/dni [DNI]` - Consultar datos por DNI
- `/familiares [DNI]` - Consultar familiares por DNI
- `/minseg [DNI]` - Consultar información en MinSeg por DNI
- `/boleto [DNI]` - Consultar boleto por DNI

## 🚀 Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar el token del bot en `bot_ultra_simple.py`

3. Ejecutar:
```bash
python bot_ultra_simple.py
```

## 🔧 Configuración

- **Token**: Configurar `TOKEN_BOT` en el archivo principal
- **API**: Configurar `APIKEY` y `API_BASE_URL` para las consultas
- **MinSeg API**: Configurar `MINSEG_API_URL` (por defecto: localhost:5011)
- **Boleto API**: Configurar `BOLETO_API_URL` (por defecto: localhost:5020)

## 📝 Autor

Peke77 