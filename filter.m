% Read the WAV file
[inputSignal, fs] = audioread('ljudklipp/main_file.wav');

% Design a highpass filter
cutoffFreq = 5000; % Cutoff frequency in Hz
filterOrder = 4; % Filter order
[b, a] = butter(filterOrder, cutoffFreq/(fs/2), 'high');

% Apply the highpass filter
filteredSignal = filter(b, a, inputSignal);

% Write the filtered signal to a new WAV file
audiowrite('filtered_output.wav', filteredSignal, fs);