function [Im, ef, ew] = obj_function (vec_s, Pi, W, V, num_neuron, gamma, func_Im)
Sigma = V * Pi * V';
Im = 0;
for i = 1:num_neuron
    for j = i+1:num_neuron
%         if i~=j
            Im = Im - func_Im(i,j)  * log(Sigma(i,i) * Sigma(j,j) - Sigma(i,j)^2) +  func_Im(i,j)  *log(Sigma(i,i))+ func_Im(i,j)  *log(Sigma(j,j));    
%         end
    end
end
r = V * vec_s;
ef = sum(r) ;
ew = sum(sum(W(find(W>0)).^gamma)) ;
