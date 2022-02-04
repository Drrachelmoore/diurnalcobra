# DIURNALcobra
Makes diurnal (24 h) model from standard genome-based metabolic models


To create a metabolic model that operates on a 24 hour timeline (12 hours light, 12 hours dark):
start with metabolic model of photosynthetic organism (e.g., _Rhodopseudomonas palustris_ https://www.biorxiv.org/content/10.1101/2021.09.07.459191v2.full)
1. Create duplicates of the model (i.e., copy it to model1 and model2)
2. Set compartment id in model1 to c0
3. Set compartment id in model2 to c00 and external compartment to e2
4. Run make_diurnal_model(model1, model2)

Function returns diurnal_model.xml

Ensure photon flux is only occuring during the 12 hours of "light"

Example:

diurnal_model.reactions.get_by_id("EX_photon_e0").lower_bound = -100

diurnal_model.reactions.get_by_id("EX_photon_e0").upper_bound = 100

diurnal_model.reactions.get_by_id("EX_photon_e2").lower_bound = 0

diurnal_model.reactions.get_by_id("EX_photon_e2").upper_bound = 0

where e0 and e2 are the extracellular space during light and dark, respectively. 
