#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sat Sep  2 13:26:58 2023
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
psychopyVersion = '2022.2.5'
expName = 'TimeProductionTask'  # from the Builder filename that created this script
expInfo = {
    'Subject ID (###)': '',
    'Session Condition (A or NA)': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'TPTdata/%s_%s_TPT' % (expInfo['Subject ID (###)'], expInfo['Session Condition (A or NA)'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/xiao/Documents/Study 1.2/PsychoPy/TimeProductionTask.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# --- Initialize components for Routine "Instructions" ---
insText = visual.TextStim(win=win, name='insText',
    text='This is a time perception task. You will be given several time intervals (ie. 5 seconds), and asked to push a button to start and end a timer when you think the time has elapsed.\n\nRemember DO NOT count the seconds. The purpose of this task is not to be "correct". Rather, we want to know how fast or slow time passes for YOU. There are no right or wrong answers.\n\nThere will be 9 rounds total.\n\nClick the NEXT button to continue.',
    font='Open Sans',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nextButton = visual.ButtonStim(win, 
    text='NEXT', font='Arvo',
    pos=(0, -.27),
    letterHeight=0.03,
    size=(.18,.1), borderWidth=0.0,
    fillColor=[-1.0000, -1.0000, 1.0000], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='nextButton'
)
nextButton.buttonClock = core.Clock()

# --- Initialize components for Routine "start_trial" ---
start_text = visual.TextStim(win=win, name='start_text',
    text='',
    font='Open Sans',
    pos=(0, .05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startButton = visual.ButtonStim(win, 
    text='START', font='Arvo',
    pos=(-0.2, -0.20),
    letterHeight=0.03,
    size=(.18, .1), borderWidth=0.0,
    fillColor='green', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='startButton'
)
startButton.buttonClock = core.Clock()

# --- Initialize components for Routine "end_trial" ---
promptText = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, .05),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='promptText',
     autoLog=True,
)
endButton = visual.ButtonStim(win, 
    text='END', font='Arvo',
    pos=(0.2, -0.20),
    letterHeight=0.03,
    size=(.18, .1), borderWidth=0.0,
    fillColor='red', borderColor='red',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='endButton'
)
endButton.buttonClock = core.Clock()

# --- Initialize components for Routine "close" ---
endText = visual.TextStim(win=win, name='endText',
    text='Thank you. You have reached the end of the task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endMouse = event.Mouse(win=win)
x, y = [None, None]
endMouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = [insText, nextButton]
for thisComponent in InstructionsComponents:
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

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insText* updates
    if insText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insText.frameNStart = frameN  # exact frame index
        insText.tStart = t  # local t and not account for scr refresh
        insText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insText, 'tStartRefresh')  # time at next scr refresh
        insText.setAutoDraw(True)
    
    # *nextButton* updates
    if nextButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        nextButton.frameNStart = frameN  # exact frame index
        nextButton.tStart = t  # local t and not account for scr refresh
        nextButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton, 'tStartRefresh')  # time at next scr refresh
        nextButton.setAutoDraw(True)
    if nextButton.status == STARTED:
        # check whether nextButton has been pressed
        if nextButton.isClicked:
            if not nextButton.wasClicked:
                nextButton.timesOn.append(nextButton.buttonClock.getTime()) # store time of first click
                nextButton.timesOff.append(nextButton.buttonClock.getTime()) # store time clicked until
            else:
                nextButton.timesOff[-1] = nextButton.buttonClock.getTime() # update time clicked until
            if not nextButton.wasClicked:
                continueRoutine = False  # end routine when nextButton is clicked
                None
            nextButton.wasClicked = True  # if nextButton is still clicked next frame, it is not a new click
        else:
            nextButton.wasClicked = False  # if nextButton is clicked next frame, it is a new click
    else:
        nextButton.wasClicked = False  # if nextButton is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
timeInt = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/xiao/Documents/Study 1.2/PsychoPy/intervals_loop.xlsx'),
    seed=None, name='timeInt')
thisExp.addLoop(timeInt)  # add the loop to the experiment
thisTimeInt = timeInt.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTimeInt.rgb)
if thisTimeInt != None:
    for paramName in thisTimeInt:
        exec('{} = thisTimeInt[paramName]'.format(paramName))

for thisTimeInt in timeInt:
    print(thisTimeInt)
    # abbreviate parameter names if possible (e.g. rgb = thisTimeInt.rgb)
    if thisTimeInt != None:
        for paramName in thisTimeInt:
            exec('{} = thisTimeInt[paramName]'.format(paramName))
    
    currentInterval = thisTimeInt[paramName]
    
    # --- Prepare to start Routine "start_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    start_text.setText(f'Please estimate {currentInterval} seconds. The timer will begin when you click START and it will end when you click END. Click START when you are ready to begin the clock.')
    # keep track of which components have finished
    start_trialComponents = [start_text, startButton]
    for thisComponent in start_trialComponents:
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
    
    # --- Run Routine "start_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_text* updates
        if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_text.frameNStart = frameN  # exact frame index
            start_text.tStart = t  # local t and not account for scr refresh
            start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
            start_text.setAutoDraw(True)
        
        # *startButton* updates
        if startButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            startButton.frameNStart = frameN  # exact frame index
            startButton.tStart = t  # local t and not account for scr refresh
            startButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startButton, 'tStartRefresh')  # time at next scr refresh
            startButton.setAutoDraw(True)
        if startButton.status == STARTED:
            # check whether startButton has been pressed
            if startButton.isClicked:
                if not startButton.wasClicked:
                    startTime = globalClock.getTime() # store time since start of exp
                else:
                    startButton.timesOff[-1] = globalClock.getTime() # update time clicked until
                if not startButton.wasClicked:
                    continueRoutine = False  # end routine when startButton is clicked
                    None
                startButton.wasClicked = True  # if startButton is still clicked next frame, it is not a new click
            else:
                startButton.wasClicked = False  # if startButton is clicked next frame, it is a new click
        else:
            startButton.wasClicked = False  # if startButton is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_trial" ---
    for thisComponent in start_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #timeInt.addData('startButton.numClicks', startButton.numClicks)
    timeInt.addData('startTime', startTime)
    routineTimer.reset()
    
    # --- Prepare to start Routine "end_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    promptText.reset()
    promptText.setText(f'Click END when you think {currentInterval} seconds has elapsed.')
    # keep track of which components have finished
    end_trialComponents = [promptText, endButton]
    for thisComponent in end_trialComponents:
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
    
    # --- Run Routine "end_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *promptText* updates
        if promptText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            promptText.frameNStart = frameN  # exact frame index
            promptText.tStart = t  # local t and not account for scr refresh
            promptText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(promptText, 'tStartRefresh')  # time at next scr refresh
            promptText.setAutoDraw(True)
        
        # *endButton* updates
        if endButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            endButton.frameNStart = frameN  # exact frame index
            endButton.tStart = t  # local t and not account for scr refresh
            endButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endButton, 'tStartRefresh')  # time at next scr refresh
            endButton.setAutoDraw(True)
        if endButton.status == STARTED:
            # check whether endButton has been pressed
            if endButton.isClicked:
                if not endButton.wasClicked:
                    endTime = globalClock.getTime() # store time relative to start of experiment
                else:
                    endButton.timesOff[-1] = globalClock.getTime() # update time clicked until
                if not endButton.wasClicked:
                    continueRoutine = False  # end routine when endButton is clicked
                    None
                endButton.wasClicked = True  # if endButton is still clicked next frame, it is not a new click
            else:
                endButton.wasClicked = False  # if endButton is clicked next frame, it is a new click
        else:
            endButton.wasClicked = False  # if endButton is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_trial" ---
    for thisComponent in end_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    timeInt.addData('endTime', endTime)
    prodTime = endTime - startTime
    errorProp = (prodTime - currentInterval)/currentInterval
    timeInt.addData('prodTime', prodTime)
    timeInt.addData('errorProportion', errorProp)
    # the Routine "end_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'timeInt'


# --- Prepare to start Routine "close" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the endMouse
endMouse.x = []
endMouse.y = []
endMouse.leftButton = []
endMouse.midButton = []
endMouse.rightButton = []
endMouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
closeComponents = [endText, endMouse]
for thisComponent in closeComponents:
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

# --- Run Routine "close" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    # *endMouse* updates
    if endMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endMouse.frameNStart = frameN  # exact frame index
        endMouse.tStart = t  # local t and not account for scr refresh
        endMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endMouse, 'tStartRefresh')  # time at next scr refresh
        endMouse.status = STARTED
        endMouse.mouseClock.reset()
        prevButtonState = endMouse.getPressed()  # if button is down already this ISN'T a new click
    if endMouse.status == STARTED:  # only update if started and not finished!
        buttons = endMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = endMouse.getPos()
                endMouse.x.append(x)
                endMouse.y.append(y)
                buttons = endMouse.getPressed()
                endMouse.leftButton.append(buttons[0])
                endMouse.midButton.append(buttons[1])
                endMouse.rightButton.append(buttons[2])
                endMouse.time.append(endMouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in closeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "close" ---
for thisComponent in closeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()
# the Routine "close" was not non-slip safe, so reset the non-slip timer
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
