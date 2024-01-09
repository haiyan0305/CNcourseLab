#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on January 09, 2024, at 14:30
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
expName = 'IAT'  # from the Builder filename that created this script
expInfo = {
    '请填写您的姓名：': '',
    '请填写您的学号：': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['请填写您的姓名：'], expInfo['请填写您的学号：'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\CourseLab\\CNcourseLab\\Lab6_IAT\\IAT_lastrun.py',
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
    size=[1607, 930], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
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

# --- Initialize components for Routine "IAT_Instruction" ---
# Run 'Begin Experiment' code from blocks_order_code
blocks_order = str(int(random()*2+1))
IAT_instr_image = visual.ImageStim(
    win=win,
    name='IAT_instr_image', units='height', 
    image='materials/instruction.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
IAT_instr_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "upper_hint" ---
upper_hint_image = visual.ImageStim(
    win=win,
    name='upper_hint_image', 
    image='materials/upper_hint.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.778,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Step_Instruction" ---
# Run 'Begin Experiment' code from code_nstep
nStep = 0


instr_image = visual.ImageStim(
    win=win,
    name='instr_image', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
nstep_text = visual.TextStim(win=win, name='nstep_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Blank" ---
blank_text = visual.TextStim(win=win, name='blank_text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Trial" ---
# Run 'Begin Experiment' code from interval_time_code
corr_record = []
rt_record = []


interval_time_list = [0.1, 0.4, 0.7]
trial_test_background_img = visual.ImageStim(
    win=win,
    name='trial_test_background_img', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
stimuli_text = visual.TextStim(win=win, name='stimuli_text',
    text='',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
response = keyboard.Keyboard()

# --- Initialize components for Routine "Trial_Feedback" ---
error_feedback_img = visual.ImageStim(
    win=win,
    name='error_feedback_img', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
error_feedback_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Condition_Feedback" ---
condition_feedback_background_img = visual.ImageStim(
    win=win,
    name='condition_feedback_background_img', units='height', 
    image='materials/condition_feedback_background.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
condition_feedback_resp = keyboard.Keyboard()

# --- Initialize components for Routine "End" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='测试结束！感谢您的参与！',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_image = visual.ImageStim(
    win=win,
    name='end_image', units='height', 
    image='materials/IAT_code.jpg', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1.778, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
end_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "IAT_Instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from blocks_order_code
cfile = 'conditions/conditions' +blocks_order+ '.xlsx'
IAT_instr_key_resp.keys = []
IAT_instr_key_resp.rt = []
_IAT_instr_key_resp_allKeys = []
# keep track of which components have finished
IAT_InstructionComponents = [IAT_instr_image, IAT_instr_key_resp]
for thisComponent in IAT_InstructionComponents:
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

# --- Run Routine "IAT_Instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAT_instr_image* updates
    if IAT_instr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAT_instr_image.frameNStart = frameN  # exact frame index
        IAT_instr_image.tStart = t  # local t and not account for scr refresh
        IAT_instr_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAT_instr_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAT_instr_image.started')
        IAT_instr_image.setAutoDraw(True)
    
    # *IAT_instr_key_resp* updates
    waitOnFlip = False
    if IAT_instr_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAT_instr_key_resp.frameNStart = frameN  # exact frame index
        IAT_instr_key_resp.tStart = t  # local t and not account for scr refresh
        IAT_instr_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAT_instr_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAT_instr_key_resp.started')
        IAT_instr_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAT_instr_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAT_instr_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAT_instr_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = IAT_instr_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _IAT_instr_key_resp_allKeys.extend(theseKeys)
        if len(_IAT_instr_key_resp_allKeys):
            IAT_instr_key_resp.keys = _IAT_instr_key_resp_allKeys[-1].name  # just the last key pressed
            IAT_instr_key_resp.rt = _IAT_instr_key_resp_allKeys[-1].rt
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
    for thisComponent in IAT_InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAT_Instruction" ---
for thisComponent in IAT_InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IAT_instr_key_resp.keys in ['', [], None]:  # No response was made
    IAT_instr_key_resp.keys = None
thisExp.addData('IAT_instr_key_resp.keys',IAT_instr_key_resp.keys)
if IAT_instr_key_resp.keys != None:  # we had a response
    thisExp.addData('IAT_instr_key_resp.rt', IAT_instr_key_resp.rt)
thisExp.nextEntry()
# the Routine "IAT_Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "upper_hint" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
upper_hintComponents = [upper_hint_image]
for thisComponent in upper_hintComponents:
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

# --- Run Routine "upper_hint" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *upper_hint_image* updates
    if upper_hint_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        upper_hint_image.frameNStart = frameN  # exact frame index
        upper_hint_image.tStart = t  # local t and not account for scr refresh
        upper_hint_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(upper_hint_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'upper_hint_image.started')
        upper_hint_image.setAutoDraw(True)
    if upper_hint_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > upper_hint_image.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            upper_hint_image.tStop = t  # not accounting for scr refresh
            upper_hint_image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'upper_hint_image.stopped')
            upper_hint_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in upper_hintComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "upper_hint" ---
for thisComponent in upper_hintComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cfile),
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
    
    # --- Prepare to start Routine "Step_Instruction" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_nstep
    nStep += 1
    
    nstep_msg = f'第{nStep}轮'
    
    print(step_order_filename)
    
    instr_image.setImage(step_instruction_filename)
    nstep_text.setText(nstep_msg)
    instr_key_resp.keys = []
    instr_key_resp.rt = []
    _instr_key_resp_allKeys = []
    # keep track of which components have finished
    Step_InstructionComponents = [instr_image, nstep_text, instr_key_resp]
    for thisComponent in Step_InstructionComponents:
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
    
    # --- Run Routine "Step_Instruction" ---
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
        
        # *nstep_text* updates
        if nstep_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nstep_text.frameNStart = frameN  # exact frame index
            nstep_text.tStart = t  # local t and not account for scr refresh
            nstep_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nstep_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nstep_text.started')
            nstep_text.setAutoDraw(True)
        
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
        for thisComponent in Step_InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Step_Instruction" ---
    for thisComponent in Step_InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instr_key_resp.keys in ['', [], None]:  # No response was made
        instr_key_resp.keys = None
    blocks.addData('instr_key_resp.keys',instr_key_resp.keys)
    if instr_key_resp.keys != None:  # we had a response
        blocks.addData('instr_key_resp.rt', instr_key_resp.rt)
    # the Routine "Step_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankComponents = [blank_text]
    for thisComponent in BlankComponents:
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
    
    # --- Run Routine "Blank" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_text* updates
        if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_text.frameNStart = frameN  # exact frame index
            blank_text.tStart = t  # local t and not account for scr refresh
            blank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_text.started')
            blank_text.setAutoDraw(True)
        if blank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_text.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_text.tStop = t  # not accounting for scr refresh
                blank_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_text.stopped')
                blank_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Blank" ---
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(step_order_filename),
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
        
        # --- Prepare to start Routine "Trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from interval_time_code
        
        shuffle(interval_time_list)
        interval_time = interval_time_list[0]
        print(stimuli_words)
        trial_test_background_img.setImage(step_background_filename)
        stimuli_text.setText(stimuli_words)
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        TrialComponents = [trial_test_background_img, stimuli_text, response]
        for thisComponent in TrialComponents:
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
        
        # --- Run Routine "Trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_test_background_img* updates
            if trial_test_background_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_test_background_img.frameNStart = frameN  # exact frame index
                trial_test_background_img.tStart = t  # local t and not account for scr refresh
                trial_test_background_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_test_background_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_test_background_img.started')
                trial_test_background_img.setAutoDraw(True)
            
            # *stimuli_text* updates
            if stimuli_text.status == NOT_STARTED and tThisFlip >= interval_time-frameTolerance:
                # keep track of start time/frame for later
                stimuli_text.frameNStart = frameN  # exact frame index
                stimuli_text.tStart = t  # local t and not account for scr refresh
                stimuli_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_text.started')
                stimuli_text.setAutoDraw(True)
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= interval_time-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response.started')
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['e','i'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(CorrAns)) or (response.keys == CorrAns):
                        response.corr = 1
                    else:
                        response.corr = 0
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
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial" ---
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from interval_time_code
        corr_record.append(response.corr)
        rt_record.append(response.rt)
        thisExp.addData('response.interval_time', interval_time)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('response.keys',response.keys)
        trials.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        error_feedback_img.setImage(step_error_filename)
        error_feedback_resp.keys = []
        error_feedback_resp.rt = []
        _error_feedback_resp_allKeys = []
        # Run 'Begin Routine' code from trial_feedback_code
        print('MSG', error_feedback_resp.corr, error_feedback_resp.keys, CorrAns, error_feedback_resp.keys == CorrAns)
        
        
        
        # keep track of which components have finished
        Trial_FeedbackComponents = [error_feedback_img, error_feedback_resp]
        for thisComponent in Trial_FeedbackComponents:
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
        
        # --- Run Routine "Trial_Feedback" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *error_feedback_img* updates
            if error_feedback_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                error_feedback_img.frameNStart = frameN  # exact frame index
                error_feedback_img.tStart = t  # local t and not account for scr refresh
                error_feedback_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(error_feedback_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'error_feedback_img.started')
                error_feedback_img.setAutoDraw(True)
            
            # *error_feedback_resp* updates
            waitOnFlip = False
            if error_feedback_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                error_feedback_resp.frameNStart = frameN  # exact frame index
                error_feedback_resp.tStart = t  # local t and not account for scr refresh
                error_feedback_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(error_feedback_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'error_feedback_resp.started')
                error_feedback_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(error_feedback_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(error_feedback_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if error_feedback_resp.status == STARTED and not waitOnFlip:
                theseKeys = error_feedback_resp.getKeys(keyList=['e','i'], waitRelease=False)
                _error_feedback_resp_allKeys.extend(theseKeys)
                if len(_error_feedback_resp_allKeys):
                    error_feedback_resp.keys = _error_feedback_resp_allKeys[-1].name  # just the last key pressed
                    error_feedback_resp.rt = _error_feedback_resp_allKeys[-1].rt
                    # was this correct?
                    if (error_feedback_resp.keys == str(CorrAns)) or (error_feedback_resp.keys == CorrAns):
                        error_feedback_resp.corr = 1
                    else:
                        error_feedback_resp.corr = 0
            # Run 'Each Frame' code from trial_feedback_code
            if (not need_feedback) or (response.corr):
                continueRoutine = False
            
            if error_feedback_resp.keys == CorrAns:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Feedback" ---
        for thisComponent in Trial_FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if error_feedback_resp.keys in ['', [], None]:  # No response was made
            error_feedback_resp.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               error_feedback_resp.corr = 1;  # correct non-response
            else:
               error_feedback_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('error_feedback_resp.keys',error_feedback_resp.keys)
        trials.addData('error_feedback_resp.corr', error_feedback_resp.corr)
        if error_feedback_resp.keys != None:  # we had a response
            trials.addData('error_feedback_resp.rt', error_feedback_resp.rt)
        # the Routine "Trial_Feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Condition_Feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from condition_feedback_code
    
    average_corr = sum(corr_record) / len(corr_record) * 100
    average_rt = sum(rt_record) / len(rt_record)
    
    corr_feedback_message = f'这一轮你的正确率为：{round(average_corr, 2)}%'
    rt_corr_feedback_message = f'这一轮你的平均反应时间为：{round(average_rt, 2)} 秒'
     
    feedback_message = f'{corr_feedback_message}\n{rt_corr_feedback_message}'
    corr_record = [] # 这一轮结束后，将这一轮存储的corr信息清零
    rt_record = []   # 这一轮结束后，将这一轮存储的rt信息清零
    feedback_text.setText(feedback_message)
    condition_feedback_resp.keys = []
    condition_feedback_resp.rt = []
    _condition_feedback_resp_allKeys = []
    # keep track of which components have finished
    Condition_FeedbackComponents = [condition_feedback_background_img, feedback_text, condition_feedback_resp]
    for thisComponent in Condition_FeedbackComponents:
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
    
    # --- Run Routine "Condition_Feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *condition_feedback_background_img* updates
        if condition_feedback_background_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_feedback_background_img.frameNStart = frameN  # exact frame index
            condition_feedback_background_img.tStart = t  # local t and not account for scr refresh
            condition_feedback_background_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_feedback_background_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition_feedback_background_img.started')
            condition_feedback_background_img.setAutoDraw(True)
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            feedback_text.setAutoDraw(True)
        
        # *condition_feedback_resp* updates
        waitOnFlip = False
        if condition_feedback_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_feedback_resp.frameNStart = frameN  # exact frame index
            condition_feedback_resp.tStart = t  # local t and not account for scr refresh
            condition_feedback_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_feedback_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition_feedback_resp.started')
            condition_feedback_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(condition_feedback_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(condition_feedback_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if condition_feedback_resp.status == STARTED and not waitOnFlip:
            theseKeys = condition_feedback_resp.getKeys(keyList=['space'], waitRelease=False)
            _condition_feedback_resp_allKeys.extend(theseKeys)
            if len(_condition_feedback_resp_allKeys):
                condition_feedback_resp.keys = _condition_feedback_resp_allKeys[-1].name  # just the last key pressed
                condition_feedback_resp.rt = _condition_feedback_resp_allKeys[-1].rt
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
        for thisComponent in Condition_FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Condition_Feedback" ---
    for thisComponent in Condition_FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if condition_feedback_resp.keys in ['', [], None]:  # No response was made
        condition_feedback_resp.keys = None
    blocks.addData('condition_feedback_resp.keys',condition_feedback_resp.keys)
    if condition_feedback_resp.keys != None:  # we had a response
        blocks.addData('condition_feedback_resp.rt', condition_feedback_resp.rt)
    # the Routine "Condition_Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'blocks'

# get names of stimulus parameters
if blocks.trialList in ([], [None], None):
    params = []
else:
    params = blocks.trialList[0].keys()
# save data for this loop
blocks.saveAsExcel(filename + '.xlsx', sheetName='blocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_key_resp.keys = []
end_key_resp.rt = []
_end_key_resp_allKeys = []
# keep track of which components have finished
EndComponents = [end_text, end_image, end_key_resp]
for thisComponent in EndComponents:
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

# --- Run Routine "End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_text.started')
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.stopped')
            end_text.setAutoDraw(False)
    
    # *end_image* updates
    if end_image.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        end_image.frameNStart = frameN  # exact frame index
        end_image.tStart = t  # local t and not account for scr refresh
        end_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_image.started')
        end_image.setAutoDraw(True)
    
    # *end_key_resp* updates
    waitOnFlip = False
    if end_key_resp.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_key_resp.keys in ['', [], None]:  # No response was made
    end_key_resp.keys = None
thisExp.addData('end_key_resp.keys',end_key_resp.keys)
if end_key_resp.keys != None:  # we had a response
    thisExp.addData('end_key_resp.rt', end_key_resp.rt)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
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
