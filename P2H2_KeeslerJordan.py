# CTI-110
# P2HW2 - Score Avg
# Your Name 
# Date
#

score1 = float(input("Enter score #1: "))
score2 = float(input("Enter score #2: "))
score3 = float(input("Enter score #3: "))
score4 = float(input("Enter score #4: "))
score5 = float(input("Enter score #5: "))
score6 = float(input("Enter score #6: "))
score7 = float(input("Enter score #7: "))
scores = [score1, score2, score3, score4, score5, score6, score7]
lowest_score = min(scores)
scores.remove(lowest_score)
scores_avg = sum(scores) / len(scores)
scores_ans = "{:.2f}".format(scores_avg)
 

print("-------------Results-------------")

print("Lowest score : ",lowest_score )

print("Modified List : ",scores )

print("Scores Average: ", scores_ans)

print("---------------------------------")
