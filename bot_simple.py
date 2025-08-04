import os
import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configuración básica
TOKEN_BOT = "8251615729:AAHu8lG5zxycBtqpu3iV_QZxReEEIkorRrc"

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ----------------- COMANDOS BÁSICOS ----------------- #

def start(update: Update, context: CallbackContext):
    """Comando /start - Mensaje de bienvenida"""
    user = update.effective_user
    
    welcome_message = (
        f"🤖 <b>¡Hola {user.first_name}!</b>\n\n"
        f"Bienvenido a mi bot personal.\n\n"
        f"📋 <b>Comandos disponibles:</b>\n"
        f"• /start - Este mensaje\n"
        f"• /comandos - Ver todos los comandos\n"
        f"• /me - Información sobre ti\n"
        f"• /ping - Probar si el bot responde\n\n"
        f"🆔 Tu ID: <code>{user.id}</code>"
    )
    
    update.message.reply_text(welcome_message, parse_mode=ParseMode.HTML)

def comandos(update: Update, context: CallbackContext):
    """Comando /comandos - Lista todos los comandos disponibles"""
    commands_text = (
        "📋 <b>Comandos disponibles:</b>\n\n"
        "🔹 <b>Comandos básicos:</b>\n"
        "• /start - Mensaje de bienvenida\n"
        "• /comandos - Ver esta lista\n"
        "• /me - Información del usuario\n"
        "• /ping - Probar si el bot responde\n\n"
        "🔹 <b>Comandos de prueba:</b>\n"
        "• /echo [texto] - Repetir tu mensaje\n"
        "• /info - Información del bot\n\n"
        "🚀 <b>¡Más comandos próximamente!</b>"
    )
    
    update.message.reply_text(commands_text, parse_mode=ParseMode.HTML)

def me(update: Update, context: CallbackContext):
    """Comando /me - Información del usuario"""
    user = update.effective_user
    
    user_info = (
        f"👤 <b>Información del usuario:</b>\n\n"
        f"🆔 <b>ID:</b> <code>{user.id}</code>\n"
        f"👤 <b>Nombre:</b> {user.first_name}\n"
        f"📝 <b>Username:</b> @{user.username or 'Sin username'}\n"
        f"📅 <b>Idioma:</b> {user.language_code or 'No especificado'}\n"
        f"🆕 <b>Es bot:</b> {'Sí' if user.is_bot else 'No'}"
    )
    
    update.message.reply_text(user_info, parse_mode=ParseMode.HTML)

def ping(update: Update, context: CallbackContext):
    """Comando /ping - Probar si el bot responde"""
    update.message.reply_text("🏓 ¡Pong! El bot está funcionando correctamente.")

def echo(update: Update, context: CallbackContext):
    """Comando /echo - Repetir el mensaje del usuario"""
    if not context.args:
        update.message.reply_text("❌ Uso: /echo [texto]")
        return
    
    texto = " ".join(context.args)
    update.message.reply_text(f"📢 <b>Tu mensaje:</b> {texto}", parse_mode=ParseMode.HTML)

def info(update: Update, context: CallbackContext):
    """Comando /info - Información del bot"""
    bot_info = (
        "🤖 <b>Información del Bot:</b>\n\n"
        "📱 <b>Nombre:</b> Mi Bot Personal\n"
        "🔧 <b>Versión:</b> 1.0.0\n"
        "📅 <b>Estado:</b> ✅ Funcionando\n"
        "👨‍💻 <b>Desarrollador:</b> Tú\n\n"
        "💡 <b>Próximas funciones:</b>\n"
        "• Sistema de usuarios\n"
        "• Comandos de administración\n"
        "• Consultas de información\n"
        "• Y mucho más..."
    )
    
    update.message.reply_text(bot_info, parse_mode=ParseMode.HTML)

# ----------------- MAIN ----------------- #

def main():
    """Función principal del bot"""
    print("🤖 Iniciando bot simple...")
    
    # Crear updater
    updater = Updater(TOKEN_BOT, use_context=True)
    dispatcher = updater.dispatcher
    
    # Agregar handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("comandos", comandos))
    dispatcher.add_handler(CommandHandler("me", me))
    dispatcher.add_handler(CommandHandler("ping", ping))
    dispatcher.add_handler(CommandHandler("echo", echo))
    dispatcher.add_handler(CommandHandler("info", info))
    
    print("✅ Bot configurado correctamente")
    print("📱 Ve a tu bot en Telegram y envía /start")
    print("🔄 El bot está escuchando mensajes...")
    print("⏹️  Presiona Ctrl+C para detener")
    
    # Ejecutar bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main() 