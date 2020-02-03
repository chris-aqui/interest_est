principle = input('deposit: ')
rate = input('bank rate: ')
converted_rate = (float(rate)/100)/12
print('You deposited ', principle, ' with a rate of ', converted_rate)
months = input('# of months: ')
cal_num = float(principle)

for x in range(int(months)):
  # print(x)
  cal_num = (cal_num * converted_rate) + cal_num
  # print('new value ',cal_num, ' with added interest of ', cal_num * converted_rate)
  cal_num = cal_num + 500
  # print('monthly saving ', cal_num)
  # print('')
  # print('')
  # print('')
  # print('')
  # print('//////////////////////////////////////////////////////')


print(cal_num)