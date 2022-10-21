clear all
clc

%% Set Up Fieldtrip
ft_defaults
% cd('N:\Del Grosso NA\Data\PriceAgree1');

%% ft_definetrial
% clear cfg
% cfg.dataset = 'PriceAgree1_7Dec2011mittriggers.cnt'
% cfg.trialdef.eventtype = 'trigger';
% cfg.trialdef.eventvalue = [1:6];
% cfg.trialdef.prestim = 0.2;
% cfg.trialdef.poststim = 1;
% 
% cfg = ft_definetrial(cfg)
% 
% %% ft_preprocessing
% cfg.lpfilter = 'no';
% cfg.lpfreq = 35;
% cfg.hpfilter = 'no';
% cfg.demean = 'yes';
% cfg.baselinewindow = [-.2 0];
% 
% data = ft_preprocessing(cfg)

%%  ft_rejectvisual
% 
% clear cfg
% cfg.trials = 'all'
% cfg.channels = 'all'
% 
% data = ft_rejectvisual(cfg,data)

%% ft_timelockanalysis

clear cfg
cfg.keeptrials = 'yes';

timelock = ft_timelockanalysis(cfg,data)

%% Plot
figure(3)
for ee = 1:32;
    subplot(6,6,ee), plot(timelock.time,timelock.avg(ee,:));
    title(timelock.label{ee})
end