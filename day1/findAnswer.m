function answer = findAnswer(file_name)
fileID = fopen(file_name,'r');
list = fscanf(fileID,'%d\n');
fclose(fileID);

n = findPair(list);
answer = prod(n);


function n = findPair(numberList)
n = zeros(3,1);
for idx1 = 1:length(numberList)
    for idx2 = 1:length(numberList)
        for idx3 = 1:length(numberList)
            n(1) = numberList(idx1);
            n(2) = numberList(idx2);
            n(3) = numberList(idx3);
            if sum(n) == 2020
                return;
            end
        end
    end
end



