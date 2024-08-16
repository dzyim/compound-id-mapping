#!/usr/bin/env python
from rdkit import Chem
from rdkit.Chem import inchi

smiles = 'C1=NC(=NC(=O)N1[C@H]2[C@@H]([C@@H]([C@H](O2)CO)O)O)N'
canon = Chem.MolToSmiles(Chem.MolFromSmiles(smiles))

inchi1 = inchi.MolToInchi(Chem.MolFromSmiles(smiles))
inchi2 = inchi.MolToInchi(Chem.MolFromSmiles(canon))

print('InChI from SMILES:', inchi1)
print('InChI from Canonical SMILES:', inchi2)

output = Chem.MolToSmiles(Chem.MolFromInchi(inchi1))
print('InChI to SMILES:', output)
