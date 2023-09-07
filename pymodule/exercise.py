def LeapYear(year):
    isLeapYear = '평년'
    result = '잘못 입력하셨습니다!!'

    try:
        year = int(year)
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            isLeapYear = '윤년'
        result = f'{year}년은 {isLeapYear}입니다.'

    except:
        pass

    return result

def Interest(account, rate):
    nums = 1
    result = 0
    msg = '잘못 입력하셨습니다'

    try:
        account = int(account)
        rate = float(rate)
        limit = account * 2

        while True:
            result = account * (1 + rate) ** nums
            if (result >= limit): 
                msg = f'{nums}년 일 때 통장잔액은 {result:,.0f}원입니다'
                break
            nums += 1
        
    except:
        pass
        
    return msg