% Load test audio file
[test_file_path, test_sample_rate] = audioread('test - background noise.WAV');

% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features.csv', test_coeffs);