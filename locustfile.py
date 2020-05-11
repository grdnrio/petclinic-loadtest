from locust import HttpLocust, TaskSet, task, between
from random import randint, choice
import names
from faker import Faker

from faker.providers import address
fake = Faker()
fake.add_provider(address)


class WebTasks(TaskSet):

    @task
    def load(self):

        self.client.get("/")
        self.client.get("/owners")
        self.client.post("/owners/new", data={"address": str(randint(1, 100)) + " " + names.get_first_name() + " Street", "city": fake.city(), "firstName": names.get_first_name(), "lastName": names.get_last_name(), "telephone": randint(000000, 999999)})

class Web(HttpLocust):
    task_set = WebTasks
    wait_time = between(0, 15)