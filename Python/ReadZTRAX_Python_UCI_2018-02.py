# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:57:59 2018

@author: wyatt clarke
"""

# MACHINERY TO WORK WITH ZTRAX DATA
############################################################################################################
import pandas as pd
import os 

os.chdir(r'G:\Zillow')

#Load layout file for ZTrans
layout_ZTrans = pd.read_excel(r'Created\Layout.xlsx', sheetname='ZTrans')
layout_ZAsmt = pd.read_excel(r'Created\Layout.xlsx', sheetname='ZAsmt')

# LOAD FUNCTIONS FOR READING ZTRAX TABLES
# Function for reading a Ztrans table with row and column criteria
def read_ZTrans(state_code, table_name, col_indices, row_crit_field, row_crit_content):
    path = "G:\\Zillow\\{}\\ZTrans\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZTrans.loc[layout_ZTrans.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName'][col_indices]
    dtype=layout_temp['PandasDataType'][col_indices].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3
    chunksize=500000

    iter = pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, usecols=col_indices, iterator=True, chunksize=chunksize)
    return pd.concat([chunk[(chunk[row_crit_field].isin(row_crit_content))] for chunk in iter])

# Function for reading a ZAsmt table with row and column criteria
def read_ZAsmt(state_code, table_name, col_indices, row_crit_field, row_crit_content):
    path = "G:\\Zillow\\{}\\ZAsmt\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZAsmt.loc[layout_ZAsmt.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName'][col_indices]
    dtype=layout_temp['PandasDataType'][col_indices].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3
    chunksize=500000

    iter = pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, usecols=col_indices, iterator=True, chunksize=chunksize)
    return pd.concat([chunk[(chunk[row_crit_field].isin(row_crit_content))] for chunk in iter])

# Function for reading a Ztrans table with ALL rows and column criterion
def read_ZTrans_long(state_code, table_name, col_indices):
    path = "G:\\Zillow\\{}\\ZTrans\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZTrans.loc[layout_ZTrans.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName'][col_indices]
    dtype=layout_temp['PandasDataType'][col_indices].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3

    return pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, usecols=col_indices)

# Function for reading a ZAsmt table with ALL rows and column criterion
def read_ZAsmt_long(state_code, table_name, col_indices):
    path = "G:\\Zillow\\{}\\ZAsmt\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZAsmt.loc[layout_ZAsmt.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName'][col_indices]
    dtype=layout_temp['PandasDataType'][col_indices].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3

    return pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, usecols=col_indices)

# Function for reading a Ztrans table with row criterion and ALL columns
def read_ZTrans_wide(state_code, table_name, row_crit_field, row_crit_content):
    path = "G:\\Zillow\\{}\\ZTrans\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZTrans.loc[layout_ZTrans.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName']
    dtype=layout_temp['PandasDataType'].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3
    chunksize=500000

    iter = pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, iterator=True, chunksize=chunksize)
    return pd.concat([chunk[(chunk[row_crit_field].isin(row_crit_content))] for chunk in iter])

# Function for reading a ZAsmt table with row criterion and ALL columns
def read_ZAsmt_wide(state_code, table_name, row_crit_field, row_crit_content):
    path = "G:\\Zillow\\{}\\ZAsmt\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZAsmt.loc[layout_ZAsmt.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName']
    dtype=layout_temp['PandasDataType'].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3
    chunksize=500000

    iter = pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, iterator=True, chunksize=chunksize)
    return pd.concat([chunk[(chunk[row_crit_field].isin(row_crit_content))] for chunk in iter])

# Function for reading a ZAsmtHist table with row criterion and ALL columns
def read_ZAsmtHist_wide(state_code, table_name, row_crit_field, row_crit_content):
    path = "G:\\Zillow\\ZAsmt_historical\\{}\\ZAsmt\\{}.txt".format(state_code, table_name)
    layout_temp = layout_ZAsmt.loc[layout_ZAsmt.TableName=='ut{}'.format(table_name), :].reset_index()
    names=layout_temp['FieldName']
    dtype=layout_temp['PandasDataType'].to_dict()
    encoding='ISO-8859-1'
    sep = '|'
    header=None
    quoting=3
    chunksize=500000

    iter = pd.read_csv(path, quoting=quoting, names=names, dtype=dtype, encoding=encoding, sep=sep, header=header, iterator=True, chunksize=chunksize)
    return pd.concat([chunk[(chunk[row_crit_field].isin(row_crit_content))] for chunk in iter])
##########################################################################################################