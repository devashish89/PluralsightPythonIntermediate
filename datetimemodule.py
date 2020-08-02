import datetime

#########################################################################################################
# datetime class  <- date class (year, month and day) and time class (hour, minute, second, microsecond)
# time class <- tzinfo class <- timezone class
# timedelta class
#
########################################################################################################

##### date ##########
d = datetime.date(year=2020, month=4, day=21)
print(d)
print(d.isoformat())
print(d.year, d.month, d.day)
print("Todays Datetime", datetime.datetime.today())
print("Today's Date", datetime.date.today())

print(d.weekday()) # 0 = Monday and Tuesday = 1
print(d.isoweekday()) # 1 = Monday and 2= Tuesday...

# string-format-time strftime

print(datetime.date.today().strftime("%A %d %m %B %Y"))


########### time ######################
T1 = datetime.time(hour=2, minute=30, second=15, microsecond=122209)
print(T1.hour, T1.minute, T1.second, T1.microsecond)
print(type(T1))
print(T1.strftime("%H:%M:%S"))


####### datetime #####################################

t1 = datetime.datetime(year=2020, month=4, day=21, hour=14, minute=30, second=0, microsecond=123456) #datetime
t2 = datetime.datetime.now()#datetime

print("datetime.datetime.now() == datetime.datetime.today(): ", datetime.datetime.now() == datetime.datetime.today())

print("UTC time", datetime.datetime.utcnow())


### combine date and time into datetime object ##################

date = datetime.date.today()
time = datetime.time(hour=18, minute=15, second=43)

datetimeTimestanp = datetime.datetime.combine(date, time)
print(datetimeTimestanp)

######### string - parse - time ######
x = datetime.datetime.strptime("2020-04-01 23:40:20", "%Y-%m-%d %H:%M:%S")
print(x)

print(x.strftime("%A %Y-%B-%d %H:%M:%S"))

date = datetime.date(year=x.year, month=x.month, day=x.day)
time = datetime.time(x.hour, x.minute, x.second)
print(date, time)

### timedelta ##############

t1 = datetime.datetime(year=2020, month=4, day=21, hour=21, minute=30, second=23)
t2 = datetime.datetime.today()

ts = t2  - t1
print(type(ts))

print(ts)
print(ts.total_seconds())

#########################
new_datetime = datetime.date.today() + datetime.timedelta(weeks=3)
print(new_datetime)

########## Timezone ##############

ist = datetime.timezone(datetime.timedelta(hours=5.5))

t1 = datetime.datetime(year=2020, month=4, day=21, hour=21, minute=41, tzinfo=datetime.timezone.utc)
t2 = datetime.datetime(year=2020, month=4, day=22, hour=3, minute=11, tzinfo=ist)
print(t1, t2)
diff = t2-t1
print(diff)


