import unittest
import os
from agents.api_agent import *
import getpass  # Get username like whoami

import agents.api_agent as api

"""
    API agent unit tests
"""


class TestAPIAgentModule(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        username = getpass.getuser()
        self.test_path = "/home/" + username

    ##############################################################################################

    def setUp(self):
        celery.conf.update(task_always_eager=True)

    ##############################################################################################

    def test1_read_photo_configuration(self):
        # Sample configuration file
        file_content = b'---\n\nphoto:\n    resolution: "HIGH"\n    rotation: 180\n   ' \
                       b' vflip: False\n    hflip: True\n' \
                       b'\nvideo:\n    resolution: "MEDIUM"\n   ' \
                       b' rotation: 90\n    vflip: False\n    hflip: False\n    showDatetime: True\n\n\n\n\n'

        file_path = os.path.join(self.test_path, "modules_config.yml")

        # Writing content
        f = open(file_path, 'w')
        f.write(file_content.decode("utf-8"))
        f.close()

        # Read configuration file
        photo_configuration = read_photo_configuration(config_file_path=file_path)

        # Check if file is created
        exist_config_file = os.path.isfile(file_path)

        # Parameters
        resolution = photo_configuration['resolution']
        rotation = photo_configuration['rotation']
        vflip = photo_configuration['vflip']
        hflip = photo_configuration['hflip']

        # Delete file created
        os.remove(file_path)

        exist_config_file_after_deleting = os.path.isfile(file_path)

        # ----------------------------------------------------------------------------------------#
        #                                     CHECKS                                              #
        # ----------------------------------------------------------------------------------------#

        self.assertTrue(exist_config_file)
        self.assertTrue(resolution, "HIGH")
        self.assertEqual(rotation, 180)
        self.assertFalse(vflip)
        self.assertTrue(hflip)
        self.assertFalse(exist_config_file_after_deleting)

    ##############################################################################################

    def test2_read_video_configuration(self):
        # Sample configuration file
        file_content = b'---\n\nphoto:\n    resolution: "HIGH"\n    rotation: 180\n   ' \
                       b' vflip: False\n    hflip: True\n' \
                       b'\nvideo:\n    resolution: "MEDIUM"\n   ' \
                       b' rotation: 90\n    vflip: False\n    hflip: False\n    showDatetime: True\n\n\n\n\n'

        file_path = os.path.join(self.test_path, "modules_config.yml")

        # Writing content
        f = open(file_path, 'w')
        f.write(file_content.decode("utf-8"))
        f.close()

        # Read configuration file
        video_configuration = read_video_configuration(config_file_path=file_path)

        # Check if file is created
        exist_config_file = os.path.isfile(file_path)

        # Parameters
        resolution = video_configuration['resolution']
        rotation = video_configuration['rotation']
        vflip = video_configuration['vflip']
        hflip = video_configuration['hflip']
        showDatetime = video_configuration['showDatetime']

        # Delete file created
        os.remove(file_path)

        exist_config_file_after_deleting = os.path.isfile(file_path)

        # ----------------------------------------------------------------------------------------#
        #                                     CHECKS                                              #
        # ----------------------------------------------------------------------------------------#

        self.assertTrue(exist_config_file)
        self.assertTrue(resolution, "MEDIUM")
        self.assertEqual(rotation, 90)
        self.assertFalse(vflip)
        self.assertFalse(hflip)
        self.assertTrue(showDatetime)
        self.assertFalse(exist_config_file_after_deleting)

    ##############################################################################################

    def test3_take_photo(self):
        # Take photo
        photo_file = take_photo(photo_path=self.test_path)

        # Check if the image exist in the destination directory
        exist_image = os.path.isfile(photo_file)

        # Delete test image
        os.remove(photo_file)

        # Check if the image exist in the destination directory
        exist_image_after_deleting = os.path.isfile(photo_file)

        # ----------------------------------------------------------------------------------------#
        #                                     CHECKS                                              #
        # ----------------------------------------------------------------------------------------#

        self.assertTrue(exist_image)
        self.assertFalse(exist_image_after_deleting)

    ##############################################################################################

    def test4_record_video(self):
        # Record a video
        video_file = record_video(record_time=5, video_path=self.test_path)

        # Check if the video exist in the destination directory
        exist_video = os.path.isfile(video_file)

        # Delete test video
        os.remove(video_file)

        # Check if the video exist in the destination directory
        exist_video_after_deleting = os.path.isfile(video_file)

        # ----------------------------------------------------------------------------------------#
        #                                     CHECKS                                              #
        # ----------------------------------------------------------------------------------------#

        self.assertTrue(exist_video)
        self.assertFalse(exist_video_after_deleting)

        ##############################################################################################