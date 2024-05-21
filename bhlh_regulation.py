import pandas as pd

df_leaves=pd.read_csv('interactions_leaves.tsv', sep='\t')
df_roots=pd.read_csv('interactions_roots.tsv', sep='\t')
df = pd.DataFrame(columns=['Module', 'Gene'])

modules = ["M1","M2", "M3", "M4", "M5", "M6", "M7"]

for module in modules:

    set_leaves = set(df_leaves["Gene1"][df_leaves['Module'] == 'M1'].unique())
    set_roots = set(df_roots["Gene1"][df_roots['Module'] == 'M1'].unique())
    z = set_leaves.intersection(set_roots)
    for item in z:
        new_row = {'Module':module, 'Gene':item}
        df = df.append(new_row, ignore_index=True)

df.to_csv('bhlh_regulation.csv', index=False)
