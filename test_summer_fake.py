import os
os.environ["UNIT_TEST"] = "true"

import mod2

def test_summber_fake():
    assert "11" == mod2.summer(5, 6)