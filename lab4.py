from repository.repository import Repository
from service.service import Service
from ui.ui import Ui
from utils.utils import computeDistance

# berlin52.txt, Berlin (Germany), 52, optimal path=7542
repository = Repository("data/berlin52.txt","data/out.txt",False)
service = Service(repository)
ui = Ui(service)
ui.run()