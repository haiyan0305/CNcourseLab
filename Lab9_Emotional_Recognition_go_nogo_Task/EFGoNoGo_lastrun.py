#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on May 24, 2023, at 15:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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
expName = 'Lab3_EFGoGo'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Psychopy Cognitive Assessment\\Psychopy_Lab\\Lab3_Emotional_Recognition_go_nogo_Task\\Lab3_EFGoNoGo_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
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

# --- Initialize components for Routine "instruct" ---
key_resp = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='intro/inC.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "child_instruct1" ---
ready = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='intro/s1C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Pre" ---
pre = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='intro/p1C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pre_trail" ---
pre_pic_1 = visual.ImageStim(
    win=win,
    name='pre_pic_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
pre_resp = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from message
#msg variable just needs some value at start
msg=''
msgcolor = ''

feedback_01 = visual.TextStim(win=win, name='feedback_01',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "main_trail_1" ---
key_main = keyboard.Keyboard()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='intro/p2C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_01" ---
target_pic = visual.ImageStim(
    win=win,
    name='target_pic', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_1 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_2
time = 0.5
msge = ''
corr = []
rts = []
keys = []

rts_value = 0
effect = 0

# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "child_instruct2" ---
ready_2 = keyboard.Keyboard()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='intro/s2C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_02" ---
target_pic_2 = visual.ImageStim(
    win=win,
    name='target_pic_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code
time = 0.5
msge = ''
corr_2 = []
rts_2 = []
keys_2 = []



# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "child_instruct3" ---
ready_3 = keyboard.Keyboard()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='intro/s3C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_03" ---
target_pic_3 = visual.ImageStim(
    win=win,
    name='target_pic_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_3
time = 0.5
msge = ''
corr_3 = []
rts_3 = []
keys_3 = []

rts_value = 0
effect = 0

# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "child_instruct4" ---
ready_4 = keyboard.Keyboard()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='intro/s4C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_04" ---
target_pic_4 = visual.ImageStim(
    win=win,
    name='target_pic_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_4
time = 0.5
msge = ''
corr_4 = []
rts_4 = []
keys_4 = []

rts_value = 0
effect = 0

# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "child_instruct5" ---
ready_5 = keyboard.Keyboard()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='intro/s5C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_05" ---
target_pic_5 = visual.ImageStim(
    win=win,
    name='target_pic_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_5
time = 0.5
msge = ''
corr_5 = []
rts_5 = []
keys_5 = []

rts_value = 0
effect = 0

# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "child_instruct6" ---
ready_6 = keyboard.Keyboard()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='intro/s6C.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "add_signal" ---
pre_3 = visual.TextStim(win=win, name='pre_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_06" ---
target_pic_6 = visual.ImageStim(
    win=win,
    name='target_pic_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
response_6 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_6
time = 0.5
msge = ''
corr_6 = []
rts_6 = []
keys_6 = []

rts_value = 0
effect = 0

# --- Initialize components for Routine "feedback_trial" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "thanks" ---
end_heading_2 = visual.TextStim(win=win, name='end_heading_2',
    text='您现在已经完成了上机部分的实验，\n\n请您休息一会儿，谢谢您的参与！',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructComponents = [key_resp, image_2]
for thisComponent in instructComponents:
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

# --- Run Routine "instruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruct" ---
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "child_instruct1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready.keys = []
ready.rt = []
_ready_allKeys = []
# keep track of which components have finished
child_instruct1Components = [ready, image]
for thisComponent in child_instruct1Components:
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

# --- Run Routine "child_instruct1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready* updates
    waitOnFlip = False
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready.started')
        ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=None, waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # just the last key pressed
            ready.rt = _ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct1" ---
for thisComponent in child_instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "child_instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Pre" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pre.keys = []
pre.rt = []
_pre_allKeys = []
# keep track of which components have finished
PreComponents = [pre, image_3]
for thisComponent in PreComponents:
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

# --- Run Routine "Pre" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre* updates
    waitOnFlip = False
    if pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre.frameNStart = frameN  # exact frame index
        pre.tStart = t  # local t and not account for scr refresh
        pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pre.started')
        pre.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(pre.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(pre.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pre.status == STARTED and not waitOnFlip:
        theseKeys = pre.getKeys(keyList=None, waitRelease=False)
        _pre_allKeys.extend(theseKeys)
        if len(_pre_allKeys):
            pre.keys = _pre_allKeys[-1].name  # just the last key pressed
            pre.rt = _pre_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Pre" ---
for thisComponent in PreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if pre.keys in ['', [], None]:  # No response was made
    pre.keys = None
thisExp.addData('pre.keys',pre.keys)
if pre.keys != None:  # we had a response
    thisExp.addData('pre.rt', pre.rt)
thisExp.nextEntry()
# the Routine "Pre" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pref.xlsx'),
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
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "pre_trail" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    pre_pic_1.setImage(locat)
    pre_resp.keys = []
    pre_resp.rt = []
    _pre_resp_allKeys = []
    # keep track of which components have finished
    pre_trailComponents = [pre_pic_1, pre_resp]
    for thisComponent in pre_trailComponents:
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
    
    # --- Run Routine "pre_trail" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_pic_1* updates
        if pre_pic_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pre_pic_1.frameNStart = frameN  # exact frame index
            pre_pic_1.tStart = t  # local t and not account for scr refresh
            pre_pic_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_pic_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_pic_1.started')
            pre_pic_1.setAutoDraw(True)
        if pre_pic_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_pic_1.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_pic_1.tStop = t  # not accounting for scr refresh
                pre_pic_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_pic_1.stopped')
                pre_pic_1.setAutoDraw(False)
        
        # *pre_resp* updates
        waitOnFlip = False
        if pre_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pre_resp.frameNStart = frameN  # exact frame index
            pre_resp.tStart = t  # local t and not account for scr refresh
            pre_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_resp.started')
            pre_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pre_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pre_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pre_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_resp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_resp.tStop = t  # not accounting for scr refresh
                pre_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_resp.stopped')
                pre_resp.status = FINISHED
        if pre_resp.status == STARTED and not waitOnFlip:
            theseKeys = pre_resp.getKeys(keyList=['space'], waitRelease=False)
            _pre_resp_allKeys.extend(theseKeys)
            if len(_pre_resp_allKeys):
                pre_resp.keys = _pre_resp_allKeys[-1].name  # just the last key pressed
                pre_resp.rt = _pre_resp_allKeys[-1].rt
                # was this correct?
                if (pre_resp.keys == str(corrAns)) or (pre_resp.keys == corrAns):
                    pre_resp.corr = 1
                else:
                    pre_resp.corr = 0
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
        for thisComponent in pre_trailComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pre_trail" ---
    for thisComponent in pre_trailComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pre_resp.keys in ['', [], None]:  # No response was made
        pre_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           pre_resp.corr = 1;  # correct non-response
        else:
           pre_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('pre_resp.keys',pre_resp.keys)
    trials.addData('pre_resp.corr', pre_resp.corr)
    if pre_resp.keys != None:  # we had a response
        trials.addData('pre_resp.rt', pre_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from message
    if pre_resp.corr:#stored on last run routine
      if pre_resp.keys is None:
        msg="回答正确! 反应时 RT NOT EXISTS !"
      else:
        msg="回答正确! 反应时 RT(s)=%.3f" %(round(pre_resp.rt,5))
      msgcolor = 'green'
    else:
      msg="很遗憾，你的选择有误。"
      msgcolor = 'red'
    feedback_01.setColor(msgcolor, colorSpace='rgb')
    feedback_01.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_01]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_01* updates
        if feedback_01.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_01.frameNStart = frameN  # exact frame index
            feedback_01.tStart = t  # local t and not account for scr refresh
            feedback_01.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_01, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_01.started')
            feedback_01.setAutoDraw(True)
        if feedback_01.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_01.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_01.tStop = t  # not accounting for scr refresh
                feedback_01.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_01.stopped')
                feedback_01.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "main_trail_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_main.keys = []
key_main.rt = []
_key_main_allKeys = []
# keep track of which components have finished
main_trail_1Components = [key_main, image_4]
for thisComponent in main_trail_1Components:
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

# --- Run Routine "main_trail_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_main* updates
    waitOnFlip = False
    if key_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_main.frameNStart = frameN  # exact frame index
        key_main.tStart = t  # local t and not account for scr refresh
        key_main.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_main, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_main.started')
        key_main.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_main.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_main.status == STARTED and not waitOnFlip:
        theseKeys = key_main.getKeys(keyList=None, waitRelease=False)
        _key_main_allKeys.extend(theseKeys)
        if len(_key_main_allKeys):
            key_main.keys = _key_main_allKeys[-1].name  # just the last key pressed
            key_main.rt = _key_main_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_trail_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "main_trail_1" ---
for thisComponent in main_trail_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_main.keys in ['', [], None]:  # No response was made
    key_main.keys = None
thisExp.addData('key_main.keys',key_main.keys)
if key_main.keys != None:  # we had a response
    thisExp.addData('key_main.rt', key_main.rt)
thisExp.nextEntry()
# the Routine "main_trail_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_A.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_01" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic.setImage(locat)
    response_1.keys = []
    response_1.rt = []
    _response_1_allKeys = []
    # keep track of which components have finished
    trial_01Components = [target_pic, response_1]
    for thisComponent in trial_01Components:
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
    
    # --- Run Routine "trial_01" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic* updates
        if target_pic.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic.frameNStart = frameN  # exact frame index
            target_pic.tStart = t  # local t and not account for scr refresh
            target_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic.started')
            target_pic.setAutoDraw(True)
        if target_pic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic.tStop = t  # not accounting for scr refresh
                target_pic.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic.stopped')
                target_pic.setAutoDraw(False)
        
        # *response_1* updates
        waitOnFlip = False
        if response_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_1.frameNStart = frameN  # exact frame index
            response_1.tStart = t  # local t and not account for scr refresh
            response_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_1.started')
            response_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_1.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_1.tStop = t  # not accounting for scr refresh
                response_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_1.stopped')
                response_1.status = FINISHED
        if response_1.status == STARTED and not waitOnFlip:
            theseKeys = response_1.getKeys(keyList=['space'], waitRelease=False)
            _response_1_allKeys.extend(theseKeys)
            if len(_response_1_allKeys):
                response_1.keys = _response_1_allKeys[-1].name  # just the last key pressed
                response_1.rt = _response_1_allKeys[-1].rt
                # was this correct?
                if (response_1.keys == str(corrAns)) or (response_1.keys == corrAns):
                    response_1.corr = 1
                else:
                    response_1.corr = 0
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
        for thisComponent in trial_01Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_01" ---
    for thisComponent in trial_01Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_1.keys in ['', [], None]:  # No response was made
        response_1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_1.corr = 1;  # correct non-response
        else:
           response_1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('response_1.keys',response_1.keys)
    trials_2.addData('response_1.corr', response_1.corr)
    if response_1.keys != None:  # we had a response
        trials_2.addData('response_1.rt', response_1.rt)
    # Run 'End Routine' code from code_2
    print(response_1.rt)
    
    corr.append(response_1.corr)
    rts.append(response_1.rt)
    keys.append(response_1.keys)
    print(len(corr))
    
    
    if len(corr) == 12  :
        print(len(corr),keys)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr)):
            if corr[i] == 1 and keys[i] == "space":
                rts_value += rts[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr)/len(corr))+"\n\n\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续实验。"
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "child_instruct2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready_2.keys = []
ready_2.rt = []
_ready_2_allKeys = []
# keep track of which components have finished
child_instruct2Components = [ready_2, image_9]
for thisComponent in child_instruct2Components:
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

# --- Run Routine "child_instruct2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_2* updates
    waitOnFlip = False
    if ready_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_2.frameNStart = frameN  # exact frame index
        ready_2.tStart = t  # local t and not account for scr refresh
        ready_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready_2.started')
        ready_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready_2.status == STARTED and not waitOnFlip:
        theseKeys = ready_2.getKeys(keyList=None, waitRelease=False)
        _ready_2_allKeys.extend(theseKeys)
        if len(_ready_2_allKeys):
            ready_2.keys = _ready_2_allKeys[-1].name  # just the last key pressed
            ready_2.rt = _ready_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct2" ---
for thisComponent in child_instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready_2.keys in ['', [], None]:  # No response was made
    ready_2.keys = None
thisExp.addData('ready_2.keys',ready_2.keys)
if ready_2.keys != None:  # we had a response
    thisExp.addData('ready_2.rt', ready_2.rt)
thisExp.nextEntry()
# the Routine "child_instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_B.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_02" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic_2.setImage(locat)
    response_2.keys = []
    response_2.rt = []
    _response_2_allKeys = []
    # keep track of which components have finished
    trial_02Components = [target_pic_2, response_2]
    for thisComponent in trial_02Components:
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
    
    # --- Run Routine "trial_02" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic_2* updates
        if target_pic_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic_2.frameNStart = frameN  # exact frame index
            target_pic_2.tStart = t  # local t and not account for scr refresh
            target_pic_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic_2.started')
            target_pic_2.setAutoDraw(True)
        if target_pic_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic_2.tStop = t  # not accounting for scr refresh
                target_pic_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic_2.stopped')
                target_pic_2.setAutoDraw(False)
        
        # *response_2* updates
        waitOnFlip = False
        if response_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_2.started')
            response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_2.tStop = t  # not accounting for scr refresh
                response_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_2.stopped')
                response_2.status = FINISHED
        if response_2.status == STARTED and not waitOnFlip:
            theseKeys = response_2.getKeys(keyList=['space'], waitRelease=False)
            _response_2_allKeys.extend(theseKeys)
            if len(_response_2_allKeys):
                response_2.keys = _response_2_allKeys[-1].name  # just the last key pressed
                response_2.rt = _response_2_allKeys[-1].rt
                # was this correct?
                if (response_2.keys == str(corrAns)) or (response_2.keys == corrAns):
                    response_2.corr = 1
                else:
                    response_2.corr = 0
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
        for thisComponent in trial_02Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_02" ---
    for thisComponent in trial_02Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_2.keys in ['', [], None]:  # No response was made
        response_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_2.corr = 1;  # correct non-response
        else:
           response_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('response_2.keys',response_2.keys)
    trials_3.addData('response_2.corr', response_2.corr)
    if response_2.keys != None:  # we had a response
        trials_3.addData('response_2.rt', response_2.rt)
    # Run 'End Routine' code from code
    corr_2.append(response_2.corr)
    rts_2.append(response_2.rt)
    keys_2.append(response_2.keys)
    print(len(corr_2))
    
    
    if len(corr_2) == 12  :
        print(len(corr_2),keys_2)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr_2)):
            if corr_2[i] == 1 and keys_2[i] == "space":
                rts_value += rts_2[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr_2)/len(corr_2))+"\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续."
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# --- Prepare to start Routine "child_instruct3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready_3.keys = []
ready_3.rt = []
_ready_3_allKeys = []
# keep track of which components have finished
child_instruct3Components = [ready_3, image_8]
for thisComponent in child_instruct3Components:
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

# --- Run Routine "child_instruct3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_3* updates
    waitOnFlip = False
    if ready_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_3.frameNStart = frameN  # exact frame index
        ready_3.tStart = t  # local t and not account for scr refresh
        ready_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready_3.started')
        ready_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready_3.status == STARTED and not waitOnFlip:
        theseKeys = ready_3.getKeys(keyList=None, waitRelease=False)
        _ready_3_allKeys.extend(theseKeys)
        if len(_ready_3_allKeys):
            ready_3.keys = _ready_3_allKeys[-1].name  # just the last key pressed
            ready_3.rt = _ready_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct3" ---
for thisComponent in child_instruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready_3.keys in ['', [], None]:  # No response was made
    ready_3.keys = None
thisExp.addData('ready_3.keys',ready_3.keys)
if ready_3.keys != None:  # we had a response
    thisExp.addData('ready_3.rt', ready_3.rt)
thisExp.nextEntry()
# the Routine "child_instruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_C.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_03" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic_3.setImage(locat)
    response_3.keys = []
    response_3.rt = []
    _response_3_allKeys = []
    # keep track of which components have finished
    trial_03Components = [target_pic_3, response_3]
    for thisComponent in trial_03Components:
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
    
    # --- Run Routine "trial_03" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic_3* updates
        if target_pic_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic_3.frameNStart = frameN  # exact frame index
            target_pic_3.tStart = t  # local t and not account for scr refresh
            target_pic_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic_3.started')
            target_pic_3.setAutoDraw(True)
        if target_pic_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic_3.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic_3.tStop = t  # not accounting for scr refresh
                target_pic_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic_3.stopped')
                target_pic_3.setAutoDraw(False)
        
        # *response_3* updates
        waitOnFlip = False
        if response_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_3.frameNStart = frameN  # exact frame index
            response_3.tStart = t  # local t and not account for scr refresh
            response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_3.started')
            response_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_3.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_3.tStop = t  # not accounting for scr refresh
                response_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_3.stopped')
                response_3.status = FINISHED
        if response_3.status == STARTED and not waitOnFlip:
            theseKeys = response_3.getKeys(keyList=['space'], waitRelease=False)
            _response_3_allKeys.extend(theseKeys)
            if len(_response_3_allKeys):
                response_3.keys = _response_3_allKeys[-1].name  # just the last key pressed
                response_3.rt = _response_3_allKeys[-1].rt
                # was this correct?
                if (response_3.keys == str(corrAns)) or (response_3.keys == corrAns):
                    response_3.corr = 1
                else:
                    response_3.corr = 0
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
        for thisComponent in trial_03Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_03" ---
    for thisComponent in trial_03Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_3.keys in ['', [], None]:  # No response was made
        response_3.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_3.corr = 1;  # correct non-response
        else:
           response_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('response_3.keys',response_3.keys)
    trials_5.addData('response_3.corr', response_3.corr)
    if response_3.keys != None:  # we had a response
        trials_5.addData('response_3.rt', response_3.rt)
    # Run 'End Routine' code from code_3
    corr_3.append(response_3.corr)
    rts_3.append(response_3.rt)
    keys_3.append(response_3.keys)
    
    
    if len(corr_3) == 12  :
        print(len(corr_3),keys_3)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr_3)):
            if corr_3[i] == 1 and keys_3[i] == "space":
                rts_value += rts_3[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr_3)/len(corr_3))+"\n\n\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续实验。"
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_5.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_5.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_5'


# --- Prepare to start Routine "child_instruct4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready_4.keys = []
ready_4.rt = []
_ready_4_allKeys = []
# keep track of which components have finished
child_instruct4Components = [ready_4, image_7]
for thisComponent in child_instruct4Components:
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

# --- Run Routine "child_instruct4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_4* updates
    waitOnFlip = False
    if ready_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_4.frameNStart = frameN  # exact frame index
        ready_4.tStart = t  # local t and not account for scr refresh
        ready_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready_4.started')
        ready_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready_4.status == STARTED and not waitOnFlip:
        theseKeys = ready_4.getKeys(keyList=None, waitRelease=False)
        _ready_4_allKeys.extend(theseKeys)
        if len(_ready_4_allKeys):
            ready_4.keys = _ready_4_allKeys[-1].name  # just the last key pressed
            ready_4.rt = _ready_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct4" ---
for thisComponent in child_instruct4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready_4.keys in ['', [], None]:  # No response was made
    ready_4.keys = None
thisExp.addData('ready_4.keys',ready_4.keys)
if ready_4.keys != None:  # we had a response
    thisExp.addData('ready_4.rt', ready_4.rt)
thisExp.nextEntry()
# the Routine "child_instruct4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_D.xlsx'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_04" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic_4.setImage(locat)
    response_4.keys = []
    response_4.rt = []
    _response_4_allKeys = []
    # keep track of which components have finished
    trial_04Components = [target_pic_4, response_4]
    for thisComponent in trial_04Components:
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
    
    # --- Run Routine "trial_04" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic_4* updates
        if target_pic_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic_4.frameNStart = frameN  # exact frame index
            target_pic_4.tStart = t  # local t and not account for scr refresh
            target_pic_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic_4.started')
            target_pic_4.setAutoDraw(True)
        if target_pic_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic_4.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic_4.tStop = t  # not accounting for scr refresh
                target_pic_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic_4.stopped')
                target_pic_4.setAutoDraw(False)
        
        # *response_4* updates
        waitOnFlip = False
        if response_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_4.frameNStart = frameN  # exact frame index
            response_4.tStart = t  # local t and not account for scr refresh
            response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_4.started')
            response_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_4.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_4.tStop = t  # not accounting for scr refresh
                response_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_4.stopped')
                response_4.status = FINISHED
        if response_4.status == STARTED and not waitOnFlip:
            theseKeys = response_4.getKeys(keyList=['space'], waitRelease=False)
            _response_4_allKeys.extend(theseKeys)
            if len(_response_4_allKeys):
                response_4.keys = _response_4_allKeys[-1].name  # just the last key pressed
                response_4.rt = _response_4_allKeys[-1].rt
                # was this correct?
                if (response_4.keys == str(corrAns)) or (response_4.keys == corrAns):
                    response_4.corr = 1
                else:
                    response_4.corr = 0
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
        for thisComponent in trial_04Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_04" ---
    for thisComponent in trial_04Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_4.keys in ['', [], None]:  # No response was made
        response_4.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_4.corr = 1;  # correct non-response
        else:
           response_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('response_4.keys',response_4.keys)
    trials_6.addData('response_4.corr', response_4.corr)
    if response_4.keys != None:  # we had a response
        trials_6.addData('response_4.rt', response_4.rt)
    # Run 'End Routine' code from code_4
    corr_4.append(response_4.corr)
    rts_4.append(response_4.rt)
    keys_4.append(response_4.keys)
    
    if len(corr_4) == 12  :
        print(len(corr_4),keys_4)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr_4)):
            if corr_4[i] == 1 and keys_4[i] == "space":
                rts_value += rts_4[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr_4)/len(corr_4))+"\n\n\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续实验。"
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_6.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_6.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_6'


# --- Prepare to start Routine "child_instruct5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready_5.keys = []
ready_5.rt = []
_ready_5_allKeys = []
# keep track of which components have finished
child_instruct5Components = [ready_5, image_6]
for thisComponent in child_instruct5Components:
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

# --- Run Routine "child_instruct5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_5* updates
    waitOnFlip = False
    if ready_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_5.frameNStart = frameN  # exact frame index
        ready_5.tStart = t  # local t and not account for scr refresh
        ready_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready_5.started')
        ready_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready_5.status == STARTED and not waitOnFlip:
        theseKeys = ready_5.getKeys(keyList=None, waitRelease=False)
        _ready_5_allKeys.extend(theseKeys)
        if len(_ready_5_allKeys):
            ready_5.keys = _ready_5_allKeys[-1].name  # just the last key pressed
            ready_5.rt = _ready_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct5" ---
for thisComponent in child_instruct5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready_5.keys in ['', [], None]:  # No response was made
    ready_5.keys = None
thisExp.addData('ready_5.keys',ready_5.keys)
if ready_5.keys != None:  # we had a response
    thisExp.addData('ready_5.rt', ready_5.rt)
thisExp.nextEntry()
# the Routine "child_instruct5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_E.xlsx'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_05" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic_5.setImage(locat)
    response_5.keys = []
    response_5.rt = []
    _response_5_allKeys = []
    # keep track of which components have finished
    trial_05Components = [target_pic_5, response_5]
    for thisComponent in trial_05Components:
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
    
    # --- Run Routine "trial_05" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic_5* updates
        if target_pic_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic_5.frameNStart = frameN  # exact frame index
            target_pic_5.tStart = t  # local t and not account for scr refresh
            target_pic_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic_5.started')
            target_pic_5.setAutoDraw(True)
        if target_pic_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic_5.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic_5.tStop = t  # not accounting for scr refresh
                target_pic_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic_5.stopped')
                target_pic_5.setAutoDraw(False)
        
        # *response_5* updates
        waitOnFlip = False
        if response_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_5.frameNStart = frameN  # exact frame index
            response_5.tStart = t  # local t and not account for scr refresh
            response_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_5.started')
            response_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_5.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_5.tStop = t  # not accounting for scr refresh
                response_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_5.stopped')
                response_5.status = FINISHED
        if response_5.status == STARTED and not waitOnFlip:
            theseKeys = response_5.getKeys(keyList=['space'], waitRelease=False)
            _response_5_allKeys.extend(theseKeys)
            if len(_response_5_allKeys):
                response_5.keys = _response_5_allKeys[-1].name  # just the last key pressed
                response_5.rt = _response_5_allKeys[-1].rt
                # was this correct?
                if (response_5.keys == str(corrAns)) or (response_5.keys == corrAns):
                    response_5.corr = 1
                else:
                    response_5.corr = 0
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
        for thisComponent in trial_05Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_05" ---
    for thisComponent in trial_05Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_5.keys in ['', [], None]:  # No response was made
        response_5.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_5.corr = 1;  # correct non-response
        else:
           response_5.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('response_5.keys',response_5.keys)
    trials_7.addData('response_5.corr', response_5.corr)
    if response_5.keys != None:  # we had a response
        trials_7.addData('response_5.rt', response_5.rt)
    # Run 'End Routine' code from code_5
    corr_5.append(response_5.corr)
    rts_5.append(response_5.rt)
    keys_5.append(response_5.keys)
    
    
    if len(corr_5) == 12  :
        print(len(corr_5),keys_5)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr_5)):
            if corr_5[i] == 1 and keys_5[i] == "space":
                rts_value += rts_5[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr_5)/len(corr_5))+"\n\n\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续实验。"
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_7.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_7.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_7'


# --- Prepare to start Routine "child_instruct6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready_6.keys = []
ready_6.rt = []
_ready_6_allKeys = []
# keep track of which components have finished
child_instruct6Components = [ready_6, image_5]
for thisComponent in child_instruct6Components:
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

# --- Run Routine "child_instruct6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_6* updates
    waitOnFlip = False
    if ready_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_6.frameNStart = frameN  # exact frame index
        ready_6.tStart = t  # local t and not account for scr refresh
        ready_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready_6.started')
        ready_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready_6.status == STARTED and not waitOnFlip:
        theseKeys = ready_6.getKeys(keyList=None, waitRelease=False)
        _ready_6_allKeys.extend(theseKeys)
        if len(_ready_6_allKeys):
            ready_6.keys = _ready_6_allKeys[-1].name  # just the last key pressed
            ready_6.rt = _ready_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in child_instruct6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "child_instruct6" ---
for thisComponent in child_instruct6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready_6.keys in ['', [], None]:  # No response was made
    ready_6.keys = None
thisExp.addData('ready_6.keys',ready_6.keys)
if ready_6.keys != None:  # we had a response
    thisExp.addData('ready_6.rt', ready_6.rt)
thisExp.nextEntry()
# the Routine "child_instruct6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_F.xlsx'),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "add_signal" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    add_signalComponents = [pre_3]
    for thisComponent in add_signalComponents:
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
    
    # --- Run Routine "add_signal" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_3* updates
        if pre_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pre_3.frameNStart = frameN  # exact frame index
            pre_3.tStart = t  # local t and not account for scr refresh
            pre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pre_3.started')
            pre_3.setAutoDraw(True)
        if pre_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pre_3.tStop = t  # not accounting for scr refresh
                pre_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pre_3.stopped')
                pre_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in add_signalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "add_signal" ---
    for thisComponent in add_signalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "trial_06" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target_pic_6.setImage(locat)
    response_6.keys = []
    response_6.rt = []
    _response_6_allKeys = []
    # keep track of which components have finished
    trial_06Components = [target_pic_6, response_6]
    for thisComponent in trial_06Components:
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
    
    # --- Run Routine "trial_06" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_pic_6* updates
        if target_pic_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target_pic_6.frameNStart = frameN  # exact frame index
            target_pic_6.tStart = t  # local t and not account for scr refresh
            target_pic_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_pic_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_pic_6.started')
            target_pic_6.setAutoDraw(True)
        if target_pic_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_pic_6.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target_pic_6.tStop = t  # not accounting for scr refresh
                target_pic_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_pic_6.stopped')
                target_pic_6.setAutoDraw(False)
        
        # *response_6* updates
        waitOnFlip = False
        if response_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_6.frameNStart = frameN  # exact frame index
            response_6.tStart = t  # local t and not account for scr refresh
            response_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_6.started')
            response_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_6.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                response_6.tStop = t  # not accounting for scr refresh
                response_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_6.stopped')
                response_6.status = FINISHED
        if response_6.status == STARTED and not waitOnFlip:
            theseKeys = response_6.getKeys(keyList=['space'], waitRelease=False)
            _response_6_allKeys.extend(theseKeys)
            if len(_response_6_allKeys):
                response_6.keys = _response_6_allKeys[-1].name  # just the last key pressed
                response_6.rt = _response_6_allKeys[-1].rt
                # was this correct?
                if (response_6.keys == str(corrAns)) or (response_6.keys == corrAns):
                    response_6.corr = 1
                else:
                    response_6.corr = 0
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
        for thisComponent in trial_06Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_06" ---
    for thisComponent in trial_06Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_6.keys in ['', [], None]:  # No response was made
        response_6.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_6.corr = 1;  # correct non-response
        else:
           response_6.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_8 (TrialHandler)
    trials_8.addData('response_6.keys',response_6.keys)
    trials_8.addData('response_6.corr', response_6.corr)
    if response_6.keys != None:  # we had a response
        trials_8.addData('response_6.rt', response_6.rt)
    # Run 'End Routine' code from code_6
    
    corr_6.append(response_6.corr)
    rts_6.append(response_6.rt)
    keys_6.append(response_6.keys)
    
    
    if len(corr_6) == 12  :
        print(len(corr_6),keys_6)
        time =  10
        rts_value = 0
        effect = 0
        for i in range(len(corr_6)):
            if corr_6[i] == 1 and keys_6[i] == "space":
                rts_value += rts_6[i]
                effect += 1
        msge = "你的准确率为:" + str(sum(corr_6)/len(corr_6))+"\n\n\n\n你的平均反应时为: "+str(rts_value/effect)+".\n\n请按任意键以继续实验。"
    else:
        time = 0.0
        msge = ""
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "feedback_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText(msge)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    feedback_trialComponents = [text_3, key_resp_3]
    for thisComponent in feedback_trialComponents:
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
    
    # --- Run Routine "feedback_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
        for thisComponent in feedback_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_trial" ---
    for thisComponent in feedback_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_8.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_8.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "feedback_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_8'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
thanksComponents = [end_heading_2, key_resp_7]
for thisComponent in thanksComponents:
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

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 8.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_heading_2* updates
    if end_heading_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_heading_2.frameNStart = frameN  # exact frame index
        end_heading_2.tStart = t  # local t and not account for scr refresh
        end_heading_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_heading_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_heading_2.started')
        end_heading_2.setAutoDraw(True)
    if end_heading_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_heading_2.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            end_heading_2.tStop = t  # not accounting for scr refresh
            end_heading_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_heading_2.stopped')
            end_heading_2.setAutoDraw(False)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_7.started')
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_7.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_7.tStop = t  # not accounting for scr refresh
            key_resp_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
            key_resp_7.status = FINISHED
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=None, waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
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
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-8.000000)

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
