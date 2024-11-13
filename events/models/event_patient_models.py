"""Module models for events."""

from django.db import models

from events.models.gender_models import Gender
from events.models.race_models import Race
from utils import mixins


class EventPatient(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing an Event Patient.

    This model stores information about a patient involved in an event,
    including their name, attendance number, record number, birth date,
    internment date, gender, and race. It extends functionality from
    `TimestampModelMixin` and `SoftDeleteModelMixin` to handle timestamps
    and soft deletion.

    Inherits from:
        mixins.TimestampModelMixin: Adds `created_at` and `updated_at` fields.
        mixins.SoftDeleteModelMixin: Adds soft delete functionality.

    Attributes:
        patient_name (CharField): The name of the patient.
        attendance (IntegerField): The attendance number for the event.
        record (IntegerField): The patient's record number.
        birth_date (DateField): The birth date of the patient.
        internment_date (DateField): The date the patient was interned.
        genere (ForeignKey): A reference to the `Gender` model, nullable.
        race (ForeignKey): A reference to the `Race` model, nullable.

    Meta:
        ordering (list): Default ordering by `created_at`.
        verbose_name (str): Human-readable name for the model in singular form.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database indexes for optimizing queries on specified
        fields.

    Methods:
        __str__(): Returns a string representation of the patient,
                   including the name and attendance number.
    """

    patient_name = models.CharField(
        max_length=225, help_text="Nome do paciente"
    )
    attendance = models.IntegerField(
        help_text="Número do Atendimento",
    )
    record = models.IntegerField(
        help_text="Número do prontuário.",
    )
    birth_date = models.DateField(help_text="Data de nascimento.")
    internment_date = models.DateField(help_text="Data de internação.")
    genere = models.ForeignKey(
        Gender,
        help_text="Gênero",
        on_delete=models.PROTECT,
        related_name="event_genere",
        null=True,
        blank=True,
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.PROTECT,
        related_name="event_race",
        null=True,
        blank=True,
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for Event Patient model."""

        ordering = ["created_at"]
        verbose_name = "Paciente Ocorrência"
        verbose_name_plural = "Pacientes Ocorrências"
        indexes = [
            models.Index(fields=["patient_name"]),
            models.Index(fields=["attendance"]),
            models.Index(fields=["record"]),
            models.Index(fields=["birth_date"]),
            models.Index(fields=["internment_date"]),
            models.Index(fields=["genere"]),
            models.Index(fields=["race"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the event patient.

        The representation includes the patient's name and their
        attendance number for better identification.

        Returns:
            str: A formatted string with the patient's name and attendance number.
        """
        return f"Paciente: {self.patient_name}, Atendimento: {self.attendance}"
