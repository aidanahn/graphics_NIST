import spekpy as sp
import matplotlib.pyplot as plt
import os 
import shutil
from matplotlib import rc

# Name, kVp, Mo, Rh, Al, mA
params = (("Mo_Mo23", 23, 0.032, 0, 0, 10), 
          ("Mo_Mo25", 25, 0.032, 0, 0, 10), 
          ("Mo_Mo28", 28, 0.032, 0, 0, 5),
          ("Mo_Mo30", 30, 0.032, 0, 0, 5),
          ("Mo_Mo35", 35, 0.032, 0, 0, 5),
          ("Mo_Rh28", 28, 0, 0.029, 0, 5),
          ("Mo_Rh32", 32, 0, 0.029, 0, 5),
          ("Mo_Mo25x", 25, 0.03, 0, 2, 20),
          ("Mo_Mo28x", 28, 0.03, 0, 2, 20),
          ("Mo_Mo30x", 30, 0.03, 0, 2, 20),
          ("Mo_Mo35x", 35, 0.03, 0, 2, 10))

dk = 0.1

if os.path.exists("results"):
    shutil.rmtree("results")
os.makedirs("results")
for name, kVp, Mo, Rh, Al, mA in params:
    spek_instance = sp.Spek(targ="Mo")
    spek_instance.make_matl(matl_name="Polyimide", matl_density=1.43, chemical_formula="C22H10N2O5")
    spek_instance.multi_filter((("Mo", Mo), ("Rh", Rh), ("Al", Al), ("Polyimide", 0.075), ("Air", 1000)))
    spek_instance.set(
        kvp=kVp,
        dk=dk,
        mu_data_source='nist',
        physics='kqp',
        mas=mA,
    )
    spectra = spek_instance.get_spectrum()

    plt.rcParams.update({'font.size': 18})
    plt.figure(figsize=(12, 9))
    plt.plot(spectra[0], spectra[1])
    plt.xlabel("Energy (keV)", fontsize=18, labelpad=24)
    plt.ylabel("Fluence (cm⁻² keV⁻¹)", fontsize=18, labelpad=24)
    plt.title(f"Beam Code: {name}", fontsize=24, pad=24)
    plt.savefig(f"./results/{name}.png")
    plt.clf()



