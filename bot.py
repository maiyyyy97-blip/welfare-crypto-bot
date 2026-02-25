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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

async def start(update, context):
    text = (
        "👋 *Welcome to Cryptocurrency Wallet*\n\n"
        "A secure and manually verified digital asset service.\n\n"
        "🔐 *Key Principles*\n"
        "• Manual verification only\n"
        "• Transparent processing\n"
        "• Security-first approach\n\n"
        "Please choose an option below to continue."
    )

    keyboard = [
        [InlineKeyboardButton("💳 Deposit USDT", callback_data="menu_deposit")],
        [InlineKeyboardButton("💱 Buy USDT", callback_data="menu_buy")],
        [InlineKeyboardButton("💸 Withdraw", callback_data="menu_withdraw")],
        [InlineKeyboardButton("🆘 Support", callback_data="menu_support")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    )

async def buy_usdt(update, context):
    text = (
        "💱 *Buy USDT*\n\n"
        "Send payment to the UPI ID below:\n\n"
        f"`{UPI_ID}`\n\n"
        "📌 *Process*\n"
        "• Payment is verified manually\n"
        "• USDT credited after confirmation\n\n"
        "After payment, notify us."
    )

    keyboard = [
        [InlineKeyboardButton("📋 Copy UPI ID", callback_data="copy_upi")],
        [InlineKeyboardButton("✅ I’ve Paid", callback_data="sent_payment")],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_menu")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
async def deposit(update, context):
    text = (
        "💳 *USDT Deposit*\n\n"
        "Send USDT using the *BEP20 (BSC)* network to the address below:\n\n"
        f"`{USDT_ADDRESS}`\n\n"
        "📌 *Notes*\n"
        "• Network: BEP20 only\n"
        "• Deposits are verified manually\n\n"
        "After sending, confirm below."
    )

    keyboard = [
        [InlineKeyboardButton("📋 Copy Address", callback_data="copy_usdt")],
        [InlineKeyboardButton("✅ I’ve Sent Payment", callback_data="sent_payment")],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_menu")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )

    )

async def withdraw(update, context):
    text = (
        "💸 *Withdraw Request*\n\n"
        "To request a withdrawal, please send:\n\n"
        "• Amount\n"
        "• Receiving address\n\n"
        "📌 Withdrawals are processed *manually* after verification."
    )

    keyboard = [
        [InlineKeyboardButton("🆘 Contact Support", callback_data="menu_support")],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_menu")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )

from telegram.ext import CallbackQueryHandler

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "copy_usdt":
        await query.message.reply_text(
            f"📋 *USDT Address*\n\n`{USDT_ADDRESS}`",
            parse_mode=ParseMode.MARKDOWN
        )

    elif query.data == "copy_upi":
        await query.message.reply_text(
            f"📋 *UPI ID*\n\n`{UPI_ID}`",
            parse_mode=ParseMode.MARKDOWN
        )

    elif query.data == "sent_payment":
        await query.message.reply_text(
            "✅ *Payment Noted*\n\n"
            "Please send transaction hash or screenshot to support.\n"
            "Your request will be verified shortly.",
            parse_mode=ParseMode.MARKDOWN
        )

    elif query.data == "menu_support":
        await query.message.reply_text(
            "🆘 *Support*\n\n"
            "Please contact the admin for assistance.",
            parse_mode=ParseMode.MARKDOWN
        )

    elif query.data == "back_menu":
        await start(query.message, context)

    keyboard = [
        [InlineKeyboardButton("🆘 Contact Support", callback_data="menu_support")],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_menu")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy_usdt", buy_usdt))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("support", support))

app.run_polling()
