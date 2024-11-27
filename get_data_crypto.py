import pandas as pd
import ccxt


timeframe='1d'
# Список криптовалют
crypto_symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'XRP/USDT']
# Настройка ccxt для загрузки данных о котировках криптовалют
exchange = ccxt.binance()


# Функция для загрузки данных о котировках криптовалют
def download_crypto_data(symbols, timeframe, since=None):
    all_data = {}
    for symbol in symbols:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since)
        data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        all_data[symbol] = data
    return all_data

# Загрузка данных о котировках криптовалют
crypto_data = download_crypto_data(crypto_symbols, timeframe)

# Сохранение данных о котировках криптовалют в файлы CSV
for symbol, data in crypto_data.items():
    data.to_csv(f'data/crypto/{symbol.replace("/", "_")}_data.csv', index=False)

print("Данные успешно загружены и сохранены в файлы CSV.")