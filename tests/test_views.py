from application import create_app
from flask_testing import TestCase
import unittest

from application.addviews import wagon


class test_views(TestCase):
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        return app

    def setUp(self):
        self.client = self.app.test_client()

    def test_index(self):
        self.assert200(self.client.get("/"))

    def test_add_get(self):
        self.assert200(self.client.get("/add/locomotive"))
        self.assert200(self.client.get("/add/wagon"))
