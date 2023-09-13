import speed_function

distance = float(input('Jaki dystans pokonałeś? '))
time = float(input('W jakim czasie pokonałeś dany dystans? '))
print(f'Poruszałeś się ze średnią prędkością {speed_function.average_speed(distance,time)}')
