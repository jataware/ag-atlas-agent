from beaker_bunsen.bunsen_context import BunsenContext
from typing import TYPE_CHECKING, Any, Dict, List

from .agent import AgAgent

import pandas as pd

# load the data resources
mean_yield = pd.read_csv('data/Mean_yield_difference@1.csv')
spotlight = pd.read_csv('data/spotlight2_Extended Table 2.csv')
mean_yield_readme = open('data/mean_yield.txt').read()
spotlight_readme = open('data/spotlight.txt').read()

class AgContext(BunsenContext):

    agent_cls = AgAgent
    enabled_subkernels = ["python3"]

    async def setup(self, context_info=None, parent_header=None):
        super().setup(context_info, parent_header)
        return await self.load_dataset(parent_header=parent_header)

    async def load_dataset(self, parent_header={}):
        code = self.get_code("load_datasets")
        response = await self.evaluate(
            code,
            parent_header=parent_header,
        )        

    @classmethod
    def default_payload(cls) -> str:
        return "{}"    

    async def auto_context(self):
        return f"""
You are an assistant helping a user understand the Africa Agriculture Adapatation Atlas. This is a data source
that can help the users understand the impact of farm management practices such as fertilizer application on crop yields in Africa.
The data is organized by agroecological zone and crop type. Agro-Ecological Zone, is a land resource classification system developed by the Food and Agriculture Organization (FAO) 
of the United Nations. It is used for the assessment of agricultural resources and potential. The classification is based on climate, soil, 
topography, and vegetation to delineate land with similar potentials and constraints for agricultural production. AEZs help in planning 
sustainable agricultural practices and land use management. 

Farm management practices refer to the methods and strategies used by farmers to manage their farms efficiently and 
sustainably. These practices encompass a wide range of activities, including crop selection and rotation, 
soil management, water use, pest and disease control, livestock care, and the use of inputs such as fertilizers 
and pesticides. The goal of farm management practices is to optimize agricultural production, ensure profitability, 
and minimize environmental impact. Examples include conservation tillage, organic farming, precision agriculture, 
integrated pest management, and agroforestry.

You have access to two pandas dataframes:
1. `mean_yield` - This contains the yield difference for each crop and farm management practice by agroecological zone and crop. It's columns are {mean_yield.columns}.
2. `spotlight` - This contains information about various outcomes farm management practices. It's columns are {spotlight.columns}.

Here is the data dictionary for `mean_yield`. Note that each key is the name of a column.

```
{mean_yield_readme}
```

Here is the data dictionary for `spotlight`. Note that each key is a column name

```
{spotlight_readme}
```

You should use these dataframes in conjunction with the PythonTool to help the user understand the data and answer questions for the user.

When you write python code with the PythonTool, you should use your knowledge of the column names and values in the dataframes to craft
correct code and queries that will help the user understand the data better. You can also use the PythonTool to plot graphs and visualize the data; 
when doing so, default to using seaborn and writing descriptive titles and captions.
        """.strip()

