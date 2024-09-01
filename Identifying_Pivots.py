import pandas as pd

# Creating the DataFrame
sample_input = pd.read_csv('Sample_input.txt', sep=';', header=None, names=["DATE & TIME", "OPEN", "HIGH", "LOW", "CLOSE", "VOLUME", "SPL", "SPH"])
sample_input['DATE & TIME'] = pd.to_datetime(sample_input['DATE & TIME'])
sample_input['SPL'] = None
sample_input['SPH'] = None
sample_input = sample_input.loc[:, sample_input.columns != 'VOLUME']


# Function to verify pivots
def check_pivot(df):
    toggle = True

    for i in range(len(df) - 2):
        if toggle:
            if df['HIGH'].iloc[i] < df['HIGH'].iloc[i + 1] and df['HIGH'].iloc[i] < df['HIGH'].iloc[i + 2] and df['CLOSE'].iloc[i] < df['CLOSE'].iloc[i + 1] and df['CLOSE'].iloc[i] < df['CLOSE'].iloc[i + 2]:
                df.at[i, 'SPL'] = 'SPL'
                toggle = False
        else:
            if df['LOW'].iloc[i] > df['LOW'].iloc[i + 1] and df['LOW'].iloc[i] > df['LOW'].iloc[i + 2] and df['CLOSE'].iloc[i] > df['CLOSE'].iloc[i + 1] and df['CLOSE'].iloc[i] > df['CLOSE'].iloc[i + 2]:
                df.at[i, 'SPH'] = 'SPH'
                toggle = True

    return df


# Aplying the function to the dataframe and exporting it as CSV
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
sample_input = check_pivot(sample_input)
print(sample_input)
sample_input.to_csv('sample_input.csv', index=False)
