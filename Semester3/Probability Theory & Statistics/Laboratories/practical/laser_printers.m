clear
clc
close all

%A study is conducted to compare the total printing time in seconds of two
%brands of laser printers on serious tasks. Data below are for the printing
%of the charts (normality of the two populations is assumed);
x=[29.8, 30.6, 29.0, 27.7, 29.9, 29.6, 30.5, 31.1, 30.2, 28.1, 29.4, 28.5];
y=[31.5, 30.2, 31.2, 29.0, 31.4, 31.1, 32.5, 33.0, 31.3, 30.9, 30.7, 29.9];

%a) At 5% significance level, do the population variances seem to differ?
%Null hypothesis: the population variances are equal.
%Alternative hypothesis: the population variances differ.

alpha = input("significance level= ");

n1 =length(x);
n2 =length(y);

mx =mean(x);
my =mean(y);
sx =var(x);
sy =var(y);
fprintf('a)\n')
fprintf('SIGNIFICANCE LEVEL %f:\n',alpha)
fprintf("We are doing a two-tailed test for variances.\n");

[ha, pa, cia, valstata] = vartest2(x, y, alpha, 0);
fprintf('The value of the test statistic  is (given by vartest2 %f).\n',valstata.fstat)
fprintf('The P-value of the test is %f.\n',pa)
if ha==1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end    
 r=icdf('f',1-alpha/2,n1,n2);%Inverse cumulative distribution function for f
 l=icdf('f',alpha/2,n1,n2);
 fprintf('The rejection region, RR, is (%f,%f)U(%f, %f)\n',-Inf,l,r,Inf)

%b)At the same significance level, on average, does the Brand A printer
%seem to be faster?
%From a), we find if the variances of the populations are equal or not and
%we have to use this information here.
%In this case, the null hypothesis is that the means are equal.
%The alternative hypothesis is that the mean of the supplier A is greater
%than the one for supplier B.

fprintf('b)\n');
fprintf('SIGNIFICANCE LEVEL %f:\n',alpha)
fprintf('We are doing a right-tailed test for the difference of means.\n');
typeb=1; %right-tailed test 
if ha==0 
   vartype='equal';
   n=n1+n2-2;
   t=(mx-my)/sqrt((n1-1)*sx+(n2-1)*sy)*sqrt((n1+n2-2)/(1/n1+1/n2));
else
   vartype='unequal';
   c=(sx/n1)/(sx/n1+sy/n2);
   n=ceil(1/(c^2/(n1-1)+(1-c)^2/(n2-1)));
   t=(mx-my)/sqrt(sx/n1+sy/n2);
end
[hb,pb,cib,valstatb]=ttest2(x,y,alpha,typeb,vartype);
fprintf('The value of the test statistc t is %f (given by ttest2 %f).\n',t,valstatb.tstat)
fprintf('The P-value of the test is %.10f.\n',pb)
fprintf("The confidence interval is (%4.4f,%4.4f).\n", cib)
l=icdf('t',1-alpha,n);%Inverse cumulative distribution function for T
r=Inf;
fprintf('The rejection region, RR, is (%f, %f)\n',l,r)
if hb==1
    fprintf('The null hypothesis is rejected (t in RR), i.e. Brand A seems to be faster.\n')
else
    fprintf('The null hypothesis is NOT rejected (t not in RR), i.e. Brand A seems to not be faster.\n')
end  
