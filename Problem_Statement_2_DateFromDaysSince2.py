
def DateFromDaysSince2(date):
	addDays = addDays(toDate(date), -11)
	addDaysDate= toDate(addDays)
	return addDaysDate

if __name__ == "__main__":
    DateFromDaysSince2()