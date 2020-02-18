import calendar


yy = int(input("enter year"))
mm = int(input("enter month"))


print(calendar.month(yy, mm))

print(calendar.calendar(yy))

print(calendar.isleap(yy))

print(calendar.leapdays(yy, 2030))
