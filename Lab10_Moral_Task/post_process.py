import pandas as pd 
import numpy as np
import os 
import matplotlib.pyplot as plt


DIR_FILE = 'subject_results.csv'
def get_filename(number: int) -> str:
    try:
        for i in os.listdir("data"):
            keyword = str(number)+"_"
            if i[-3:] == 'csv' and i.startswith(keyword):
                filename = i # Only One!
        return filename
    except Exception:
        return 'NAN'

def data_processing(number: int) -> pd.DataFrame:
    '''
    para:
        number of subject
    '''
    k = get_filename(number)
    if get_filename(number) == 'NAN':
        return 'NAN'    
    else:
        filename = "data/"+ k 
    return pd.read_csv(filename)

def get_data():
    mylists = []
    for item in os.listdir("data"):
        if item[-3:] == 'csv':
            mylists.append(item)
    
    return mylists


def get_trials(data:pd.DataFrame) -> int:
    return len(data.dropna(subset='slider.response'))


def get_rtmean(data: pd.DataFrame) -> float:
    return data['slider.rt'].mean()

def get_scoremean(data: pd.DataFrame) -> float:
    return data['slider.response'].mean()

def get_goodPhappyE_score(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'goodPhappyE']
    return childata['slider.response'].mean()

def get_goodPhappyE_rt(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'goodPhappyE']
    return childata['slider.rt'].mean()

def get_goodPsadE_score(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'goodPsadE']
    return childata['slider.response'].mean()

def get_goodPsadE_rt(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'goodPsadE']
    return childata['slider.rt'].mean()

def get_badPhappyE_score(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'badPhappyE']
    return childata['slider.response'].mean()

def get_badPhappyE_rt(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'badPhappyE']
    return childata['slider.rt'].mean()

def get_badPsadE_score(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'badPsadE']
    return childata['slider.response'].mean()

def get_badPsadE_rt(data: pd.DataFrame) -> float:
    childata = data[data['cond'] == 'badPsadE']
    return childata['slider.rt'].mean()

def show_fig(data):
    '''plot rt time'''
    '''xaxis = trials, yaxis = rt'''
    m = data.dropna(subset='slider.response')
    x = np.arange(1, get_trials(data)+1)
    y = m['slider.response'].tolist()

    
    plt.xlabel('trials')
    plt.ylabel('scores')
    # plt.title(''+'')
    plt.bar(x,y)

    plt.show()

def write(data: pd.DataFrame):
    data.to_csv(DIR_FILE, index=False)


if __name__ == '__main__':
    exp = get_data()
    fullist = []
    for item in exp:
        sublabel = []
        sublabel.append(item.split('_')[0])
        mexp = pd.read_csv('data/'+item)

        sublabel.append(get_trials(mexp))

        sublabel.append(get_scoremean(mexp))

        sublabel.append(get_rtmean(mexp))

        sublabel.append(get_goodPhappyE_score(mexp))

        sublabel.append(get_goodPhappyE_rt(mexp))
        sublabel.append(get_goodPsadE_score(mexp))
        sublabel.append(get_goodPsadE_rt(mexp))       
        sublabel.append(get_badPhappyE_score(mexp))
        sublabel.append(get_badPhappyE_rt(mexp))
        sublabel.append(get_badPsadE_score(mexp))
        sublabel.append(get_badPsadE_rt(mexp))
        print(sublabel)
        fullist.append(sublabel)

    columns = ['subject_ID','trials','mean_score','mean_rt',
                'mean_goodPropose_happyEnd_score', 'mean_goodPropose_happyEnd_rt',
                'mean_goodPropose_sadEnd_score','mean_goodPropose_sadEnd_rt',
                'mean_badPropose_happyEnd_score','mean_badPropose_happyEnd_rt',
                'mean_badPropose_sadEnd_score','mean_badPropose_sadEnd_rt' ]
    fulldata = pd.DataFrame(columns=columns, data=fullist)
    write(fulldata)
