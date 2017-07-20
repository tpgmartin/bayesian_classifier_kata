import pandas as pd


def trained():
    df = pd.DataFrame(
        data=[
            ['nice', 1, 1, 1, 0],
            ['not_nice', 1, 1, 0, 1]
        ],
        columns=['cat', 'John', 'is', 'good', 'bad']
    )
    return df

def fprob(c, f, df_trained):
    feature = df_trained[f]
    category = df_trained['cat']

    prob_f_given_c_num = ((feature == 1) & (category == c)).count()
    prob_f_given_c_denom = (category == c).count()
    prob_f_given_c = prob_f_given_c_num / prob_f_given_c_denom

    prob_f_num = (feature == 1).count()
    prob_f_denom = len(df_trained)
    prob_f = prob_f_num / prob_f_denom

    prob_c_num = (category == c).count()
    prob_c_denom = len(df_trained)
    prob_c = prob_f_num / prob_f_denom

    return prob_f_given_c * prob_c / prob_f

"""
  Tests
  1. Prob(nice | 'good') == 1.0
  2. Prob(nice | 'John') == 0.5
  3. Prob(nice | 'foo') == 0.0
  4. Prob(nice | category) == 0.5?
"""

"""
  TODO
  * Implements tests
  * How to handle new feature
  * Refactor data structure
  * Handling multiple features
  * Compare probs for 'Mary is good' as nice or not_nice
  * Build the trainer
"""
