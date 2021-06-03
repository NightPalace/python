# 3-4
guests=['大空翼','四驱兄弟','悟空','黑猫警长']
print('我想邀请' + guests[0] + ', ' + guests[1] + ', ' + guests[2] + ', ' + guests[3] + '一起共进晚餐')
can_not_come_guest = '四驱兄弟'
guests.remove(can_not_come_guest)
print('但是' + can_not_come_guest + '无法前来了')
new_guest='钢之炼金术师'
guests.append(new_guest)
print('我又邀请了' + new_guest)
print('最终，受邀前来的客人如下：' + guests[0] + ', ' + guests[1] + ', ' + guests[2] + ', ' + guests[3])
print('找到了一个更大的餐桌，我可以多邀请三个宾客了')
guests.insert(0, '莱纳')
guests.insert(2, '马纳')
guests.append('圣诞老人')
print('新的受邀名单如下：' + guests[0] + ', ' + guests[1] + ', ' + guests[2] + ', ' + guests[3] + ', ' + guests[4] + ', ' + guests[5] + ', ' + guests[6])
print('真是一波三折，餐具不够了，我只能邀请两名客人了')
guest_1 = guests.pop(0)
print('很遗憾' + guest_1+ '，我无法邀请您来共进晚餐了')
guest_1 = guests.pop(0)
print('很遗憾' + guest_1+ '，我无法邀请您来共进晚餐了')
guest_1 = guests.pop(0)
print('很遗憾' + guest_1+ '，我无法邀请您来共进晚餐了')
guest_1 = guests.pop(0)
print('很遗憾' + guest_1+ '，我无法邀请您来共进晚餐了')
guest_1 = guests.pop(0)
print('很遗憾' + guest_1+ '，我无法邀请您来共进晚餐了')
print('您好' + guests[0]+ '，欢迎您来共进晚餐')
del guests[0]
print('您好' + guests[0]+ '，欢迎您来共进晚餐')
del guests[0]
print('最终名单：', guests)