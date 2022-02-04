import cobra
from cobra import Model, Reaction, Metabolite


# User supplies metabolic models of organism
# model1 in in format A and model2 in format B
# returns diurnal_model after Knies et al. 2015
def make_diurnal_model(model1, model2):
    index = 1
    suffix = "e2"
    model = Model('setoftransfer')
    for x in model1.metabolites:
        y = str(x)
        if y.endswith(suffix, 8):
            continue
        else:
            print("rxn%s: %s --> %s0" % (index, x, x))
            reaction_number = 'reaction_R%s' % (index)
            reaction_metabolite1 = '%s' % (x)
            reaction_metabolite2 = '%s0' % (x)
            my_reaction = Reaction(reaction_number)
            my_reaction.name = reaction_number
            my_reaction.subsystem = 'Transfer'
            my_reaction.lower_bound = -1000
            my_reaction.upper_bound = 1000
            reaction_metabolite1 = Metabolite(
                reaction_metabolite1,
                formula='X',
                name='X',
                compartment='c0')
            reaction_metabolite2 = Metabolite(
                reaction_metabolite2,
                formula='X',
                name='X',
                compartment='c00')
            my_reaction.add_metabolites({
                reaction_metabolite1: -1.0,
                reaction_metabolite2: 1.0
            })
            model.add_reactions([my_reaction])
        index += 1
    diurnal_model = model2.merge(right=model, objective='left')
    cobra.io.write_sbml_model(diurnal_model, "diurnal_model.xml")
    print("Diurnal model is saved in working directory")

make_diurnal_model(model1, model2)
