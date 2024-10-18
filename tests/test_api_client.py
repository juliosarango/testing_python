import unittest, requests
from src.api_client import get_location
from unittest.mock import patch


class ApiClientTest(unittest.TestCase):
    # Sobre escribimos la función donde hacemos la petición al api
    @patch("src.api_client.requests.get")
    def test_get_location_return_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        
        # Establecemos los datos que deseamos y la estructura que necesitamos.
        # Mockeamos la respuesta del API
        mock_get.return_value.json.return_value = {            
            'countryName': 'USA', 
            'regionName': 'Florida', 
            'cityName': 'MIAMI',
            'countryCode': "US"
        }            
        
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "MIAMI")
        self.assertEqual(result.get("code"), "US")
        
        # Nos aseguramos que la petición sea con la url y el parámetro correcto
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
        
        
    @patch("src.api_client.requests.get")
    def test_get_location_return_side_effect(self, mock_get):
        # Se realizarán dos llamadas, una con error y otra correctamente
        
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'countryName': 'USA', 
                    'regionName': 'Florida', 
                    'cityName': 'MIAMI',
                    'countryCode': "US"                    
                }
                
            )
        ]               
        
        with self.assertRaises(
            requests.exceptions.RequestException
        ):
            get_location("8.8.8.8")            
        
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "MIAMI")
        self.assertEqual(result.get("code"), "US")


    @patch("src.api_client.requests.get")
    def test_get_location_return_side_effect_with_invalid_ip(self, mock_get):
        # Se realizarán dos llamadas, una con error y otra correctamente
        
        mock_get.side_effect = [
            requests.exceptions.HTTPError("8.8.0 does not appear to be an IPv4 or IPv6 address"),            
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'countryName': 'USA', 
                    'regionName': 'Florida', 
                    'cityName': 'MIAMI',
                    'countryCode': "US"                    
                }
                
            )
        ]                
        
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location("8.8.8.8")
        
        
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "MIAMI")
        self.assertEqual(result.get("code"), "US")        
        
        
        
        
        
        
        