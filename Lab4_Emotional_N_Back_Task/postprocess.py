#-*- coding : utf-8-*-

import pandas as pd 
import numpy as np
import os 

LOCAL_DIR_FILE = 'subjects_results.csv'
def get_filename(number: int) -> str:
    try:
        for i in os.listdir("data"):
            keyword = str(number)+"_"
            if i[-3:] == 'csv' and int(i.split("_")[0]) == number:
                filename = i # Only One!
        return filename
    except Exception as e:
        print(e,'ERROR')
        return 'NAN'

def data_processing(number: int) -> pd.DataFrame:
    '''
    para:
        number of subject
    '''
    k = get_filename(number)
    if get_filename(number) == 'NAN':
        return None
    else:
        filename = "data/"+ k 

    x = ''
    with open(filename,'r+', encoding='utf-8') as file:
        x = file.read()
        x = x.replace('\n\n','').replace('，\n','，').replace('？\n','')
    file.close()

    with open(filename,'w', encoding='utf-8') as file2:
        file2.write(x)
    file2.close()

    template = pd.read_csv(filename)
        
    if len(template.columns) == 1:
        print('\\t sep required......')
        return pd.read_csv(filename,sep='\t',encoding='gbk')
    else:
        return template
  
def data_cut(df, back, emotion):
    df = df[df['emotion'] == emotion]
    df = df[df['back'] == back]
    df = df[df['corrAns'] != 'None' ]  # delete practice data or instruct items
    df = df.dropna(subset=['key_2.corr'])

    return df


class PostProcess:
    def __init__(self):
        # key_2
        # self.labels_explain = ['积极情绪-回溯1组符号对','中性情绪-回溯1组符号对','消极情绪-回溯1组符号对','积极情绪-回溯1组符号对','中性情绪-回溯2组符号对','消极情绪-回溯2组符号对','积极情绪-回溯3组符号对','消极情绪-回溯3组符号对']
        self.labels_explain = ['积极情绪-回溯1组符号对','中性情绪-回溯1组符号对','消极情绪-回溯1组符号对','积极情绪-回溯1组符号对','中性情绪-回溯2组符号对','消极情绪-回溯2组符号对']
        self.tables = []
        self.blocks = None
        self.raw_data = None
        self.number =  0
        self.subjects_results = []
        # self.names = ['subject_num','1_back_pos_corr','1_back_pos_rt','1_back_neu_corr','1_back_neu_rt','1_back_neg_corr','1_back_neg_rt','2_back_pos_corr','2_back_pos_rt','2_back_neu_corr','2_back_neu_rt','2_back_neg_corr','2_back_neg_rt','3_back_pos_corr','3_back_pos_rt','3_back_neg_corr','3_back_neg_rt', 'avg_whole_cor','avg_whole_rt']
        self.names = ['subject_num','1_back_pos_corr','1_back_pos_rt','1_back_neu_corr','1_back_neu_rt','1_back_neg_corr','1_back_neg_rt','2_back_pos_corr','2_back_pos_rt','2_back_neu_corr','2_back_neu_rt','2_back_neg_corr','2_back_neg_rt', 'avg_whole_cor','avg_whole_rt']
    
        self.dframe = pd.read_csv(LOCAL_DIR_FILE)
        self.raw = len(self.dframe)

    def fillin_table(self,number: int) -> int:
        self.raw_data = data_processing(number)
        self.number = number  # number of the subject
        self.subjects_results.append(number) # add number of subjects
        if self.raw_data is None:
            return 0
        else:
            # for itemx in ['1-back','2-back','3-back']:
            for itemx in ['1-back','2-back']:
                for itemy in ['positive','neutral','negative']:
                    if (itemx == '3-back' and itemy == 'neutral'):
                        pass
                    else:
                        self.tables.append(data_cut(self.raw_data,itemx, itemy))

    #         for item in range(len(self.labels_explain)):
    #             self.blocks = self.raw_data[self.raw_data.loc[:,'cond'] == self.labels[item]]
    #             self.blocks = self.blocks.loc[:,['lexicality', 'word', 'validity', 'standard_deviation', 'arousal', 'standard_deviation_1', 'dominance', 'standard_deviation_2', 'familiarity', 'standard_deviation_3',
    #    'specificity', 'standard_deviation_4', 'first_word_strokes', 'last_word_strokes', 'word_frequency', 'first_word_frequency', 'last_word_frequency',self.corrs[item],self.rts[item],'cond','corrAns']]
    #             self.tables.append(self.blocks)
            return 1
    
    def sub_information_gen(self) -> pd.DataFrame :
        # whole_trials = 20 * (3+3+2)
        whole_trials = 20 * (3+3)
        count = 0
        wh_rt = 0.0
        len_all = 0

        for number in range(len(self.tables)):
            block_data = self.tables[number]
            true_data = block_data[block_data['key_2.corr'] == 1]
            corr_block_rate = len(true_data)/len(block_data)  # accurancy rate of one block

            sum_block_rt = true_data['key_2.rt'].sum()
            avg_block_rt = true_data['key_2.rt'].mean() # average reaction time in a block. reminder to cut error results"

            count += len(true_data)  # count in one block
            wh_rt += sum_block_rt    # reaction time in one block
            len_all += len(true_data) # block_data
            print(len_all)

            self.subjects_results.append(corr_block_rate)
            self.subjects_results.append(avg_block_rt)
            
        self.subjects_results.append(count/whole_trials)
        self.subjects_results.append(wh_rt/len_all)

        
        # self.dframe.loc[self.raw] = self.subjects_results
        print(self.subjects_results,'\n',len(self.subjects_results))
        print(self.dframe.columns,'\n',len(self.dframe.columns))
        self.dframe.loc[self.raw] = self.subjects_results # write into uncommited pandas

        # self.raw += 1
        
        return self.dframe

    def update(self):
        print(self.dframe)
        self.dframe.to_csv(LOCAL_DIR_FILE,index=False)

    # report for the subject: write down as log files 
    def reporter_for_sub(self,outfilename:str,numb=None)-> None:
        # 直接查表技术实现，如果查不到重新生成查表即可
        if numb is None:
            numb = self.number
        sub_frame = self.dframe[self.dframe.loc[:,'subject_num'] == numb]
        if numb not in self.dframe['subject_num'].tolist():
            return 0

        with open(outfilename,'w') as f:
            index = 0 
            full_value = 1 # discard Subject Number
            while True:
                # print(sub_frame)
                
                f.write('被试编号(Subject Number)： '+str(numb)+'\n')
                f.write("组块数Block: "+str(index+1)+"\n")
                f.write("组块信息(Block information): "+self.labels_explain[index]+'\n')
                
                f.write("您在该组块的平均准确率为 (Your accurancy rate is): "+str(sub_frame.iloc[:,full_value].tolist()[0])+"\n")
                full_value += 1
                f.write("您在该组块的平均反应时为(单位：秒)(Your average reaction time is): "+str(sub_frame.iloc[:,full_value].tolist()[0])+"\n\n")
                full_value += 1
                index += 1
                if  full_value == len(sub_frame.columns) -2:
                    break

            f.write("\n总体结果(WHOLE RESULTS): \n")
            f.write("您在总体平均准确率为(Your whole accurancy rate is): "+str(sub_frame['avg_whole_cor'].tolist()[0])+"\n")
            f.write("您的总体平均反应时为(单位：秒)(Your whole average reaction time is  [s]): "+str(sub_frame['avg_whole_rt'].tolist()[0])+"\n")
        f.close()
        return 1

    # data reporter for experimenter
    def reporter_for_experiments(self,outputfilename = None):
        return self.dframe.mean()


if __name__ == "__main__":
    # subject generate test files:
    flag = 1
    subject_num = int(input("Please input the number of subject:   "))
    print(os.getcwd())
    post = PostProcess()

    write_file = 'output/subject_'+str(subject_num)+'.log'
    # print(write_file)
    if post.reporter_for_sub(write_file,subject_num) == 0:
        # 重新更新
        print('A new subject test, waiting for reload......')
        if post.fillin_table(subject_num) == 0:
            print("对不起，找不到您所说的被试编号(Error: No matched subject number).")
            flag = 0
        if flag == 1:
            print(post.sub_information_gen())
            post.reporter_for_sub(write_file)
            post.update()
    if flag != 0:
        os.system(os.getcwd()+'/'+ write_file)
        print(post.reporter_for_experiments())
    
    # experinemter deal with data

