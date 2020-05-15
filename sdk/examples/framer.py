import pandas as pd
import pyarrow as pa
import os


class Framer(object):

    def __init__(self, path):
        self.data = self._to_pd_frame(path)

    def _to_pd_frame(self, path):
        return pd.read_json(path)

    def to_arrow(self):
        schema = pa.Schema.from_pandas(self.data)
        table = pa.Table.from_pandas(self.data, schema=schema)
        return (table, schema)


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "data/framer-data.json")
    f = Framer(path)
    a = f.to_arrow()
    print(a[0].to_pandas(), a[1])
