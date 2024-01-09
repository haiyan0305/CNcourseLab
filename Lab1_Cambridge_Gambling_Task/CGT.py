#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on July 10, 2023, at 13:38
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'CGT'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\cpy\\Lab9\\Lab9_Cambridge_Gambling_Task\\Cambridge-Gambling-Task\\CGT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1600, 720], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instr" ---
instr_image = visual.ImageStim(
    win=win,
    name='instr_image', 
    image='instruction/instruction.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.778, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "block_init" ---
instr_blocks_text = visual.TextStim(win=win, name='instr_blocks_text',
    text='准备好后按空格键进入下一组实验\n\n你的代币将会重置为100',
    font='microsoft yahei',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_blocks_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "decision_trial" ---
choice_color = keyboard.Keyboard()
image_0 = visual.ImageStim(
    win=win,
    name='image_0', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_1 = visual.ImageStim(
    win=win,
    name='image_1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
red_image = visual.ImageStim(
    win=win,
    name='red_image', 
    image='stimuli/r.jpg', mask=None, anchor='center',
    ori=0, pos=(-0.3, -0.2), size=(0.356, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
blue_image = visual.ImageStim(
    win=win,
    name='blue_image', 
    image='stimuli/b.jpg', mask=None, anchor='center',
    ori=0, pos=(0.3, -0.2), size=(0.356, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
arrow_image = visual.ImageStim(
    win=win,
    name='arrow_image', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
money_text = visual.TextStim(win=win, name='money_text',
    text='',
    font='microsoft yahei',
    pos=(-0.2, 0.08), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
introduction_text = visual.TextStim(win=win, name='introduction_text',
    text='按左方向键选择红色\n按右方向键选择蓝色',
    font='microsoft yahei',
    pos=(0, -0.03), height=0.04, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# --- Initialize components for Routine "rate_trial" ---
choice_stake = keyboard.Keyboard()
image_9_0 = visual.ImageStim(
    win=win,
    name='image_9_0', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.08, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
red_image_2 = visual.ImageStim(
    win=win,
    name='red_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.3, -0.2), size=(0.356, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
blue_image_2 = visual.ImageStim(
    win=win,
    name='blue_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.3, -0.2), size=(0.356, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
money_text_2 = visual.TextStim(win=win, name='money_text_2',
    text='',
    font='microsoft yahei',
    pos=(-0.2, 0.08), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
count_down_text_0 = visual.TextStim(win=win, name='count_down_text_0',
    text='',
    font='microsoft yahei',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
count_down_text_1 = visual.TextStim(win=win, name='count_down_text_1',
    text='',
    font='microsoft yahei',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
count_down_text_2 = visual.TextStim(win=win, name='count_down_text_2',
    text='',
    font='microsoft yahei',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='1.0000, 1.0000, -1.0000', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
count_down_text_3 = visual.TextStim(win=win, name='count_down_text_3',
    text='',
    font='microsoft yahei',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
count_down_text_4 = visual.TextStim(win=win, name='count_down_text_4',
    text='',
    font='microsoft yahei',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
stake_text = visual.TextStim(win=win, name='stake_text',
    text='赌注:',
    font='microsoft yahei',
    pos=(.09, 0.08), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
arrow_image_2 = visual.ImageStim(
    win=win,
    name='arrow_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.09, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)

# --- Initialize components for Routine "feedback" ---
stake_num_text = visual.TextStim(win=win, name='stake_num_text',
    text='',
    font='microsoft yahei',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
result_text = visual.TextStim(win=win, name='result_text',
    text='',
    font='microsoft yahei',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
total_token_text = visual.TextStim(win=win, name='total_token_text',
    text='',
    font='microsoft yahei',
    pos=(0, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
arrow_image_3 = visual.ImageStim(
    win=win,
    name='arrow_image_3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
# Run 'Begin Experiment' code from code_end
l9 = []
l8 = []
l7 = []
l6 = []
ll = []

# --- Initialize components for Routine "end" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='测试结束！感谢你的参与！',
    font='microsoft yahei',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_text = visual.TextStim(win=win, name='space_text',
    text='按空格键正式结束实验',
    font='microsoft yahei',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_JS
sumlist = sum
# Run 'Begin Routine' code from code_config
# --- origion meney will be 100 --- 
token = 100

# --- config position of bule and red cards ---
posl = [[-0.45, 0.25],
        [-0.35, 0.25],
        [-0.25, 0.25],
        [-0.15, 0.25],
        [-0.05, 0.25],
        [0.05, 0.25],
        [0.15, 0.25],
        [0.25, 0.25],
        [0.35, 0.25],
        [0.45, 0.25]]

# --- stimuli deifination --- 
# not only save words but also easy to modify
stims = ['stimuli/red.png', 'stimuli/blue.png']
cstims = ['stimuli/rc.jpg', 'stimuli/bc.jpg']
ncstims = ['stimuli/r.jpg', 'stimuli/b.jpg']


# --- count down time --- 
ct1 = 2 # aka, time interval
ct2 = ct1 * 2
ct3 = ct1 * 3
ct4 = ct1 * 4
ct5 = ct1 * 5


# --- rate sequence ---
counthighlow = [.95 , .75, .5, .25, .05]
countlowhigh = [0.05, 0.25, .5, 0.75, 0.95]

# --- stake number (position) ---
bpos = [.24, 0]

# --- arrow position ---
arrPos = [0.5, -0.35]

# --- other info --- 
# red card => left position (-0.2, 0)
# blue card => right position (0.2, 0)


instr_key_resp.keys = []
instr_key_resp.rt = []
_instr_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [instr_image, instr_key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_image* updates
    if instr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_image.frameNStart = frameN  # exact frame index
        instr_image.tStart = t  # local t and not account for scr refresh
        instr_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_image.started')
        instr_image.setAutoDraw(True)
    
    # *instr_key_resp* updates
    waitOnFlip = False
    if instr_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_key_resp.frameNStart = frameN  # exact frame index
        instr_key_resp.tStart = t  # local t and not account for scr refresh
        instr_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_key_resp.started')
        instr_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_key_resp_allKeys.extend(theseKeys)
        if len(_instr_key_resp_allKeys):
            instr_key_resp.keys = _instr_key_resp_allKeys[-1].name  # just the last key pressed
            instr_key_resp.rt = _instr_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr" ---
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_key_resp.keys in ['', [], None]:  # No response was made
    instr_key_resp.keys = None
thisExp.addData('instr_key_resp.keys',instr_key_resp.keys)
if instr_key_resp.keys != None:  # we had a response
    thisExp.addData('instr_key_resp.rt', instr_key_resp.rt)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition/main.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block_init" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_init
    if block_type == 'up':
        arrow = 'stimuli/tri.png'
    elif block_type == 'down':
        arrow = 'stimuli/tri_r.png'
    
    # --- origion meney will be 100 --- 
    token = 100
    instr_blocks_key_resp.keys = []
    instr_blocks_key_resp.rt = []
    _instr_blocks_key_resp_allKeys = []
    # keep track of which components have finished
    block_initComponents = [instr_blocks_text, instr_blocks_key_resp]
    for thisComponent in block_initComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_init" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_blocks_text* updates
        if instr_blocks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_blocks_text.frameNStart = frameN  # exact frame index
            instr_blocks_text.tStart = t  # local t and not account for scr refresh
            instr_blocks_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_blocks_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_blocks_text.started')
            instr_blocks_text.setAutoDraw(True)
        
        # *instr_blocks_key_resp* updates
        waitOnFlip = False
        if instr_blocks_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_blocks_key_resp.frameNStart = frameN  # exact frame index
            instr_blocks_key_resp.tStart = t  # local t and not account for scr refresh
            instr_blocks_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_blocks_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_blocks_key_resp.started')
            instr_blocks_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_blocks_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_blocks_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_blocks_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_blocks_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _instr_blocks_key_resp_allKeys.extend(theseKeys)
            if len(_instr_blocks_key_resp_allKeys):
                instr_blocks_key_resp.keys = _instr_blocks_key_resp_allKeys[-1].name  # just the last key pressed
                instr_blocks_key_resp.rt = _instr_blocks_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_initComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_init" ---
    for thisComponent in block_initComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instr_blocks_key_resp.keys in ['', [], None]:  # No response was made
        instr_blocks_key_resp.keys = None
    blocks.addData('instr_blocks_key_resp.keys',instr_blocks_key_resp.keys)
    if instr_blocks_key_resp.keys != None:  # we had a response
        blocks.addData('instr_blocks_key_resp.rt', instr_blocks_key_resp.rt)
    # the Routine "block_init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condition_file),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "decision_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_decision
        # yep, it's kind of unatral for Python
        # Python allows ['stimuli/red.png'] * red_num
        # But we should take online version into consideration
        
        # --- config picture of bule and red cards ---
        # --- setting these at the begin of trials ---
        # --- Method : append picture into an array ---
        # --- in image components will empoly picl ---
        picl = []
        for i in range(red_num):
            picl.append(stims[0])
        
        for i in range(blue_num):
            picl.append(stims[1])
        
        print(picl)
        # --- generate now token number --- 
        token_show = '总金额：' + str(int(token))
        print("token_show: ",token_show)
        choice_color.keys = []
        choice_color.rt = []
        _choice_color_allKeys = []
        image_0.setPos([posl[0]])
        image_0.setImage(picl[0])
        image_1.setPos([posl[1]])
        image_1.setImage(picl[1])
        image_2.setPos([posl[2]])
        image_2.setImage(picl[2])
        image_3.setPos([posl[3]])
        image_3.setImage(picl[3])
        image_4.setPos([posl[4]])
        image_4.setImage(picl[4])
        image_5.setPos([posl[5]])
        image_5.setImage(picl[5])
        image_6.setPos([posl[6]])
        image_6.setImage(picl[6])
        image_7.setPos([posl[7]])
        image_7.setImage(picl[7])
        image_8.setPos([posl[8]])
        image_8.setImage(picl[8])
        image_9.setPos([posl[9]])
        image_9.setImage(picl[9])
        arrow_image.setPos(arrPos)
        arrow_image.setImage(arrow)
        money_text.setText(token_show)
        # keep track of which components have finished
        decision_trialComponents = [choice_color, image_0, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, red_image, blue_image, arrow_image, money_text, introduction_text]
        for thisComponent in decision_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decision_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *choice_color* updates
            waitOnFlip = False
            if choice_color.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choice_color.frameNStart = frameN  # exact frame index
                choice_color.tStart = t  # local t and not account for scr refresh
                choice_color.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice_color, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'choice_color.started')
                choice_color.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice_color.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice_color.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice_color.status == STARTED and not waitOnFlip:
                theseKeys = choice_color.getKeys(keyList=['left','right'], waitRelease=False)
                _choice_color_allKeys.extend(theseKeys)
                if len(_choice_color_allKeys):
                    choice_color.keys = _choice_color_allKeys[0].name  # just the first key pressed
                    choice_color.rt = _choice_color_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_0* updates
            if image_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_0.frameNStart = frameN  # exact frame index
                image_0.tStart = t  # local t and not account for scr refresh
                image_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_0.started')
                image_0.setAutoDraw(True)
            
            # *image_1* updates
            if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1.frameNStart = frameN  # exact frame index
                image_1.tStart = t  # local t and not account for scr refresh
                image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1.started')
                image_1.setAutoDraw(True)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                image_2.setAutoDraw(True)
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                image_3.setAutoDraw(True)
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                image_4.setAutoDraw(True)
            
            # *image_5* updates
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                image_5.setAutoDraw(True)
            
            # *image_6* updates
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                image_6.setAutoDraw(True)
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                image_7.setAutoDraw(True)
            
            # *image_8* updates
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.started')
                image_8.setAutoDraw(True)
            
            # *image_9* updates
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.started')
                image_9.setAutoDraw(True)
            
            # *red_image* updates
            if red_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_image.frameNStart = frameN  # exact frame index
                red_image.tStart = t  # local t and not account for scr refresh
                red_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_image.started')
                red_image.setAutoDraw(True)
            
            # *blue_image* updates
            if blue_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blue_image.frameNStart = frameN  # exact frame index
                blue_image.tStart = t  # local t and not account for scr refresh
                blue_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blue_image.started')
                blue_image.setAutoDraw(True)
            
            # *arrow_image* updates
            if arrow_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_image.frameNStart = frameN  # exact frame index
                arrow_image.tStart = t  # local t and not account for scr refresh
                arrow_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow_image.started')
                arrow_image.setAutoDraw(True)
            
            # *money_text* updates
            if money_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                money_text.frameNStart = frameN  # exact frame index
                money_text.tStart = t  # local t and not account for scr refresh
                money_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(money_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'money_text.started')
                money_text.setAutoDraw(True)
            
            # *introduction_text* updates
            if introduction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                introduction_text.frameNStart = frameN  # exact frame index
                introduction_text.tStart = t  # local t and not account for scr refresh
                introduction_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(introduction_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'introduction_text.started')
                introduction_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decision_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decision_trial" ---
        for thisComponent in decision_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if choice_color.keys in ['', [], None]:  # No response was made
            choice_color.keys = None
        trials.addData('choice_color.keys',choice_color.keys)
        if choice_color.keys != None:  # we had a response
            trials.addData('choice_color.rt', choice_color.rt)
        # the Routine "decision_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rate_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_rate
        # --- set picture of red_image_2/blue_image_2 up to previous key --- 
        print("ncstims: ", ncstims)
        print("cstims: ", cstims)
        if choice_color.keys == 'left':
            rpic = cstims[0]
            bpic = ncstims[1]
        elif choice_color.keys == 'right':
            bpic = cstims[1]
            rpic = ncstims[0]
        else:
            print('error in setting chose picture')
        
        # --- handling bet number sequences ---
        if count_down_type == 'high_to_low':
            count_seq = counthighlow
        elif count_down_type == 'low_to_high':
            count_seq = countlowhigh
        else:
            print('error in setting count down sequence' )
        
        
        # --- use count down seqence to show text ---
        countdownl = []
        
        for i in count_seq:
            temp = str(int(token*i))
            countdownl.append(temp)
        choice_stake.keys = []
        choice_stake.rt = []
        _choice_stake_allKeys = []
        image_9_0.setPos([posl[0]])
        image_9_0.setImage(picl[0])
        image_10.setPos([posl[1]])
        image_10.setImage(picl[1])
        image_11.setPos([posl[2]])
        image_11.setImage(picl[2])
        image_12.setPos([posl[3]])
        image_12.setImage(picl[3])
        image_13.setPos([posl[4]])
        image_13.setImage(picl[4])
        image_14.setPos([posl[5]])
        image_14.setImage(picl[5])
        image_15.setPos([posl[6]])
        image_15.setImage(picl[6])
        image_16.setPos([posl[7]])
        image_16.setImage(picl[7])
        image_17.setPos([posl[8]])
        image_17.setImage(picl[8])
        image_18.setPos([posl[9]])
        image_18.setImage(picl[9])
        red_image_2.setImage(rpic)
        blue_image_2.setImage(bpic)
        money_text_2.setText(token_show)
        count_down_text_0.setPos(bpos)
        count_down_text_0.setText(countdownl[0])
        count_down_text_1.setPos(bpos)
        count_down_text_1.setText(countdownl[1])
        count_down_text_2.setPos(bpos)
        count_down_text_2.setText(countdownl[2])
        count_down_text_3.setPos(bpos)
        count_down_text_3.setText(countdownl[3])
        count_down_text_4.setPos(bpos)
        count_down_text_4.setText(countdownl[4])
        arrow_image_2.setPos(arrPos)
        arrow_image_2.setImage(arrow)
        # keep track of which components have finished
        rate_trialComponents = [choice_stake, image_9_0, image_10, image_11, image_12, image_13, image_14, image_15, image_16, image_17, image_18, red_image_2, blue_image_2, money_text_2, count_down_text_0, count_down_text_1, count_down_text_2, count_down_text_3, count_down_text_4, stake_text, arrow_image_2]
        for thisComponent in rate_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rate_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *choice_stake* updates
            waitOnFlip = False
            if choice_stake.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choice_stake.frameNStart = frameN  # exact frame index
                choice_stake.tStart = t  # local t and not account for scr refresh
                choice_stake.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice_stake, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'choice_stake.started')
                choice_stake.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice_stake.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice_stake.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice_stake.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > choice_stake.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    choice_stake.tStop = t  # not accounting for scr refresh
                    choice_stake.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'choice_stake.stopped')
                    choice_stake.status = FINISHED
            if choice_stake.status == STARTED and not waitOnFlip:
                theseKeys = choice_stake.getKeys(keyList=['down'], waitRelease=False)
                _choice_stake_allKeys.extend(theseKeys)
                if len(_choice_stake_allKeys):
                    choice_stake.keys = _choice_stake_allKeys[-1].name  # just the last key pressed
                    choice_stake.rt = _choice_stake_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_9_0* updates
            if image_9_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9_0.frameNStart = frameN  # exact frame index
                image_9_0.tStart = t  # local t and not account for scr refresh
                image_9_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9_0.started')
                image_9_0.setAutoDraw(True)
            if image_9_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_9_0.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_9_0.tStop = t  # not accounting for scr refresh
                    image_9_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9_0.stopped')
                    image_9_0.setAutoDraw(False)
            
            # *image_10* updates
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.started')
                image_10.setAutoDraw(True)
            if image_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_10.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_10.tStop = t  # not accounting for scr refresh
                    image_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.stopped')
                    image_10.setAutoDraw(False)
            
            # *image_11* updates
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_11.started')
                image_11.setAutoDraw(True)
            if image_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_11.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_11.tStop = t  # not accounting for scr refresh
                    image_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.stopped')
                    image_11.setAutoDraw(False)
            
            # *image_12* updates
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_12.started')
                image_12.setAutoDraw(True)
            if image_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_12.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_12.tStop = t  # not accounting for scr refresh
                    image_12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.stopped')
                    image_12.setAutoDraw(False)
            
            # *image_13* updates
            if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_13.frameNStart = frameN  # exact frame index
                image_13.tStart = t  # local t and not account for scr refresh
                image_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_13.started')
                image_13.setAutoDraw(True)
            if image_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_13.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_13.tStop = t  # not accounting for scr refresh
                    image_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_13.stopped')
                    image_13.setAutoDraw(False)
            
            # *image_14* updates
            if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_14.frameNStart = frameN  # exact frame index
                image_14.tStart = t  # local t and not account for scr refresh
                image_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_14.started')
                image_14.setAutoDraw(True)
            if image_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_14.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_14.tStop = t  # not accounting for scr refresh
                    image_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_14.stopped')
                    image_14.setAutoDraw(False)
            
            # *image_15* updates
            if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.started')
                image_15.setAutoDraw(True)
            if image_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_15.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_15.tStop = t  # not accounting for scr refresh
                    image_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_15.stopped')
                    image_15.setAutoDraw(False)
            
            # *image_16* updates
            if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_16.frameNStart = frameN  # exact frame index
                image_16.tStart = t  # local t and not account for scr refresh
                image_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_16.started')
                image_16.setAutoDraw(True)
            if image_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_16.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_16.tStop = t  # not accounting for scr refresh
                    image_16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_16.stopped')
                    image_16.setAutoDraw(False)
            
            # *image_17* updates
            if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_17.frameNStart = frameN  # exact frame index
                image_17.tStart = t  # local t and not account for scr refresh
                image_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_17.started')
                image_17.setAutoDraw(True)
            if image_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_17.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_17.tStop = t  # not accounting for scr refresh
                    image_17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_17.stopped')
                    image_17.setAutoDraw(False)
            
            # *image_18* updates
            if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_18.frameNStart = frameN  # exact frame index
                image_18.tStart = t  # local t and not account for scr refresh
                image_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_18.started')
                image_18.setAutoDraw(True)
            if image_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_18.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_18.tStop = t  # not accounting for scr refresh
                    image_18.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_18.stopped')
                    image_18.setAutoDraw(False)
            
            # *red_image_2* updates
            if red_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_image_2.frameNStart = frameN  # exact frame index
                red_image_2.tStart = t  # local t and not account for scr refresh
                red_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_image_2.started')
                red_image_2.setAutoDraw(True)
            if red_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_image_2.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    red_image_2.tStop = t  # not accounting for scr refresh
                    red_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'red_image_2.stopped')
                    red_image_2.setAutoDraw(False)
            
            # *blue_image_2* updates
            if blue_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blue_image_2.frameNStart = frameN  # exact frame index
                blue_image_2.tStart = t  # local t and not account for scr refresh
                blue_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blue_image_2.started')
                blue_image_2.setAutoDraw(True)
            if blue_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blue_image_2.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    blue_image_2.tStop = t  # not accounting for scr refresh
                    blue_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blue_image_2.stopped')
                    blue_image_2.setAutoDraw(False)
            
            # *money_text_2* updates
            if money_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                money_text_2.frameNStart = frameN  # exact frame index
                money_text_2.tStart = t  # local t and not account for scr refresh
                money_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(money_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'money_text_2.started')
                money_text_2.setAutoDraw(True)
            if money_text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > money_text_2.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    money_text_2.tStop = t  # not accounting for scr refresh
                    money_text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'money_text_2.stopped')
                    money_text_2.setAutoDraw(False)
            
            # *count_down_text_0* updates
            if count_down_text_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                count_down_text_0.frameNStart = frameN  # exact frame index
                count_down_text_0.tStart = t  # local t and not account for scr refresh
                count_down_text_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(count_down_text_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'count_down_text_0.started')
                count_down_text_0.setAutoDraw(True)
            if count_down_text_0.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > ct1-frameTolerance:
                    # keep track of stop time/frame for later
                    count_down_text_0.tStop = t  # not accounting for scr refresh
                    count_down_text_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'count_down_text_0.stopped')
                    count_down_text_0.setAutoDraw(False)
            
            # *count_down_text_1* updates
            if count_down_text_1.status == NOT_STARTED and tThisFlip >= ct1-frameTolerance:
                # keep track of start time/frame for later
                count_down_text_1.frameNStart = frameN  # exact frame index
                count_down_text_1.tStart = t  # local t and not account for scr refresh
                count_down_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(count_down_text_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'count_down_text_1.started')
                count_down_text_1.setAutoDraw(True)
            if count_down_text_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > ct2-frameTolerance:
                    # keep track of stop time/frame for later
                    count_down_text_1.tStop = t  # not accounting for scr refresh
                    count_down_text_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'count_down_text_1.stopped')
                    count_down_text_1.setAutoDraw(False)
            
            # *count_down_text_2* updates
            if count_down_text_2.status == NOT_STARTED and tThisFlip >= ct2-frameTolerance:
                # keep track of start time/frame for later
                count_down_text_2.frameNStart = frameN  # exact frame index
                count_down_text_2.tStart = t  # local t and not account for scr refresh
                count_down_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(count_down_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'count_down_text_2.started')
                count_down_text_2.setAutoDraw(True)
            if count_down_text_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > ct3-frameTolerance:
                    # keep track of stop time/frame for later
                    count_down_text_2.tStop = t  # not accounting for scr refresh
                    count_down_text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'count_down_text_2.stopped')
                    count_down_text_2.setAutoDraw(False)
            
            # *count_down_text_3* updates
            if count_down_text_3.status == NOT_STARTED and tThisFlip >= ct3-frameTolerance:
                # keep track of start time/frame for later
                count_down_text_3.frameNStart = frameN  # exact frame index
                count_down_text_3.tStart = t  # local t and not account for scr refresh
                count_down_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(count_down_text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'count_down_text_3.started')
                count_down_text_3.setAutoDraw(True)
            if count_down_text_3.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > ct4-frameTolerance:
                    # keep track of stop time/frame for later
                    count_down_text_3.tStop = t  # not accounting for scr refresh
                    count_down_text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'count_down_text_3.stopped')
                    count_down_text_3.setAutoDraw(False)
            
            # *count_down_text_4* updates
            if count_down_text_4.status == NOT_STARTED and tThisFlip >= ct4-frameTolerance:
                # keep track of start time/frame for later
                count_down_text_4.frameNStart = frameN  # exact frame index
                count_down_text_4.tStart = t  # local t and not account for scr refresh
                count_down_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(count_down_text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'count_down_text_4.started')
                count_down_text_4.setAutoDraw(True)
            if count_down_text_4.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    count_down_text_4.tStop = t  # not accounting for scr refresh
                    count_down_text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'count_down_text_4.stopped')
                    count_down_text_4.setAutoDraw(False)
            
            # *stake_text* updates
            if stake_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stake_text.frameNStart = frameN  # exact frame index
                stake_text.tStart = t  # local t and not account for scr refresh
                stake_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stake_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stake_text.started')
                stake_text.setAutoDraw(True)
            if stake_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stake_text.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    stake_text.tStop = t  # not accounting for scr refresh
                    stake_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stake_text.stopped')
                    stake_text.setAutoDraw(False)
            
            # *arrow_image_2* updates
            if arrow_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_image_2.frameNStart = frameN  # exact frame index
                arrow_image_2.tStart = t  # local t and not account for scr refresh
                arrow_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow_image_2.started')
                arrow_image_2.setAutoDraw(True)
            if arrow_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow_image_2.tStartRefresh + ct5-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_image_2.tStop = t  # not accounting for scr refresh
                    arrow_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow_image_2.stopped')
                    arrow_image_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rate_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rate_trial" ---
        for thisComponent in rate_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if choice_stake.keys in ['', [], None]:  # No response was made
            choice_stake.keys = None
        trials.addData('choice_stake.keys',choice_stake.keys)
        if choice_stake.keys != None:  # we had a response
            trials.addData('choice_stake.rt', choice_stake.rt)
        # the Routine "rate_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from feedback_code
        
        # --- decide which choice (idx = index) was select ---
        if choice_stake.rt:
            idx = int(choice_stake.rt/5)
        else:
            idx = 4
        stake_num = countdownl[idx]
        count_here = count_seq[idx]
        
        
        # --- show text of stake number ---
        snshow = '赌注: ' + str(stake_num)
        
        # --- decide what result ---
        temp = random() * 10
        if temp< red_num:
            result_color = 'red'
            result_direction = 'left'
        else:
            result_color = 'blue'
            result_direction = 'right'
        
        if choice_color.keys == result_direction:
            result = 'win'
            result_t = '你猜对了！'
            token += int(stake_num)
        else:
            result = 'lose'
            result_t = '你猜错了！'
            token -= int(stake_num)
        
        
        # --- token number ---
        token_show = '总金额：' + str(int(token))
        
        # --- add  data (remember to check JS)
        thisExp.addData('choice_stake.choice', stake_num)
        thisExp.addData('choice_stake.result_color', result_color)
        thisExp.addData('choice_stake.result_direction', result_direction)
        thisExp.addData('choice_stake.result', result)
        
        stake_num_text.setText(snshow )
        result_text.setText(result_t)
        total_token_text.setText(token_show)
        arrow_image_3.setPos(arrPos)
        arrow_image_3.setImage(arrow)
        # Run 'Begin Routine' code from code_end
        # --- collect data ---
        if (red_num == 1) or (red_num==9):
            l9.append(count_here)
        elif (red_num == 2) or (red_num==8):
            l8.append(count_here)
        elif (red_num == 3) or (red_num==7):
            l7.append(count_here)
        elif (red_num == 4) or (red_num==6):
            l6.append(count_here)
        ll.append(count_here)
        # keep track of which components have finished
        feedbackComponents = [stake_num_text, result_text, total_token_text, arrow_image_3]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stake_num_text* updates
            if stake_num_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stake_num_text.frameNStart = frameN  # exact frame index
                stake_num_text.tStart = t  # local t and not account for scr refresh
                stake_num_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stake_num_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stake_num_text.started')
                stake_num_text.setAutoDraw(True)
            if stake_num_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stake_num_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stake_num_text.tStop = t  # not accounting for scr refresh
                    stake_num_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stake_num_text.stopped')
                    stake_num_text.setAutoDraw(False)
            
            # *result_text* updates
            if result_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                result_text.frameNStart = frameN  # exact frame index
                result_text.tStart = t  # local t and not account for scr refresh
                result_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(result_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'result_text.started')
                result_text.setAutoDraw(True)
            if result_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > result_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    result_text.tStop = t  # not accounting for scr refresh
                    result_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'result_text.stopped')
                    result_text.setAutoDraw(False)
            
            # *total_token_text* updates
            if total_token_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                total_token_text.frameNStart = frameN  # exact frame index
                total_token_text.tStart = t  # local t and not account for scr refresh
                total_token_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(total_token_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'total_token_text.started')
                total_token_text.setAutoDraw(True)
            if total_token_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > total_token_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    total_token_text.tStop = t  # not accounting for scr refresh
                    total_token_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'total_token_text.stopped')
                    total_token_text.setAutoDraw(False)
            
            # *arrow_image_3* updates
            if arrow_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_image_3.frameNStart = frameN  # exact frame index
                arrow_image_3.tStart = t  # local t and not account for scr refresh
                arrow_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arrow_image_3.started')
                arrow_image_3.setAutoDraw(True)
            if arrow_image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow_image_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_image_3.tStop = t  # not accounting for scr refresh
                    arrow_image_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'arrow_image_3.stopped')
                    arrow_image_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_end
        if token <=1:
            trials.finished = True
            
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'blocks'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_key_resp.keys = []
end_key_resp.rt = []
_end_key_resp_allKeys = []
# Run 'Begin Routine' code from code_report
a = sumlist(l9)*2
b = sumlist(l8)
c = sumlist(l7)
d = sumlist(l6)*2
e = sumlist(ll)/len(ll)
print('Risk_Adjustmenrt', (a+b-c-d)/e)
# keep track of which components have finished
endComponents = [end_text, space_text, end_key_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_text.started')
        end_text.setAutoDraw(True)
    
    # *space_text* updates
    if space_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_text.frameNStart = frameN  # exact frame index
        space_text.tStart = t  # local t and not account for scr refresh
        space_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_text.started')
        space_text.setAutoDraw(True)
    
    # *end_key_resp* updates
    waitOnFlip = False
    if end_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp.frameNStart = frameN  # exact frame index
        end_key_resp.tStart = t  # local t and not account for scr refresh
        end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_key_resp.started')
        end_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_allKeys.extend(theseKeys)
        if len(_end_key_resp_allKeys):
            end_key_resp.keys = _end_key_resp_allKeys[-1].name  # just the last key pressed
            end_key_resp.rt = _end_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_key_resp.keys in ['', [], None]:  # No response was made
    end_key_resp.keys = None
thisExp.addData('end_key_resp.keys',end_key_resp.keys)
if end_key_resp.keys != None:  # we had a response
    thisExp.addData('end_key_resp.rt', end_key_resp.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
