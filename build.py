from __future__ import division   # Get float values for all division operations.
from scipy import stats

'''
    Assumptions:
        The populations from which the samples were obtained must be normally or approximately normally distributed.
        The samples must be independent.
        The variances of the populations must be equal.

    Hypotheses
        The null hypothesis will be that all population means are equal, the alternative hypothesis is that at least one mean is different.

    Decision Rule :
        The decision will be to reject the null hypothesis if the test statistic from the table is greater than
        the F critical value with k-1 numerator and N-k denominator degrees of freedom.

        If the decision is to reject the null, then at least one of the means is different.
        However, the ANOVA does not tell you where the difference lies. For this, you need another test, either the Scheffe' or Tukey test.

        F Value/F Ratio in One Way ANOVA: When to Reject the Null :
            The F Value in ANOVA
                The F value (also called an F statistic or F Ratio) in one way ANOVA is a tool to help you answer
                the question "Is the variance between the means of two populations significantly different?""
                The F value in the ANOVA test also determines the P value; The P value is the probability of getting a result at least as extreme as the one that was actually observed, given that the null hypothesis is true.

            Reject the null when your p value is smaller than your alpha level.
            You should not reject the null if your critical f value is smaller than your F Value,
            unless you also have a small p-value.

            Where this could get confusing is where one of these values seems to indicate that you should
            reject the null hypothesis and one of the values indicates you should not. For example,
            let's say your One Way ANOVA has a p value of 0.68 and an alpha level of 0.05. As the p value is large,
            you should not reject the null hypothesis. However, your f value is 0.40 with an f critical value of 3.2.
            Should you now reject the null hypothesis? The answer is NO.

            Why?
                The F value should always be used along with the p value in deciding whether your results
                are significant enough to reject the null hypothesis. If you get a large f value
                (one that is bigger than the F critical value found in a table), it means something is significant,
                while a small p value means all your results are significant. The F statistic just compares the
                joint effect of all the variables together.

                To put it simply, reject the null hypothesis only if your alpha level is larger than your p value.

'''


def solution(set1, set2, set3, probability_level):

    placebo  = set1
    low_dose = set2
    moderate_dose = set3

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    								# Method 1

    f_statistic_or_f_value, p_value = stats.f_oneway(placebo, low_dose, moderate_dose)
    print(f_statistic_or_f_value, p_value )

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    								# Mthod 2

    # Calculating using Python (i.e., pure Python ANOVA)
    n = len(placebo)  	# Number of items in sample. Here all samples has equal length. If it has different length, different method has to follow.
    k = 3  				# Number of independent groups
    N = len(placebo) + len(low_dose) + len(moderate_dose)  # N is the total sample size.


    T1 = sum(placebo)
    T2 = sum(low_dose)
    T3 = sum(moderate_dose)

    T1_square = T1**2
    T2_square = T2**2
    T3_square = T3**2

    GT = T1 + T2 + T3 	# Grand Total

    # SSwithin
    sum_placebo_square = sum([x**2 for x in placebo])
    sum_low_does_square =  sum([x**2 for x in low_dose])
    sum_moderate_dose_square = sum([x**2 for x in moderate_dose])

    SSwithin = (sum_placebo_square - T1_square / n) + (sum_low_does_square - T2_square / n) + (sum_moderate_dose_square - T3_square / n)


    # SSbetween
    SSbetween = ((T1_square / n) + (T2_square / n) + (T3_square / n)) - (GT**2 / N)

    # SSTotal
    SSTotal_original = (sum_placebo_square + sum_low_does_square + sum_moderate_dose_square) - (GT**2 / N )
    SSTotal = SSbetween + SSwithin
    if round(SSTotal_original,5) != round(SSTotal, 5):
    	print("Error in calculation")
    	exit(-1)

    print(SSTotal_original, SSTotal)

    # ------------------------------------
    DFbetween = k - 1
    DFwithin = N - k

    # ------------------------------------
    MSbetween = SSbetween/DFbetween
    MSwithin = SSwithin/DFwithin

    # ------------------------------------
    # Calculating the F-value
    f_statistic_or_f_value = MSbetween/MSwithin

    '''
    	To reject the null hypothesis we check if the obtained F-value is above the critical value for rejecting the null hypothesis.
    	We could look it up in a F-value table based on the DFwithin and DFbetween. However, there is a method in SciPy for obtaining a p-value.
    '''

    # ------------------------------------
    # Calculate p value
    p_value = stats.f.sf(f_statistic_or_f_value, DFbetween, DFwithin)

    print(f_statistic_or_f_value, p_value )

    # ------------------------------------
    # Finally, we are also going to calculate effect size. We start with the commonly used eta-squared :
    eta_sqrd = SSbetween/SSTotal

    '''
     	However, eta-squared is somewhat biased because it is based purely on sums of squares from the sample.
     	No adjustment is made for the fact that what we aiming to do is to estimate the effect size in the population.
     	Thus, we can use the less biased effect size measure Omega squared:
    '''
    om_sqrd = (SSbetween - (DFbetween * MSwithin))/(SSTotal + MSwithin)
    om_sqrd = (SSbetween - (DFbetween * MSwithin))/(SSTotal + MSwithin)

    print(eta_sqrd, om_sqrd)


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
    	Decision Rule :
    		The decision will be to reject the null hypothesis if the test statistic from the table is greater than
    		the F critical value with k-1 numerator and N-k denominator degrees of freedom.
    '''

    if probability_level > p_value:
        return True

    return False
