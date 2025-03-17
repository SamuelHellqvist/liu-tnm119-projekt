% Load audio file
[file_path, sample_rate] = audioread('ljudklipp/inspelat ljud/main_file.wav');

% Extract MFCCs
coeffs = mfcc(file_path, sample_rate);

% Save MFCCs to a CSV file
csvwrite('mfcc_features.csv', coeffs);