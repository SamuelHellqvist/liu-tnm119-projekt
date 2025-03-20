%this matlab script is made to create some positive and negative 
% training data

%positives
[pos_file_path, pos_sample_rate] = audioread('ljudklipp/testljud/10secOfPingPongBalls.WAV');
pos_coeffs = mfcc(pos_file_path, pos_sample_rate);

csvwrite('features/pos_mfcc_features.csv', pos_coeffs);

%%
%negatives
[neg_file_path, neg_sample_rate] = audioread('ljudklipp/testljud/backGroundNoise.WAV');
neg_coeffs = mfcc(neg_file_path, neg_sample_rate);
csvwrite('neg_mfcc_features.csv', neg_coeffs);

% silence (should also be negatives)
[silence_file_path, silence_sample_rate] = audioread('ljudklipp/inspelat ljud/silence.WAV');
silence_coeffs = mfcc(silence_file_path, silence_sample_rate);
csvwrite('silence_mfcc_features.csv', silence_coeffs);

%% data from the internet
[thirdparty_file_path, thirdparty_sample_rate] = audioread('ljudklipp/testljud/fallandeBoll.WAV');
thirdparty_coeffs = mfcc(thirdparty_file_path, thirdparty_sample_rate);
csvwrite('features/thirdparty_mfcc_features.csv', thirdparty_coeffs);


