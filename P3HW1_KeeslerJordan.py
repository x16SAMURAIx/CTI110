# CTI 110
# P3HW1-Debugging
# Jordan Keesler
# 8 MAY 2022

def main():
  # This program gets a numeric test score from the user and displays the corresponding letter grade.
  # 10-point grading scale defined by corresponding grades
  A_SCORE = 90
  B_SCORE = 80
  C_SCORE = 70
  D_SCORE = 60

  #User input for grade
  score = float(input('Enter your test score: '))

  #If statements that will output corresponding letter grade according to 10-Point grading scale
  if score >= A_SCORE:
    print ('Your grade is A.')
  elif score >= B_SCORE:
    print('Your grade is B.')
  elif score >= C_SCORE:
    print('Your grade is C.')
  elif score >= D_SCORE:
    print('Your grade is D.')
  else:
    print('Your grade is F.')

#program start
main() 
