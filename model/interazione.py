from dataclasses import dataclass


@dataclass
class Interazione:
    cromosoma1: str
    cromosoma2: str
    id_gene1 : str
    id_gene2 : str
    correlazione : int

    def __str__(self):
        return f"id1: {self.id_gene1} - id2: {self.id_gene2} - correlazione: {self.correlazione}"

    def __repr__(self):
        return f"{self.id_gene1} - {self.id_gene2} {self.correlazione}"

    def __eq__(self, other):
        return self.id_gene1 == other.id_gene1 and self.id_gene2 == other.id_gene2

    def __hash__(self):
        return hash(self.id_gene1)