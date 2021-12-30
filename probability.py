'''
Author: Afton Lawver
'''

from fractions import Fraction

# Probability Module
# Will house the classes used to run probability tests/generate distributions
# For each of the distributions listed below:
# generate the PMF or CDF depending on whether discrete or continuous.
# Conditional Probabilities
# Bayesian Probabilities
# Binomial Distribution
# Bernoulli Distribution
# Hypergeometric Distribution
# Poisson Distribution

class Probability():
    '''
    Class that calculates conditional probabilities of two events.
    Allows us to ask questions like what is the probability of event A
    given that event B has occurred and vice versa.

    '''

    def __init__(self, name_of_event_A:str, name_of_event_B:str, 
                probability_event_A:str,
                probability_event_B:str, A_is_subsumed = False, 
                B_is_subsumed = False):
        '''
        Parameters
        ----------
        probability_event_A
            the probability of event A happening (can be a float or fraction)
        probability_event_B
            the probability of event B happening (can be a float or fraction)
        '''
        self.name_of_event_A = name_of_event_A
        self.name_of_event_B = name_of_event_B
        self.probability_event_A = float(probability_event_A)
        self.probability_event_B = float(probability_event_B)
        self.B_is_subsumed = B_is_subsumed
        self.A_is_subsumed = A_is_subsumed
    
    def convert_probabilities_fraction_to_float(self):
        self.probability_event_A = float(Fraction(self.probability_event_A))
        self.probability_event_B = float(Fraction(self.probability_event_B))
        

    def get_probability_event_A(self):
        print("The probability that {} is: {}".format(self.name_of_event_A,
             self.probability_event_A))
        return self.probability_event_A

    def get_probability_event_B(self):
        return self.probability_event_B
    
    def set_probability_event_A(self, new_probability:float):
        self.probability_event_A = new_probability

    def set_probability_event_B(self, new_probability:float):
        self.probability_event_B = new_probability

    def probability_A_not_occurring(self):
        return 1 - self.probability_event_A

    def probability_B_not_occurring(self):
        return 1 - self.probability_event_B
    
    def probability_A_and_B(self):
        if self.A_is_subsumed == True:
            return self.probability_event_B
        elif self.B_is_subsumed == True:
            return self.probability_event_A
        else:
            return self.probability_event_A * self.probability_event_B

    def probability_A_or_B_or_both(self):
        return (self.probability_event_A + self.probability_event_B) - \
            (self.probability_event_A * self.probability_event_B)
    
    def probability_A_or_B_not_both(self):
        return (self.probability_event_A + self.probability_event_B) \
            - (2 * self.probability_event_A * self.probability_event_B)
    
    def probability_neither_A_nor_B(self):
        return (1 - ((self.probability_event_A + self.probability_event_B) - \
            (self.probability_event_A * self.probability_event_B)))
    
    def probability_A_occurs_not_B(self):
        return (self.probability_event_A * (1 - self.probability_event_B))

    def probability_B_occurs_not_A(self):
        return (1 - self.probability_event_A) * (self.probability_event_B)

    def multiplication_rule(self, trials:int, 
                            probability_of_event_of_interest:float):
        '''
        Only valid if the two events are independent. 
        It only works if one event does not change the
        probability of the other event.

        Example
        You toss a fair coin 3 times:
        What is the probability of three heads (HHH)?
        
        Parameters
        ----------
        trials
            number of trials you run (i.e. flip a coin 3 times; 3 is 
            the number of trials)
        probability
            the probability of success for what you are looking for(i.e. heads)
        '''
        return probability_of_event_of_interest ** trials 
         

class Conditional_Probability(Probability):
    '''
    Likelihood of an event or outcome occurring, based on the occurrence
    of a previous event or outcome. 
    '''

    def __init__(self, object:Probability):
        self.name_of_event_A = object.name_of_event_A
        self.name_of_event_B = object.name_of_event_B
        self.probability_event_A = float(object.probability_event_A)
        self.probability_event_B = float(object.probability_event_B)
        self.B_is_subsumed = object.B_is_subsumed
        self.A_is_subsumed = object.A_is_subsumed
        

    '''
    Example

    '''

    def get_A_given_B(self, probability_A_and_B:float, 
                        probability_event_B:float):
        print(probability_A_and_B)
        print(probability_event_B)

        return(probability_A_and_B/probability_event_B)


    def get_B_given_A(self, probability_A_and_B:float, 
                        probability_event_A:float):
        return(probability_A_and_B/probability_event_A)


class Bayesian_Probability(Probability):
    '''
    Responsible for finding Bayesian probabilities (using Bayes Rule).
    Finding probability of event A happening given that event B has already
    occurred. 
    '''

    def __init__(self):
        pass

    def probability_a_given_B(self):
        pass

    def probability_B_and_A(self):
        pass

# Testing --------------------------------------------------------------------
'''
my_probability = Probability(0.25, 0.5)
print(my_probability.probability_A_not_occurring())
print(my_probability.probability_B_not_occurring())
print(my_probability.probability_A_and_B())
print(my_probability.probability_A_or_B_or_both())
print(my_probability.probability_A_or_B_not_both())
print(my_probability.probability_neither_A_nor_B())
print(my_probability.probability_A_occurs_not_B())
print(my_probability.probability_B_occurs_not_A())
print(my_probability.multiplication_rule(3, 0.5))
'''

'''
You are drawing three marbles from a bag, one red, one green, and one blue.
Each marble has an equal chance of being drawn.
What is the conditional probability of drawing the red marble after already
drawing the blue one?
'''

my_probability = Probability("the first card is a heart", "second card is red"
                            ,13/51, 26/52)
my_probability.convert_probabilities_fraction_to_float()
my_probability.get_probability_event_A()
prob_A_and_B = my_probability.probability_A_and_B()
print("P(A and B) = {}".format(prob_A_and_B))
my_conditional = Conditional_Probability(my_probability)
print(my_conditional.get_A_given_B(prob_A_and_B, 
                                    my_probability.probability_event_B))

# End of testing -------------------------------------------------------------
class Bernoulli_Distribution(Probability):
    '''
    An event that has a Bernoulli Distribution has two outcomes.
    For example, flipping a coin, the outcome can be heads or tails.
    Or in our case, the probability of profit or loss, not both. 
    Can create a random variable that maps profit to 1 and loss to 0.   

    Parameters
    ----------
    p: probability of success
    '''
    def __init__(self, p:float):
        self.p = p

    def PMF(self, success_or_failure:str):
        success = self.p
        failure = 1 - self.p
        if success_or_failure == "success":
            return success
        elif success_or_failure == "failure":
            return failure

    def expectation(self):
        pass

class Binomial_Distribution(Probability):
    '''
    A binomial distribution happens when a Bernoulli trial is repeated 
    n times. Like a coin flipped 10 times. 

    Parameters
    ----------
    n: number of trials
    p: probability of success
    '''

    def __init__(self, n:float, p:float):
        self.n = n
        self.p = p

    def PMF(self):
        pass

    def expectation(self):
        pass


class Geometric_Distribution(Probability):
    '''
    X has a Geom(p) if X is the number of failures before the first
    success occurs. Consider a sequence of independent Bernoulli trials,
    each with the same success probability p. For example, we flip a fair
    coin until it lands heads for the first time, then the number of tails
    before the first head is distributed as Geom(1/2).

    Parameters
    -----------
    p: probability of success
    '''

    def __init__(self, p:float):
        self.p = p

    def PMF(self):
        pass

    def expectation(self):
        pass

class First_Success_Distribution(Probability):
    '''
    In a sequence of independent Bernoulli trials with success probability
    p, let X be the number of trials until the first successful trial, 
    including the success.

    Parameters
    -----------
    p: probability of success
    '''

    def __init__(self, p:float):
        self.p = p

    def PMF(self):
        pass

    def expectation(self):
        pass

class Hypergeometric_Distribution(Probability):
    '''
    You have two groups of things. Lets say you have white balls and 
    and black balls. You draw n balls out of the basket without replacement. 

    If X is the number of white balls, then X follows a Hypergeometric 
    distribution. 

    Parameters
    -----------
    w: white balls
    b: black balls
    n: number of trials
    '''

    def __init__(self, w:int, b:int, n:int):
        self.w = w
        self.b = b
        self.n = n

    def PMF(self):
        pass

    def expectation(self):
        pass

class Negative_Binomial_Distribution(Probability):
    '''
    In a sequence of independent Bernoulli trials with success probability p, 
    if X is the number of failures before the rth success, then X is said to
    have the negativeBinomialDistribution.

    Counts the number of failures until a fixed number of successes.

    Parameters
    -----------
    r: number of successes
    p: probability of success
    '''

    def __init__(self, r:float, p:float):
        self.r = r
        self.p = p

    def PMF(self):
        pass

    def expectation(self):
        pass

class Negative_Hypergeometric_Distribution(Probability):
    '''
    You have two groups of things. Lets say you have white balls and 
    and black balls. You draw n balls out of the basket without replacement.
    You draw the balls until rth white ball is obtained. X will be the 
    number of balls drawn until rth white ball is obtained.

    Parameters
    -----------
    w: white balls (category 1)
    b: black balls (category 2)
    r: number of white balls obtained
    '''

    def __init__(self):
        pass

    def PMF(self):
        pass

    def expectation(self):
        pass

class Poisson_Distribution(Probability):
    '''
    Poisson distribution is used in situations where we are 
    counting the number of successes in a particular region
    or interval of time, and there are a large number of trials,
    each with a small probability of success. For example, the 
    number of emails you receive in an hour. 
    Imagine subdividing the hour into seconds. There is a small
    probability that you will get an email in each second, 
    but there are many seconds in an hour. 

    In other words, a poisson process is a model for a series of 
    discrete events where the average time between events is known, 
    but the exact timing of events is random.
    
    Parameters
    -----------
    lambda : rate of occurrence
    '''

    def __init__(self):
        pass

    def PMF(self):
        pass

    def expectation(self):
        pass





    
