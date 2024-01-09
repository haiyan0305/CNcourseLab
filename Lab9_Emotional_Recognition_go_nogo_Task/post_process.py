import pandas as pd 
import numpy as np
import os 

LOCAL_DIR_FILE = 'subjects_results.csv'
def get_filename(number: int) -> str:
    try:
        for i in os.listdir("data"):
            keyword = str(number)+"_"
            if i[-3:] == 'csv' and i.startswith(keyword):
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
        template = pd.read_csv(filename)
        if len(template.columns) == 1:
            print('\\t sep required......')
            return pd.read_csv(filename,sep='\t')
        else:
            return template
  

class PostProcess:
    def __init__(self):
        self.labels = ['htsd','htnd','nthd','ntsd','sthd','stnd']
        self.labels_explain = ['happy target and sad distraction','happy target and neutral distraction','neutral target and happy distraction','neutral target and sad distraction','sad target and happy distraction','sad target and neutral distraction']
        self.rts = ['response_'+str(i+1)+'.rt' for i in range(6) ]
        self.corrs = ['response_'+str(i+1)+'.corr' for i in range(6)]
        self.tables = []
        self.blocks = None
        self.raw_data = None
        self.number =  0
        self.subjects_results = []
        self.names = ['subject_num','avg_cor_1','avg_rt_1','avg_cor_2','avg_rt_2','avg_cor_3','avg_rt_3','avg_cor_4','avg_rt_4','avg_cor_5','avg_rt_5','avg_cor_6','avg_rt_6','avg_whole_cor','avg_whole_rt','ED_score']
        self.dframe = pd.read_csv(LOCAL_DIR_FILE)
        self.raw = len(self.dframe)

    def fillin_table(self,number: int) -> int:
        self.raw_data = data_processing(number)
        self.number = number
        self.subjects_results.append(number)
        if self.raw_data is None:
            return 0
        else:
            for item in range(6):
                self.blocks = self.raw_data[self.raw_data.loc[:,'cond'] == self.labels[item]]
                self.blocks = self.blocks.loc[:,['number','corrAns','pleasantness','arousal','dominance','attraction',self.corrs[item],self.rts[item],'cond']]
                self.tables.append(self.blocks)
            return 1
    
    def sub_information_gen(self) -> pd.DataFrame :
        whole_trials = 12*6
        count = 0
        wh_rt = 0.0
        len_all = 0

        hs_rt = 0.0
        sh_rt = 0.0
        # f.write()
        for number in range(len(self.tables)):
            # f.write("Block: "+str(number+1)+"\n")
            # f.write("Block information: "+self.labels_explain[number]+'\n')
            block_data = self.tables[number]
            true_data = block_data[block_data[self.corrs[number]] == 1]
            corr_block_rate = len(true_data)/len(block_data)  # accurancy rate of one block
            # f.write("Your accurancy rate is: "+str(corr_block_rate)+"\n")
            true_space_data = true_data[true_data['corrAns'] == 'space']# true and has space
            sum_block_rt = true_space_data[self.rts[number]].sum()
            avg_block_rt = sum_block_rt / len(true_data) # average reaction time in a block. reminder to cut error results"
            # f.write("Your average reaction time is:"+str(avg_block_rt)+"\n\n")
            count += len(true_data)
            wh_rt += sum_block_rt
            len_all += len(true_space_data)
            print(len_all)

            self.subjects_results.append(corr_block_rate)
            self.subjects_results.append(avg_block_rt)
            
                # calculate Emotional deviation score
            if number == 0:
                hs_rt += avg_block_rt
            elif number == 4: 
                sh_rt += avg_block_rt

        self.subjects_results.append(count/whole_trials)
        self.subjects_results.append(wh_rt/len_all)
        self.subjects_results.append(hs_rt - sh_rt)
        
        # self.dframe.loc[self.raw] = self.subjects_results
        print(self.subjects_results)
        self.dframe.loc[self.raw] = self.subjects_results

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
        # print("Avg_cor_2:\n")
        # print(sub_frame['avg_cor_2'].tolist()[0])
        with open(outfilename,'w') as f:
            for index in range(6):
                # print(sub_frame)
                f.write('Subject Number: '+str(numb)+'\n')
                f.write("Block: "+str(index+1)+"\n")
                f.write("Block information: "+self.labels_explain[index]+'\n')
                f.write("Your accurancy rate is: "+str(sub_frame['avg_cor_'+str(index+1)].tolist()[0])+"\n")
                f.write("Your average reaction time is: "+str(sub_frame['avg_rt_'+str(index+1)].tolist()[0])+"\n\n")
            f.write("\nWHOLE RESULTS:\n")
            f.write("Your whole accurancy rate is: "+str(sub_frame['avg_whole_cor'].tolist()[0])+"\n")
            f.write("Your whole average reaction time is: "+str(sub_frame['avg_whole_rt'].tolist()[0])+"\n")
            f.write("Your Emotional deviation score is: "+ str(sub_frame['ED_score'].tolist()[0] ) +"\n")
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
            print("Error: No matched subject number.")
            flag = 0
        if flag == 1:
            print(post.sub_information_gen())
            post.reporter_for_sub(write_file)
            post.update()
    if flag != 0:
        print(post.reporter_for_experiments())
        os.system(os.getcwd()+'/'+ write_file)
    # experinemter deal with data

