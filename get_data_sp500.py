import pandas as pd
import yfinance as yf


start_date='2020-01-01'
end_date='2023-01-01'
num_tickers=2

# Загрузка списка S&P 500
sp500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()
# print(sp500_tickers)

# Функция для загрузки данных о котировках акций
def download_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return None

    # Проверяем, что данные были загружены
    if data.empty:
        print("Нет данных для указанных дат.")
        return None

    # Возвращаем нужные столбцы
    return data[['Adj Close', 'Open', 'High', 'Low', 'Close', 'Volume']]



# Загрузка и сохранение данных о котировках акций
for i, ticker in enumerate(sp500_tickers):
    if i >= num_tickers:
        break
    data = download_stock_data(ticker, start_date, end_date)
    if data is not None and not data.empty:
        data.to_csv(f'data/sp500/sp500_{ticker}.csv')
        print(f"Загружены данные для тикера {ticker}")
    else:
        print(f"Данные для тикера {ticker} не были загружены или DataFrame пустой.")
