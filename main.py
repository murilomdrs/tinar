import traceback
from src.bot import Bot
from src.logs import setup_logging

def main():
  try:
    # Diretórios do projeto
    bot_name = "Tinar"
    bot_folder = "Robôs"
    bot = Bot(bot_name, bot_folder)

    # Início do programa
    bot.log("Início - Main")

  except Exception as e:
    bot.error(f"Ocorreu um erro: {e}\n{traceback.format_exc()}")

if __name__ == "__main__":
  main()