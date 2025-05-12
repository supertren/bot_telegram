import asyncio
from telegram import Bot
import datetime
import argparse
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
    parser = argparse.ArgumentParser(description="Bot recurrente en Railway")
    parser.add_argument('--intervalo', type=float, default=float(os.getenv("INTERVALO", 60)), help='Intervalo en segundos')
    args = parser.parse_args()

    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = int(os.getenv("TELEGRAM_CHAT_ID"))

    if not token or not chat_id:
        print("❌ Faltan las variables de entorno TELEGRAM_TOKEN y TELEGRAM_CHAT_ID")
        exit(1)

    asyncio.run(main(token, chat_id, args.intervalo))
