from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

tasks = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi,Welcome")

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please add your task,eg:    /add   study lesson ")
        return
    tasks.append(" ".join(context.args))
    await update.message.reply_text("Your task has been added")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not tasks:
        await update.message.reply_text("No task registered")
        return
    text = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
    await update.message.reply_text(text)

# -------------------------
# DELETE FUNCTION (اضافه شد)
# -------------------------
async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please enter the task number to delete. Example: /delete 2")
        return

    try:
        index = int(context.args[0]) - 1
    except:
        await update.message.reply_text("Only numbers are allowed.")
        return

    if index < 0 or index >= len(tasks):
        await update.message.reply_text("This task number does not exist.")
        return

    removed = tasks.pop(index)
    await update.message.reply_text(f"Task '{removed}' has been deleted.")

def main():
    app = ApplicationBuilder().token("8498758893:AAGBLW_HX63BJ1xLSVVZPGT-9jXOj2VmtTE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add_task))
    app.add_handler(CommandHandler("list", list_tasks))

    
    app.add_handler(CommandHandler("delete", delete_task))

    app.run_polling()

if __name__ == "__main__":
    main()
