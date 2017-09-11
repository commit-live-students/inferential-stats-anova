# Anova

We want to examine the effectiveness of a new antidepressant. Depressed patients were randomly assigned to three groups: *a placebo group*, *low dose group*, *moderate dose group*. After four weeks of treatment, the patients were tested. The higher the score, the more depressed the patient. The data are presented below.

    Placebo -> 38, 47, 39, 25, 42
    Low Dose -> 22, 19, 8, 23, 31
    Moderate Dose -> 14, 26, 11, 18, 5

### Write a function that:

##### Takes 4 parameters:
    dataset1: List
    dataset2: List
    dataset3: List
    probability_level: float

##### Returns: 
    True, if there is difference between the three sets.
    False, if there is no difference.