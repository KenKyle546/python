grade_percent = float(input('What is you grade percentage? '))

if grade_percent >= 90:
    letter = 'A'
elif grade_percent >= 80:
    letter = 'B'
elif grade_percent >= 70:
    letter = 'C'
elif grade_percent >= 60:
    letter = 'D'
else:
    letter = 'F'

last_digit = grade_percent% 10
if last_digit >=7:
    sign = '+'
elif last_digit <3:
    sign = '-'
else:
    sign = ''
if 93 <= grade_percent or grade_percent < 60:
    sign = ''
print(f'Your letter grade is {letter}{sign}. ')
if grade_percent >= 70:
    print('Nice job! You passed the class!! ')
else:
    print('See you again next year. :( ')
