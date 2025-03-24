%% renaming
% Define the folder containing the files
folder = 'linus_data_wav';

% Get all files in the folder
files = dir(fullfile(folder, '*'));

% Loop through each file
for i = 1:length(files)
    % Only process files (skip directories)
    if ~files(i).isdir
        % Get the original file name (without extension)
        [~, name, ext] = fileparts(files(i).name);
        
        % Check if the file name is a number
        if ~isempty(regexp(name, '^\d+$', 'once'))
            % Construct the new file name
            new_name = ['pong_' name ext];
            
            % Rename the file
            movefile(fullfile(folder, files(i).name), fullfile(folder, new_name));
        end
    end
end

%% til linus filer
% Filename
initialString = 'linus_data_wav/pong_';

% Number of files
numIterations = 116;

% Loop through each file
for i = 1:numIterations
    saveAs = 'linus_data_csv/pong_';
    % Create the new string by appending the iteration number
    newString = [initialString, num2str(i)];
    newFilePath = [newString, '.wav'];

    % saving mfcc
    [file_path, sample_rate] = audioread(newFilePath);
    coeffs = mfcc(file_path, sample_rate, 'NumCoeffs', 13);

     coeffs = coeffs(:, 1:13);  % Ensure only 13 coefficients are used

    saveAs = [saveAs, num2str(i) '.csv'];
    csvwrite(saveAs, coeffs);

    % Print the new string
    disp(newFilePath)
    disp(saveAs)
end

%% synthetic data
% Filename
initialString = 'synthetic_';

% Number of files
numIterations = 4;

% Loop through each file
for i = 1:numIterations
    % Create the new string by appending the iteration number
    newString = [initialString, num2str(i)];
    newFilePath = [newString, '.wav'];

    % saving mfcc
    [file_path, sample_rate] = audioread(newFilePath);
    coeffs = mfcc(file_path, sample_rate, NumCoeffs=13);

    saveAs = [newString, '.csv'];
    csvwrite(saveAs, coeffs);

    % Print the new string
    disp(newFilePath)
    disp(saveAs)
end
