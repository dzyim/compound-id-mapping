#!/usr/bin/env python
from rdkit import Chem
from rdkit.Chem import inchi

smiles1 = 'C1=NC(=NC(=O)N1[C@H]2[C@@H]([C@@H]([C@H](O2)CO)O)O)N'
smiles2 = 'C1=NC(=NC(=O)N1[C@H]2[C@H]([C@@H]([C@H](O2)CO)O)O)N'

canon1 = Chem.MolToSmiles(Chem.MolFromSmiles(smiles1))
canon2 = Chem.MolToSmiles(Chem.MolFromSmiles(smiles2))

inchi1 = inchi.MolToInchi(Chem.MolFromSmiles(smiles1))
ickey1 = inchi.InchiToInchiKey(inchi1)

inchi2 = inchi.MolToInchi(Chem.MolFromSmiles(smiles2))
ickey2 = inchi.InchiToInchiKey(inchi2)

print('InChIKey 1:', ickey1)
print('InChIKey 2:', ickey2)
