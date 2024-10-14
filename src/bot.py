import os
import logging
from src.logs import setup_logging

class Bot:
  def __init__(self, bot_name, root_folder):
    user_folder = os.path.expanduser("~")
    self.bot_name = bot_name
    self.root_folder = os.path.join(user_folder, root_folder)
    self.bot_folder = os.path.join(self.root_folder, bot_name)
    self.log_folder = os.path.join(self.bot_folder, "logs")
    
    # Cria os diretórios necessários para a operação do bot.
    os.makedirs(self.bot_folder, exist_ok=True)
    os.makedirs(self.log_folder, exist_ok=True)

    # Configura o sistema de logs
    setup_logging(self.log_folder)
    self.logger = logging.getLogger(self.bot_name)

  def log(self, message):
    """
    Registra uma mensagem no log.

    :param message: A mensagem a ser registrada.
    """
    self.logger.info(message)

  def error(self, message):
    """
    Registra uma mensagem de erro no log.

    :param message: A mensagem de erro a ser registrada.
    """
    self.logger.error(message)