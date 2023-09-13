import calculations.investment

capital = int(input('Podaj kapital poczatkowy: '))
percent = float(input('Podaj oprocentowanie lokaty: '))
time = int(input('Podaj okres na jaki chcesz wplacic pieniadze: '))
print(f'Po {time} latach na twojej lokacie bedzie {calculations.investment.investment_value(capital, percent, time):.2f} zł')