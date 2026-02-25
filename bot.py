import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ================== EDIT ONLY THESE 4 LINES ==================
TOKEN = "8718249602:AAEiYQXajo47qOBnBshcSKydHM6m4Flbt5U"
ADMIN_ID = 923890824
UPI_ID = "8790656604@ybl"
USDT_ADDRESS = "0x14a1de9f7e1b729050ea54f3a5b9714696b73bfa"
# ============================================================

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Welfare Crypto Service\n\n"
        "We provide manual USDT buy & transfer assistance.\n\n"
        "📌 No auto balance\n"
        "📌 Manual processing only\n"
        "📌 TXID shared after transfer\n\n"
        "Commands:\n"
        "/buy_usdt – Buy USDT\n"
        "/deposit – Get deposit address\n"
        "/withdraw – Withdraw request\n"
        "/support – Contact support"
    )

async def buy_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💱 BUY USDT (Manual)\n\n"
        f"Send payment to UPI:\n"
        f"{UPI_ID}\n\n"
        f"After payment, send:\n"
        f"• Screenshot\n"
        f"• Your USDT wallet address\n\n"
        f"⏳ Processing: 5–30 minutes"
    )

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📥 USDT Deposit Address\n\n"
        f"Network: BEP20\n"
        f"Address:\n"
        f"{USDT_ADDRESS}\n\n"
        f"⚠️ Send only USDT on BEP20 network"
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📤 Withdraw Request\n\n"
        "Please send:\n"
        "1️⃣ Amount\n"
        "2️⃣ Network\n"
        "3️⃣ Wallet Address\n\n"
        "Admin will process manually and share TXID."
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Support\n\n"
        "Please contact admin for assistance."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy_usdt", buy_usdt))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("support", support))

app.run_polling()
