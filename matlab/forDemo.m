% ping pong ball
[test_file_path, test_sample_rate] = audioread('ball.WAV');

% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

test_coeffs = test_coeffs(:, 1:13);  % Ensure only 13 coefficients are used

% Save MFCCs to a CSV file
csvwrite('ball.csv', test_coeffs);

% hello
[test_file_path, test_sample_rate] = audioread('hello.WAV');

% Extract MFCCs from test audio
test_coeffs = mfcc(test_file_path, test_sample_rate, 'NumCoeffs', 13);

test_coeffs = test_coeffs(:, 1:13);  % Ensure only 13 coefficients are used

% Save MFCCs to a CSV file
csvwrite('hello.csv', test_coeffs);