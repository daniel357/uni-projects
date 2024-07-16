clear
clc

% a) 5% significance level, do the population variances seem to differ?

X1 = [1021, 980, 1017, 988, 1005, 998, 1014, 985, 995, 1004, 1030, 1015, 995, 1023,];
X2 = [1070, 970, 993, 1013, 1006, 1002, 1014, 997, 1002, 1010, 975];

n1 = length(X1);
n2 = length(X2);
mx=mean(X1);
my =mean(X2);
sx =var(X1);
sy=var(X2);

% null hypothesis is H0 : variances are equal
% research hypothesis is H1: variances are different

fprintf("a) two tailed test for variances\n");

alpha = input("singificance level= ");

[h, p, ci, stats] = vartest2(X1, X2, alpha,0);% 0-stands for a two tailes test


% build rejection region
f1 = finv(alpha/2, n1-1, n2-1);
f2 = finv(1 - alpha/2, n1-1, n2-1);

fprintf('\n H is %d', h)
if h==1 % result of the test, h = 0, if H0 is NOT rejected, h = 1, if H0 IS rejected
    fprintf('\nthe null hypothesis is rejected,\n') 
    fprintf('i.e. the variances seem to be different.\n')
else
    fprintf('\nthe null hypothesis is not rejected,\n')
    fprintf('i.e. the variances seem to be equal.\n')
end   
fprintf('the rejection region for F is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
fprintf('The value of the test statistic f is %4.4f\n', stats.fstat)
fprintf('The P-value of the test is %4.4f\n', p)
fprintf("The confidence interval is (%4.4f,%4.4f).\n", ci)





      
fprintf('b) 95 percent confidence interval for the diference of the average weights\n');

alpha = 0.05;
if h==1% confidence interval DIFFERENCE -> case: the variances are different
    c=(sx/n1)/(sx/n1+sx/n2);
    n=1/(c^2/(n1-1)+(1-c)^2/(n2-1));
    t=icdf('t',1-alpha/2,n);
    rad=sqrt(sx/n1+sx/n2);
    li=mx-my-t*rad;
    ri=mx-my+t*rad;
else % confidence interval DIFFERENCE -> case: the variances are equal
    n=n1+n2-2;
    t=icdf('t',1-alpha/2,n);
    rad=sqrt(1/n1+1/n2);
    sp=sqrt(((n1-1)*sx+(n2-1)*sy)/n);
    li=mx-my-t*sp*rad;
    ri=mx-my+t*sp*rad;
end

fprintf('Confidence interval for the difference of the means(%.4f,%.4f)\n',li,ri)



























