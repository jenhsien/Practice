# coding=utf-8

#字串	(string)	：不可變
#串列	(list)		：可變
#序對	(tuple)		：不可變
#字典	(dictionary)：可變
#集合	(set)

#直接建立串列(list)
list_car=['bmw','lexus','nissan','benz']
#用split()分割將string切割成list
device='iphone/ipad/macbook/apple watch/ipod'
list_device=device.split('/')

#用[]取得list的項目
print(list_car[0],list_car[1])

#list的list
list_shopping=[list_car,list_device,'house']
print(list_shopping)
#取得list_shopping的第2項(list_device)
a=list_shopping[1]
print(a)
#取得list_shopping的第2項裡面的第3項(list_device裡的macbook)
#方法：指令兩個索引值
b=list_shopping[1][2]
print(b)

c=[1,2,3,4,5,6,7]
print(c)
c[2]=9			#更改項目
print(c)		
print(c[:3])	#以slice取出項目(由開始到第3-1項)
d=[8,9]
c.append(d)		#以append加入，會以串列形式而非項目
print(c)

del c[-1]		#以del刪除項目
print(c)
c.extend(d)		#以extend加入，會以項目形式
print(c)

c.insert(2,3)	#以insert在位移2的地方加入3
print(c)

c.remove(9)		#以remove移除第一個出現的9
print(c)		



