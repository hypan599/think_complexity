class Cdf:

    def __init__(self):
        self.values = None
        self.probabilities = None

    def from_list(self, *args):
        temp_dict = {}
        probs = [(i + 1) / len(args) for i in range(len(args))]
        for idx, v in enumerate(sorted(args)):
            temp_dict[v] = probs[idx]

        self.values = list(temp_dict.keys())

        self.probabilities = list(temp_dict.values())

    def prob(self, v):
        if v not in self.values:
            raise ValueError("%s not found in Cdf!" % v)
        for idx, value in enumerate(self.values):
            if v < value:
                break
        return self.probabilities[idx-1]

    def value(self, prob):
        if prob > 1 or prob < 0:
            raise ValueError("invalid p")
        for idx, p in enumerate(self.probabilities):
            if p > prob:
                break
        return self.values[idx-1]

    def render(self):
        double_values = []
        double_probs = [0.0]
        for i in self.values:
            double_values.append(i)
            double_values.append(i)
        for i in self.probabilities:
            double_probs.append(i)
            double_probs.append(i)
        double_probs.pop(-1)
        return double_values, double_probs
