clear
clc
close all

%To reach the maximum efficiency in performing an assembling operation in a
%manufacturing plant, new employees are required to take a 1-month training
%course. A new method was suggested, and the manager wants to compare the
%new method with the standard one, by looking at the lengths of time
%required for employees to assemble a certain device. They are given below
%(and assumed approximately normally distributed):
x = [46, 37, 39, 48, 47, 44, 35, 31, 44, 37];
y = [35, 33, 31, 35, 34, 30, 27, 32, 31, 31];
n1 = length(x);
n2 = length(y);
mx = mean(x);
my = mean(y);
sx = var(x);
sy = var(y);

%a) At the 5% significance level, do the population variances seem to
%differ?
%Null hypothesis: the variances are equal.
%Alternative hypothesis: the variances are different.

fprintf('a)\n');
fprintf('We are doing a two-test for the variances.\n');


alpha = input('Significance level = ');
[ha, pa, cia, valstata] = vartest2(x, y, alpha, 0); 
f=sx/sy;

r=icdf('f',1-alpha/2,n1,n2); %find the rejection region
l=icdf('f',alpha/2,n1,n2);
fprintf('The rejection region, RR, is (%f,%f)U(%f, %f)\n',-Inf,l,r,Inf)
fprintf('The value of the test statistic f is %f (given by vartest2 %f).\n',f,valstata.fstat)
fprintf('The P-value of the test is %f.\n',pa)
if ha==1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end  

%b) Find a 95% confidence interval for the difference of the average
%assembling times.
fprintf('b)\n');
confidence = input("Confidence interval = ");
alpha = 1-confidence;

if ha==1% confidence interval DIFFERENCE -> case: the variances are different
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