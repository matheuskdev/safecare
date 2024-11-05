"""Service for calculate deadline in model response_ocurrence_models"""
from classifications.models import (
    OcurrenceClassification, DamageClassification
)


class CalculateDeadline:
    """Calculate Deadline"""
    def __init__(
            self,
            ocurrence: OcurrenceClassification,
            damage: DamageClassification
    ) -> None:
        self.ocurrence_classification = ocurrence
        self.damage_classification = damage

    def calculate(self,):
        """
        Calcula o prazo de retorno com base nas classificações de ocorrência
        e dano.
        O prazo é definido somando-se um número de dias com base nas
        classificações.
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
