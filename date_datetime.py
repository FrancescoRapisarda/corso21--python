#domenica 29.10.23
#   - importare modulo datetime
#   - creare un oggetto data con now() e data predefinita
#   - il metodo strftime per formattare la data
#   - parametri formattazione data

    #  %a   Wednesday, short version                                            | Wed
    #  %A   Wednesday, full version                                             | Wednesday
    #  %w   Wednesday as a number 0-6, 0 is Sunday                              | 3
    #  %d   Day of month 01-31                                                  | 31
    #  %b   Month name, short version                                           | Dec
    #  %B   Month name, full version                                            | December
    #  %m   Month as a number 01-12                                             | 12
    #  %y   Year, short version, without century                                | 18
    #  %Y   Year, full version                                                  | 2018
    #  %H   Hour 00-23                                                          | 17
    #  %I   Hour 00-12                                                          | 05
    #  %p   AM/PM                                                               | PM
    #  %M   Minute 00-59                                                        | 41
    #  %S   Second 00-59                                                        | 08
    #  %f   Microsecond 000000-999999                                           | 548513
    #  %z   UTC offset                                                          | +0100
    #  %Z   Timezone                                                            | CST
    #  %j   Day number of year 001-366                                          | 365
    #  %U   Week number of year, Sunday as the first day of week, 00-53         | 52
    #  %W   Week number of year, Monday as the first day of week, 00-53         | 52
    #  %c   Local version of date and time                                      | Mon Dec 31 17:41:00 2018
    #  %x   Local version of date                                               | 12/31/18
    #  %X   Local version of time                                               | 17:41:00
    #  %G   ISO 8601 year                                                       | 2018
    #  %u   ISO 8601 weekday (1-7)                                              | 1
    #  %V   ISO 8601 weeknumber (01-53)                                         | 01
    
#   - esempi formattazione data

import datetime

x = datetime.datetime.now()
print(x)

y = datetime.datetime(2023,10,29)
print(y)
    
    
#String format time:

z = datetime.datetime.now()
print(z.strftime("%B"))
print(z.strftime("%b"))
print(z.strftime("%a"))
print(z.strftime("%A"))
print(z.strftime("%A %d/%m/%Y"))