import telegram
from telegram.ext import Updater, CommandHandler
import logging
import random

# Seu token do BotFather aqui
TOKEN = "7934330924:AAF6xHyuus2I5lJcjKgUFK7mlISUoxXIQJg"

# Configuração de logging (opcional)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Inicializa o Bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Função para enviar sinais simulados
def enviar_sinal(update, context):
    sinais = [
        "🔥 COMPRA FORTE no EUR/USD às 15h32",
        "🚀 VENDA FORTE no GBP/USD às 15h37",
        "⏳ Aguardando melhor entrada..."
    ]
    sinal_aleatorio = random.choice(sinais)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"[PJOTTA TRADE] {sinal_aleatorio}")

# Comando para iniciar
start_handler = CommandHandler('start', enviar_sinal)
dispatcher.add_handler(start_handler)

# Inicia o bot
updater.start_polling()
