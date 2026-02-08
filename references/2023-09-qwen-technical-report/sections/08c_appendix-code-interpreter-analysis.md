# A.3 Analysis of Code Interpreter [p. 58–59]

[p. 58] A case of comparison between CODE LLAMA and QWEN-CHAT is provided. This case demonstrates the advantages of QWEN-CHAT in processing tabular data and performing complex tasks.

**Figure 5** (p. 59): "Example showcasing QWEN-CHAT's ability in using a code interpreter via ReAct prompting. The ReAct instruction is omitted for clarity. QWEN creates a two-step plan and first investigates the columns present in the CSV file before proceeding to draw the plot, as shown in the top-left figure. CODE LLAMA, however, attempts to plot based on non-existent columns in its initial attempt, as seen in the bottom figure. CODE LLAMA can only reliably perform the task if the columns are provided in the user query, as shown in the top-right figure."

The figure shows four panels comparing QWEN-CHAT and CODE LLAMA on the task: "Create a scatter plot with different size and color settings" given an uploaded CSV file (`scatter_data.csv`).

- **Top-left panel (QWEN-CHAT):** QWEN-CHAT first uses the code interpreter to load the data with `pd.read_csv('scatter_data.csv')` and displays the first few rows using `df.head()`. The observation shows the dataframe has columns: `x`, `y`, `sizes`, `colors`. In the second step, QWEN-CHAT uses the discovered column names to create the scatter plot: `ax.scatter(df['x'], df['y'], s=df['sizes'], c=df['colors'])`. The resulting scatter plot is correctly rendered.

- **Top-right panel (CODE LLAMA with column names provided):** When the user query explicitly provides the column names, CODE LLAMA successfully loads the data and creates the scatter plot with proper axis labels (`plt.xlabel('x')`, `plt.ylabel('y')`) and uses `plt.scatter(df['x'], df['y'], s=df['sizes'], c=df['colors'])`. The resulting scatter plot is correctly rendered.

- **Bottom-left panel (CODE LLAMA without column names):** CODE LLAMA attempts to create the scatter plot directly without first inspecting the data. It uses `plt.scatter(data['x'], data['y'], s=data['size'], c=data['color'])` — referencing columns `'size'` and `'color'` (singular) which do not exist in the CSV file (the actual columns are `'sizes'` and `'colors'`).

- **Bottom-right panel (CODE LLAMA error output):** The code execution results in a `KeyError: 'size'`, demonstrating that CODE LLAMA fails when it does not first investigate the data structure.

The key finding is that QWEN-CHAT employs a two-step ReAct strategy — first examining the data, then acting on the discovered structure — while CODE LLAMA attempts to act immediately, which fails when column names are not explicitly provided by the user. [p. 58–59]
