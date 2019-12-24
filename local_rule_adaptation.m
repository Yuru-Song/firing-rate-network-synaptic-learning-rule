clear all;
clc;
num_neuron = 100;
vec_s = ones(num_neuron,1)*2;
Pi = diag(random('unif',0,1,[num_neuron,1]));
learning_rate = 1e-5;
ratio_ef_i = 0.0001;
ratio_ew_i = 1;
gamma = 2;
update_time = 20000;
scale_factor = num_neuron;
W = random('unif',0,1,[2,num_neuron,num_neuron]);
for i = 1 : num_neuron
    W(:,i,i) = 0;
end
W = W/scale_factor;
total_Im = zeros(update_time,1);
total_e_f = zeros(update_time,1);
total_e_w = zeros(update_time,1);
func_Im = ones(num_neuron,num_neuron);
func_Im = func_Im - diag(diag(func_Im));
for t1=1:update_time
    if mod(t1,50)==0
        disp('Working mode, please do not touch me!')
        disp('timestep:')
        disp(t1)
    end
    W(1,:,:) = W(2,:,:);
    V = pinv(diag(ones(num_neuron,1)) - reshape(W(1,:,:),[num_neuron,num_neuron]));
    Sigma = V * Pi * V';
    W2 = reshape(W(1,:,:),[num_neuron,num_neuron])*reshape(W(1,:,:),[num_neuron,num_neuron]);
    r = V * vec_s;
    for i = 1: num_neuron
        for j = 1:num_neuron
            delta_w = 0;
            for s = 1:num_neuron
                for t = s+1 : num_neuron
                    delta_w = delta_w + (W(1,s,i) + W2(s,i))*(Sigma(s,s)*Sigma(j,t)-Sigma(s,t)*Sigma(j,s))/Sigma(s,s);
                    delta_w = delta_w + (W(1,t,i) + W2(t,i))*(Sigma(t,t)*Sigma(j,s)-Sigma(s,t)*Sigma(j,t))/Sigma(t,t);
                    delta_w = 1./(delta_w*delta_w);
                    delta_w =  (Sigma(s,s)*Sigma(t,t)-Sigma(s,t))*(Sigma(s,s)*Sigma(t,t)-Sigma(s,t)) / Sigma(s,t);
                    delta_w = delta_w * func_Im(s,t);
                end
            end
            delta_w = delta_w - ratio_ef_i * r(j)^(-2) * ( sum(W(1,:,i)) + sum(W2(:,i)) )^(-2);
            delta_w = delta_w - ratio_ew_i * gamma * W(1,i,j)^(gamma-1);
            delta_w = delta_w * learning_rate;
            delta_w = delta_w * func_Im(i,j);
            W(2,i,j) = W(1,i,j) + delta_w;
            if i > j
                total_Im(t1,1) = total_Im(t1,1) - .5 * log(Sigma(i,i) * Sigma(j,j) - Sigma(i,j)^2) + .5 * log(Sigma(i,i)) + .5 * log(Sigma(j,j));
            end
        end
    end
    total_e_f(t1,1) = sum(r);
    total_e_w(t1,1) = sum(sum(W(1,:,:).^2));
end




