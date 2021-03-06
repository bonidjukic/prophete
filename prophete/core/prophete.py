import os

import pandas as pd
import numpy as np
from fbprophet import Prophet

class Prophete:

  def __init__(self, prediction):
    self.prediction = prediction
    self.df = pd.read_csv(prediction.data_upload)
    self.prophet = Prophet()

  def predict(self, *args, **kwargs):

    apply_log = kwargs.pop('apply_log', False)
    periods = kwargs.pop('periods', 30)

    if apply_log:
      self.df['y'] = np.log(self.df['y'])

    self.df.head()
    self.prophet.fit(self.df)

    future = self.prophet.make_future_dataframe(periods=periods)

    forecast = self.prophet.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    print(forecast)

    try:
      self.prophet.plot(forecast).savefig(self._get_savefig_path('plot_1.png'))
      self.prophet.plot_components(forecast).savefig(self._get_savefig_path('plot_2.png'))
    except Exception as e:
      print(e)

  def _get_savefig_path(self, filename):
    return os.path.join(
      self.prediction.get_media_dir(absolute_path=True),
      filename
    )