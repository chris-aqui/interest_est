principle = float(input('deposit: '))
rate = float(input('bank rate: '))
constNum = float(100)
constMonth = float(12)

rate = rate/constNum
rate = rate/constMonth
converted_rate = (rate)
# print('You deposited ', principle, ' with a rate of ', converted_rate)

months = input('# of months: ')

for x in range(int(months)):
  principle = (principle * converted_rate) + principle
  print(x ,' new value ',principle, ' with added interest of ', principle * converted_rate)
  principle = principle + 500


print(principle)