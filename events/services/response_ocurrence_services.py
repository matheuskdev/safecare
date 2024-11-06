"""Service for calculate deadline in model response_ocurrence_models"""
from classifications.models import (
    DamageClassification,
    OcurrenceClassification,
)


class CalculateDeadline:
    """
    Service class to calculate the deadline for response to an occurrence.

    This class calculates the response deadline based on the classifications of
    the occurrence and the damage. The deadline is determined by summing a number
    of days based on these classifications.

    Attributes:
        ocurrence_classification (OcurrenceClassification): The classification of the occurrence.
        damage_classification (DamageClassification): The classification of the damage.

    Methods:
        __init__(ocurrence, damage):
            Initializes the CalculateDeadline instance with the given occurrence and damage classifications.

        calculate():
            Calculates and returns the deadline for response based on the occurrence and damage classifications.
    """

    def __init__(
            self,
            ocurrence: OcurrenceClassification,
            damage: DamageClassification
    ) -> None:
        """
        Initializes the CalculateDeadline instance with the provided occurrence and damage classifications.

        Args:
            ocurrence (OcurrenceClassification): The occurrence classification object.
            damage (DamageClassification): The damage classification object.
        """
        self.ocurrence_classification = ocurrence
        self.damage_classification = damage

    def calculate(self):
        """
        Calculates the deadline for response based on the occurrence and damage classifications.

        The deadline is defined by adding a certain number of days according to the 
        classifications of the occurrence and the damage.

        Occurrence Classification:
            - "Improcedente": 1 day
            - "Não conformidade", "Circustância de Risco", "Quebra de contratualização", 
              "Desvio da Qualidade": 15 days
            - "Incidente sem dano": 10 days

        Damage Classification:
            - "Nenhum": 15 days
            - "Dano Leve": 7 days
            - "Dano Moderado": 5 days
            - "Dano Grave": 3 days
            - "Dano Óbito": 15 days

        Returns:
            int: The total number of days for the response deadline.
        """
        days_of_response = 0

        # Classificação da ocorrência
        if self.ocurrence_classification.classification == "Improcedente":
            days_of_response += 1
        elif self.ocurrence_classification.classification in [
            "Não conformidade", "Circustância de Risco", 
            "Quebra de contratualização", "Desvio da Qualidade"
        ]:
            days_of_response += 15
        elif self.ocurrence_classification.classification == "Incidente sem dano":
            days_of_response += 10

        # Classificação do dano
        if self.damage_classification.classification == "Nenhum":
            days_of_response += 15
        elif self.damage_classification.classification == "Dano Leve":
            days_of_response += 7
        elif self.damage_classification.classification == "Dano Moderado":
            days_of_response += 5
        elif self.damage_classification.classification == "Dano Grave":
            days_of_response += 3
        elif self.damage_classification.classification == "Dano Óbito":
            days_of_response += 15

        return days_of_response
