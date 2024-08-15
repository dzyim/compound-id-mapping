#!/usr/bin/env python
import re
import requests
import pandas as pd
from datetime import datetime

def get_pubchem_xrefs(cid):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/xrefs/RegistryID/JSON"
    # Another REST with more detailed info:
    # https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        xrefs = data['InformationList']['Information'][0]
        return xrefs
    else:
        return None

def extract_identifiers(xrefs, cid):
    ids = xrefs['RegistryID']

    chebi_id = None
    chebi_ids = [i for i in ids if re.match('CHEBI', i)]
    if chebi_ids:
        chebi_id = chebi_ids[0]

    chembl_id = None
    chembl_ids = [i for i in ids if re.match('CHEMBL', i)]
    if chembl_ids:
        chembl_id = chembl_ids[0]

    drugbank_id = None
    drugbank_ids = [i for i in ids if re.match('DB\\d{5}$', i)]
    if drugbank_ids:
        drugbank_id = drugbank_ids[0]

    zinc_id = None
    zinc_ids = [i for i in ids if re.match('ZINC', i)]
    if zinc_ids:
        zinc_id = zinc_ids[0]

    return {
        'PubChem_CID': cid,
        'ChEBI_ID': chebi_id,
        'ChEMBL_ID': chembl_id,
        'DrugBank_ID': drugbank_id,
        'ZINC_ID': zinc_id,
    }

def download_pubchem_xrefs(cids):
    records = []
    for cid in cids:
        xrefs = get_pubchem_xrefs(cid)
        if xrefs:
            identifiers = extract_identifiers(xrefs, cid)
            records.append(identifiers)
    df = pd.DataFrame(records)
    return df

if __name__ == '__main__':
    cids = [9444, 47751]
    outfile = datetime.strftime(datetime.now(), 'pubchem_xrefs.%Y%m%d%H%M%S.csv')
    pubchem_xrefs = download_pubchem_xrefs(cids)
    pubchem_xrefs.to_csv(outfile, index=False)
