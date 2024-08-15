#!/usr/bin/env python
import requests
import pandas as pd
from io import StringIO
from datetime import datetime

if __name__ == '__main__':
    cids = [9444, 47751]
    cid_list = ','.join(map(str, cids))
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid_list}/property/IsomericSMILES,CanonicalSMILES/CSV"
    response = requests.get(url)

    if response.status_code == 200:
        outfile = datetime.strftime(datetime.now(), 'pubchem_smiles.%Y%m%d%H%M%S.csv')
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(outfile, index=False)
    else:
        print(f"Error: {response.status_code}, {response.text}")
