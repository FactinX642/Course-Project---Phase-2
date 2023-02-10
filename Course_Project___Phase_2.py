#   Student Name
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate):")
    return empname


def GetDatesWorked():
    fromdate = input("Enter from date (mm/dd/yyyy):")
    todate = input("Enter to date (mm/dd/yyyy):")
    return fromdate, todate


def GetHoursWorked():
    hours = float(input("Enter amount of hours worked:"))
    return hours


def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate:"))
    return hourlyrate


def GetTaxRate():
    taxrate = float(input("Enter tax rate:"))
    return taxrate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * (taxrate / 100)
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


def printinfo(EmpDetailList, EmpTotals):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(
            fromdate,
            todate,
            empname,
            f"{hours:,.2f}",
            f"{hourlyrate:,.2f}",
            f"{grosspay:,.2f}",
            f"{taxrate/100:,.1%}",
            f"{incometax:,.2f}",
            f"{netpay:,.2f}",
        )

        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay


def PrintTotals(EmpTotals):
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Number Of Hours: {EmpTotals["TotHours"]}')
    print(f'Total Number Of GrossPay: {EmpTotals["TotGrossPay"]}')
    print(f'Total Number Of Taxes: {EmpTotals["TotTax"]}')
    print(f'Total Number Of NetPay: {EmpTotals["TotNetPay"]}')


if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}

    while True:
        empname = GetEmpName()
        if empname.upper() == "END":
            break

        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()

        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)

    printinfo(EmpDetailList, EmpTotals)
    PrintTotals(EmpTotals)

