addpath /storage/share/matlab/labbox/Helper/
addpath /storage/share/matlab/labbox/TF

%% Set Path and Parameters
loadpath = '~/Documents/soundtest/';
cd(loadpath)

filelist = dir('*.wav');

filenames = {}
for file = filelist';
    if isempty(strfind(file.name, 'Fan'));
        continue
    end
    temp = file.name;
    %temp = strrep(temp, '_', ' ');
    filenames{end+1} = temp;%(1:end-13);
    
end
ref_file = dir('Fan0_Closed*.wav')
assert(length(ref_file)==1)
ref_file = ref_file.name
ref_idx = find(ismember(filenames, ref_file));

freq_range = [0 15000];
nfft = 4096 ;

%% Calculate Periodogram
n = 0
all_power = []
for file = filenames;    
    n = n + 1;  % File Index 
    
    [data, fs, nbits] = wavread(file{1}); % Read file
    time = 1/fs: 1/fs: length(data)/fs;
    data = data - mean(data);  % Mean-center data
        
    
    % calculate Periodogram
    %[power, freq] = periodogram(data, [], nfft, fs, 'psd'); 
    [power, freq] = mtcsd(data, nfft, fs, nfft);
    all_power = [all_power; power'];
end 

figure()
loglog(freq, all_power, 'LineWidth', 1.5)
xlabel('Frequency (Hz)');
ylabel('Power');
title('Noise Periodogram, using mtcsd() Function')

legend_names = {}
for name = filenames;
    name = strrep(name{1}, '_', ' ');
    legend_names{end+1} = name(1:end-13); 
end
legend(legend_names)
saveas(gcf, 'All Fan Comparison.tif')
% %figure()
% ref_power = repmat( all_power(ref_idx, :), [size(all_power, 1), 1])
% loglog(freq, 1 ./ log(all_power) ./ log(ref_power))



