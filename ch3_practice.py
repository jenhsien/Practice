# coding=utf-8

#3.1 出生年到第五個生日（五歲？）
year_list = [1986,1987,1988,1989,1990,1991]
#3.2 第三個生日
print(year_list [3])
#3.3 最老的一年
year_list.sort(reverse = True)
print(year_list [0])	#其實直接 print(year_list[-1]就好)

#------------------------------------------------

#3.4 
things = ['mozzarella','cinderella','salmonella']
#3.5 人名首字改大寫
things[1].capitalize()	#但不會改list的項目，只是操作？
things[1] = things[1].capitalize()	#所以必須重新指派
print(things)
#3.6 起司全大寫
things[0] = things[0].upper()
print(things)
#3.7 去除不良
things.pop()	#在最後面，可用pop()，或其他很多方法。
print(things)

#------------------------------------------------

#3.8 
surprice = ['Groucho','Chico','Harpo']
#3.9 最後一個改小寫後反過來，再改首字大寫
surprice[-1] = surprice[-1].lower()			#改小寫
surprice[-1] = surprice[-1][-1::-1]			#反向排序
surprice[-1] = surprice[-1].capitalize()	#首字大寫
print(surprice[-1])

#------------------------------------------------

#3.10
E2F = {'dog':'chien','cat':'chat','walrus':'morse'}
print(E2F)
#3.11 印出walrus的法文單字
print(E2F['walrus'])
#3.12 製作法英字典F2E
F2E = {}
for English, French in E2F.items():
    F2E[French] = English
print(F2E)
#3.13
print(F2E['chien'])
#3.14
print(E2F.keys())

#------------------------------------------------

#3.15
life = {
    'animals':{
        'cats':['Henri','Grumpi','Lucy'],
        'octopi':{},
        'emus':{}},
    'plants':{},
    'other':{}
}
#3.16
print(life.keys())
#3.17
print(life['animals'].keys())
#3.18 
print(life['animals']['cats'])


