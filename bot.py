from telegram.ext import ApplicationBuilder, CommandHandler
import random

TOKEN = "7934330924:AAF6xHyuus2I5lJcjKgUFK7mlISUoxXIQJg
"

# Cria o bot
app = ApplicationBuilder().token(TOKEN).build()

# Função para enviar sinais simulados
async def enviar_sinal(update, context):
    sinais = [
        "🔥 COMPRA FORTE no EUR/USD às 15h32",
        "🚀 VENDA FORTE no GBP/USD às 15h37",
        "⏳ Aguardando melhor entrada..."
    ]
    sinal_aleatorio = random.choice(sinais)
    await update.message.reply_text(f"[PJOTTA TRADE] {sinal_aleatorio}")

# Adiciona o comando /start
app.add_handler(CommandHandler("start", enviar_sinal))

# Roda o bot
app.run_polling()
