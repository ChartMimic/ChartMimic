class BaseAgent:
    def __init__(self):
        super().__init__()

    def run(self):
        pass

    @classmethod
    def from_config(cls, llm_model, config):
        pass
