#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Sep  6 15:36:46 2023
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
expName = 'TimeEstimationTask'  # from the Builder filename that created this script
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
filename = _thisDir + os.sep + u'TETdata/%s_%s_TET' % (expInfo['Subject ID (###)'], expInfo['Session Condition (A or NA)'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/xiao/Documents/Study 1.2/PsychoPy/TimeEstimationTask.py',
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
    text='This is a time estimation task. On the next screen there will be a lightbulb that you can press a button to turn on. It will remain on for some period of time and we would like you to estimate how long. \n\nEnter the amount of time in SECONDS that you think the lightbulb was on. There will be 9 rounds with 9 different time periods. \n\nPlease DO NOT count the seconds. There are no right or wrong answers, we simply want to understand how time passes for YOU. \n\nClick anywhere on the screen to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
insMouse = event.Mouse(win=win)
x, y = [None, None]
insMouse.mouseClock = core.Clock()

# --- Initialize components for Routine "lightOn" ---
lightOffImg = visual.ImageStim(
    win=win,
    name='lightOffImg', 
    image='/Users/xiao/Documents/Study 1.2/lightOff.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
lightOnImg = visual.ImageStim(
    win=win,
    name='lightOnImg', 
    image='/Users/xiao/Documents/Study 1.2/lightOn.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
onButton = visual.ButtonStim(win, 
    text='ON', font='Arvo',
    pos=(0, -0.35),
    letterHeight=0.03,
    size=(.18,.06), borderWidth=0.0,
    fillColor='green', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='onButton'
)
onButton.buttonClock = core.Clock()
# Run 'Begin Experiment' code from code
myClock = core.Clock()

# --- Initialize components for Routine "timeEst" ---
estimateText = visual.TextStim(win=win, name='estimateText',
    text='Now estimate the \namount of time \nyou feel has passed \nand enter only the \nNUMBER in SECONDS \nin the field below. \n\nClick SUMBIT \nwhen you are done.',
    font='Open Sans',
    pos=(0.3, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
submitButton = visual.ButtonStim(win, 
    text='SUBMIT', font='Arvo',
    pos=(0.25, -0.35),
    letterHeight=0.03,
    size=(.18, .06), borderWidth=0.0,
    fillColor='red', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='submitButton'
)
submitButton.buttonClock = core.Clock()
lightOffImg_2 = visual.ImageStim(
    win=win,
    name='lightOffImg_2', 
    image='/Users/xiao/Documents/Study 1.2/lightOff.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
textEntry = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.35),     letterHeight=0.03,
     size=(.2, .08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textEntry',
     autoLog=True,
)
bell = sound.Sound('bell-ding.wav', secs=0.15, stereo=True, hamming=True,
    name='bell')
bell.setVolume(1.0)

# --- Initialize components for Routine "endScreen" ---
endText = visual.TextStim(win=win, name='endText',
    text='You have reached the end of the experiment. \n\nClick anwhere to exit.',
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
# setup some python lists for storing info about the insMouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsComponents = [insText, insMouse]
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
    # *insMouse* updates
    if insMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insMouse.frameNStart = frameN  # exact frame index
        insMouse.tStart = t  # local t and not account for scr refresh
        insMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insMouse, 'tStartRefresh')  # time at next scr refresh
        insMouse.status = STARTED
        prevButtonState = insMouse.getPressed()  # if button is down already this ISN'T a new click
    if insMouse.status == STARTED:  # only update if started and not finished!
        buttons = insMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/xiao/Documents/Study 1.2/PsychoPy/intervals_loop.xlsx'),
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
            
    # --- Prepare to start Routine "lightOn" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    status = 0
    print(f'The time interval is {timeInterval}')
    
    myClock.reset()
    # keep track of which components have finished
    lightOnComponents = [lightOffImg, lightOnImg, onButton]
    for thisComponent in lightOnComponents:
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
    
    # --- Run Routine "lightOn" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lightOffImg* updates
        if lightOffImg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            lightOffImg.frameNStart = frameN  # exact frame index
            lightOffImg.tStart = t  # local t and not account for scr refresh
            lightOffImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lightOffImg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lightOffImg.started')
            lightOffImg.setAutoDraw(True)
        if lightOffImg.status == STARTED:
            if bool(status == 1):
                # keep track of stop time/frame for later
                lightOffImg.tStop = t  # not accounting for scr refresh
                lightOffImg.frameNStop = frameN  # exact frame index
                lightOffImg.setAutoDraw(False)
        
        # *lightOnImg* updates
        if lightOnImg.status == NOT_STARTED and status == 1:
            # keep track of start time/frame for later
            lightOnImg.frameNStart = frameN  # exact frame index
            lightOnImg.tStart = t  # local t and not account for scr refresh
            lightOnImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lightOnImg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lightOnImg.started')
            lightOnImg.setAutoDraw(True)
        if lightOnImg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lightOnImg.tStartRefresh + timeInterval-frameTolerance:
                # keep track of stop time/frame for later
                lightOnImg.tStop = t  # not accounting for scr refresh
                lightOnImg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lightOnImg.stopped')
                lightOnImg.setAutoDraw(False)
        
        # *onButton* updates
        if onButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            onButton.frameNStart = frameN  # exact frame index
            onButton.tStart = t  # local t and not account for scr refresh
            onButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(onButton, 'tStartRefresh')  # time at next scr refresh
            onButton.setAutoDraw(True)
        if onButton.status == STARTED:
            # check whether onButton has been pressed
            if onButton.isClicked:
                if not onButton.wasClicked:
                    onButton.timesOn.append(globalClock.getTime()) # store time of first click
                    onButton.timesOff.append(globalClock.getTime()) # store time clicked until
                else:
                    onButton.timesOff[-1] = globalClock.getTime() # update time clicked until
                if not onButton.wasClicked:
                    status = 1
                onButton.wasClicked = True  # if onButton is still clicked next frame, it is not a new click
            else:
                onButton.wasClicked = False  # if onButton is clicked next frame, it is a new click
        else:
            onButton.wasClicked = False  # if onButton is clicked next frame, it is a new click
        # Run 'Each Frame' code from code
        if myClock.getTime() < timeInterval:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lightOnComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "lightOn" ---
    for thisComponent in lightOnComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('onButton.numClicks', onButton.numClicks)
    if onButton.numClicks:
       trials.addData('onButton.timesClicked', onButton.timesOn)
    else:
       trials.addData('onButton.timesClicked', "")
    # the Routine "lightOn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "timeEst" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textEntry.reset()
    bell.setSound('bell-ding.wav', secs=0.15, hamming=True)
    bell.setVolume(1.0, log=False)
    # keep track of which components have finished
    timeEstComponents = [estimateText, submitButton, lightOffImg_2, textEntry, bell]
    for thisComponent in timeEstComponents:
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
    
    # --- Run Routine "timeEst" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *estimateText* updates
        if estimateText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            estimateText.frameNStart = frameN  # exact frame index
            estimateText.tStart = t  # local t and not account for scr refresh
            estimateText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(estimateText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'estimateText.started')
            estimateText.setAutoDraw(True)
        
        # *submitButton* updates
        if submitButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            submitButton.frameNStart = frameN  # exact frame index
            submitButton.tStart = t  # local t and not account for scr refresh
            submitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submitButton, 'tStartRefresh')  # time at next scr refresh
            submitButton.setAutoDraw(True)
        if submitButton.status == STARTED:
            # check whether submitButton has been pressed
            if submitButton.isClicked:
                if not submitButton.wasClicked:
                    submitButton.timesOn.append(globalClock.getTime()) # store time of first click
                    submitButton.timesOff.append(globalClock.getTime()) # store time clicked until
                else:
                    submitButton.timesOff[-1] = globalClock.getTime() # update time clicked until
                if not submitButton.wasClicked:
                    continueRoutine = False  # end routine when submitButton is clicked
                    None
                submitButton.wasClicked = True  # if submitButton is still clicked next frame, it is not a new click
            else:
                submitButton.wasClicked = False  # if submitButton is clicked next frame, it is a new click
        else:
            submitButton.wasClicked = False  # if submitButton is clicked next frame, it is a new click
        
        # *lightOffImg_2* updates
        if lightOffImg_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            lightOffImg_2.frameNStart = frameN  # exact frame index
            lightOffImg_2.tStart = t  # local t and not account for scr refresh
            lightOffImg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lightOffImg_2, 'tStartRefresh')  # time at next scr refresh
            lightOffImg_2.setAutoDraw(True)
        
        # *textEntry* updates
        if textEntry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEntry.frameNStart = frameN  # exact frame index
            textEntry.tStart = t  # local t and not account for scr refresh
            textEntry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEntry, 'tStartRefresh')  # time at next scr refresh
            textEntry.setAutoDraw(True)
        # start/stop bell
        if bell.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bell.frameNStart = frameN  # exact frame index
            bell.tStart = t  # local t and not account for scr refresh
            bell.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('bell.started', tThisFlipGlobal)
            bell.play(when=win)  # sync with win flip
        if bell.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bell.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                bell.tStop = t  # not accounting for scr refresh
                bell.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bell.stopped')
                bell.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in timeEstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "timeEst" ---
    for thisComponent in timeEstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('submitButton.numClicks', submitButton.numClicks)
    if submitButton.numClicks:
       trials.addData('submitButton.timesClicked', submitButton.timesOn[0])
    else:
       trials.addData('submitButton.timesClicked', "")
    trials.addData('textEntry.text',textEntry.text)
    print(f'Estimated time: {textEntry.text}')
    bell.stop()  # ensure sound has stopped at end of routine
    # the Routine "timeEst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "endScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the endMouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
endScreenComponents = [endText, endMouse]
for thisComponent in endScreenComponents:
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

# --- Run Routine "endScreen" ---
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
        prevButtonState = endMouse.getPressed()  # if button is down already this ISN'T a new click
    if endMouse.status == STARTED:  # only update if started and not finished!
        buttons = endMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endScreen" ---
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "endScreen" was not non-slip safe, so reset the non-slip timer
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
