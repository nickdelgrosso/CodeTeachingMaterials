function [ Order ] = balanced_latin_squares( nConditions )
%BALANCED_LATIN_SQUARES Generates a condition order for experimens, where
%each condition immediately follows and is immediately preceded by each
%every other condition exactly once.
%   
% Function taken from : https://medium.com/@graycoding/balanced-latin-squares-in-python-2c3aa6ec95b9
% n: Total Number of Conditions
% Order: Matrix of condition order (rows: subjects, columns: order)
%
%  Example: balanced_latin_squares(4)
%  ans =
%      1     2     4     3
%      2     3     1     4
%      3     4     2     1
%      4     1     3     2
%
%
Order = [];
for i = 0:nConditions-1;
    row = [];
    for j = 0:nConditions-1;
        if mod(j, 2) ~= 0;
            condition = floor(j / 2) + 1;
        else
            condition = nConditions - floor(j / 2);
        end
        condition = mod(condition + i, nConditions);
        row = [row, condition];
    end
    Order = [Order; row];
end

% If nConditions is odd, add on a reversed set
if mod(nConditions, 2) ~= 0;
    Order = [Order; fliplr(Order)];
end

Order = Order + 1;
end

