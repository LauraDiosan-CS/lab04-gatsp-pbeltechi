from repository.repository import Repository

from repository.repository import Repository
from service.service import Service
from ui.ui import Ui

from utils.utils import computeDistance


repository = Repository("data/berlin52.txt","data/out.txt",False)
service = Service(repository)
ui = Ui(service)
ui.run()