# -*- coding: utf-8 -*-
"""
初始是4对野兔
每只野兔的成长期是3年
生育期是4年，在生育期每对兔子每年能生4只小兔
老年期是3年，老年期不能生小兔，
第10年死亡
问：
分别在10年后，20年后，100年后，各个年龄阶段的野兔是多少只？
"""
#%%
def RabbitGrowth( countOfYear ):
    
    Count_of_age_list=[0,0,0,0,0,0,0,0,0,0] 
    Count_of_age_list[-1]=8

    for i in range(countOfYear):
        count_of_year_at_4 = Count_of_age_list[-4]
        count_of_year_at_5 = Count_of_age_list[-5]
        count_of_year_at_6 = Count_of_age_list[-6]
        count_of_year_at_7 = Count_of_age_list[-7]
    
        sumGiveBirth=(count_of_year_at_4 +count_of_year_at_5+count_of_year_at_6+count_of_year_at_7)
        sumChild = int((sumGiveBirth/2)*4)
        print(Count_of_age_list[0])
        del Count_of_age_list[0]
        Count_of_age_list.append(sumChild)
        
    return Count_of_age_list

print( RabbitGrowth(20))
print( RabbitGrowth(100))



    
    
    
    
    
    













