import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir):
  """
  Configura o sistema de logs, permitindo a definição dinâmica do diretório de logs.
    
  :param log_dir: Caminho para o diretório onde os logs serão armazenados.
  """
  # Configuração de sistema de logs
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)

  # Formatação dos logs
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  # Configuração de logs em arquivo
  log_file = os.path.join(log_dir, "log.log")
  file_handler = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=5)
  file_handler.setFormatter(formatter)

  # Configuração de logs em console
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)

  # Adiciona os handlers ao logger
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)