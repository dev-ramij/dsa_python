def getMonthlyReturn(monthly_investment, extra_hike, return_rate, tenure):
    
    monthly_pay = monthly_investment
    extra_pay = 0
    yearly_investment = 0
    for i in range(tenure):
        if i != 0:
            extra_pay = (monthly_pay * extra_hike) // 100
        monthly_pay += extra_pay
        
        yearly_investment += monthly_pay * 12
        yearly_investment += ((yearly_investment * return_rate) // 100)
        print(monthly_pay,yearly_investment)
    return yearly_investment


print(getMonthlyReturn(7000, 10, 15, 30))
