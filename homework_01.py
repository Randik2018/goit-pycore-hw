from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    
    current_date = datetime.today()
    
    delta = current_date - input_date
    
    return delta.days


print(get_days_from_today("2021-10-09"))