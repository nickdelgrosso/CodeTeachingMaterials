from psychopy import logging, data, clock


stim_clock = clock.CountdownTimer(0)

stim_order = [{'vr_object': 10, 'location': 'left',  'duration': .5},
              {'vr_object': 20, 'location': 'right', 'duration': .2}]

trials = data.TrialHandler(stim_order, nReps=4, method='random')

a = 100
for trial in trials:
    stim_clock.reset(trial['duration'])
    while stim_clock.getTime() > 0:
       trials.addData('timeOnClock', stim_clock.getTime())
       print a

    trials.addData('rt', a)
    a += 1
    
    #print trial['vr_object']

#logging.flush()

trials.saveAsText('./test11.txt', appendFile=False)
