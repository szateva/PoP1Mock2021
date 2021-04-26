# 13021326

def day_of_year(d, m):
    if d < 0 or d > 31 or m < 0 or m > 12:
        return -1
    else:
        days_of_2020 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        days_since_yr_start = {1:0, 2:31, 3:60, 4:91, 5:121, 6:152, 7:182, 8:213, 9:244, 10:274, 11:305, 12:335}

        if days_of_2020[m] < d:
            return -1
        else:
            return days_since_yr_start[m] + d - 1

print(day_of_year(3,1))
assert day_of_year(3,1)==2 #must be True
assert day_of_year(10,5)==130 #must be True
assert day_of_year(31,6)==-1 #must be True