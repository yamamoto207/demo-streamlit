import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""

# 章
## 節
### 項

```python
import streamlit as st
import pandas as pd
import numpy as np

```
"""

st.write('プログレスバーの表示')
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

