from datetime import datetime
import locale

def date_range_to_string(date_range):
    weekdays = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    date_strings = [datetime.strptime(date, '%Y-%m-%d') for date in date_range]
    start_date = date_strings[0].strftime('%d')
    end_date = date_strings[-1].strftime('%d')
    locale.setlocale(locale.LC_TIME, "id_ID.utf8")
    start_month = date_strings[0].strftime('%B')
    end_month = date_strings[-1].strftime('%B')
    start_year = date_strings[0].strftime('%Y')
    end_year = date_strings[-1].strftime('%Y')
    start_weekday = weekdays[date_strings[0].weekday()]
    end_weekday = weekdays[date_strings[-1].weekday()]
    print(start_year, end_year)
    if (start_year != end_year) and (start_month != end_month):
        return f"{start_weekday} - {end_weekday}, {start_date} {start_month} {start_year} - {end_date} {end_month} {end_year}"
    elif (start_year == end_year) and (start_month != end_month):
        return f"{start_weekday} - {end_weekday}, {start_date} {start_month} - {end_date} {end_month} {start_year}"
    else:
        return f"{start_weekday} - {end_weekday}, {start_date} - {end_date} {start_month} {start_year}"

date_range = ['2023-12-31', '2024-01-01']
print(date_range_to_string(date_range))

date_range = ['2023-11-30', '2023-12-01']
print(date_range_to_string(date_range))

date_range = ['2023-12-01', '2023-12-02']
print(date_range_to_string(date_range))