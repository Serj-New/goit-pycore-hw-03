from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        today = datetime.today().date()
        
        delta = today - given_date
        
        return delta.days
    
    except ValueError:
        print("Невірний формат дати. Використовуйте 'YYYY-MM-DD'")
        return None

# Перевірка:  
print(get_days_from_today("1991-11-30"))