from flytekit.remote import FlyteRemote
from flytekit.configuration import Config
from workflows.example import wf

remote = FlyteRemote(config=Config.auto(), \
                      default_project="flytesnacks", default_domain="development")

execution = remote.execute(wf, inputs={"name": "Kermit"}, image_config=any)

print(f"Execution url: {remote.generate_console_url(execution)}")
