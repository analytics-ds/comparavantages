# -*- coding: utf-8 -*-
ARTICLE = dict(
 cat="cartes-cadeaux", slug="cheques-cadeaux-noel",
 title="Quel montant de chèques cadeaux de Noël offrir sans charges en 2026 ?",
 desc="Combien offrir en chèques cadeaux de Noël sans cotisations en 2026 ? 200 euros par salarié, autant par enfant jusqu'à 16 ans. Règles URSSAF, calendrier et budget.",
 kicker="Budget", h1="Quel montant de chèques cadeaux de Noël offrir sans charges ?",
 lead="Le plafond URSSAF, la règle des enfants, le calendrier de commande et le budget pour 20, 100 et 500 salariés. Tout ce qu'un dirigeant ou un élu de CSE doit savoir avant de commander les cadeaux de fin d'année.",
 img="art-6.jpg", img_alt="Cadeaux de Noël emballés sous un sapin dans un bureau",
 date="2026-10-03", date_fr="3 octobre 2026", reading="8", nb="11", nb_unit="situations URSSAF",
 brief_answer="Quel montant de chèques cadeaux de Noël offrir sans charges en 2026 ? Jusqu'à <b>200 euros par salarié</b>, soit 5 % du plafond mensuel de la Sécurité sociale de 4 005 euros, et le même plafond <b>pour chaque enfant jusqu'à 16 ans</b>. Le montant se cumule avec les autres événements de l'année, comme la naissance ou la rentrée scolaire. Pour une livraison avant les fêtes, commandez <b>avant la mi-novembre</b>.",
 brief=[
  "Le plafond mensuel de la Sécurité sociale est fixé à 4 005 euros en 2026, d'où un plafond cadeaux de 200 euros",
  "Le plafond s'apprécie par événement, Noël salarié et Noël enfant en étant deux distincts",
  "Au-delà du plafond, la totalité du montant devient soumise à cotisations",
  "L'attribution ne doit pas être discriminatoire, mais peut être modulée selon des critères objectifs",
 ],
 table=dict(
  head=["Bénéficiaire","Note /10 de clarté","Plafond exonéré","Condition","Cumulable","À retenir"],
  rows=[
   ["Salarié pour Noël","9,5","200 €","Être salarié à la date de remise","Oui","Un plafond par salarié",1],
   ["Enfant de salarié","8,8","200 €","Jusqu'à 16 ans dans l'année","Oui","Un plafond par enfant",0],
   ["Salarié pour la naissance","9,0","200 €","Naissance dans l'année","Oui","Événement distinct",0],
   ["Salarié pour la rentrée","8,5","200 €","Enfant scolarisé jusqu'à 26 ans","Oui","Lien avec la scolarité",0],
   ["Salarié pour un mariage ou un Pacs","9,0","200 €","Événement dans l'année","Oui","Lien avec l'événement",0],
   ["Salarié pour la retraite","9,0","200 €","Départ dans l'année","Oui","Lien avec le départ",0],
  ],
  note="Plafond calculé à 5 % du plafond mensuel de la Sécurité sociale 2026 (4 005 euros), arrondi. Relevé de démonstration des règles URSSAF en octobre 2026."),
 podium=[
  ("repere","Par salarié","200 €","pour Noël, sans cotisations","1"),
  ("repere","Par enfant","200 €","jusqu'à 16 ans","2"),
  ("repere","Date limite conseillée","mi-novembre","pour une livraison avant les fêtes","3"),
 ],
 sections=[
  dict(h2="Le plafond de 200 euros, comment il se calcule", id="plafond", body=[
   ("p","200 euros. C'est le montant que la plupart des entreprises retiennent pour Noël, et ce n'est pas un hasard. L'URSSAF tolère l'exonération des cadeaux et bons d'achat lorsque leur montant ne dépasse pas 5 % du plafond mensuel de la Sécurité sociale. Ce plafond est de 4 005 euros en 2026, soit 200,25 euros, ramenés à 200 euros dans la pratique."),
   ("p","Le seuil s'apprécie par salarié, par événement et par année civile. Noël pour le salarié et Noël pour chacun de ses enfants sont des événements distincts."),
  ]),
  dict(h2="Les montants par bénéficiaire", id="tableau", body=[
   ("p","Le tableau reprend les principaux événements reconnus par l'URSSAF. Chaque ligne ouvre son propre plafond."),
   ("table",None),
   ("img",dict(src="in-cheques-cadeaux-noel-1.jpg",alt="Enveloppe de vœux et cadeau posés sur un bureau",cap="Le chèque cadeau de Noël reste souvent remis en main propre, dans une carte de vœux.")),
   ("p","Une famille de deux enfants peut donc recevoir 600 euros de cadeaux de Noël exonérés, 200 pour le salarié et 200 par enfant. Si les deux parents travaillent dans la même entreprise, chaque enfant n'ouvre droit qu'à un seul plafond."),
  ]),
  dict(h2="Le budget pour 20, 100 et 500 salariés", id="budget", body=[
   ("p","Nous avons retenu 200 euros par salarié et 0,7 enfant de moins de 16 ans par salarié, moyenne courante dans les entreprises du secteur privé."),
   ("table2",dict(
     head=["Effectif","Cadeaux salariés","Cadeaux enfants","Budget total"],
     rows=[["20 salariés","4 000 €","2 800 €","6 800 €"],["100 salariés","20 000 €","14 000 €","34 000 €"],["500 salariés","100 000 €","70 000 €","170 000 €"]],
     note="Relevé de démonstration, hypothèse de 0,7 enfant éligible par salarié, hors frais de l'émetteur.")),
   ("img",dict(src="in-cheques-cadeaux-noel-2.jpg",alt="Équipe réunie pour un pot de fin d'année au bureau",cap="Le cadeau de Noël s'accompagne souvent d'un moment collectif en fin d'année.")),
   ("quote","Rien n'oblige à aller jusqu'à 200 euros. Mais au-delà, ne serait-ce que d'un euro, c'est toute la somme qui est soumise à cotisations."),
  ]),
  dict(h2="Qui commande, l'employeur ou le CSE", id="qui", body=[
   ("p","Dans une entreprise d'au moins 50 salariés, ce sont en général les élus du CSE qui organisent les cadeaux de Noël, sur le budget des activités sociales et culturelles. En dessous, c'est l'employeur, ou le CSE s'il dispose d'un budget."),
   ("ul",[
    "Le CSE ne peut pas exclure un salarié pour un motif discriminatoire, mais peut moduler le montant selon des critères objectifs comme la présence dans l'effectif à une date donnée",
    "L'employeur peut offrir des cadeaux en plus de ceux du CSE, mais le plafond de 200 euros se partage entre les deux",
    "Les salariés en CDD, à temps partiel et en alternance doivent être traités comme les autres",
    "Le cadeau doit être utilisable dans des enseignes en rapport avec Noël, jouets, culture, mode, loisirs",
   ]),
  ]),
  dict(h2="Le calendrier pour ne pas rater Noël", id="calendrier", body=[
   ("h3","En octobre"),
   ("p","Arrêter le montant, la liste des bénéficiaires et le support. Demander deux ou trois devis."),
   ("h3","Avant la mi-novembre"),
   ("p","Passer commande. Les chèques et cartes physiques demandent 5 à 10 jours de délai, davantage en décembre quand tous les CSE commandent en même temps."),
   ("h3","Début décembre"),
   ("p","Distribuer, ou programmer l'envoi des e-cartes, qui arrivent en quelques minutes."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "En 2026, vous pouvez offrir jusqu'à 200 euros de chèques ou cartes cadeaux de Noël par salarié, et autant par enfant de moins de 16 ans, sans aucune cotisation. Au-delà, tout le montant est soumis à cotisations.",
  "Si vos équipes sont connectées, l'e-carte évite les délais de livraison. Si vous tenez à remettre le cadeau en main propre, commandez les chèques ou les cartes avant la mi-novembre.",
 ]),
 faq=[
  ("Quel est le montant maximum des chèques cadeaux de Noël en 2026 ?","Environ 200 euros par salarié, soit 5 % du plafond mensuel de la Sécurité sociale de 4 005 euros. Chaque enfant de moins de 16 ans ouvre droit au même plafond."),
  ("Que se passe-t-il si on dépasse 200 euros ?","La totalité du montant offert pour l'événement est soumise à cotisations sociales, et non seulement la part qui dépasse le plafond."),
  ("Les enfants des salariés ont-ils droit à un chèque cadeau de Noël ?","Oui, jusqu'à 16 ans révolus dans l'année civile, avec leur propre plafond d'environ 200 euros par enfant."),
  ("Un salarié en CDD peut-il recevoir un chèque cadeau de Noël ?","Oui, il doit être traité comme les salariés en CDI. Une condition d'ancienneté objective et identique pour tous reste possible."),
  ("Quand commander les chèques cadeaux de Noël ?","Idéalement avant la mi-novembre pour les chèques et cartes physiques. Les e-cartes peuvent être commandées jusqu'à quelques jours avant la distribution."),
 ],
)
