# Mark Joshwel (SXXXXXXXX) - IM02

times = input("Enter time taken of 2 laps separated by semi-colon (seconds):")

times_list = times.split(";")

firstlap_time = int(times_list[0])
secondlap_time = int(times_list[1])

if firstlap_time > secondlap_time:
    best = secondlap_time
else:
    best = firstlap_time

total = firstlap_time + secondlap_time

print(
    "Tom's best time is {:.1f} s and average time is {total} s".format(
        best, total=(total / len(times_list))
    )
)
