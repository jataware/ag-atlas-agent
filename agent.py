from archytas.react import ReActAgent, FailedTaskError
from archytas.tools import PythonTool

from easyrepl import REPL

import pandas as pd

# load the data resources
mean_yield = pd.read_csv('data/Mean_yield_difference@1.csv')
spotlight = pd.read_csv('data/spotlight2_Extended Table 2@1.csv')

# create the agent with the tools list
python = PythonTool(
    prelude='import pandas as pd\nfrom matplotlib import pyplot as plt\nimport seaborn as sns\n',
    locals={'mean_yield': mean_yield, 'spotlight': spotlight},
)
tools = [python]

agent = ReActAgent(tools=tools, verbose=True)
context = f"""
You are an assistant helping a user understand the Africa Agriculture Adapatation Atlas. This is a data source
that can help the users understand the impact of crop interventions such as fertilizer application on crop yields in Africa.

You have access to two pandas dataframes:
1. `mean_yield` - This contains the yield difference for each crop intervention. It's columns are: {{mean_yield.columns}}.
2. `spotlight` - This contains information about various outcomes of crop interventions. It's columns are: {{spotlight.columns}}.

You should use these in conjunction with the PythonTool to help the user understand the data and answer questions for the user.
"""
id = agent.add_context(context)

# REPL to interact with agent
for query in REPL():
    try:
        answer = agent.react(query)
        print(answer)
    except FailedTaskError as e:
        print(f"Error: {e}")