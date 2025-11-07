import pandas as pd
import scipy.stats as stats
import numpy as np


df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/DEMO_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/BPQ_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/CBC_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/BPXO_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/HEPB_S_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/KIQ_U_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/PAQ_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/VID_L.xpt', format='xport')
df = pd.read_sas('/Users/a.desai/Documents/Python/HHA_507/nhanes_inferential_2021_23/WHQ_L.xpt', format='xport')

#### Married vs unmarried
df['MarriedStatus'] = df['DMDMARTZ'].replace({
    1: 'Married',      # Married
    6: 'Married',      # Living with partner -> treat as "Married"
    2: 'Not Married',  # Widowed
    3: 'Not Married',  # Divorced
    4: 'Not Married',  # Separated
    5: 'Not Married',  # Never married
    77: pd.NA,         # Missing
    99: pd.NA          # Refused
})

print(df[['DMDMARTZ', 'MarriedStatus']])

### Education Level
df['Education'] = df['DMDEDUC2'].replace({
    1: 'Less than Bachelor’s',
    2: 'Less than Bachelor’s',
    3: 'Less than Bachelor’s',
    4: 'Less than Bachelor’s',
    5: 'Bachelor’s or Higher',
    7: pd.NA,
    9: pd.NA
})

print(df[['DMDEDUC2', 'Education']])

###Age
df['AgeYears'] = pd.to_numeric(df['RIDAGEYR'], errors='coerce')

print(df[['RIDAGEYR', 'AgeYears']])


## Systolic vs Diastolic
df['SystolicBP'] = pd.to_numeric(df['BPXOSY3'], errors='coerce')
df['DiastolicBP'] = pd.to_numeric(df['BPXODI3'], errors='coerce')

print(df[['BPXOSY3', 'SystolicBP', 'BPXODI3', 'DiastolicBP']])

### Vitamin D Status
df['VitaminD_Status'] = df['LBDVD2LC']

print(df[['LBDVD2LC', 'VitaminD_Status']])

### Hepatitis B Status
df['HepB_Status'] = df['LBXHBS'].replace({
    1: 'Reactive',
    2: 'Non-reactive',
    3: pd.NA,
    7: pd.NA,
    9: pd.NA
})

print(df[['LBXHBS', 'HepB_Status']])

### Weak/Failing Kidneys
df['WeakKidneys'] = df['KIQ022'].replace({
    1: 'Yes',
    2: 'No',
    7: pd.NA,
    9: pd.NA
})

print(df[['KIQ022', 'WeakKidneys']])

### Minutes of Sedentary Activity
df['SedentaryMinutes'] = pd.to_numeric(df['PAQ650'], errors='coerce')   
print(df[['PAQ650', 'SedentaryMinutes']])

### Current self reported health status
df['Weight_kg'] = pd.to_numeric(df['WHD020'], errors='coerce')
df['Weight_kg'] = df['Weight_kg'].replace([7777, 9999], np.nan)

print(df[['WHD020', 'Weight_kg']])


###Keep
demo = pd.read_sas("DEMO_L.XPT", format="xport")
demo = demo[["SEQN", "DMDEDUC2", "DMDEDUC2" "RIDAGEYR"]]

bp = pd.read_sas("BPXO_L.XPT", format="xport")
bp = bp[["SEQN", "BPXOSY3", "BPXODI3"]]

vid = pd.read_sas("VID_L.XPT", format="xport")
vid = vid[["SEQN", "LBDVD2LC"]]

hep = pd.read_sas("HEPB_S_L.XPT", format="xport")
hep = hep[["SEQN", "LBXHBS"]]   

kid = pd.read_sas("KIQ_U_L.XPT", format="xport")
kid = kid[["SEQN", "KIQ022"]]

paq = pd.read_sas("PAQ_L.XPT", format="xport")
paq = paq[["SEQN", "PAD680"]]

weight = pd.read_sas("WHQ_L.XPT", format="xport")
weight = weight[["SEQN", "WHD020"]]

### Merge
df = demo.merge(bp, on="SEQN", how="inner") \
         .merge(vid, on="SEQN", how="inner") \
         .merge(hep, on="SEQN", how="inner") \
         .merge(kid, on="SEQN", how="inner") \
         .merge(paq, on="SEQN", how="inner") \
         .merge(eighr, on="SEQN", how="inner")

print(df.shape)


