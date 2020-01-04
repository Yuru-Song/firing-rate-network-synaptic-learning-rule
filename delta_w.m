function delta_w = delta_w(vec_s, Pi, W, V, num_neuron, Im0, ef0, ew0, gamma, func_Im,  phys_adj, ei_ratio)
r = V * vec_s;
Sigma = V * Pi * V';
delta_w = zeros(num_neuron, num_neuron);
for i = 1:num_neuron
    for j = 1: num_neuron
        if i~=j && phys_adj(i,j)>0
         
            for s = 1:num_neuron
                for t = s + 1 : num_neuron
                    if (s~=t) && Sigma(s,t)^2/(Sigma(s,s) * Sigma(t,t)) < 0.999 
                        delta_w(i,j) = delta_w(i,j) + func_Im(s,t) * (V(s,i) * (Sigma(s,s) * Sigma(j,t) - Sigma(s,t) * Sigma(j,s)) / Sigma(s,s) + V(t,i) * (Sigma(t,t) * Sigma(j,s)   - Sigma(s,t) * Sigma(j,t)) / Sigma(t,t)) * (Sigma(s,s)*Sigma(t,t) - Sigma(s,t)^2)/Sigma(s,t) ;            
%                     delta_w(i,j) = delta_w(i,j)  ...
%                         + func_Im(s,t)  ...
%                         * (V(s,i) * (Sigma(j,t) +  Sigma(j,s) / (Sigma(s,s) * Sigma(s,t)) - Sigma(j,s)*Sigma(t,t)/Sigma(s,t))...
%                             + V(t,i) * (Sigma(j,s) +  Sigma(j,t) / (Sigma(t,t) * Sigma(s,t)) - Sigma(j,t)*Sigma(s,s)/Sigma(s,t))) ...
%                         * Sigma(s,t)/(Sigma(s,s)*Sigma(t,t) - Sigma(s,t)^2) ;            
                    
                    end
                end
            end
            delta_w(i,j) = delta_w(i,j) *2;
        delta_w(i,j) = delta_w(i,j) / Im0;
        delta_w(i,j) = delta_w(i,j) - ei_ratio * r(j) * sum(V(:,i)) / ef0 ;
        delta_w(i,j) = delta_w(i,j) - ei_ratio * gamma * W(i,j)^(gamma - 1) / ew0 ;
        end
        
    end
end