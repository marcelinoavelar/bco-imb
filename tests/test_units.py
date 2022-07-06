from tkinter.messagebox import NO
import pytest
from src.domain.entities.property import Property


class TestProperties:

    def test_should_create_property(self):
        property = Property(price=250000.50,rental=500.00,owner="Marcelino Avelar",status='purchased')
        assert property.price == 250000.50
        assert property.rental == 500.00
        assert property.status == 'purchased'
        assert property.owner == "Marcelino Avelar"

    def test_should_create_property_whitout_owner(self):
        property = Property(price=250000.50,rental=500.00)
        assert property.price == 250000.50
        assert property.rental == 500.00
        assert property.status == 'available'
        assert property.owner == None

    def test_should_not_create_invalid_property(self):
        with pytest.raises(ValueError, match='Invalid price'):
            Property(price=0.0,rental=0.1,owner="Marcelino Avelar",status='purchased')
        with pytest.raises(ValueError, match='Invalid rental'):
            Property(price=0.1,rental=0.0,owner="Marcelino Avelar",status='purchased')