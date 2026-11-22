from unittest.mock import Mock 
from payment import OrderProcessor

def test_processor_charges_correct_amount():
    gateway = Mock() 
    gateway.charge.return_value = "OK"

    processor = OrderProcessor(gateway)
    processor.process(250)

    gateway.charge.assert_called_once_with(250)