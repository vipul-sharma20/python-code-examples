import subprocess
import plotly
import plotly.plotly as py  
import plotly.tools as tls   
from plotly.graph_objs import *
import numpy as np

stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[0]
stream = Stream(
            token=stream_id,
            maxpoints=80  
                )
trace1 = Scatter(
            x=[],
            y=[],
            mode='lines+markers',
            stream=stream
                        )

data = Data([trace1])
layout = Layout(title='Time Series')
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename='Idle Memory vs Time')
s = py.Stream(stream_id)

print unique_url
s.open()

import datetime
import time
def main():
    #try:
        while True:
    
            x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            y = int(str(subprocess.Popen('vmstat', stdout=subprocess.PIPE, shell=True).communicate()).split('\\n')[2].split(' ')[5])/1024
            s.write(dict(x=x,y=y))
            time.sleep(0.08)
    #except:
    #    main()
main()
