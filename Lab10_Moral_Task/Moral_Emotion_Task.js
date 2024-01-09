/*************************** 
 * Moral_Emotion_Task Test *
 ***************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Moral_Emotion_Task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '1',
    'randomization': '-1',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
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
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'materials/badpropose/28.PNG', 'path': 'materials/badpropose/28.PNG'},
    {'name': 'materials/happyending/41.PNG', 'path': 'materials/happyending/41.PNG'},
    {'name': 'materials/badpropose/27.PNG', 'path': 'materials/badpropose/27.PNG'},
    {'name': 'materials/sadending/5.PNG', 'path': 'materials/sadending/5.PNG'},
    {'name': 'materials/situations/10.PNG', 'path': 'materials/situations/10.PNG'},
    {'name': 'materials/happyending/5.PNG', 'path': 'materials/happyending/5.PNG'},
    {'name': 'materials/goodpropose/7.PNG', 'path': 'materials/goodpropose/7.PNG'},
    {'name': 'materials/happyending/2.PNG', 'path': 'materials/happyending/2.PNG'},
    {'name': 'materials/badpropose/25.PNG', 'path': 'materials/badpropose/25.PNG'},
    {'name': 'materials/sadreason/48.PNG', 'path': 'materials/sadreason/48.PNG'},
    {'name': 'materials/happyending/13.PNG', 'path': 'materials/happyending/13.PNG'},
    {'name': 'materials/sadreason/4.PNG', 'path': 'materials/sadreason/4.PNG'},
    {'name': 'materials/sadreason/3.PNG', 'path': 'materials/sadreason/3.PNG'},
    {'name': 'materials/happyreason/44.PNG', 'path': 'materials/happyreason/44.PNG'},
    {'name': 'materials/happyreason/46.PNG', 'path': 'materials/happyreason/46.PNG'},
    {'name': 'materials/sadreason/40.PNG', 'path': 'materials/sadreason/40.PNG'},
    {'name': 'materials/situations/14.PNG', 'path': 'materials/situations/14.PNG'},
    {'name': 'materials/situations/42.PNG', 'path': 'materials/situations/42.PNG'},
    {'name': 'materials/sadending/41.PNG', 'path': 'materials/sadending/41.PNG'},
    {'name': 'materials/happyreason/48.PNG', 'path': 'materials/happyreason/48.PNG'},
    {'name': 'materials/sadending/3.PNG', 'path': 'materials/sadending/3.PNG'},
    {'name': 'materials/happyending/15.PNG', 'path': 'materials/happyending/15.PNG'},
    {'name': 'materials/happyreason/9.PNG', 'path': 'materials/happyreason/9.PNG'},
    {'name': 'materials/sadreason/7.PNG', 'path': 'materials/sadreason/7.PNG'},
    {'name': 'materials/goodpropose/28.PNG', 'path': 'materials/goodpropose/28.PNG'},
    {'name': 'materials/sadending/40.PNG', 'path': 'materials/sadending/40.PNG'},
    {'name': 'materials/goodpropose/4.PNG', 'path': 'materials/goodpropose/4.PNG'},
    {'name': 'materials/goodpropose/43.PNG', 'path': 'materials/goodpropose/43.PNG'},
    {'name': 'materials/situations/19.PNG', 'path': 'materials/situations/19.PNG'},
    {'name': 'materials/happyreason/14.PNG', 'path': 'materials/happyreason/14.PNG'},
    {'name': 'materials/badpropose/42.PNG', 'path': 'materials/badpropose/42.PNG'},
    {'name': 'materials/goodpropose/34.PNG', 'path': 'materials/goodpropose/34.PNG'},
    {'name': 'materials/sadreason/17.PNG', 'path': 'materials/sadreason/17.PNG'},
    {'name': 'materials/happyreason/12.PNG', 'path': 'materials/happyreason/12.PNG'},
    {'name': 'materials/happyending/46.PNG', 'path': 'materials/happyending/46.PNG'},
    {'name': 'materials/badpropose/6.PNG', 'path': 'materials/badpropose/6.PNG'},
    {'name': 'materials/situations/41.PNG', 'path': 'materials/situations/41.PNG'},
    {'name': 'materials/sadreason/43.PNG', 'path': 'materials/sadreason/43.PNG'},
    {'name': 'materials/happyreason/20.PNG', 'path': 'materials/happyreason/20.PNG'},
    {'name': 'materials/situations/13.PNG', 'path': 'materials/situations/13.PNG'},
    {'name': 'materials/sadending/8.PNG', 'path': 'materials/sadending/8.PNG'},
    {'name': 'materials/goodpropose/22.PNG', 'path': 'materials/goodpropose/22.PNG'},
    {'name': 'materials/happyending/22.PNG', 'path': 'materials/happyending/22.PNG'},
    {'name': 'materials/badpropose/20.PNG', 'path': 'materials/badpropose/20.PNG'},
    {'name': 'materials/sadreason/9.PNG', 'path': 'materials/sadreason/9.PNG'},
    {'name': 'materials/happyreason/5.PNG', 'path': 'materials/happyreason/5.PNG'},
    {'name': 'materials/happyending/14.PNG', 'path': 'materials/happyending/14.PNG'},
    {'name': 'materials/happyreason/19.PNG', 'path': 'materials/happyreason/19.PNG'},
    {'name': 'materials/sadreason/10.PNG', 'path': 'materials/sadreason/10.PNG'},
    {'name': 'materials/goodpropose/18.PNG', 'path': 'materials/goodpropose/18.PNG'},
    {'name': 'materials/sadending/35.PNG', 'path': 'materials/sadending/35.PNG'},
    {'name': 'materials/happyending/6.PNG', 'path': 'materials/happyending/6.PNG'},
    {'name': 'materials/goodpropose/29.PNG', 'path': 'materials/goodpropose/29.PNG'},
    {'name': 'materials/badpropose/29.PNG', 'path': 'materials/badpropose/29.PNG'},
    {'name': 'materials/sadending/42.PNG', 'path': 'materials/sadending/42.PNG'},
    {'name': 'materials/sadreason/12.PNG', 'path': 'materials/sadreason/12.PNG'},
    {'name': 'materials/badpropose/41.PNG', 'path': 'materials/badpropose/41.PNG'},
    {'name': 'materials/situations/23.PNG', 'path': 'materials/situations/23.PNG'},
    {'name': 'materials/goodpropose/2.PNG', 'path': 'materials/goodpropose/2.PNG'},
    {'name': 'materials/happyending/21.PNG', 'path': 'materials/happyending/21.PNG'},
    {'name': 'materials/happyreason/18.PNG', 'path': 'materials/happyreason/18.PNG'},
    {'name': 'materials/happyreason/37.PNG', 'path': 'materials/happyreason/37.PNG'},
    {'name': 'materials/badpropose/21.PNG', 'path': 'materials/badpropose/21.PNG'},
    {'name': 'materials/happyreason/33.PNG', 'path': 'materials/happyreason/33.PNG'},
    {'name': 'materials/sadreason/34.PNG', 'path': 'materials/sadreason/34.PNG'},
    {'name': 'materials/happyending/9.PNG', 'path': 'materials/happyending/9.PNG'},
    {'name': 'materials/happyending/33.PNG', 'path': 'materials/happyending/33.PNG'},
    {'name': 'materials/sadreason/37.PNG', 'path': 'materials/sadreason/37.PNG'},
    {'name': 'materials/situations/21.PNG', 'path': 'materials/situations/21.PNG'},
    {'name': 'materials/sadending/12.PNG', 'path': 'materials/sadending/12.PNG'},
    {'name': 'materials/situations/35.PNG', 'path': 'materials/situations/35.PNG'},
    {'name': 'materials/situations/24.PNG', 'path': 'materials/situations/24.PNG'},
    {'name': 'materials/situations/28.PNG', 'path': 'materials/situations/28.PNG'},
    {'name': 'materials/badpropose/45.PNG', 'path': 'materials/badpropose/45.PNG'},
    {'name': 'materials/goodpropose/12.PNG', 'path': 'materials/goodpropose/12.PNG'},
    {'name': 'materials/happyreason/45.PNG', 'path': 'materials/happyreason/45.PNG'},
    {'name': 'materials/sadreason/42.PNG', 'path': 'materials/sadreason/42.PNG'},
    {'name': 'materials/sadending/28.PNG', 'path': 'materials/sadending/28.PNG'},
    {'name': 'materials/goodpropose/39.PNG', 'path': 'materials/goodpropose/39.PNG'},
    {'name': 'materials/situations/27.PNG', 'path': 'materials/situations/27.PNG'},
    {'name': 'materials/happyending/37.PNG', 'path': 'materials/happyending/37.PNG'},
    {'name': 'materials/goodpropose/11.PNG', 'path': 'materials/goodpropose/11.PNG'},
    {'name': 'materials/badpropose/33.PNG', 'path': 'materials/badpropose/33.PNG'},
    {'name': 'materials/sadending/17.PNG', 'path': 'materials/sadending/17.PNG'},
    {'name': 'materials/happyending/17.PNG', 'path': 'materials/happyending/17.PNG'},
    {'name': 'materials/situations/8.PNG', 'path': 'materials/situations/8.PNG'},
    {'name': 'materials/situations/31.PNG', 'path': 'materials/situations/31.PNG'},
    {'name': 'materials/happyending/19.PNG', 'path': 'materials/happyending/19.PNG'},
    {'name': 'materials/badpropose/12.PNG', 'path': 'materials/badpropose/12.PNG'},
    {'name': 'materials/happyending/43.PNG', 'path': 'materials/happyending/43.PNG'},
    {'name': 'materials/goodpropose/9.PNG', 'path': 'materials/goodpropose/9.PNG'},
    {'name': 'materials/situations/4.PNG', 'path': 'materials/situations/4.PNG'},
    {'name': 'materials/sadending/26.PNG', 'path': 'materials/sadending/26.PNG'},
    {'name': 'materials/goodpropose/33.PNG', 'path': 'materials/goodpropose/33.PNG'},
    {'name': 'materials/situations/9.PNG', 'path': 'materials/situations/9.PNG'},
    {'name': 'materials/badpropose/34.PNG', 'path': 'materials/badpropose/34.PNG'},
    {'name': 'materials/sadending/46.PNG', 'path': 'materials/sadending/46.PNG'},
    {'name': 'materials/happyending/34.PNG', 'path': 'materials/happyending/34.PNG'},
    {'name': 'materials/sadreason/6.PNG', 'path': 'materials/sadreason/6.PNG'},
    {'name': 'materials/badpropose/14.PNG', 'path': 'materials/badpropose/14.PNG'},
    {'name': 'materials/goodpropose/19.PNG', 'path': 'materials/goodpropose/19.PNG'},
    {'name': 'materials/happyreason/17.PNG', 'path': 'materials/happyreason/17.PNG'},
    {'name': 'materials/situations/33.PNG', 'path': 'materials/situations/33.PNG'},
    {'name': 'materials/sadending/4.PNG', 'path': 'materials/sadending/4.PNG'},
    {'name': 'materials/sadreason/2.PNG', 'path': 'materials/sadreason/2.PNG'},
    {'name': 'materials/goodpropose/26.PNG', 'path': 'materials/goodpropose/26.PNG'},
    {'name': 'materials/badpropose/48.PNG', 'path': 'materials/badpropose/48.PNG'},
    {'name': 'materials/sadending/30.PNG', 'path': 'materials/sadending/30.PNG'},
    {'name': 'materials/goodpropose/8.PNG', 'path': 'materials/goodpropose/8.PNG'},
    {'name': 'materials/situations/26.PNG', 'path': 'materials/situations/26.PNG'},
    {'name': 'materials/sadreason/30.PNG', 'path': 'materials/sadreason/30.PNG'},
    {'name': 'materials/sadending/25.PNG', 'path': 'materials/sadending/25.PNG'},
    {'name': 'materials/badpropose/15.PNG', 'path': 'materials/badpropose/15.PNG'},
    {'name': 'materials/situations/6.PNG', 'path': 'materials/situations/6.PNG'},
    {'name': 'materials/happyending/28.PNG', 'path': 'materials/happyending/28.PNG'},
    {'name': 'materials/sadreason/1.PNG', 'path': 'materials/sadreason/1.PNG'},
    {'name': 'materials/situations/44.PNG', 'path': 'materials/situations/44.PNG'},
    {'name': 'materials/sadending/9.PNG', 'path': 'materials/sadending/9.PNG'},
    {'name': 'materials/situations/29.PNG', 'path': 'materials/situations/29.PNG'},
    {'name': 'materials/sadreason/13.PNG', 'path': 'materials/sadreason/13.PNG'},
    {'name': 'materials/sadending/13.PNG', 'path': 'materials/sadending/13.PNG'},
    {'name': 'materials/sadending/14.PNG', 'path': 'materials/sadending/14.PNG'},
    {'name': 'materials/happyreason/15.PNG', 'path': 'materials/happyreason/15.PNG'},
    {'name': 'materials/badpropose/47.PNG', 'path': 'materials/badpropose/47.PNG'},
    {'name': 'materials/happyending/8.PNG', 'path': 'materials/happyending/8.PNG'},
    {'name': 'materials/sadreason/45.PNG', 'path': 'materials/sadreason/45.PNG'},
    {'name': 'materials/sadending/48.PNG', 'path': 'materials/sadending/48.PNG'},
    {'name': 'materials/sadreason/24.PNG', 'path': 'materials/sadreason/24.PNG'},
    {'name': 'materials/situations/17.PNG', 'path': 'materials/situations/17.PNG'},
    {'name': 'materials/sadreason/36.PNG', 'path': 'materials/sadreason/36.PNG'},
    {'name': 'materials/goodpropose/32.PNG', 'path': 'materials/goodpropose/32.PNG'},
    {'name': 'materials/sadending/37.PNG', 'path': 'materials/sadending/37.PNG'},
    {'name': 'materials/sadreason/19.PNG', 'path': 'materials/sadreason/19.PNG'},
    {'name': 'materials/sadending/10.PNG', 'path': 'materials/sadending/10.PNG'},
    {'name': 'materials/situations/39.PNG', 'path': 'materials/situations/39.PNG'},
    {'name': 'materials/sadreason/21.PNG', 'path': 'materials/sadreason/21.PNG'},
    {'name': 'materials/situations/2.PNG', 'path': 'materials/situations/2.PNG'},
    {'name': 'materials/badpropose/17.PNG', 'path': 'materials/badpropose/17.PNG'},
    {'name': 'materials/situations/34.PNG', 'path': 'materials/situations/34.PNG'},
    {'name': 'materials/happyending/44.PNG', 'path': 'materials/happyending/44.PNG'},
    {'name': 'materials/sadending/45.PNG', 'path': 'materials/sadending/45.PNG'},
    {'name': 'materials/sadreason/27.PNG', 'path': 'materials/sadreason/27.PNG'},
    {'name': 'materials/happyending/10.PNG', 'path': 'materials/happyending/10.PNG'},
    {'name': 'materials/sadreason/41.PNG', 'path': 'materials/sadreason/41.PNG'},
    {'name': 'materials/happyending/39.PNG', 'path': 'materials/happyending/39.PNG'},
    {'name': 'materials/badpropose/24.PNG', 'path': 'materials/badpropose/24.PNG'},
    {'name': 'materials/goodpropose/31.PNG', 'path': 'materials/goodpropose/31.PNG'},
    {'name': 'materials/happyreason/10.PNG', 'path': 'materials/happyreason/10.PNG'},
    {'name': 'materials/sadending/43.PNG', 'path': 'materials/sadending/43.PNG'},
    {'name': 'materials/happyreason/26.PNG', 'path': 'materials/happyreason/26.PNG'},
    {'name': 'materials/sadreason/5.PNG', 'path': 'materials/sadreason/5.PNG'},
    {'name': 'materials/goodpropose/41.PNG', 'path': 'materials/goodpropose/41.PNG'},
    {'name': 'materials/happyreason/1.PNG', 'path': 'materials/happyreason/1.PNG'},
    {'name': 'materials/happyending/12.PNG', 'path': 'materials/happyending/12.PNG'},
    {'name': 'materials/happyreason/2.PNG', 'path': 'materials/happyreason/2.PNG'},
    {'name': 'materials/happyreason/28.PNG', 'path': 'materials/happyreason/28.PNG'},
    {'name': 'materials/situations/5.PNG', 'path': 'materials/situations/5.PNG'},
    {'name': 'materials/happyreason/8.PNG', 'path': 'materials/happyreason/8.PNG'},
    {'name': 'materials/goodpropose/14.PNG', 'path': 'materials/goodpropose/14.PNG'},
    {'name': 'materials/happyending/23.PNG', 'path': 'materials/happyending/23.PNG'},
    {'name': 'materials/happyending/20.PNG', 'path': 'materials/happyending/20.PNG'},
    {'name': 'materials/badpropose/8.PNG', 'path': 'materials/badpropose/8.PNG'},
    {'name': 'materials/sadending/38.PNG', 'path': 'materials/sadending/38.PNG'},
    {'name': 'materials/sadreason/38.PNG', 'path': 'materials/sadreason/38.PNG'},
    {'name': 'materials/situations/11.PNG', 'path': 'materials/situations/11.PNG'},
    {'name': 'materials/situations/7.PNG', 'path': 'materials/situations/7.PNG'},
    {'name': 'materials/sadending/2.PNG', 'path': 'materials/sadending/2.PNG'},
    {'name': 'materials/sadreason/8.PNG', 'path': 'materials/sadreason/8.PNG'},
    {'name': 'materials/sadending/22.PNG', 'path': 'materials/sadending/22.PNG'},
    {'name': 'materials/badpropose/38.PNG', 'path': 'materials/badpropose/38.PNG'},
    {'name': 'materials/badpropose/46.PNG', 'path': 'materials/badpropose/46.PNG'},
    {'name': 'materials/sadending/32.PNG', 'path': 'materials/sadending/32.PNG'},
    {'name': 'materials/situations/46.PNG', 'path': 'materials/situations/46.PNG'},
    {'name': 'materials/situations/38.PNG', 'path': 'materials/situations/38.PNG'},
    {'name': 'materials/situations/40.PNG', 'path': 'materials/situations/40.PNG'},
    {'name': 'materials/goodpropose/45.PNG', 'path': 'materials/goodpropose/45.PNG'},
    {'name': 'materials/goodpropose/40.PNG', 'path': 'materials/goodpropose/40.PNG'},
    {'name': 'materials/happyending/45.PNG', 'path': 'materials/happyending/45.PNG'},
    {'name': 'materials/situations/3.PNG', 'path': 'materials/situations/3.PNG'},
    {'name': 'materials/happyending/40.PNG', 'path': 'materials/happyending/40.PNG'},
    {'name': 'materials/badpropose/5.PNG', 'path': 'materials/badpropose/5.PNG'},
    {'name': 'materials/badpropose/1.PNG', 'path': 'materials/badpropose/1.PNG'},
    {'name': 'materials/badpropose/31.PNG', 'path': 'materials/badpropose/31.PNG'},
    {'name': 'materials/badpropose/7.PNG', 'path': 'materials/badpropose/7.PNG'},
    {'name': 'materials/Test_intro.JPG', 'path': 'materials/Test_intro.JPG'},
    {'name': 'materials/sadending/6.PNG', 'path': 'materials/sadending/6.PNG'},
    {'name': 'materials/happyreason/23.PNG', 'path': 'materials/happyreason/23.PNG'},
    {'name': 'materials/badpropose/26.PNG', 'path': 'materials/badpropose/26.PNG'},
    {'name': 'materials/badpropose/13.PNG', 'path': 'materials/badpropose/13.PNG'},
    {'name': 'materials/situations/15.PNG', 'path': 'materials/situations/15.PNG'},
    {'name': 'materials/happyending/26.PNG', 'path': 'materials/happyending/26.PNG'},
    {'name': 'materials/happyreason/31.PNG', 'path': 'materials/happyreason/31.PNG'},
    {'name': 'materials/happyreason/21.PNG', 'path': 'materials/happyreason/21.PNG'},
    {'name': 'materials/situations/12.PNG', 'path': 'materials/situations/12.PNG'},
    {'name': 'materials/goodpropose/44.PNG', 'path': 'materials/goodpropose/44.PNG'},
    {'name': 'materials/situations/20.PNG', 'path': 'materials/situations/20.PNG'},
    {'name': 'materials/situations/25.PNG', 'path': 'materials/situations/25.PNG'},
    {'name': 'materials/badpropose/9.PNG', 'path': 'materials/badpropose/9.PNG'},
    {'name': 'materials/sadending/1.PNG', 'path': 'materials/sadending/1.PNG'},
    {'name': 'materials/happyreason/40.PNG', 'path': 'materials/happyreason/40.PNG'},
    {'name': 'materials/goodpropose/46.PNG', 'path': 'materials/goodpropose/46.PNG'},
    {'name': 'materials/happyreason/41.PNG', 'path': 'materials/happyreason/41.PNG'},
    {'name': 'materials/situations/1.PNG', 'path': 'materials/situations/1.PNG'},
    {'name': 'materials/happyending/1.PNG', 'path': 'materials/happyending/1.PNG'},
    {'name': 'materials/situations/37.PNG', 'path': 'materials/situations/37.PNG'},
    {'name': 'materials/goodpropose/24.PNG', 'path': 'materials/goodpropose/24.PNG'},
    {'name': 'materials/happyreason/6.PNG', 'path': 'materials/happyreason/6.PNG'},
    {'name': 'materials/goodpropose/20.PNG', 'path': 'materials/goodpropose/20.PNG'},
    {'name': 'materials/sadending/11.PNG', 'path': 'materials/sadending/11.PNG'},
    {'name': 'materials/happyreason/34.PNG', 'path': 'materials/happyreason/34.PNG'},
    {'name': 'materials/happyending/36.PNG', 'path': 'materials/happyending/36.PNG'},
    {'name': 'materials/happyreason/22.PNG', 'path': 'materials/happyreason/22.PNG'},
    {'name': 'materials/happyreason/11.PNG', 'path': 'materials/happyreason/11.PNG'},
    {'name': 'sessions/session2/order_0.xlsx', 'path': 'sessions/session2/order_0.xlsx'},
    {'name': 'materials/sadending/36.PNG', 'path': 'materials/sadending/36.PNG'},
    {'name': 'materials/happyending/24.PNG', 'path': 'materials/happyending/24.PNG'},
    {'name': 'materials/sadending/19.PNG', 'path': 'materials/sadending/19.PNG'},
    {'name': 'materials/happyreason/7.PNG', 'path': 'materials/happyreason/7.PNG'},
    {'name': 'materials/goodpropose/10.PNG', 'path': 'materials/goodpropose/10.PNG'},
    {'name': 'materials/happyreason/24.PNG', 'path': 'materials/happyreason/24.PNG'},
    {'name': 'materials/sadreason/35.PNG', 'path': 'materials/sadreason/35.PNG'},
    {'name': 'materials/happyending/48.PNG', 'path': 'materials/happyending/48.PNG'},
    {'name': 'materials/happyreason/25.PNG', 'path': 'materials/happyreason/25.PNG'},
    {'name': 'materials/badpropose/43.PNG', 'path': 'materials/badpropose/43.PNG'},
    {'name': 'materials/sadending/29.PNG', 'path': 'materials/sadending/29.PNG'},
    {'name': 'materials/situations/36.PNG', 'path': 'materials/situations/36.PNG'},
    {'name': 'materials/sadreason/32.PNG', 'path': 'materials/sadreason/32.PNG'},
    {'name': 'materials/goodpropose/37.PNG', 'path': 'materials/goodpropose/37.PNG'},
    {'name': 'materials/sadreason/14.PNG', 'path': 'materials/sadreason/14.PNG'},
    {'name': 'materials/sadreason/22.PNG', 'path': 'materials/sadreason/22.PNG'},
    {'name': 'materials/sadreason/33.PNG', 'path': 'materials/sadreason/33.PNG'},
    {'name': 'materials/sadending/21.PNG', 'path': 'materials/sadending/21.PNG'},
    {'name': 'materials/happyreason/13.PNG', 'path': 'materials/happyreason/13.PNG'},
    {'name': 'materials/sadending/24.PNG', 'path': 'materials/sadending/24.PNG'},
    {'name': 'materials/happyending/11.PNG', 'path': 'materials/happyending/11.PNG'},
    {'name': 'materials/badpropose/2.PNG', 'path': 'materials/badpropose/2.PNG'},
    {'name': 'materials/goodpropose/27.PNG', 'path': 'materials/goodpropose/27.PNG'},
    {'name': 'materials/badpropose/40.PNG', 'path': 'materials/badpropose/40.PNG'},
    {'name': 'materials/situations/22.PNG', 'path': 'materials/situations/22.PNG'},
    {'name': 'materials/situations/43.PNG', 'path': 'materials/situations/43.PNG'},
    {'name': 'materials/happyending/31.PNG', 'path': 'materials/happyending/31.PNG'},
    {'name': 'materials/situations/48.PNG', 'path': 'materials/situations/48.PNG'},
    {'name': 'materials/happyending/25.PNG', 'path': 'materials/happyending/25.PNG'},
    {'name': 'materials/goodpropose/48.PNG', 'path': 'materials/goodpropose/48.PNG'},
    {'name': 'materials/badpropose/11.PNG', 'path': 'materials/badpropose/11.PNG'},
    {'name': 'materials/goodpropose/23.PNG', 'path': 'materials/goodpropose/23.PNG'},
    {'name': 'materials/happyreason/27.PNG', 'path': 'materials/happyreason/27.PNG'},
    {'name': 'materials/happyending/27.PNG', 'path': 'materials/happyending/27.PNG'},
    {'name': 'materials/badpropose/36.PNG', 'path': 'materials/badpropose/36.PNG'},
    {'name': 'materials/sadending/33.PNG', 'path': 'materials/sadending/33.PNG'},
    {'name': 'materials/happyreason/39.PNG', 'path': 'materials/happyreason/39.PNG'},
    {'name': 'materials/sadending/34.PNG', 'path': 'materials/sadending/34.PNG'},
    {'name': 'materials/sadreason/28.PNG', 'path': 'materials/sadreason/28.PNG'},
    {'name': 'materials/situations/30.PNG', 'path': 'materials/situations/30.PNG'},
    {'name': 'materials/goodpropose/42.PNG', 'path': 'materials/goodpropose/42.PNG'},
    {'name': 'materials/badpropose/19.PNG', 'path': 'materials/badpropose/19.PNG'},
    {'name': 'materials/sadending/15.PNG', 'path': 'materials/sadending/15.PNG'},
    {'name': 'materials/badpropose/30.PNG', 'path': 'materials/badpropose/30.PNG'},
    {'name': 'materials/sadreason/46.PNG', 'path': 'materials/sadreason/46.PNG'},
    {'name': 'materials/goodpropose/36.PNG', 'path': 'materials/goodpropose/36.PNG'},
    {'name': 'materials/goodpropose/1.PNG', 'path': 'materials/goodpropose/1.PNG'},
    {'name': 'materials/happyending/18.PNG', 'path': 'materials/happyending/18.PNG'},
    {'name': 'materials/sadreason/26.PNG', 'path': 'materials/sadreason/26.PNG'},
    {'name': 'materials/situations/32.PNG', 'path': 'materials/situations/32.PNG'},
    {'name': 'materials/happyreason/36.PNG', 'path': 'materials/happyreason/36.PNG'},
    {'name': 'materials/sadreason/11.PNG', 'path': 'materials/sadreason/11.PNG'},
    {'name': 'materials/sadreason/29.PNG', 'path': 'materials/sadreason/29.PNG'},
    {'name': 'materials/happyreason/43.PNG', 'path': 'materials/happyreason/43.PNG'},
    {'name': 'materials/sadreason/15.PNG', 'path': 'materials/sadreason/15.PNG'},
    {'name': 'materials/situations/47.PNG', 'path': 'materials/situations/47.PNG'},
    {'name': 'materials/happyreason/47.PNG', 'path': 'materials/happyreason/47.PNG'},
    {'name': 'materials/goodpropose/38.PNG', 'path': 'materials/goodpropose/38.PNG'},
    {'name': 'materials/happyending/7.PNG', 'path': 'materials/happyending/7.PNG'},
    {'name': 'materials/badpropose/37.PNG', 'path': 'materials/badpropose/37.PNG'},
    {'name': 'materials/sadending/7.PNG', 'path': 'materials/sadending/7.PNG'},
    {'name': 'materials/happyending/47.PNG', 'path': 'materials/happyending/47.PNG'},
    {'name': 'materials/sadreason/25.PNG', 'path': 'materials/sadreason/25.PNG'},
    {'name': 'materials/goodpropose/15.PNG', 'path': 'materials/goodpropose/15.PNG'},
    {'name': 'materials/goodpropose/35.PNG', 'path': 'materials/goodpropose/35.PNG'},
    {'name': 'materials/goodpropose/21.PNG', 'path': 'materials/goodpropose/21.PNG'},
    {'name': 'materials/situations/18.PNG', 'path': 'materials/situations/18.PNG'},
    {'name': 'materials/sadending/27.PNG', 'path': 'materials/sadending/27.PNG'},
    {'name': 'materials/badpropose/18.PNG', 'path': 'materials/badpropose/18.PNG'},
    {'name': 'materials/goodpropose/3.PNG', 'path': 'materials/goodpropose/3.PNG'},
    {'name': 'materials/goodpropose/13.PNG', 'path': 'materials/goodpropose/13.PNG'},
    {'name': 'materials/situations/45.PNG', 'path': 'materials/situations/45.PNG'}
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


var introClock;
var image;
var key_resp;
var backgroundClock;
var back;
var key_resp_2;
var predictClock;
var predictp;
var key_resp_3;
var pseClock;
var predictp_2;
var key_resp_5;
var behClock;
var text;
var resClock;
var predictp_3;
var trialClock;
var trialnum;
var slider;
var text_2;
var text_3;
var text_4;
var restClock;
var dur;
var text_5;
var key_resp_6;
var thanksClock;
var text_11;
var key_resp_4;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  // Run 'Begin Experiment' code from startup_code
  //import * as random from 'random';
  //import * as np from 'numpy';
  //var order_num, seed;
  //seed = Number.parseInt(expInfo["randomization"]);
  //if ((seed === (- 1))) {
  //    seed = Number.parseInt(expInfo["participant"]);
  //}
  //np.random.seed(seed);
  //random.seed(seed);
  //order_num = Number.parseInt((Math.random() * 50));
  //order_file = ((`sessions/session${expInfo["session"]}/order_` + order_num.toString()) + ".xlsx");
  //order_file = (("sessions/session" + expInfo['session']+"/order_" + order_num.toString()) + ".xlsx");
  //console.log(order_file)
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'materials/Test_intro.JPG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "background"
  backgroundClock = new util.Clock();
  back = new visual.ImageStim({
    win : psychoJS.window,
    name : 'back', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "predict"
  predictClock = new util.Clock();
  predictp = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictp', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pse"
  pseClock = new util.Clock();
  predictp_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictp_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "beh"
  behClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "res"
  resClock = new util.Clock();
  predictp_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictp_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Run 'Begin Experiment' code from code_3
  trialnum = 0;
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: 4,
    size: [0.8, 0.08], pos: [0, (- 0.2)], ori: 0.0, units: 'height',
    labels: [1, 2, 3, 4, 5, 6, 7], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '绝对不可以的                                                       完全可以的',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.01), (- 0.13)], height: 0.04,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), 1.0, 1.0]),  opacity: undefined,
    depth: -3.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '请使用鼠标移动滑块以给出您的评分',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  dur = 0;
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '您现在已经完成了新20个试次，\n\n您可以休息最多60秒\n\n按任意键以继续实验',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '您现在已经完成了上机部分的实验，\n\n请您休息一会儿，\n谢谢您的参与！',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(image);
    introComponents.push(key_resp);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
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
      trialList: 'sessions/session2/order_0.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(backgroundRoutineBegin(snapshot));
      trialsLoopScheduler.add(backgroundRoutineEachFrame());
      trialsLoopScheduler.add(backgroundRoutineEnd(snapshot));
      trialsLoopScheduler.add(predictRoutineBegin(snapshot));
      trialsLoopScheduler.add(predictRoutineEachFrame());
      trialsLoopScheduler.add(predictRoutineEnd(snapshot));
      trialsLoopScheduler.add(pseRoutineBegin(snapshot));
      trialsLoopScheduler.add(pseRoutineEachFrame());
      trialsLoopScheduler.add(pseRoutineEnd(snapshot));
      trialsLoopScheduler.add(behRoutineBegin(snapshot));
      trialsLoopScheduler.add(behRoutineEachFrame());
      trialsLoopScheduler.add(behRoutineEnd(snapshot));
      trialsLoopScheduler.add(resRoutineBegin(snapshot));
      trialsLoopScheduler.add(resRoutineEachFrame());
      trialsLoopScheduler.add(resRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(restRoutineBegin(snapshot));
      trialsLoopScheduler.add(restRoutineEachFrame());
      trialsLoopScheduler.add(restRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
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


var _key_resp_2_allKeys;
var backgroundComponents;
function backgroundRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'background' ---
    t = 0;
    backgroundClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    back.setImage(situation);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    backgroundComponents = [];
    backgroundComponents.push(back);
    backgroundComponents.push(key_resp_2);
    
    for (const thisComponent of backgroundComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function backgroundRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'background' ---
    // get current time
    t = backgroundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *back* updates
    if (t >= 0.0 && back.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      back.tStart = t;  // (not accounting for frame time here)
      back.frameNStart = frameN;  // exact frame index
      
      back.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (back.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      back.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of backgroundComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function backgroundRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'background' ---
    for (const thisComponent of backgroundComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var predictComponents;
function predictRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'predict' ---
    t = 0;
    predictClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    predictp.setImage(reason);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    predictComponents = [];
    predictComponents.push(predictp);
    predictComponents.push(key_resp_3);
    
    for (const thisComponent of predictComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function predictRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'predict' ---
    // get current time
    t = predictClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *predictp* updates
    if (t >= 0.0 && predictp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictp.tStart = t;  // (not accounting for frame time here)
      predictp.frameNStart = frameN;  // exact frame index
      
      predictp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictp.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
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
    for (const thisComponent of predictComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function predictRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'predict' ---
    for (const thisComponent of predictComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var pseComponents;
function pseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pse' ---
    t = 0;
    pseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.300000);
    // update component parameters for each repeat
    predictp_2.setImage(propose);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    pseComponents = [];
    pseComponents.push(predictp_2);
    pseComponents.push(key_resp_5);
    
    for (const thisComponent of pseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pse' ---
    // get current time
    t = pseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *predictp_2* updates
    if (t >= 0.0 && predictp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictp_2.tStart = t;  // (not accounting for frame time here)
      predictp_2.frameNStart = frameN;  // exact frame index
      
      predictp_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictp_2.setAutoDraw(false);
    }
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    frameRemains = 0.0 + 2.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_5.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: [], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
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
    for (const thisComponent of pseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pse' ---
    for (const thisComponent of pseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var behComponents;
function behRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'beh' ---
    t = 0;
    behClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    text.setText(behave);
    // keep track of which components have finished
    behComponents = [];
    behComponents.push(text);
    
    for (const thisComponent of behComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function behRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'beh' ---
    // get current time
    t = behClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
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
    for (const thisComponent of behComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function behRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'beh' ---
    for (const thisComponent of behComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var resComponents;
function resRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'res' ---
    t = 0;
    resClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.300000);
    // update component parameters for each repeat
    predictp_3.setImage(ending);
    // keep track of which components have finished
    resComponents = [];
    resComponents.push(predictp_3);
    
    for (const thisComponent of resComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function resRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'res' ---
    // get current time
    t = resClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *predictp_3* updates
    if (t >= 0.0 && predictp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictp_3.tStart = t;  // (not accounting for frame time here)
      predictp_3.frameNStart = frameN;  // exact frame index
      
      predictp_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictp_3.setAutoDraw(false);
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
    for (const thisComponent of resComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function resRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'res' ---
    for (const thisComponent of resComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider.reset()
    text_3.setText(evaluation);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(slider);
    trialComponents.push(text_2);
    trialComponents.push(text_3);
    trialComponents.push(text_4);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // Check slider for response to end routine
    if (slider.getRating() !== undefined && slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
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
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_3
    trialnum += 1;
    
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_6_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest' ---
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    if (((trialnum % 20) === 0)) {
        dur = 60;
    }
    
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(text_5);
    restComponents.push(key_resp_6);
    
    for (const thisComponent of restComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest' ---
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    frameRemains = 0.0 + dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_6.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: [], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
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
    for (const thisComponent of restComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest' ---
    for (const thisComponent of restComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code
    dur = 0;
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_4_allKeys;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(text_11);
    thanksComponents.push(key_resp_4);
    
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_11.setAutoDraw(false);
    }
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: [], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
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
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    for (const thisComponent of thanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
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
