from core.api import MinerAPI

api = MinerAPI()

print(api.ping())
print(api.get_summary())
