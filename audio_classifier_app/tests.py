import unittest
import requests
import subprocess

class AudioClassificationServiceTests(unittest.TestCase):

    def setUp(self):
        # Set up any necessary configurations or test data
        self.base_url = 'http://localhost:5000'  # Adjust the URL based on your service
    
    def send_classification_curl(self, audio_file_path):
        # Helper method to send a classification request using curl
        curl_command = [
            'curl',
            '-X', 'POST',
            '-F', f'file=@{audio_file_path}',
            f'{self.base_url}/upload'
        ]

        try:
            # Run the curl command using subprocess
            result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            return result
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during the subprocess execution
            return e

    def test_audio_classification_endpoint(self):
        # Test the endpoint that handles audio classification requests

        # Test case 1: Valid audio file
        audio_file_path = './uploads/jingle-bell-2.wav'
        response = self.send_classification_curl(audio_file_path)
        self.assertEqual(response.returncode, 0) # 0 means success in curl
        
        # Test case 2: Invalid audio file
        non_existent_path = 'my_way.wav'
        response = self.send_classification_curl(non_existent_path)
        self.assertEqual(response.returncode, 26)  # curl returns 26 for couldn't open files


    def send_classification_request(self, audio_file_path):
    # Helper method to send a classification request using requests library
        files = {'file': open(audio_file_path, 'rb')}
        url = f'{self.base_url}/upload'
        response = requests.post(url, files=files)
        return response

    def test_audio_classification_endpoint_requests(self):
        # Test the endpoint that handles audio classification requests using requests library

        # Test case 1: Valid audio file
        audio_file_path = './uploads/jingle-bell-2.wav'
        response = self.send_classification_request(audio_file_path)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
    