class JsonComp:
    def __init__(self, json1, json2):
        self.json1 = json1
        self.json2 = json2

    def ordered(self, json):
        if isinstance(json, dict):
            return sorted((k, self.ordered(v)) for k, v in json.items())
        if isinstance(json, list):
            return sorted(self.ordered(x) for x in json)
        else:
            return json

    def comp(self):
        return self.ordered(self.json1) == self.ordered(self.json2)

