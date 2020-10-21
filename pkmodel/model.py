#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    compartments: numeric, optional
        the number of peripheral compartments

    """
    def __init__(self, compartments=0):
        self._compartments = compartments

