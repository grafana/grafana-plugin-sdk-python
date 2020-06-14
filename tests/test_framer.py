import os
from unittest import TestCase
import json

import pyarrow as pa

from sdk.framer import Framer
from sdk.converters import epoch_to_datetime


class TestFramer(TestCase):

    def setUp(self):
        path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'test_data.json')
        with open(path, 'r') as f:
            self.data = json.load(f)

    def test_json_users(self):

        f = Framer(json.dumps(self.data['users']))

        self.assertEqual((10, 8), f.shape)

        geo = [
            pa.field('lat', pa.string()),
            pa.field('lng', pa.string())
        ]

        address = [
            pa.field('city', pa.string()),
            pa.field('geo', pa.struct(geo)),
            pa.field('street', pa.string()),
            pa.field('suite', pa.string()),
            pa.field('zipcode', pa.string())
        ]

        company = [
            pa.field('bs', pa.string()),
            pa.field('catchPhrase', pa.string()),
            pa.field('name', pa.string())
        ]

        self.assertEqual(f.data.column(0).type, pa.int64())
        self.assertEqual(f.data.column(1).type, pa.string())
        self.assertEqual(f.data.column(2).type, pa.string())
        self.assertEqual(f.data.column(3).type, pa.string())
        self.assertEqual(f.data.column(4).type, pa.struct(address))
        self.assertEqual(f.data.column(5).type, pa.string())
        self.assertEqual(f.data.column(6).type, pa.string())
        self.assertEqual(f.data.column(7).type, pa.struct(company))

    def test_json_metrics(self):

        f = Framer(json.dumps(self.data['metrics']))

        self.assertEqual((60, 7), f.shape)

        self.assertEqual(f.data.column(0).type, pa.float64())
        self.assertEqual(f.data.column(1).type, pa.float64())
        self.assertEqual(f.data.column(2).type, pa.int64())
        self.assertEqual(f.data.column(3).type, pa.int64())
        self.assertEqual(f.data.column(4).type, pa.list_(pa.string()))
        self.assertEqual(f.data.column(5).type, pa.list_(pa.string()))

    def test_custom_schema_metrics(self):

        schema = pa.schema([
            ('average.diskWritesPerSecond', pa.float64()),
            ('average.memoryUsedBytes / memoryTotalBytes * 100', pa.float64()),
            ('beginTimeSeconds', pa.timestamp('s')),
            ('endTimeSeconds', pa.timestamp('s')),
            ('entityIdentityNamelinuxDistribution', pa.list_(pa.string())),
            ('facet', pa.list_(pa.string())),
            ('max.memoryUsedBytes', pa.int64()),
        ])

        for item in self.data['metrics']:
            item['beginTimeSeconds'] = epoch_to_datetime(
                item['beginTimeSeconds'])
            item['endTimeSeconds'] = epoch_to_datetime(
                item['endTimeSeconds'])

        f = Framer(json.dumps(self.data['metrics']), schema=schema)

        self.assertEqual(f.data.column(0).type, pa.float64())
        self.assertEqual(f.data.column(1).type, pa.float64())
        self.assertEqual(f.data.column(2).type, pa.timestamp('s'))
        self.assertEqual(f.data.column(3).type, pa.timestamp('s'))
        self.assertEqual(f.data.column(4).type, pa.list_(pa.string()))
        self.assertEqual(f.data.column(5).type, pa.list_(pa.string()))
        self.assertEqual(f.data.column(6).type, pa.int64())
