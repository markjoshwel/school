cuml_s = int(input("Please enter the time to be converted, in sec: "))
time_h = cuml_s // 3600  # get hours
_time_m = cuml_s // 60  # get cumulative minutes
time_s = cuml_s - (_time_m * 60)  # get last seconds since last hour
time_m = _time_m - (time_h * 60)  # get lapsed minutes since last hour
print(f"Time: {time_h} hr, {time_m} min, {time_s} sec")
