# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:49:28 2017

@author: wyatt clarke
"""

# Load functions used to read ZTRAX data files. Might need to open file to adjust file paths or function options.
exec(open(r'C:\Users\wyatt\Research\Zillow\ReadZTRAX.py').read())

# SPECIFY COUNTIES TO EXTRACT AND FILE PATH
state = '06'
zip_list = ['92617', '92660', '92603', '92614']
os.chdir(r'G:\Zillow\')

# PULL ZTRANS DATA
# Load ZTrans PropertyInfo spreadsheet (which contains property ZIP) for transactions from interesting ZIP codes, and save it as CSV
PropertyInfo = read_ZTrans_wide(state_code=state, table_name='PropertyInfo', row_crit_field='PropertyZip', row_crit_content=zip_list)   
PropertyInfo.to_csv(r'ZTrans\PropertyInfo.csv', index=False)
# Extract list of uniq IDs for transactions from PropertyInfo
uniq_trans = PropertyInfo['TransId'].drop_duplicates().tolist()
# load transactions found in the list 'uniq_trans' from the rest of the ZTRANS tables
tables = ['BuyerName', 'Main', 'BuyerMailAddress', 'BuyerName', 'SellerName', 'BorrowerName', 'BuyerNameDescriptionCode', 'SellerNameDescriptionCode', 'SellerMailAddress', 'BorrowerNameDescriptionCode', 'ForeclosureNameAddress', 'ForeclosureOriginalLoan', 'BorrowerMailAddress']
for table in tables:
    foo = read_ZTrans_wide(state_code=state, table_name='{}'.format(table), row_crit_field='TransId', row_crit_content=uniq_trans)
    foo.to_csv(r'ZTrans\{}.csv'.format(table), index=False)
    print(table)
    
# PULL ZASMT DATA    
# Load ZAsmt Main spreadsheet (which contains property ZIP) for parcels in interesting ZIP codes
Main = read_ZAsmt_wide(state_code=state, table_name='Main', row_crit_field='PropertyZip', row_crit_content=zip_list)   
Main.to_csv(r'ZAsmt\Main.csv', index=False)
# Extract list of uniq IDs for parcels from Main
uniq_parcels = Main['RowID'].drop_duplicates().tolist()
tables = ['AdditionalPropertyAddress', 'Building', 'BuildingAreas', 'CareOfName', 'ExteriorWall', 'ExtraFeature', 'Garage', 'InteriorFlooring', 'InteriorWall', 'LotSiteAppeal', 'MailAddress', 'Main', 'Name', 'Oby', 'Pool', 'SaleData', 'TaxDistrict', 'TaxExemption', 'TypeConstruction', 'Value', 'VestingCodes']
for table in tables:
    foo = read_ZAsmt_wide(state_code=state, table_name='{}'.format(table), row_crit_field='RowID', row_crit_content=uniq_parcels)
    foo.to_csv(r'ZAsmt\{}.csv'.format(table), index=False)
    print(table)
    
# PULL ZASMT HISTORICAL DATA    
# Load ZAsmt_hist Main spreadsheet (which contains property ZIP) for parcels in interesting ZIP codes
Main = read_ZAsmtHist_wide(state_code=state, table_name='Main', row_crit_field='PropertyZip', row_crit_content=zip_list)   
Main.to_csv(r'ZAsmtHist\Main.csv', index=False)
# Extract list of uniq IDs for parcels from Main
uniq_parcels = Main['RowID'].drop_duplicates().tolist()
tables = ['Building', 'BuildingAreas', 'Garage', 'LotSiteAppeal', 'Value']
for table in tables:
    foo = read_ZAsmt_wide(state_code=state, table_name='{}'.format(table), row_crit_field='RowID', row_crit_content=uniq_parcels)
    foo.to_csv(r'ZAsmtHist\{}.csv'.format(table), index=False)
    print(table)
