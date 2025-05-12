import asyncio
from telegram import Bot
import datetime
import os

async def enviar_mensaje(bot, chat_id):
    ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensaje = f"🔔 Mensaje recurrente enviado a las {ahora}"
    await bot.send_message(chat_id=chat_id, text=mensaje)
    print(f"[{ahora}] Mensaje enviado correctamente.")

async def main(token, chat_id, intervalo):
    bot = Bot(token=token)
    print(f"Bot iniciado → Token: {token[:10]}..., Chat ID: {chat_id}, Intervalo: {intervalo}s")

    while True:
        await enviar_mensaje(bot, chat_id)
        await asyncio.sleep(intervalo)

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = int(os.getenv("TELEGRAM_CHAT_ID"))
    intervalo = float(os.getenv("INTERVALO", 60))  # <- Usa la variable de entorno INTERVALO, default 60

    if not token or not chat_id:
        print("❌ Faltan TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en las variables de entorno")
        exit(1)

    asyncio.run(main(token, chat_id, intervalo))

