import pandas as pd
import numpy as np
import os

def randomization(data: pd.DataFrame,num_to_extract, length_of_stack) -> pd.DataFrame:
    recent_values = []  # dt.number

 
    # 要提取的数字数量=160
    num_to_extract = num_to_extract

    # 提取数字
    extracted_values = pd.DataFrame(columns= data.columns) 

    while len(extracted_values) < num_to_extract:
        # 随机提取一个value
        value = data.sample()

        if int(value.number) not in recent_values:
            extracted_values = pd.concat([extracted_values,value])
            recent_values.append(int(value.number))
            data = data.drop(index = value.index)

            # 如果最近提取的数字集合中已经有了 5 个数字，则将最早加入的数字移除，类似于栈结构
            if len(recent_values) > length_of_stack:
                
                recent_values = recent_values[1:]
    print(recent_values)
    print(extracted_values)
    return extracted_values


def generate_xlsx(data: pd.DataFrame, name: str):
    data.to_excel(name, index= False)



if __name__ == '__main__':
    dt = pd.read_excel('whole_table.xlsx')
    
    for child in os.listdir('sessions'):
        for num in range(50):
            data1 = randomization(dt, 160, 5)
            locate = 'sessions/'+ child +'/order_'+ str(num+1) + '.xlsx'
            generate_xlsx(data1, locate)
    print('Generation OK')
