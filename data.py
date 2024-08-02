import pandas as pd
import numpy as np

# Sample data for ALIF PPF vs. TLIF PSI
data_alif_tlif = {
    'Cohort': ['ALIF PPF'] * 40 + ['TLIF PSI'] * 40,
    'Follow_up_months': np.random.normal(39.5, 5, 40).tolist() + np.random.normal(45.6, 5, 40).tolist(),
    'Revision_rate': [0.1] * 40 + [0.05] * 40,
    'Time_to_revision_days': np.random.normal(323.1, 50, 40).tolist() + np.random.normal(244.2, 50, 40).tolist(),
    'PI_LL_mismatch_correction': [0.813] * 40 + [0.875] * 40,
    'ODI_improvement': np.random.normal(15, 5, 40).tolist() + np.random.normal(15, 5, 40).tolist(),
    'VAS_improvement': np.random.normal(3, 1, 40).tolist() + np.random.normal(3, 1, 40).tolist()
}

# Sample data for OLIF vs. XLIF
data_olif_xlif = {
    'Cohort': ['OLIF'] * 30 + ['XLIF'] * 35,
    'Follow_up_months': np.random.normal(39.2, 5, 30).tolist() + np.random.normal(45.4, 5, 35).tolist(),
    'Revision_rate': [0.1] * 30 + [0.114] * 35,
    'Time_to_revision_days': np.random.normal(300, 50, 30).tolist() + np.random.normal(250, 50, 35).tolist(),
    'PI_LL_mismatch_correction': [0.86] * 30 + [0.83] * 35,
    'ODI_improvement': np.random.normal(20, 5, 30).tolist() + np.random.normal(20, 5, 35).tolist(),
    'VAS_improvement': np.random.normal(4, 1, 30).tolist() + np.random.normal(4, 1, 35).tolist()
}

df_alif_tlif = pd.DataFrame(data_alif_tlif)
df_olif_xlif = pd.DataFrame(data_olif_xlif)
