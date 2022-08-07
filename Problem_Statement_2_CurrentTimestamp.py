def currentTimeStamp:
	day = utc_now(“dd”)
	month = utc_now(“MM”)
	year = utc_now(“yyyy”)
	hh=utc_now(“hh”)
	mm=utc_now(“mm”)
	ss=utc_now(“ss”)
	currentTimeStamp = year + month + day + hh + mm + ss
	return currentTimeStamp

if __name__ == "__main__":
    currentTimeStamp()