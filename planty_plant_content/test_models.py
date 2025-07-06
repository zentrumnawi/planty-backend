from django.test import TestCase
from planty_plant_content.models import Plant, GeneralInformation


class PlantModelTest(TestCase):
    """Test cases for the Plant model and its relationships."""

    def setUp(self):
        """Set up test data."""
        self.plant = Plant.objects.create()
        self.general_info = GeneralInformation.objects.create(
            plant=self.plant,
            name="Test Plant",
            sub_name="Test Sub Name",
        )

    def test_plant_creation(self):
        """Test that a plant can be created."""
        self.assertIsNotNone(self.plant)
        self.assertEqual(Plant.objects.count(), 1)

    def test_general_information_relationship(self):
        """Test the relationship between Plant and GeneralInformation."""
        self.assertEqual(self.plant.general_information, self.general_info)
        self.assertEqual(self.general_info.plant, self.plant)

    def test_general_information_fields(self):
        """Test that GeneralInformation fields are correctly set."""
        self.assertEqual(self.general_info.name, "Test Plant")
        self.assertEqual(self.general_info.sub_name, "Test Sub Name")

    def test_plant_str_representation(self):
        """Test the string representation of a Plant."""
        self.assertIn("Plant object", str(self.plant))
