import json
import os


class FeeManager:

    DEFAULT_FEE = 2.0

    DEFAULT_WALLET = (
        "47mL7UvR9XXhru4yDVkFUHb5KrjgXz6h4i1CwD6iuJuxDb18inB9Lu7e4sznETRJG45PLLaHoXjESAHtdtQoirF4DZLPJto"
    )


    def __init__(self, config_path):

        self.config_path = config_path

        self.data = {
            "enabled": False,
            "accepted": False,
            "percentage": self.DEFAULT_FEE,
            "wallet": self.DEFAULT_WALLET
        }

        self.load()



    def load(self):

        if os.path.exists(self.config_path):

            try:

                with open(
                    self.config_path,
                    "r"
                ) as f:

                    saved = json.load(f)

                    self.data.update(saved)

            except Exception:

                pass



    def save(self):

        os.makedirs(
            os.path.dirname(
                self.config_path
            ),
            exist_ok=True
        )


        with open(
            self.config_path,
            "w"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4
            )



    def accept_fee(self):

        self.data["accepted"] = True
        self.data["enabled"] = True

        self.save()



    def decline_fee(self):

        self.data["accepted"] = True
        self.data["enabled"] = False

        self.save()



    def is_enabled(self):

        return (
            self.data["enabled"]
            and
            self.data["accepted"]
        )



    def percentage(self):

        return self.data["percentage"]



    def wallet(self):

        return self.data["wallet"]
