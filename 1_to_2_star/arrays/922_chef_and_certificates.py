total_students, min_lect_minutes, no_lectures = map(int, input().split())

ans = 0
for _ in range(total_students):
    stud_details = list(map(int, input().split()))
    time_arr = stud_details[:-1]
    question_asked = stud_details[-1]
    
    if question_asked <= 10 and sum(time_arr) >= min_lect_minutes:
        ans += 1

print(ans)
