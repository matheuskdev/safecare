from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from responses.models.response_ocurrence_models import OcurrenceDescription


class Command(BaseCommand):
    help = "Populates the OcurrenceDescription table with predefined data"

    def handle(self, *args, **kwargs):
        data = [
            (0, "Não se Aplica", 1),
            (
                1,
                "Meta 1 - Identificação: Paciente - dispositivo - medicamento - nutrição - Prontuário",
                1,
            ),
            (2, "Meta 2 - Falha na comunicação entre os profissionais", 1),
            (3, "Meta 3 - Farmacovigilância - Erro de Medicação", 1),
            (
                4,
                "Meta 4 - Falha na cirurgia - erro - cancelamento - reoperação 48h - óbito 7 dias, Não Sinalização de lateralidade",
                1,
            ),
            (5, "Meta 5 - Falha na higienização das mãos", 1),
            (
                6,
                "Meta 6 - LPP - Lesão por pressão - ou por lesão por dispositivo médico",
                1,
            ),
            (7, "Falha na assistência", 1),
            (8, "Tecnovigilância - Queixa técnica", 1),
            (9, "Falha do transporte", 1),
            (10, "Atraso no atendimento", 1),
            (11, "Falha no uso de EPI", 1),
            (12, "Falha na Prescrição", 1),
            (13, "Queda do paciente - meta 6", 1),
            (14, "Procedimento inadequado (Ajuste de Rotina)", 1),
            (
                15,
                "Prontuário Incompleto - falta de: protocolo - evolução - transferência - termo - sem registro de volume infundido",
                1,
            ),
            (16, "Falha na dispensação", 1),
            (
                17,
                "Hemovigilância - Reação transfusional - Ficha incompleta",
                1,
            ),
            (18, "Perda de dispositivo - SNG", 1),
            (
                19,
                "Dieta com alterações de deterioração, Defeito no conector",
                1,
            ),
            (20, "Flebite"),
            (21, "Falha na dupla checagem do material", 1),
            (22, "Glosa pelo convênio", 1),
            (
                23,
                "Readmissões em até 48h após a alta na emergência/ Internação até 48h na UTI",
                1,
            ),
            (24, "Extravasamento de contraste", 1),
            (25, "Evasão", 1),
            (26, "Óbito inesperado", 1),
            (27, "Saneantes", 1),
            (28, "IRAS - Infecção relacionada à assistência à saúde", 1),
            (29, "Desnutrição", 1),
            (30, "Diarreia", 1),
            (31, "Ergonomia", 1),
            (32, "Alta indevida", 1),
            (33, "Comportamental", 1),
            (34, "Paciente sem acompanhante", 1),
            (35, "Produto para ser substituído", 1),
            (36, "Quebra de acordo entre as partes (não conformidade)", 1),
            (37, "Reintubação 24h", 1),
            (
                38,
                "Médico sem cadastro no hospital - médico sem cadastro no sistema Medview",
                1,
            ),
            (39, "Broncoaspiração", 1),
            (40, "PAV - Pneumonia associada à ventilação mecânica", 1),
            (41, "Perda de dispositivo - SNE", 1),
            (42, "Perda de dispositivo - TOT", 1),
            (43, "Perda de dispositivo - SVD", 1),
            (44, "Perda de dispositivo - AVP", 1),
            (45, "Perda de dispositivo - AVC", 1),
            (46, "Perda de dispositivo - PICC/PAI", 1),
            (47, "Perda de dispositivo - CTL", 1),
            (48, "Reoperação 48h", 1),
            (49, "Óbito 7 dias", 1),
            (50, "Reação alérgica ao fármaco", 1),
            (51, "Erro de infusão", 1),
            (52, "Cancelamento de cirurgia", 1),
            (53, "Paciente admitida no hospital com lesões por pressão", 1),
            (
                54,
                "Registro de volume infundido da dieta enteral incompleto",
                1,
            ),
            (55, "Protocolo de dor torácica", 1),
            (56, "Falha na Higienização", 1),
            (57, "Prescrição manual", 1),
            (58, "Aprazamento", 1),
            (59, "Perda de dispositivo - GTT", 1),
            (60, "Óbito Gatilho", 1),
            (
                61,
                "Protocolo de TEV - RISCO DE TEV E USO DA PROFILAXIA EM PACIENTES CLÍNICOS INTERNADOS",
                1,
            ),
            (62, "Protocolo de Sepse", 1),
            (
                63,
                "Tempo de administração de antibioticoprofilaxia cirúrgica",
                1,
            ),
            (64, "Falha no tratamento de DOR", 1),
            (65, "ITU", 1),
            (
                66,
                "Administração de dieta enteral inadequada (Vencida, volume menor/maior do que o prescrito)",
                1,
            ),
            (67, "Organizacional", 1),
            (68, "Cardápio", 1),
            (
                69,
                "Ausência ou falha de preenchimento do Termo para procedimento cirúrgico/Anestésico/hemocomponentes",
                1,
            ),
            (70, "Infecção FO pelo Dispositivo médico", 1),
            (71, "Farmacovilância - Queixa técnica", 1),
            (72, "Fratura após assistência", 1),
            (73, "Desvio de qualidade", 1),
            (74, "Circunstância de Risco", 1),
            (75, "Falha na Comunicação", 1),
            (76, "Atraso na entrega do medicamento prescrito", 1),
            (
                77,
                "Transporte e transferência não preenchido/Transporte seguro",
                1,
            ),
            (78, "Suspensão de Cirurgia", 1),
            (79, "Prontuário Eletrônico", 1),
            (80, "Atraso na entrega de dieta", 1),
            (81, "Problemas com Equipamento- Ar condicionado, termômetro", 1),
            (82, "Suporte de TI", 1),
            (83, "Retorno < 48h", 1),
            (84, "Jejum Prolongado", 1),
            (85, "Descarte inadequado de perfurocortantes", 1),
            (86, "Extravasamento/infiltração de medicação endovenosa", 1),
            (87, "Acidente de trabalho", 1),
            (88, "DO - Declaração de Óbito", 1),
            (89, "Material CME", 1),
        ]
        User = get_user_model()
        for id_evento, descricao, owner_id in data:
            OcurrenceDescription.objects.get_or_create(
                name=descricao, owner=User.objects.get(id=owner_id)
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated OcurrenceDescription table."
            )
        )
