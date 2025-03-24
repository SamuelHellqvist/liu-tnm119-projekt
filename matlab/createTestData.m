%% ping pong ball
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/test - pingpong ball.WAV');

% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

test_coeffs = test_coeffs(:, 1:13);  % Ensure only 13 coefficients are used

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

%% silent pingpongball (should be ping pong ball)
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/tystPingPongBall2.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_silentPingPongBall.csv', test_coeffs);

%% clear pingpongball (should be ping pong ball)
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/pongStuds.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_pongStuds.csv', test_coeffs);

%% talking
[test_file_path, test_sample_rate] = audioread('ljudklipp/inspelat ljud/prat.wav');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_prat.csv', test_coeffs);

%% another positive test
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/pos_test.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_pos_test.csv', test_coeffs);

%% positive test from trappan
[test_file_path, test_sample_rate] = audioread('ljudklipp/testljud/trappan_test.WAV');


% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

% Save MFCCs to a CSV file
csvwrite('test_mfcc_features_trappan_pos.csv', test_coeffs);