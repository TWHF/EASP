# ENVIRONMENTAL ASSESSMENT FOR SUSTAINABLE PACKAGING - EASPA
Consumer shopping behaviour generally lacks awareness about the sustainability of a product , especially product packaging which has a huge impact on our environment. So even if consumers want to do their bit for the environment , there’s little to no model available to provide them with a comprehensive overview about the sustainability of a product . Research in this area is still in its nascent phase and few mathematical frameworks have been developed or are in the development phase. 
The lack of fixed parameters for determining the sustainability of product packaging , motivated us to develop a fuzzy based ecommerce model. A lot of product packaging assessment data is available but scattered. We reviewed several such literature on packaging assessment and decided on some common parameters that would form our fuzzy set
Our objective was to find data spread throughout the internet about sustainability factors like carbon footprint, amount of water used, amount of waste treated, recyclability for various products and provide users the option to shop for objects which are environmentally friendly.

## Website
The web interface was developed using the django web framework. The site html pages are defined in the templates/store folder which contains the html pages for all the site pages.The views.py file in the PSI folder is what renders the web page or gives the httpresponse to a request.
The website also offers a score called CSS(customer sustainability score), from which customers can realize their contribution for sustainable products on our site. It is calculated in such a way that the growth rate of this score automatically decreases when the customers order count increases, this design inhibits rapid growth of CSS, and can encourage the user psychologically for achieving more score over a longer time period, thus keeping the site participation active.

## Fuzzy Inference System
For implementation of automatic PSS generator, we have used ‘skfuzzy’, a scientific python library which provides complete support for development of a fuzzy inference system with a very simple API.
To understand the working of the generator, we can divide it into 4 parts 
### Universe of discourses
Total 5 universes of discourse are used where 4 are input and 1 is output. Inputs are carbon footprint, recyclability, water used in production, waste treated in production. Output is the PSS(product sustainability score). Implementation is very simple, we have two methods Antecedent and Consequent for input and output variables respectively, arguments are name of the variable and the range for the crisp input.

### Membership Functions 
For each input we have 3 linguistic variables(LOW, MEDIUM and HIGH) and all three are triangular MF. For output we have 5 linguistic variables(BAD, POOR, AVERAGE, GOOD, and EXCELLENT) and each term is a trapezoidal MF. Trapezoidal shape is used because it enables us to include more uncertainty in our terms.
### Rulebase 
In total 81 fuzzy rules were defined after serious consideration of packaging literature and evaluation of the factors data for how much worse their effect is in different amounts.
### PSS generation 
The process is very simple where we take input of crisp values, pass them through the fuzzifier, rulebase and defuzzifier and we get a crisp output. Defuzzifier algorithm is important to understand here, skfuzzy uses Mamdani’s method.

# Outcome
We have developed an example consumer shopping site which implements the proposed consumer sustainable behaviour reward model. 
The website displays the items along with the 4 environmental impact parameters which we have chosen as our fuzzy inference system inputs.(Only those items are displayed whose sustainability score has already been calculated.)

1. The website calculates the sustainability scores for each product through the fuzzy inference system described above.
2. The consumer can select items based on their needs which are added to their shopping carts and simultaneously calculate their average PSS(Product sustainability score) for      current order.
3. Couple of admin actions are implemented that are only to be used by admin, listing of items is manual and CSS score is currently updated manually so that malicious entries      can be avoided before loading them in the database.
   
   Thank you












