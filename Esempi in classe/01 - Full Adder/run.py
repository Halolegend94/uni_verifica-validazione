from pymodelica import compile_fmu
from pyfmi import load_fmu

model_name  = "FA"
model_files = [
	    "FA.mo",
            "functionFA.mo",
            "functionOR.mo",
            "functionAND.mo",
            "functionNOT.mo",
            "functionXOR.mo",
        ]
model_path = compile_fmu(model_name, model_files)
model = load_fmu(model_path)

model.set("x", True)
model.set("y", True)
model.set("c", True)

res = model.simulate(options={'ncp': 10000})

print 'z',res['z'][-1]
print 'r',res['r'][-1]

