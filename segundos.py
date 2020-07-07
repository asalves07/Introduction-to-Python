segT = int(input())
dias = segT // 86400
segT = segT % 86400
horas = segT // 3600
segT = segT % 3600
minutos = segT // 60
segT = segT % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segT, "segundos.")
