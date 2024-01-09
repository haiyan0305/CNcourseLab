/************ 
 * Iat Test *
 ************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'IAT';  // from the Builder filename that created this script
let expInfo = {'请填写您的姓名：': '', '请填写您的学号：': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(IAT_InstructionRoutineBegin());
flowScheduler.add(IAT_InstructionRoutineEachFrame());
flowScheduler.add(IAT_InstructionRoutineEnd());
flowScheduler.add(upper_hintRoutineBegin());
flowScheduler.add(upper_hintRoutineEachFrame());
flowScheduler.add(upper_hintRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var IAT_InstructionClock;
var random;
var thisExp;
var shuffle;
var sum;
var round;
var blocks_order;
var IAT_instr_image;
var IAT_instr_key_resp;
var upper_hintClock;
var upper_hint_image;
var Step_InstructionClock;
var nStep;
var instr_image;
var nstep_text;
var instr_key_resp;
var BlankClock;
var blank_text;
var TrialClock;
var corr_record;
var rt_record;
var interval_time_list;
var trial_test_background_img;
var stimuli_text;
var response;
var Trial_FeedbackClock;
var error_feedback_img;
var error_feedback_resp;
var Condition_FeedbackClock;
var condition_feedback_background_img;
var feedback_text;
var condition_feedback_resp;
var EndClock;
var end_text;
var end_image;
var end_key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "IAT_Instruction"
  IAT_InstructionClock = new util.Clock();
  random = Math.random;
  thisExp = psychoJS.experiment;
  shuffle = util.shuffle;
  Array.prototype.append = [].push;
  sum = function (arr) {return arr.reduce((a,b)=>a+b)};
  round = function(num, n=0) {
      var base = Math.pow(10, n);
      return (Math.round(num*base) / base);
      };
  blocks_order = Number.parseInt(((random() * 2) + 1)).toString();
  
  IAT_instr_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'IAT_instr_image', units : 'height', 
    image : 'materials/instruction.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.6, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  IAT_instr_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "upper_hint"
  upper_hintClock = new util.Clock();
  upper_hint_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'upper_hint_image', units : undefined, 
    image : 'materials/upper_hint.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.778, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "Step_Instruction"
  Step_InstructionClock = new util.Clock();
  nStep = 0;
  
  instr_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr_image', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.6, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  nstep_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'nstep_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instr_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank"
  BlankClock = new util.Clock();
  blank_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  corr_record = [];
  rt_record = [];
  interval_time_list = [0.1, 0.4, 0.7];
  
  trial_test_background_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial_test_background_img', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.6, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  stimuli_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimuli_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial_Feedback"
  Trial_FeedbackClock = new util.Clock();
  error_feedback_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'error_feedback_img', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.6, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  error_feedback_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Condition_Feedback"
  Condition_FeedbackClock = new util.Clock();
  condition_feedback_background_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'condition_feedback_background_img', units : 'height', 
    image : 'materials/condition_feedback_background.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.6, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  condition_feedback_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: '测试结束！感谢您的参与！',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  end_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'end_image', units : 'height', 
    image : 'materials/IAT_code.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.778, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  end_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _IAT_instr_key_resp_allKeys;
var IAT_InstructionComponents;
function IAT_InstructionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'IAT_Instruction'-------
    t = 0;
    IAT_InstructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    IAT_instr_key_resp.keys = undefined;
    IAT_instr_key_resp.rt = undefined;
    _IAT_instr_key_resp_allKeys = [];
    // keep track of which components have finished
    IAT_InstructionComponents = [];
    IAT_InstructionComponents.push(IAT_instr_image);
    IAT_InstructionComponents.push(IAT_instr_key_resp);
    
    IAT_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function IAT_InstructionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'IAT_Instruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = IAT_InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *IAT_instr_image* updates
    if (t >= 0.0 && IAT_instr_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      IAT_instr_image.tStart = t;  // (not accounting for frame time here)
      IAT_instr_image.frameNStart = frameN;  // exact frame index
      
      IAT_instr_image.setAutoDraw(true);
    }

    
    // *IAT_instr_key_resp* updates
    if (t >= 0.0 && IAT_instr_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      IAT_instr_key_resp.tStart = t;  // (not accounting for frame time here)
      IAT_instr_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { IAT_instr_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { IAT_instr_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { IAT_instr_key_resp.clearEvents(); });
    }

    if (IAT_instr_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = IAT_instr_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _IAT_instr_key_resp_allKeys = _IAT_instr_key_resp_allKeys.concat(theseKeys);
      if (_IAT_instr_key_resp_allKeys.length > 0) {
        IAT_instr_key_resp.keys = _IAT_instr_key_resp_allKeys[_IAT_instr_key_resp_allKeys.length - 1].name;  // just the last key pressed
        IAT_instr_key_resp.rt = _IAT_instr_key_resp_allKeys[_IAT_instr_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    IAT_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IAT_InstructionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'IAT_Instruction'-------
    IAT_InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('IAT_instr_key_resp.keys', IAT_instr_key_resp.keys);
    if (typeof IAT_instr_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('IAT_instr_key_resp.rt', IAT_instr_key_resp.rt);
        routineTimer.reset();
        }
    
    IAT_instr_key_resp.stop();
    // the Routine "IAT_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var upper_hintComponents;
function upper_hintRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'upper_hint'-------
    t = 0;
    upper_hintClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    upper_hintComponents = [];
    upper_hintComponents.push(upper_hint_image);
    
    upper_hintComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function upper_hintRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'upper_hint'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = upper_hintClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *upper_hint_image* updates
    if (t >= 0.0 && upper_hint_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      upper_hint_image.tStart = t;  // (not accounting for frame time here)
      upper_hint_image.frameNStart = frameN;  // exact frame index
      
      upper_hint_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (upper_hint_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      upper_hint_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    upper_hintComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function upper_hintRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'upper_hint'-------
    upper_hintComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var blocks;
var currentLoop;
function blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: (('conditions/conditions' + blocks_order) + '.xlsx'),
    seed: undefined, name: 'blocks'
  });
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  blocks.forEach(function() {
    const snapshot = blocks.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(Step_InstructionRoutineBegin(snapshot));
    thisScheduler.add(Step_InstructionRoutineEachFrame(snapshot));
    thisScheduler.add(Step_InstructionRoutineEnd(snapshot));
    thisScheduler.add(BlankRoutineBegin(snapshot));
    thisScheduler.add(BlankRoutineEachFrame(snapshot));
    thisScheduler.add(BlankRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(Condition_FeedbackRoutineBegin(snapshot));
    thisScheduler.add(Condition_FeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(Condition_FeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: step_order_filename,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(TrialRoutineBegin(snapshot));
    thisScheduler.add(TrialRoutineEachFrame(snapshot));
    thisScheduler.add(TrialRoutineEnd(snapshot));
    thisScheduler.add(Trial_FeedbackRoutineBegin(snapshot));
    thisScheduler.add(Trial_FeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(Trial_FeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}


var nstep_msg;
var _instr_key_resp_allKeys;
var Step_InstructionComponents;
function Step_InstructionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Step_Instruction'-------
    t = 0;
    Step_InstructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    nStep += 1;
    nstep_msg = `第${nStep}轮`;
    
    instr_image.setImage(step_instruction_filename);
    nstep_text.setText(nstep_msg);
    instr_key_resp.keys = undefined;
    instr_key_resp.rt = undefined;
    _instr_key_resp_allKeys = [];
    // keep track of which components have finished
    Step_InstructionComponents = [];
    Step_InstructionComponents.push(instr_image);
    Step_InstructionComponents.push(nstep_text);
    Step_InstructionComponents.push(instr_key_resp);
    
    Step_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Step_InstructionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Step_Instruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Step_InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_image* updates
    if (t >= 0.0 && instr_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_image.tStart = t;  // (not accounting for frame time here)
      instr_image.frameNStart = frameN;  // exact frame index
      
      instr_image.setAutoDraw(true);
    }

    
    // *nstep_text* updates
    if (t >= 0.0 && nstep_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nstep_text.tStart = t;  // (not accounting for frame time here)
      nstep_text.frameNStart = frameN;  // exact frame index
      
      nstep_text.setAutoDraw(true);
    }

    
    // *instr_key_resp* updates
    if (t >= 0.0 && instr_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_key_resp.tStart = t;  // (not accounting for frame time here)
      instr_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instr_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instr_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instr_key_resp.clearEvents(); });
    }

    if (instr_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instr_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instr_key_resp_allKeys = _instr_key_resp_allKeys.concat(theseKeys);
      if (_instr_key_resp_allKeys.length > 0) {
        instr_key_resp.keys = _instr_key_resp_allKeys[_instr_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instr_key_resp.rt = _instr_key_resp_allKeys[_instr_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Step_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Step_InstructionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Step_Instruction'-------
    Step_InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr_key_resp.keys', instr_key_resp.keys);
    if (typeof instr_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instr_key_resp.rt', instr_key_resp.rt);
        routineTimer.reset();
        }
    
    instr_key_resp.stop();
    // the Routine "Step_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var BlankComponents;
function BlankRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Blank'-------
    t = 0;
    BlankClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    BlankComponents = [];
    BlankComponents.push(blank_text);
    
    BlankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function BlankRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Blank'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BlankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_text* updates
    if (t >= 0.0 && blank_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_text.tStart = t;  // (not accounting for frame time here)
      blank_text.frameNStart = frameN;  // exact frame index
      
      blank_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BlankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BlankRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Blank'-------
    BlankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var interval_time;
var _response_allKeys;
var TrialComponents;
function TrialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Trial'-------
    t = 0;
    TrialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    shuffle(interval_time_list);
    interval_time = interval_time_list[0];
    
    trial_test_background_img.setImage(step_background_filename);
    stimuli_text.setText(stimuli_words);
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    // keep track of which components have finished
    TrialComponents = [];
    TrialComponents.push(trial_test_background_img);
    TrialComponents.push(stimuli_text);
    TrialComponents.push(response);
    
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function TrialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_test_background_img* updates
    if (t >= 0.0 && trial_test_background_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_test_background_img.tStart = t;  // (not accounting for frame time here)
      trial_test_background_img.frameNStart = frameN;  // exact frame index
      
      trial_test_background_img.setAutoDraw(true);
    }

    
    // *stimuli_text* updates
    if (t >= interval_time && stimuli_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_text.tStart = t;  // (not accounting for frame time here)
      stimuli_text.frameNStart = frameN;  // exact frame index
      
      stimuli_text.setAutoDraw(true);
    }

    
    // *response* updates
    if (t >= interval_time && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }

    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['e', 'i'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        // was this correct?
        if (response.keys == CorrAns) {
            response.corr = 1;
        } else {
            response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Trial'-------
    TrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    corr_record.append(response.corr);
    rt_record.append(response.rt);
    thisExp.addData("response.interval_time", interval_time);
    
    // was no response the correct answer?!
    if (response.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         response.corr = 1;  // correct non-response
      } else {
         response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('response.keys', response.keys);
    psychoJS.experiment.addData('response.corr', response.corr);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        routineTimer.reset();
        }
    
    response.stop();
    // the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _error_feedback_resp_allKeys;
var Trial_FeedbackComponents;
function Trial_FeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Trial_Feedback'-------
    t = 0;
    Trial_FeedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    error_feedback_img.setImage(step_error_filename);
    error_feedback_resp.keys = undefined;
    error_feedback_resp.rt = undefined;
    _error_feedback_resp_allKeys = [];
    console.log("MSG", error_feedback_resp.corr, error_feedback_resp.keys, CorrAns, (error_feedback_resp.keys === CorrAns));
    
    // keep track of which components have finished
    Trial_FeedbackComponents = [];
    Trial_FeedbackComponents.push(error_feedback_img);
    Trial_FeedbackComponents.push(error_feedback_resp);
    
    Trial_FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Trial_FeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Trial_Feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Trial_FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *error_feedback_img* updates
    if (t >= 0.0 && error_feedback_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      error_feedback_img.tStart = t;  // (not accounting for frame time here)
      error_feedback_img.frameNStart = frameN;  // exact frame index
      
      error_feedback_img.setAutoDraw(true);
    }

    
    // *error_feedback_resp* updates
    if (t >= 0.0 && error_feedback_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      error_feedback_resp.tStart = t;  // (not accounting for frame time here)
      error_feedback_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { error_feedback_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { error_feedback_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { error_feedback_resp.clearEvents(); });
    }

    if (error_feedback_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = error_feedback_resp.getKeys({keyList: ['e', 'i'], waitRelease: false});
      _error_feedback_resp_allKeys = _error_feedback_resp_allKeys.concat(theseKeys);
      if (_error_feedback_resp_allKeys.length > 0) {
        error_feedback_resp.keys = _error_feedback_resp_allKeys[_error_feedback_resp_allKeys.length - 1].name;  // just the last key pressed
        error_feedback_resp.rt = _error_feedback_resp_allKeys[_error_feedback_resp_allKeys.length - 1].rt;
        // was this correct?
        if (error_feedback_resp.keys == CorrAns) {
            error_feedback_resp.corr = 1;
        } else {
            error_feedback_resp.corr = 0;
        }
      }
    }
    
    if (((! need_feedback) || response.corr)) {
        continueRoutine = false;
    }
    if ((error_feedback_resp.keys === CorrAns)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trial_FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_FeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Trial_Feedback'-------
    Trial_FeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (error_feedback_resp.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         error_feedback_resp.corr = 1;  // correct non-response
      } else {
         error_feedback_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('error_feedback_resp.keys', error_feedback_resp.keys);
    psychoJS.experiment.addData('error_feedback_resp.corr', error_feedback_resp.corr);
    if (typeof error_feedback_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('error_feedback_resp.rt', error_feedback_resp.rt);
        }
    
    error_feedback_resp.stop();
    // the Routine "Trial_Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var average_corr;
var average_rt;
var corr_feedback_message;
var rt_corr_feedback_message;
var feedback_message;
var _condition_feedback_resp_allKeys;
var Condition_FeedbackComponents;
function Condition_FeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Condition_Feedback'-------
    t = 0;
    Condition_FeedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    average_corr = ((sum(corr_record) / corr_record.length) * 100);
    average_rt = (sum(rt_record) / rt_record.length);
    corr_feedback_message = `这一轮你的正确率为：${round(average_corr, 2)}%`;
    rt_corr_feedback_message = `这一轮你的平均反应时间为：${round(average_rt, 2)} 秒`;
    feedback_message = `${corr_feedback_message}
    ${rt_corr_feedback_message}`
    ;
    corr_record = [];
    rt_record = [];
    
    feedback_text.setText(feedback_message);
    condition_feedback_resp.keys = undefined;
    condition_feedback_resp.rt = undefined;
    _condition_feedback_resp_allKeys = [];
    // keep track of which components have finished
    Condition_FeedbackComponents = [];
    Condition_FeedbackComponents.push(condition_feedback_background_img);
    Condition_FeedbackComponents.push(feedback_text);
    Condition_FeedbackComponents.push(condition_feedback_resp);
    
    Condition_FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Condition_FeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Condition_Feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Condition_FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *condition_feedback_background_img* updates
    if (t >= 0.0 && condition_feedback_background_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      condition_feedback_background_img.tStart = t;  // (not accounting for frame time here)
      condition_feedback_background_img.frameNStart = frameN;  // exact frame index
      
      condition_feedback_background_img.setAutoDraw(true);
    }

    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    
    // *condition_feedback_resp* updates
    if (t >= 0.0 && condition_feedback_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      condition_feedback_resp.tStart = t;  // (not accounting for frame time here)
      condition_feedback_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { condition_feedback_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { condition_feedback_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { condition_feedback_resp.clearEvents(); });
    }

    if (condition_feedback_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = condition_feedback_resp.getKeys({keyList: ['space'], waitRelease: false});
      _condition_feedback_resp_allKeys = _condition_feedback_resp_allKeys.concat(theseKeys);
      if (_condition_feedback_resp_allKeys.length > 0) {
        condition_feedback_resp.keys = _condition_feedback_resp_allKeys[_condition_feedback_resp_allKeys.length - 1].name;  // just the last key pressed
        condition_feedback_resp.rt = _condition_feedback_resp_allKeys[_condition_feedback_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Condition_FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Condition_FeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Condition_Feedback'-------
    Condition_FeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('condition_feedback_resp.keys', condition_feedback_resp.keys);
    if (typeof condition_feedback_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('condition_feedback_resp.rt', condition_feedback_resp.rt);
        routineTimer.reset();
        }
    
    condition_feedback_resp.stop();
    // the Routine "Condition_Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _end_key_resp_allKeys;
var EndComponents;
function EndRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    end_key_resp.keys = undefined;
    end_key_resp.rt = undefined;
    _end_key_resp_allKeys = [];
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(end_text);
    EndComponents.push(end_image);
    EndComponents.push(end_key_resp);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function EndRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 1 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    frameRemains = 1 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_text.setAutoDraw(false);
    }
    
    // *end_image* updates
    if (t >= 3 && end_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_image.tStart = t;  // (not accounting for frame time here)
      end_image.frameNStart = frameN;  // exact frame index
      
      end_image.setAutoDraw(true);
    }

    
    // *end_key_resp* updates
    if (t >= 3 && end_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_key_resp.tStart = t;  // (not accounting for frame time here)
      end_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_key_resp.clearEvents(); });
    }

    if (end_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _end_key_resp_allKeys = _end_key_resp_allKeys.concat(theseKeys);
      if (_end_key_resp_allKeys.length > 0) {
        end_key_resp.keys = _end_key_resp_allKeys[_end_key_resp_allKeys.length - 1].name;  // just the last key pressed
        end_key_resp.rt = _end_key_resp_allKeys[_end_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_key_resp.keys', end_key_resp.keys);
    if (typeof end_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_key_resp.rt', end_key_resp.rt);
        routineTimer.reset();
        }
    
    end_key_resp.stop();
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
