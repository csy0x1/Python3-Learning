#1. from printing_functions import *

#2. import printing_functions

#3. from printing_functions import print_models,show_completed_models

#4. from printing_functions import print_models as pm, show_completed_models as scm

#5. 
import printing_functions as pf

unprinted_designs=['iPhone case','robot pendant','dodecahedron']
completed_models=[]

#1. 
#print_models(unprinted_designs,completed_models)
#show_completed_models(completed_models)

#2. 
#printing_functions.print_models(unprinted_designs,completed_models)
#printing_functions.show_completed_models(completed_models)

#3. 
#print_models(unprinted_designs,completed_models)
#show_completed_models(completed_models)

#4. 
#pm(unprinted_designs,completed_models)
#scm(completed_models)

#5. 
pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)

