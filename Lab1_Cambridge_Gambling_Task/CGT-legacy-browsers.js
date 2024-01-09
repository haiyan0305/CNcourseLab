/************ 
 * Cgt Test *
 ************/


// store info about the experiment session:
let expName = 'CGT';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true
});
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
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin(blocksLoopScheduler));
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/bc.jpg', 'path': 'stimuli/bc.jpg'},
    {'name': 'condition/up.xlsx', 'path': 'condition/up.xlsx'},
    {'name': 'instruction/instruction.jpg', 'path': 'instruction/instruction.jpg'},
    {'name': 'stimuli/tri.png', 'path': 'stimuli/tri.png'},
    {'name': 'condition/main.xlsx', 'path': 'condition/main.xlsx'},
    {'name': 'stimuli/rc.jpg', 'path': 'stimuli/rc.jpg'},
    {'name': 'stimuli/r.jpg', 'path': 'stimuli/r.jpg'},
    {'name': 'condition/down.xlsx', 'path': 'condition/down.xlsx'},
    {'name': 'stimuli/red.png', 'path': 'stimuli/red.png'},
    {'name': 'stimuli/tri_r.png', 'path': 'stimuli/tri_r.png'},
    {'name': 'stimuli/b.jpg', 'path': 'stimuli/b.jpg'},
    {'name': 'stimuli/blue.png', 'path': 'stimuli/blue.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

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


var instrClock;
var random;
var sumlist;
var instr_image;
var instr_key_resp;
var block_initClock;
var instr_blocks_text;
var instr_blocks_key_resp;
var decision_trialClock;
var choice_color;
var image_0;
var image_1;
var image_2;
var image_3;
var image_4;
var image_5;
var image_6;
var image_7;
var image_8;
var image_9;
var red_image;
var blue_image;
var arrow_image;
var money_text;
var introduction_text;
var rate_trialClock;
var choice_stake;
var image_9_0;
var image_10;
var image_11;
var image_12;
var image_13;
var image_14;
var image_15;
var image_16;
var image_17;
var image_18;
var red_image_2;
var blue_image_2;
var money_text_2;
var count_down_text_0;
var count_down_text_1;
var count_down_text_2;
var count_down_text_3;
var count_down_text_4;
var stake_text;
var arrow_image_2;
var introduction_text_2;
var feedbackClock;
var stake_num_text;
var result_text;
var total_token_text;
var arrow_image_3;
var l9;
var l8;
var l7;
var l6;
var ll;
var endClock;
var end_text;
var space_text;
var end_key_resp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  /* append => push */
  Array.prototype.append = [].push;
  
  random = Math.random;
  
  sumlist = function(arr){
      return arr.reduce((a, b)=>a+b);
      }
  instr_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr_image', units : undefined, 
    image : 'instruction/instruction.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.778, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  instr_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block_init"
  block_initClock = new util.Clock();
  instr_blocks_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_blocks_text',
    text: '准备好后按空格键进入下一组实验\n\n你的代币将会重置为100',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_blocks_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "decision_trial"
  decision_trialClock = new util.Clock();
  choice_color = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_0 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_0', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  red_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'red_image', units : undefined, 
    image : 'stimuli/r.jpg', mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.2)], size : [0.356, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  blue_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blue_image', units : undefined, 
    image : 'stimuli/b.jpg', mask : undefined,
    ori : 0, pos : [0.3, (- 0.2)], size : [0.356, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  arrow_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arrow_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  money_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'money_text',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [(- 0.2), 0.08], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -15.0 
  });
  
  introduction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'introduction_text',
    text: '按左方向键选择红色\n按右方向键选择蓝色',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, (- 0.03)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -16.0 
  });
  
  // Initialize components for Routine "rate_trial"
  rate_trialClock = new util.Clock();
  choice_stake = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_9_0 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9_0', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  image_17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_17', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  image_18 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_18', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.08, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  red_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'red_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.2)], size : [0.356, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  blue_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blue_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.2)], size : [0.356, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  money_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'money_text_2',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [(- 0.2), 0.08], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -14.0 
  });
  
  count_down_text_0 = new visual.TextStim({
    win: psychoJS.window,
    name: 'count_down_text_0',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -15.0 
  });
  
  count_down_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'count_down_text_1',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -16.0 
  });
  
  count_down_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'count_down_text_2',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -17.0 
  });
  
  count_down_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'count_down_text_3',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -18.0 
  });
  
  count_down_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'count_down_text_4',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -19.0 
  });
  
  stake_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stake_text',
    text: '赌注:',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0.09, 0.08], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: 1,
    depth: -20.0 
  });
  
  arrow_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arrow_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.09, 0.09],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -21.0 
  });
  introduction_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'introduction_text_2',
    text: '请准备好下注...\n按下向下方向键以停止下注',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, (- 0.03)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -22.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  stake_num_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stake_num_text',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0.2], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  result_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'result_text',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  total_token_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'total_token_text',
    text: '',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  arrow_image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arrow_image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Run 'Begin Experiment' code from code_end
  l9 = [];
  l8 = [];
  l7 = [];
  l6 = [];
  ll = [];
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: '测试结束！感谢你的参与！',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, 0.05], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  space_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_text',
    text: '按空格键正式结束实验',
    font: 'microsoft yahei',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  end_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var token;
var posl;
var stims;
var cstims;
var ncstims;
var ct1;
var ct2;
var ct3;
var ct4;
var ct5;
var counthighlow;
var countlowhigh;
var bpos;
var arrPos;
var _instr_key_resp_allKeys;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_config
    token = 100;
    posl = [[(- 0.45), 0.25], [(- 0.35), 0.25], [(- 0.25), 0.25], [(- 0.15), 0.25], [(- 0.05), 0.25], [0.05, 0.25], [0.15, 0.25], [0.25, 0.25], [0.35, 0.25], [0.45, 0.25]];
    stims = ["stimuli/red.png", "stimuli/blue.png"];
    cstims = ["stimuli/rc.jpg", "stimuli/bc.jpg"];
    ncstims = ["stimuli/r.jpg", "stimuli/b.jpg"];
    ct1 = 5;
    ct2 = (ct1 * 2);
    ct3 = (ct1 * 3);
    ct4 = (ct1 * 4);
    ct5 = (ct1 * 5);
    counthighlow = [0.95, 0.75, 0.5, 0.25, 0.05];
    countlowhigh = [0.05, 0.25, 0.5, 0.75, 0.95];
    bpos = [0.24, 0.08];
    arrPos = [0.5, (- 0.35)];
    
    instr_key_resp.keys = undefined;
    instr_key_resp.rt = undefined;
    _instr_key_resp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instr_image);
    instrComponents.push(instr_key_resp);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_image* updates
    if (t >= 0.0 && instr_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_image.tStart = t;  // (not accounting for frame time here)
      instr_image.frameNStart = frameN;  // exact frame index
      
      instr_image.setAutoDraw(true);
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
    instrComponents.forEach( function(thisComponent) {
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


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instr_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instr_key_resp.keys', instr_key_resp.keys);
    if (typeof instr_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instr_key_resp.rt', instr_key_resp.rt);
        routineTimer.reset();
        }
    
    instr_key_resp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blocks;
function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'condition/main.xlsx',
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    blocks.forEach(function() {
      snapshot = blocks.getSnapshot();
    
      blocksLoopScheduler.add(importConditions(snapshot));
      blocksLoopScheduler.add(block_initRoutineBegin(snapshot));
      blocksLoopScheduler.add(block_initRoutineEachFrame());
      blocksLoopScheduler.add(block_initRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      blocksLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      blocksLoopScheduler.add(trialsLoopScheduler);
      blocksLoopScheduler.add(trialsLoopEnd);
      blocksLoopScheduler.add(blocksLoopEndIteration(blocksLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: condition_file,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(decision_trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(decision_trialRoutineEachFrame());
      trialsLoopScheduler.add(decision_trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(rate_trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(rate_trialRoutineEachFrame());
      trialsLoopScheduler.add(rate_trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function blocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function blocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var arrow;
var _instr_blocks_key_resp_allKeys;
var block_initComponents;
function block_initRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'block_init' ---
    t = 0;
    block_initClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_init
    if ((block_type === "up")) {
        arrow = "stimuli/tri.png";
    } else {
        if ((block_type === "down")) {
            arrow = "stimuli/tri_r.png";
        }
    }
    token = 100;
    
    instr_blocks_key_resp.keys = undefined;
    instr_blocks_key_resp.rt = undefined;
    _instr_blocks_key_resp_allKeys = [];
    // keep track of which components have finished
    block_initComponents = [];
    block_initComponents.push(instr_blocks_text);
    block_initComponents.push(instr_blocks_key_resp);
    
    block_initComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function block_initRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'block_init' ---
    // get current time
    t = block_initClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_blocks_text* updates
    if (t >= 0.0 && instr_blocks_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_blocks_text.tStart = t;  // (not accounting for frame time here)
      instr_blocks_text.frameNStart = frameN;  // exact frame index
      
      instr_blocks_text.setAutoDraw(true);
    }

    
    // *instr_blocks_key_resp* updates
    if (t >= 0.0 && instr_blocks_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_blocks_key_resp.tStart = t;  // (not accounting for frame time here)
      instr_blocks_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instr_blocks_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instr_blocks_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instr_blocks_key_resp.clearEvents(); });
    }

    if (instr_blocks_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instr_blocks_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instr_blocks_key_resp_allKeys = _instr_blocks_key_resp_allKeys.concat(theseKeys);
      if (_instr_blocks_key_resp_allKeys.length > 0) {
        instr_blocks_key_resp.keys = _instr_blocks_key_resp_allKeys[_instr_blocks_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instr_blocks_key_resp.rt = _instr_blocks_key_resp_allKeys[_instr_blocks_key_resp_allKeys.length - 1].rt;
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
    block_initComponents.forEach( function(thisComponent) {
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


function block_initRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'block_init' ---
    block_initComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instr_blocks_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instr_blocks_key_resp.keys', instr_blocks_key_resp.keys);
    if (typeof instr_blocks_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instr_blocks_key_resp.rt', instr_blocks_key_resp.rt);
        routineTimer.reset();
        }
    
    instr_blocks_key_resp.stop();
    // the Routine "block_init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var picl;
var token_show;
var _choice_color_allKeys;
var decision_trialComponents;
function decision_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decision_trial' ---
    t = 0;
    decision_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_decision
    picl = [];
    for (var i = 0, _pj_a = red_num; (i < _pj_a); i += 1) {
        picl.append(stims[0]);
    }
    for (var i = 0, _pj_a = blue_num; (i < _pj_a); i += 1) {
        picl.append(stims[1]);
    }
    token_show = ("\u603b\u91d1\u989d\uff1a" + Number.parseInt(token).toString());
    
    choice_color.keys = undefined;
    choice_color.rt = undefined;
    _choice_color_allKeys = [];
    image_0.setPos(posl[0]);
    image_0.setImage(picl[0]);
    image_1.setPos(posl[1]);
    image_1.setImage(picl[1]);
    image_2.setPos(posl[2]);
    image_2.setImage(picl[2]);
    image_3.setPos(posl[3]);
    image_3.setImage(picl[3]);
    image_4.setPos(posl[4]);
    image_4.setImage(picl[4]);
    image_5.setPos(posl[5]);
    image_5.setImage(picl[5]);
    image_6.setPos(posl[6]);
    image_6.setImage(picl[6]);
    image_7.setPos(posl[7]);
    image_7.setImage(picl[7]);
    image_8.setPos(posl[8]);
    image_8.setImage(picl[8]);
    image_9.setPos(posl[9]);
    image_9.setImage(picl[9]);
    arrow_image.setPos(arrPos);
    arrow_image.setImage(arrow);
    money_text.setText(token_show);
    // keep track of which components have finished
    decision_trialComponents = [];
    decision_trialComponents.push(choice_color);
    decision_trialComponents.push(image_0);
    decision_trialComponents.push(image_1);
    decision_trialComponents.push(image_2);
    decision_trialComponents.push(image_3);
    decision_trialComponents.push(image_4);
    decision_trialComponents.push(image_5);
    decision_trialComponents.push(image_6);
    decision_trialComponents.push(image_7);
    decision_trialComponents.push(image_8);
    decision_trialComponents.push(image_9);
    decision_trialComponents.push(red_image);
    decision_trialComponents.push(blue_image);
    decision_trialComponents.push(arrow_image);
    decision_trialComponents.push(money_text);
    decision_trialComponents.push(introduction_text);
    
    decision_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function decision_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decision_trial' ---
    // get current time
    t = decision_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *choice_color* updates
    if (t >= 0.0 && choice_color.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_color.tStart = t;  // (not accounting for frame time here)
      choice_color.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choice_color.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choice_color.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choice_color.clearEvents(); });
    }

    if (choice_color.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice_color.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _choice_color_allKeys = _choice_color_allKeys.concat(theseKeys);
      if (_choice_color_allKeys.length > 0) {
        choice_color.keys = _choice_color_allKeys[0].name;  // just the first key pressed
        choice_color.rt = _choice_color_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_0* updates
    if (t >= 0.0 && image_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_0.tStart = t;  // (not accounting for frame time here)
      image_0.frameNStart = frameN;  // exact frame index
      
      image_0.setAutoDraw(true);
    }

    
    // *image_1* updates
    if (t >= 0.0 && image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1.tStart = t;  // (not accounting for frame time here)
      image_1.frameNStart = frameN;  // exact frame index
      
      image_1.setAutoDraw(true);
    }

    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }

    
    // *image_6* updates
    if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }

    
    // *image_7* updates
    if (t >= 0.0 && image_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_7.tStart = t;  // (not accounting for frame time here)
      image_7.frameNStart = frameN;  // exact frame index
      
      image_7.setAutoDraw(true);
    }

    
    // *image_8* updates
    if (t >= 0.0 && image_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_8.tStart = t;  // (not accounting for frame time here)
      image_8.frameNStart = frameN;  // exact frame index
      
      image_8.setAutoDraw(true);
    }

    
    // *image_9* updates
    if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index
      
      image_9.setAutoDraw(true);
    }

    
    // *red_image* updates
    if (t >= 0.0 && red_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      red_image.tStart = t;  // (not accounting for frame time here)
      red_image.frameNStart = frameN;  // exact frame index
      
      red_image.setAutoDraw(true);
    }

    
    // *blue_image* updates
    if (t >= 0.0 && blue_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blue_image.tStart = t;  // (not accounting for frame time here)
      blue_image.frameNStart = frameN;  // exact frame index
      
      blue_image.setAutoDraw(true);
    }

    
    // *arrow_image* updates
    if (t >= 0.0 && arrow_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arrow_image.tStart = t;  // (not accounting for frame time here)
      arrow_image.frameNStart = frameN;  // exact frame index
      
      arrow_image.setAutoDraw(true);
    }

    
    // *money_text* updates
    if (t >= 0.0 && money_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      money_text.tStart = t;  // (not accounting for frame time here)
      money_text.frameNStart = frameN;  // exact frame index
      
      money_text.setAutoDraw(true);
    }

    
    // *introduction_text* updates
    if (t >= 0.0 && introduction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction_text.tStart = t;  // (not accounting for frame time here)
      introduction_text.frameNStart = frameN;  // exact frame index
      
      introduction_text.setAutoDraw(true);
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
    decision_trialComponents.forEach( function(thisComponent) {
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


function decision_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decision_trial' ---
    decision_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(choice_color.corr, level);
    }
    psychoJS.experiment.addData('choice_color.keys', choice_color.keys);
    if (typeof choice_color.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice_color.rt', choice_color.rt);
        routineTimer.reset();
        }
    
    choice_color.stop();
    // the Routine "decision_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rpic;
var bpic;
var count_seq;
var countdownl;
var _choice_stake_allKeys;
var rate_trialComponents;
function rate_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rate_trial' ---
    t = 0;
    rate_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_rate
    if ((choice_color.keys === "left")) {
        rpic = cstims[0];
        bpic = ncstims[1];
    } else {
        if ((choice_color.keys === "right")) {
            bpic = cstims[1];
            rpic = ncstims[0];
        } else {
            console.log("error in setting chose picture");
        }
    }
    if ((count_down_type === "high_to_low")) {
        count_seq = counthighlow;
    } else {
        if ((count_down_type === "low_to_high")) {
            count_seq = countlowhigh;
        } else {
            console.log("error in setting count down sequence");
        }
    }
    countdownl = [];
    for (var i, _pj_c = 0, _pj_a = count_seq, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        temp = Number.parseInt((token * i)).toString();
        countdownl.append(temp);
    }
    
    choice_stake.keys = undefined;
    choice_stake.rt = undefined;
    _choice_stake_allKeys = [];
    image_9_0.setPos(posl[0]);
    image_9_0.setImage(picl[0]);
    image_10.setPos(posl[1]);
    image_10.setImage(picl[1]);
    image_11.setPos(posl[2]);
    image_11.setImage(picl[2]);
    image_12.setPos(posl[3]);
    image_12.setImage(picl[3]);
    image_13.setPos(posl[4]);
    image_13.setImage(picl[4]);
    image_14.setPos(posl[5]);
    image_14.setImage(picl[5]);
    image_15.setPos(posl[6]);
    image_15.setImage(picl[6]);
    image_16.setPos(posl[7]);
    image_16.setImage(picl[7]);
    image_17.setPos(posl[8]);
    image_17.setImage(picl[8]);
    image_18.setPos(posl[9]);
    image_18.setImage(picl[9]);
    red_image_2.setImage(rpic);
    blue_image_2.setImage(bpic);
    money_text_2.setText(token_show);
    count_down_text_0.setPos(bpos);
    count_down_text_0.setText(countdownl[0]);
    count_down_text_1.setPos(bpos);
    count_down_text_1.setText(countdownl[1]);
    count_down_text_2.setPos(bpos);
    count_down_text_2.setText(countdownl[2]);
    count_down_text_3.setPos(bpos);
    count_down_text_3.setText(countdownl[3]);
    count_down_text_4.setPos(bpos);
    count_down_text_4.setText(countdownl[4]);
    arrow_image_2.setPos(arrPos);
    arrow_image_2.setImage(arrow);
    // keep track of which components have finished
    rate_trialComponents = [];
    rate_trialComponents.push(choice_stake);
    rate_trialComponents.push(image_9_0);
    rate_trialComponents.push(image_10);
    rate_trialComponents.push(image_11);
    rate_trialComponents.push(image_12);
    rate_trialComponents.push(image_13);
    rate_trialComponents.push(image_14);
    rate_trialComponents.push(image_15);
    rate_trialComponents.push(image_16);
    rate_trialComponents.push(image_17);
    rate_trialComponents.push(image_18);
    rate_trialComponents.push(red_image_2);
    rate_trialComponents.push(blue_image_2);
    rate_trialComponents.push(money_text_2);
    rate_trialComponents.push(count_down_text_0);
    rate_trialComponents.push(count_down_text_1);
    rate_trialComponents.push(count_down_text_2);
    rate_trialComponents.push(count_down_text_3);
    rate_trialComponents.push(count_down_text_4);
    rate_trialComponents.push(stake_text);
    rate_trialComponents.push(arrow_image_2);
    rate_trialComponents.push(introduction_text_2);
    
    rate_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function rate_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rate_trial' ---
    // get current time
    t = rate_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *choice_stake* updates
    if (t >= 0.0 && choice_stake.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_stake.tStart = t;  // (not accounting for frame time here)
      choice_stake.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choice_stake.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choice_stake.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choice_stake.clearEvents(); });
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice_stake.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice_stake.status = PsychoJS.Status.FINISHED;
  }

    if (choice_stake.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice_stake.getKeys({keyList: ['down'], waitRelease: false});
      _choice_stake_allKeys = _choice_stake_allKeys.concat(theseKeys);
      if (_choice_stake_allKeys.length > 0) {
        choice_stake.keys = _choice_stake_allKeys[_choice_stake_allKeys.length - 1].name;  // just the last key pressed
        choice_stake.rt = _choice_stake_allKeys[_choice_stake_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_9_0* updates
    if (t >= 0.0 && image_9_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9_0.tStart = t;  // (not accounting for frame time here)
      image_9_0.frameNStart = frameN;  // exact frame index
      
      image_9_0.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_9_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_9_0.setAutoDraw(false);
    }
    
    // *image_10* updates
    if (t >= 0.0 && image_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_10.tStart = t;  // (not accounting for frame time here)
      image_10.frameNStart = frameN;  // exact frame index
      
      image_10.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_10.setAutoDraw(false);
    }
    
    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_11.setAutoDraw(false);
    }
    
    // *image_12* updates
    if (t >= 0.0 && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index
      
      image_12.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_12.setAutoDraw(false);
    }
    
    // *image_13* updates
    if (t >= 0.0 && image_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_13.tStart = t;  // (not accounting for frame time here)
      image_13.frameNStart = frameN;  // exact frame index
      
      image_13.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_13.setAutoDraw(false);
    }
    
    // *image_14* updates
    if (t >= 0.0 && image_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_14.tStart = t;  // (not accounting for frame time here)
      image_14.frameNStart = frameN;  // exact frame index
      
      image_14.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_14.setAutoDraw(false);
    }
    
    // *image_15* updates
    if (t >= 0.0 && image_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_15.tStart = t;  // (not accounting for frame time here)
      image_15.frameNStart = frameN;  // exact frame index
      
      image_15.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_15.setAutoDraw(false);
    }
    
    // *image_16* updates
    if (t >= 0.0 && image_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_16.tStart = t;  // (not accounting for frame time here)
      image_16.frameNStart = frameN;  // exact frame index
      
      image_16.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_16.setAutoDraw(false);
    }
    
    // *image_17* updates
    if (t >= 0.0 && image_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_17.tStart = t;  // (not accounting for frame time here)
      image_17.frameNStart = frameN;  // exact frame index
      
      image_17.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_17.setAutoDraw(false);
    }
    
    // *image_18* updates
    if (t >= 0.0 && image_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_18.tStart = t;  // (not accounting for frame time here)
      image_18.frameNStart = frameN;  // exact frame index
      
      image_18.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_18.setAutoDraw(false);
    }
    
    // *red_image_2* updates
    if (t >= 0.0 && red_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      red_image_2.tStart = t;  // (not accounting for frame time here)
      red_image_2.frameNStart = frameN;  // exact frame index
      
      red_image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (red_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      red_image_2.setAutoDraw(false);
    }
    
    // *blue_image_2* updates
    if (t >= 0.0 && blue_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blue_image_2.tStart = t;  // (not accounting for frame time here)
      blue_image_2.frameNStart = frameN;  // exact frame index
      
      blue_image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blue_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blue_image_2.setAutoDraw(false);
    }
    
    // *money_text_2* updates
    if (t >= 0.0 && money_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      money_text_2.tStart = t;  // (not accounting for frame time here)
      money_text_2.frameNStart = frameN;  // exact frame index
      
      money_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (money_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      money_text_2.setAutoDraw(false);
    }
    
    // *count_down_text_0* updates
    if (t >= 0.0 && count_down_text_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      count_down_text_0.tStart = t;  // (not accounting for frame time here)
      count_down_text_0.frameNStart = frameN;  // exact frame index
      
      count_down_text_0.setAutoDraw(true);
    }

    frameRemains = ct1  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((count_down_text_0.status === PsychoJS.Status.STARTED || count_down_text_0.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      count_down_text_0.setAutoDraw(false);
    }
    
    // *count_down_text_1* updates
    if (t >= ct1 && count_down_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      count_down_text_1.tStart = t;  // (not accounting for frame time here)
      count_down_text_1.frameNStart = frameN;  // exact frame index
      
      count_down_text_1.setAutoDraw(true);
    }

    frameRemains = ct2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((count_down_text_1.status === PsychoJS.Status.STARTED || count_down_text_1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      count_down_text_1.setAutoDraw(false);
    }
    
    // *count_down_text_2* updates
    if (t >= ct2 && count_down_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      count_down_text_2.tStart = t;  // (not accounting for frame time here)
      count_down_text_2.frameNStart = frameN;  // exact frame index
      
      count_down_text_2.setAutoDraw(true);
    }

    frameRemains = ct3  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((count_down_text_2.status === PsychoJS.Status.STARTED || count_down_text_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      count_down_text_2.setAutoDraw(false);
    }
    
    // *count_down_text_3* updates
    if (t >= ct3 && count_down_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      count_down_text_3.tStart = t;  // (not accounting for frame time here)
      count_down_text_3.frameNStart = frameN;  // exact frame index
      
      count_down_text_3.setAutoDraw(true);
    }

    frameRemains = ct4  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((count_down_text_3.status === PsychoJS.Status.STARTED || count_down_text_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      count_down_text_3.setAutoDraw(false);
    }
    
    // *count_down_text_4* updates
    if (t >= ct4 && count_down_text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      count_down_text_4.tStart = t;  // (not accounting for frame time here)
      count_down_text_4.frameNStart = frameN;  // exact frame index
      
      count_down_text_4.setAutoDraw(true);
    }

    frameRemains = ct5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((count_down_text_4.status === PsychoJS.Status.STARTED || count_down_text_4.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      count_down_text_4.setAutoDraw(false);
    }
    
    // *stake_text* updates
    if (t >= 0.0 && stake_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stake_text.tStart = t;  // (not accounting for frame time here)
      stake_text.frameNStart = frameN;  // exact frame index
      
      stake_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stake_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stake_text.setAutoDraw(false);
    }
    
    // *arrow_image_2* updates
    if (t >= 0.0 && arrow_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arrow_image_2.tStart = t;  // (not accounting for frame time here)
      arrow_image_2.frameNStart = frameN;  // exact frame index
      
      arrow_image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (arrow_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      arrow_image_2.setAutoDraw(false);
    }
    
    // *introduction_text_2* updates
    if (t >= 0.0 && introduction_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction_text_2.tStart = t;  // (not accounting for frame time here)
      introduction_text_2.frameNStart = frameN;  // exact frame index
      
      introduction_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + ct5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (introduction_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      introduction_text_2.setAutoDraw(false);
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
    rate_trialComponents.forEach( function(thisComponent) {
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


function rate_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rate_trial' ---
    rate_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(choice_stake.corr, level);
    }
    psychoJS.experiment.addData('choice_stake.keys', choice_stake.keys);
    if (typeof choice_stake.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice_stake.rt', choice_stake.rt);
        routineTimer.reset();
        }
    
    choice_stake.stop();
    // the Routine "rate_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var idx;
var stake_num;
var count_here;
var snshow;
var temp;
var result_color;
var result_direction;
var result;
var result_t;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    if (choice_stake.rt) {
        idx = Number.parseInt((choice_stake.rt / 5));
    } else {
        idx = 4;
    }
    stake_num = countdownl[idx];
    count_here = count_seq[idx];
    snshow = ("\u8d4c\u6ce8: " + stake_num.toString());
    temp = (Math.random() * 10);
    if ((temp < red_num)) {
        result_color = "red";
        result_direction = "left";
    } else {
        result_color = "blue";
        result_direction = "right";
    }
    if ((choice_color.keys === result_direction)) {
        result = "win";
        result_t = "\u4f60\u731c\u5bf9\u4e86\uff01";
        token += Number.parseInt(stake_num);
    } else {
        result = "lose";
        result_t = "\u4f60\u731c\u9519\u4e86\uff01";
        token -= Number.parseInt(stake_num);
    }
    console.log("token: ", token);
    console.log("stake_num:", stake_num);
    token_show = ("\u603b\u91d1\u989d\uff1a" + Number.parseInt(token).toString());
    psychoJS.experiment.addData("choice_stake.choice", stake_num);
    psychoJS.experiment.addData("choice_stake.result_color", result_color);
    psychoJS.experiment.addData("choice_stake.result_direction", result_direction);
    psychoJS.experiment.addData("choice_stake.result", result);
    
    stake_num_text.setText(snshow);
    result_text.setText(result_t);
    total_token_text.setText(token_show);
    arrow_image_3.setPos(arrPos);
    arrow_image_3.setImage(arrow);
    // Run 'Begin Routine' code from code_end
    if (((red_num === 1) || (red_num === 9))) {
        l9.append(count_here);
    } else {
        if (((red_num === 2) || (red_num === 8))) {
            l8.append(count_here);
        } else {
            if (((red_num === 3) || (red_num === 7))) {
                l7.append(count_here);
            } else {
                if (((red_num === 4) || (red_num === 6))) {
                    l6.append(count_here);
                }
            }
        }
    }
    ll.append(count_here);
    
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(stake_num_text);
    feedbackComponents.push(result_text);
    feedbackComponents.push(total_token_text);
    feedbackComponents.push(arrow_image_3);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stake_num_text* updates
    if (t >= 0.0 && stake_num_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stake_num_text.tStart = t;  // (not accounting for frame time here)
      stake_num_text.frameNStart = frameN;  // exact frame index
      
      stake_num_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stake_num_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stake_num_text.setAutoDraw(false);
    }
    
    // *result_text* updates
    if (t >= 0.0 && result_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      result_text.tStart = t;  // (not accounting for frame time here)
      result_text.frameNStart = frameN;  // exact frame index
      
      result_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (result_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      result_text.setAutoDraw(false);
    }
    
    // *total_token_text* updates
    if (t >= 0.0 && total_token_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      total_token_text.tStart = t;  // (not accounting for frame time here)
      total_token_text.frameNStart = frameN;  // exact frame index
      
      total_token_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (total_token_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      total_token_text.setAutoDraw(false);
    }
    
    // *arrow_image_3* updates
    if (t >= 0.0 && arrow_image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arrow_image_3.tStart = t;  // (not accounting for frame time here)
      arrow_image_3.frameNStart = frameN;  // exact frame index
      
      arrow_image_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (arrow_image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      arrow_image_3.setAutoDraw(false);
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
    feedbackComponents.forEach( function(thisComponent) {
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


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from code_end
    if ((token <= 1)) {
        trials.finished = true;
    }
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _end_key_resp_allKeys;
var a;
var b;
var c;
var d;
var e;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_key_resp.keys = undefined;
    end_key_resp.rt = undefined;
    _end_key_resp_allKeys = [];
    // Run 'Begin Routine' code from code_report
    a = (sumlist(l9) * 2);
    b = sumlist(l8);
    c = sumlist(l7);
    d = (sumlist(l6) * 2);
    e = (sumlist(ll) / ll.length);
    console.log("Risk_Adjustmenrt", ((((a + b) - c) - d) / e));
    
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(end_text);
    endComponents.push(space_text);
    endComponents.push(end_key_resp);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    
    // *space_text* updates
    if (t >= 0.0 && space_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_text.tStart = t;  // (not accounting for frame time here)
      space_text.frameNStart = frameN;  // exact frame index
      
      space_text.setAutoDraw(true);
    }

    
    // *end_key_resp* updates
    if (t >= 0.0 && end_key_resp.status === PsychoJS.Status.NOT_STARTED) {
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
    endComponents.forEach( function(thisComponent) {
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


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(end_key_resp.corr, level);
    }
    psychoJS.experiment.addData('end_key_resp.keys', end_key_resp.keys);
    if (typeof end_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_key_resp.rt', end_key_resp.rt);
        routineTimer.reset();
        }
    
    end_key_resp.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
