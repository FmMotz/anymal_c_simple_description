import pymeshlab
from pathlib import Path
ms = pymeshlab.MeshSet()

for target in Path('.').rglob('*.dae'):
    new_name = target.with_suffix('.stl')
    ms.load_new_mesh(str(target))
    ms.save_current_mesh(str(new_name))
    ms.clear()