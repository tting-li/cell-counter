#import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#for stat calc purpose
import scipy.stats as stats


#read file
df = pd.read_csv("cell-count.csv")

#create result list
output = []

#get all cell populations
cell_population = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]

#task 1 -- perecentage and total cell count
#tot count
df['total_count'] = df[cell_population].sum(axis=1)


#run through each sample
for i, row in df.iterrows():
    id = row["sample"]
    total_count = row["total_count"]

    #convert to percentage
    for cell_pop in cell_population:
        count = row[cell_pop]
        percentage = (count / total_count) * 100

        #add to output list 
        output.append({
            "sample": id,
            "total_count": total_count,
            "population": cell_pop,
            "count": count,
            "percentage": percentage,
            #DEBUG: include for boxplot
            "type": row["sample_type"],
            "treatment": row["treatment"],
            "condition": row["condition"],
            "response": row["response"]

            })
        
        


#convert to output csv dataframe
output_df = pd.DataFrame(output)
output_df.to_csv("cell-count-output.csv", index = False)

#task 2 --  compare melanoma patients res tr1 vs no res -- predict response to tr1

#debug check:
# if {"type", "treatment", "condition"}.issubset(output_df.columns):
    #only put pbmc samples w/ tr1 and melanoma
pbmc_df = output_df[(output_df["type"] == "PBMC") & (output_df["treatment"] == "tr1") & (output_df["condition"]== "melanoma")]

# for cell_pop in cell_population:
    #stat test performing purpose:
    # response = pbmc_df[pbmc_df["response"] == "y"][cell_pop]
    # no_response = pbmc_df[pbmc_df["response"] == "n"][cell_pop]
    #mann-whitney u test = best test
    # stat, p_val = stats.mannwhitneyu(response, no_response, alternative="two-sided")
    # output.append({"U stat": stat, "p": p_val})

#stat test performing purpose:
for cell_pop in cell_population:
    #get specific cell data for response and no responses
    cell_data = pbmc_df[pbmc_df["population"] == cell_pop]
    
    #separate by response
    response = cell_data[cell_data["response"] == "y"]["percentage"]
    no_response = cell_data[cell_data["response"] == "n"]["percentage"]

    #mannwhitney from scipy.stats
    stat, p_val = stats.mannwhitneyu(response, no_response, alternative="two-sided")
    output.append({
            "population": cell_pop,
            "U_stat": stat, 
            "p_value": p_val
    })


    #boxplot generating
plt.figure(figsize=(10,8))
sns.boxplot(x="population", y="percentage", data = pbmc_df, hue="response")
plt.title('Cell Population Frequencies of Responders vs Non-Responders to tr1')
plt.xlabel("Cell Population")
plt.ylabel("Frequency (%)")
plt.savefig("Tr1-Response-Comparison.png")
plt.show()
# else:
#     print("Error with type, treatment, and condition")


output_df = pd.DataFrame(output)
output_df.to_csv("cell-count-output-responses.csv", index = False)
print(output_df)

