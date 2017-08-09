# coding=utf-8
# \t 為對齊

print('\tabc')
print('a\tbc')
print('ab\tc')

# 用 [] 來擷取字串字元
x='abcdefg'
print(x[0])		#擷取第1字元
print(x[1])		#擷取第2字元
print(x[2])		#擷取第3字元
print(x[3])		#擷取第4字元
print(x[:])		#擷取全部字元
print(x[2:6:3])	#從2到5，間隔3字元

# print 執行時，陳述式的每個引數中間會有空格，且會有()
print(x[0],x[1],x[2])
# print 執行時，用 + 會連續，中間無空格
print(x[0]+x[1]+x[2])

#用 len() 取得長度
print(len(x))

#呼叫 join() 來連接串列合為一字串
y_list=['a','b','c']
y_string=' and '.join(y_list)
print(y_string)

