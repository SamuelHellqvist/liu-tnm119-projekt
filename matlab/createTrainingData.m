% Filename
initialString = 'pingPongSound - ';

% Number of files
numIterations = 10;

% Loop through each file
for i = 1:numIterations
    % Create the new string by appending the iteration number
    newString = [initialString, num2str(i)];
    newFilePath = [newString, '.wav'];

    % saving mfcc
    %[file_path, sample_rate] = audioread(newFilePath);
    %coeffs = mfcc(file_path, sample_rate);

    saveAs = [newString, '.csv'];
    %csvwrite(saveAs, coeffs);

    % Print the new string
    disp(newFilePath)
    disp(saveAs)
end