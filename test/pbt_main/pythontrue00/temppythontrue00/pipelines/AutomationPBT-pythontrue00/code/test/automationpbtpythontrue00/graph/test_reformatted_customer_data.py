from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from automationpbtpythontrue00.graph.reformatted_customer_data import *
from automationpbtpythontrue00.config.ConfigStore import *


class reformatted_customer_dataTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/automationpbtpythontrue00/graph/reformatted_customer_data/in0/schema.json',
            'test/resources/data/automationpbtpythontrue00/graph/reformatted_customer_data/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/automationpbtpythontrue00/graph/reformatted_customer_data/out/schema.json',
            'test/resources/data/automationpbtpythontrue00/graph/reformatted_customer_data/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = reformatted_customer_data(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("phone", "email", "customer_id", "first_name", "last_name"),
            dfOutComputed.select("phone", "email", "customer_id", "first_name", "last_name"),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
