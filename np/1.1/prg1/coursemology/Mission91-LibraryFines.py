def lib_fines(overdue_days):
    return (0.2 * overdue_days) if (overdue_days > 7) else (0.1 * overdue_days)


# overdue_days = int(input("Enter number of days overdue:"))
# fine = lib_fine(overdue_days)
# print(f"{fine:.2f}")
