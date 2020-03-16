# Created by Kaleb Griepp, 790-804557
import school

print('')
print('Midterm Scores:')
midterm = []
midterm.append(int(input('Enter 1st midterm score:')))
midterm.append(int(input('Enter 2nd midterm score:')))
midterm.append(int(input('Enter 3rd midterm score:')))
midterm.append(int(input('Enter 4th midterm score:')))
midterm.append(int(input('Enter 5th midterm score:')))
print(midterm)

print('')
print('FINAL SCORES:')
finalscore = []
finalscore.append(int(input('Enter 1st final score:')))
finalscore.append(int(input('Enter 2nd final score:')))
finalscore.append(int(input('Enter 3rd final score:')))
finalscore.append(int(input('Enter 4th final score:')))
finalscore.append(int(input('Enter 5th final score:')))
print(finalscore)

print('')
print(len(midterm), 'students took the midterm.')
print('Midterm scores ranged from', min(midterm), 'to', max(midterm))
print('Average midterm: %0.1f' % ((sum(midterm))/len(midterm)))

print('')
print(len(finalscore), 'students took the final.')
print('Final scores ranged from', min(finalscore), 'to', max(finalscore))
print('Average final: %0.1f' % ((sum(finalscore))/len(finalscore)))
