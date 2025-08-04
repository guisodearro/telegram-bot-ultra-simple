import requests
import time

# Configuración básica
TOKEN_BOT = "8251615729:AAHu8lG5zxycBtqpu3iV_QZxReEEIkorRrc"
BASE_URL = f"https://api.telegram.org/bot{TOKEN_BOT}"

# Configuración de la API para consultas
APIKEY = "1d5b57a92e0a42a69d944cdf68b86d12"
API_BASE_URL = "http://23.175.40.59:8585/back/api/v2/informe"

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    return response.json()

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    response = requests.get(url, params=params)
    return response.json()

def consultar_dni(dni):
    try:
        url = f"{API_BASE_URL}/dni/{dni}?apikey={APIKEY}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            return None
    except Exception as e:
        print(f"Error consultando API: {e}")
        return None

def formatear_persona(persona):
    nombre = persona.get("nombre_completo", "-")
    dni = persona.get("dni", "-")
    fecha_nac = persona.get("fecha_nacimiento", "-")
    domicilio = persona.get("domicilio", "-")
    municipio = persona.get("municipio", "-")
    provincia = persona.get("provincia", "-")
    telefono = persona.get("telefono", "-")
    texto = (
        f"👤 <b>Información encontrada:</b>\n\n"
        f"📝 <b>Nombre:</b> {nombre}\n"
        f"🆔 <b>DNI:</b> {dni}\n"
        f"📅 <b>Fecha nacimiento:</b> {fecha_nac}\n"
        f"🏠 <b>Domicilio:</b> {domicilio}\n"
        f"🏘️ <b>Municipio:</b> {municipio}\n"
        f"🌍 <b>Provincia:</b> {provincia}\n"
        f"📞 <b>Teléfono:</b> {telefono}"
    )
    return texto

def formatear_familiares(familiares):
    if not familiares:
        return "❌ No se encontraron familiares para ese DNI."
    mensaje = f"<b>[ ››› ] Familiares Encontrados ● {len(familiares)}</b>\n"
    for fam in familiares:
        nombre = fam.get("nombre_completo", "-")
        dni = fam.get("dni", "-")
        fecha = fam.get("fecha_nacimiento", "-")
        domicilio = fam.get("domicilio", "-")
        municipio = fam.get("municipio", "-")
        provincia = fam.get("provincia", "-")
        mensaje += (
            f"\n📝 <b>Nombre:</b> {nombre}\n"
            f"🆔 <b>DNI:</b> {dni}\n"
            f"📅 <b>Fecha nacimiento:</b> {fecha}\n"
            f"🏠 <b>Domicilio:</b> {domicilio}\n"
            f"🏘️ <b>Municipio:</b> {municipio}\n"
            f"🌍 <b>Provincia:</b> {provincia}\n"
        )
    return mensaje

def consultar_dni_por_nombre(nombre_completo):
    try:
        url = f"{API_BASE_URL}/nombre/{nombre_completo}?apikey={APIKEY}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 404:
            return None
        else:
            return None
    except Exception as e:
        print(f"Error consultando API: {e}")
        return None

def handle_message(update):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")
    user = message.get("from", {})
    if not chat_id or not text:
        return
    if text == "/start":
        welcome = (
            f"🤖 <b>¡Hola {user.get('first_name', 'Usuario')}!</b>\n\n"
            f"Bienvenido a mi bot ultra simple.\n\n"
            f"📋 <b>Comandos disponibles:</b>\n"
            f"• /start - Este mensaje\n"
            f"• /ping - Probar si el bot responde\n"
            f"• /me - Información sobre ti\n"
            f"• /buscar [nombre] - Buscar DNI por nombre\n"
            f"• /dni [dni] - Consultar datos por DNI\n"
            f"• /familiares [dni] - Consultar familiares por DNI\n\n"
            f"🆔 Tu ID: <code>{user.get('id')}</code>"
        )
        send_message(chat_id, welcome)
    elif text == "/ping":
        send_message(chat_id, "🏓 ¡Pong! El bot está funcionando correctamente.")
    elif text == "/me":
        user_info = (
            f"👤 <b>Información del usuario:</b>\n\n"
            f"🆔 <b>ID:</b> <code>{user.get('id')}</code>\n"
            f"👤 <b>Nombre:</b> {user.get('first_name', 'N/A')}\n"
            f"📝 <b>Username:</b> @{user.get('username', 'Sin username')}\n"
            f"🆕 <b>Es bot:</b> {'Sí' if user.get('is_bot') else 'No'}"
        )
        send_message(chat_id, user_info)
    elif text.startswith("/buscar "):
        nombre = text[8:].strip()
        if not nombre:
            send_message(chat_id, "❌ Uso: /buscar [nombre completo]\n\nEjemplo: /buscar JORGE PEREZ")
            return
        send_message(chat_id, f"🔍 Buscando información para: <b>{nombre}</b>")
        persona = consultar_dni_por_nombre(nombre)
        if persona:
            info_formateada = formatear_persona(persona)
            send_message(chat_id, info_formateada)
        else:
            send_message(chat_id, f"❌ No se encontró información para: <b>{nombre}</b>\n\n💡 Verifica que el nombre esté escrito correctamente.")
    elif text.startswith("/dni "):
        dni = text[5:].strip()
        if not dni.isdigit():
            send_message(chat_id, "❌ Uso: /dni [DNI]\n\nEjemplo: /dni 12345678")
            return
        send_message(chat_id, f"🔍 Buscando información para DNI: <b>{dni}</b>")
        persona = consultar_dni(dni)
        if persona:
            info_formateada = formatear_persona(persona)
            send_message(chat_id, info_formateada)
        else:
            send_message(chat_id, f"❌ No se encontró información para el DNI: <b>{dni}</b>")
    elif text.startswith("/familiares "):
        dni = text[12:].strip()
        if not dni.isdigit():
            send_message(chat_id, "❌ Uso: /familiares [DNI]\n\nEjemplo: /familiares 12345678")
            return
        send_message(chat_id, f"🔍 Buscando familiares para DNI: <b>{dni}</b>")
        persona = consultar_dni(dni)
        if persona and "familiares" in persona:
            familiares = persona["familiares"]
            mensaje = formatear_familiares(familiares)
            send_message(chat_id, mensaje)
        elif persona:
            send_message(chat_id, "❌ No se encontraron familiares para ese DNI.")
        else:
            send_message(chat_id, f"❌ No se encontró información para el DNI: <b>{dni}</b>")
    else:
        send_message(chat_id, f"📢 <b>Tu mensaje:</b> {text}")

def main():
    print("🤖 Iniciando bot ultra simple...")
    print("✅ Bot configurado correctamente")
    print("📱 Ve a tu bot en Telegram y envía /start")
    print("🔄 El bot está escuchando mensajes...")
    print("⏹️  Presiona Ctrl+C para detener")
    offset = None
    try:
        while True:
            try:
                updates = get_updates(offset)
                if updates.get("ok"):
                    for update in updates.get("result", []):
                        update_id = update.get("update_id")
                        if update_id:
                            offset = update_id + 1
                        handle_message(update)
                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)
    except KeyboardInterrupt:
        print("\n⏹️  Bot detenido por el usuario")

if __name__ == "__main__":
    main() 