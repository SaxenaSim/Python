def weeklyAttendance(**weekdays):
    totalAttendance=0
    for attendees in weekdays.values():
        totalAttendance+=attendees
    return totalAttendance

print(weeklyAttendance(monday = 265, tuesday = 698, wednesday = 365, thursday = 463, friday = 234))
print(weeklyAttendance(monday = 265, friday = 234))
print(weeklyAttendance(wednesday = 365, thursday = 463, friday = 234))