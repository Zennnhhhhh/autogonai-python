import requests


class Dashboard:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass


class Project:
    """Handles all Project Specific operations"""

    endpoint = "engine/project/"

    def __init__(self, client):
        self.client = client

    def get(self, app_id: str):
        """Fetches an existing Project

        Args:
            app_id (str): Project UUID

        Returns:
            dict: Project details
        """
        response = self.client.send_request(self.endpoint + app_id, method="get")
        return response

    def create(self, name: str, description: str) -> dict:
        """Create a project

        Args:
            name (str): name of the project
            description (str): short description for project

        Returns:
            dict: Project details
        """
        body = {"project_name": name, "project_description": description}
        response = self.client.send_request(self.endpoint, body)
        return response

    def delete(self, app_id: str) -> str:
        """Deletes a project

        Args:
            app_id (str): Project UUID

        Returns:
            str: Confirmation of delete
        """
        response = self.client.send_request(self.endpoint + app_id, method="delete")
        return response


class StateManagement:
    """Handles all StateManagement Specific operations"""
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass


class Dataset:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass
