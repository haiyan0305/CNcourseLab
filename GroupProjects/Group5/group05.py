from psychopy import visual, core, event, data, gui, logging
import random

# 实验参数设置
info = {'参与者编号': ''}
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()

# 设置窗口
win = visual.Window([800, 600], fullscr=False, color=(0, 0, 0))

# 实验指导语
instructions = visual.TextStim(win, text="In this experiment, you will see pairs of images on the screen. "
                                         "Your task is to decide if the pairs are mirror images or identical. "
                                         "Press 'm' if they are mirror images, 'n' if they are identical. "
                                         "Press any key to start.",
                               wrapWidth=1.5, color=(1, 1, 1))
instructions.draw()
win.flip()
event.waitKeys()

# 静息态
def rest_state(duration=5.0):
    rest_period = visual.TextStim(win, text="+", color=(1, 1, 1), height=0.2)
    rest_period.draw()
    win.flip()
    core.wait(duration)  # Display for 5 seconds

# 定义旋转角度
angles = [0, 60, 120, 180, 240, 300]

# 设置图像
def setup_trial(image1, image2):
    is_mirror = random.choice([True, False])
    if is_mirror:
        # 如果是镜像，使用两个不同的图像
        limage = image1
        rimage = image2
        if random.random() > 0.5:
            limage, rimage = rimage, limage
    else:
        # 如果不是镜像，使用相同的图像
        limage = rimage = image1
        if random.random() > 0.5:
            limage = rimage = image2
    # 返回最终的图像和位置
    return limage, rimage, is_mirror

# 创建试次组
def create_trials(images, name):
    trial_list = []
    for x in range(1,61):
        trial_dic = {}
        limage, rimage, is_mirror = setup_trial(images[0], images[1])
        trial_dic['left'] = limage
        trial_dic['right'] = rimage
        trial_dic['name'] = name
        trial_dic['is_mirror'] = is_mirror
        trial_list.append(trial_dic)
    return data.TrialHandler(trial_list, nReps=1, method='random')

trials_letter_1 = create_trials(['R.png', 'RR.png'], 'Letter')
trials_male_face = create_trials(['Maleface.png', 'MalefaceR.png'], 'Male Face')
trials_female_face = create_trials(['Femaleface.png', 'FemalefaceR.png'], 'Female Face')
trials_letter_2 = create_trials(['R.png', 'RR.png'], 'Letter')

# 记录数据
filename = f"data_{info['参与者编号']}.csv"
dataFile = open(filename, 'w')
dataFile.write('Trial,StimType,LeftImage,RightImage,Response,RT,Correct,LeftImageOri,RightImageOri\n')

# 实验循环
clock = core.Clock()

def run_trial(trials):
    for trial in trials:
        limage, rimage = trial['left'], trial['right']

        # Randomly position on left or right
        if random.random() > 0.5:
            limage, rimage = rimage, limage

        limage_stim = visual.ImageStim(win, image=limage, size=0.5)
        rimage_stim = visual.ImageStim(win, image=rimage, size=0.5)

        limage_stim.pos = (-0.5, 0)
        rimage_stim.pos = (0.5, 0)

        limage_ori = random.choice(angles)
        rimage_ori = random.choice(angles)
        limage_stim.ori = limage_ori
        rimage_stim.ori = rimage_ori

        limage_stim.draw()
        rimage_stim.draw()
        win.flip()
        clock.reset()

        keys = event.waitKeys(keyList=['n', 'm', 'escape'])
        rt = clock.getTime()

        if 'escape' in keys:
            break

        response = keys[0] if keys else None
        correct = (response == 'm' if trial['is_mirror'] else response == 'n')
        dataFile.write(f"{trials.thisN},{trial['name']},{limage},{rimage},{response},{rt},{correct},{limage_ori},{rimage_ori}\n")
        win.flip()
        core.wait(1.0)  # 试次间隔

# 运行试次组并在每组前加入静息态
rest_state()
run_trial(trials_letter_1)
rest_state()
run_trial(trials_male_face)
rest_state()
run_trial(trials_female_face)
rest_state()
run_trial(trials_letter_2)

# 结束语
goodbye_text = visual.TextStim(win, text="Thank you for participating! The experiment is now complete.",
                               color=(1, 1, 1))
goodbye_text.draw()
win.flip()
core.wait(5.0)

dataFile.close()
win.close()
core.quit()
