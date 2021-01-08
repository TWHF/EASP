# Notes
# running average aggregator for calculating css.
# this can work, with little modification
# even if the css calculation is done between
# some intervals and not instantly, thus saving
# immediate read and writes to our db
#
# following are the arguments this method requires
# from the schema
# old_css = current css
# avg_psi = average psi
# ord_cnt = total order count till old_css
# cur_psi = psi of current order

from fractions import Fraction as f

def get_css(old_css, avg_psi, ord_cnt, cur_psi):

    y1 = f(1, ord_cnt+1)
    # average is calculated this way so
    # that we do not lose accuracy, or
    # overflow the limit of float
    x1 = cur_psi * y1
    x2 = ord_cnt * y1
    x2 *= avg_psi

    new_css = float(old_css + x1 + x2)
    new_css = round(new_css, 2)
    return new_css
