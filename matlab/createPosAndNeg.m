%this matlab script is made to create some positive and negative 
% training data

%positives
[pos_file_path, pos_sample_rate] = audioread('ljudklipp/10secOfPingPongBalls.WAV');
pos_coeffs = mfcc(pos_file_path, pos_sample_rate);
csvwrite('pos_mfcc_features.csv', pos_coeffs);

%negatives
[neg_file_path, neg_sample_rate] = audioread('ljudklipp/backGroundNoise.WAV');
neg_coeffs = mfcc(neg_file_path, neg_sample_rate);
csvwrite('neg_mfcc_features.csv', neg_coeffs);