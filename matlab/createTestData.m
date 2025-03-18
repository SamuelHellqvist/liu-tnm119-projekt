%% ping pong ball
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/test - pingpong ball.WAV');

% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('features/test_mfcc_features_pingpongBall.csv', test_coeffs);
%% background noise
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/test - background noise.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('features/test_mfcc_features_backgroundNoise.csv', test_coeffs);

%% silence noise (should be background noice)
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/test-silence.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_silence.csv', test_coeffs);
