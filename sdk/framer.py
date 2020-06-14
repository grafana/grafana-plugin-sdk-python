import io

import pandas as pd
import pyarrow as pa
from pyarrow import json


class Framer(object):

    def __init__(self, data, schema=None):
        self.data = self._to_frame(data, schema)

    def __dict__(self):
        return self.data.to_pydict()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dict__())

    @property
    def schema(self):
        return self.data.schema

    @property
    def metadata(self):
        return self.data.schema.metadata

    @property
    def types(self):
        return self.data.schema.types

    @property
    def names(self):
        return self.data.schema.names

    @property
    def shape(self):
        return self.data.shape

    def _to_frame(self, data, schema):
        pd_frame = self._to_pd_frame(data)
        return self._to_arrow(pd_frame, schema)

    def _to_pd_frame(self, data):
        return pd.read_json(io.StringIO(data))

    def _to_arrow(self, data, schema):
        if not schema:
            schema = pa.Schema.from_pandas(data)
        return pa.Table.from_pandas(data, schema=schema)
