% Load audio file
[file_path, sample_rate] = audioread('main2.wav');

% Extract MFCCs
coeffs = mfcc(file_path, sample_rate);

% Save MFCCs to a CSV file
csvwrite('mfcc_features.csv', coeffs);