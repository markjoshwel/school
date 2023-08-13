# CalculateCommision
#   Mark Joshwel, SXXXXXXXX
# =========================
# Calculates monthly comission paid based on entered monthly sales

sales_monthly = int(input("Enter monthly sales of sales agent: "))
commission_rate = 0.10 if (sales_monthly >= 10000) else 0.05
commission_paid = sales_monthly * commission_rate

print(
    f"The commission rate is : {commission_rate * 100}%\n"
    f"The commission paid is : ${commission_paid:.2f}"
)
