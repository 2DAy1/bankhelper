# Основні налаштування
BANK_NAME = "My Bank"

# Налаштування для Telegram бота
TOKEN = '7848327268:AAGVF6rox_Cyxh95G5hMpEDsTFKoG1pq9RY'

# Налаштування бази даних
DB_USER = 'postgres'
DB_PASSWORD = 'davdad2002'
DB_NAME = 'bank_system'
DB_HOST = 'localhost'
DB_PORT = '5432'

# URL підключення до бази даних
DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
