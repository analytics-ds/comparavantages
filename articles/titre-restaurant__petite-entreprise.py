# -*- coding: utf-8 -*-
ARTICLE = dict(
 cat="titre-restaurant", slug="petite-entreprise",
 title="Titres-restaurant dans une TPE ou PME, comment les mettre en place ?",
 desc="Moins de 50 salariés et pas de cantine ? Les titres-restaurant se mettent en place en 2 à 3 semaines. Exonération à 7,32 euros, 6 étapes, coûts et pièges à éviter.",
 kicker="Guide", h1="Comment mettre en place des titres-restaurant dans une petite entreprise ?",
 lead="Aucune obligation légale, aucun seuil d'effectif, un dispositif qui coûte moins cher qu'une augmentation. Voici les six étapes pour lancer des titres-restaurant dans une TPE ou une PME de moins de 50 salariés, et les erreurs qui coûtent un redressement URSSAF.",
 img="art-3.jpg", img_alt="Petite équipe qui déjeune dans une cuisine de bureau",
 date="2026-10-06", date_fr="6 octobre 2026", reading="9", nb="6", nb_unit="étapes",
 brief_answer="Une entreprise de moins de 50 salariés peut mettre en place des titres-restaurant <b>dès le premier salarié</b>, sans accord collectif ni CSE. Il suffit de choisir un émetteur agréé, de fixer une valeur faciale et une prise en charge <b>entre 50 et 60 %</b>, puis d'en informer les salariés par écrit. La part patronale est exonérée jusqu'à <b>7,32 euros</b> par titre en 2026, et le premier chargement arrive en <b>2 à 3 semaines</b>.",
 brief=[
  "Le titre-restaurant n'est jamais obligatoire, mais une entreprise sans local de restauration doit permettre aux salariés de se restaurer",
  "La valeur faciale optimale se situe entre 12,20 et 14,64 euros pour une exonération maximale",
  "Un salarié a droit à un titre par repas compris dans son horaire de travail journalier",
  "Les CDD, les temps partiels, les alternants et les stagiaires peuvent en bénéficier",
 ],
 table=dict(
  head=["Étape","Note /10 de difficulté","Durée","Qui s'en charge","Document","Point de vigilance"],
  rows=[
   ["Choisir un émetteur agréé","3","1 semaine","Dirigeant","Devis","Comparer les frais réels",1],
   ["Fixer valeur faciale et prise en charge","2","1 jour","Dirigeant","Note interne","Rester entre 50 et 60 %",0],
   ["Informer les salariés","2","1 jour","Dirigeant ou RH","Note de service","Préciser le nombre de titres par mois",0],
   ["Collecter les données salariés","4","2 à 5 jours","RH ou comptable","Fichier salariés","Adresse de livraison des cartes",0],
   ["Commander et charger","3","3 à 7 jours","RH","Bon de commande","Jours d'absence à déduire",0],
   ["Paramétrer la paie","5","1 jour","Comptable","Bulletin de paie","Ligne de retenue salariale",0],
  ],
  note="Durées observées sur des mises en place de TPE et PME en octobre 2026. Difficulté notée sur 10."),
 podium=[
  ("repere","Valeur faciale","12,20 à 14,64 €","pour une exonération maximale","1"),
  ("repere","Prise en charge","50 à 60 %","par l'employeur","2"),
  ("repere","Plafond journalier","25 €","de dépense par jour","3"),
 ],
 sections=[
  dict(h2="Une entreprise de moins de 50 salariés est-elle obligée ?", id="obligation", body=[
   ("p","Non. Le titre-restaurant est un avantage facultatif, quel que soit l'effectif. Le Code du travail impose seulement de permettre aux salariés de se restaurer dans de bonnes conditions. En dessous de 50 salariés, l'employeur doit prévoir un emplacement pour déjeuner si au moins 25 salariés le demandent. Au-delà, un local de restauration."),
   ("p","Dans les faits, une petite entreprise sans cantine a deux options. Verser une prime de panier soumise à cotisations, ou distribuer des titres-restaurant exonérés. La seconde coûte moins cher pour le même pouvoir d'achat."),
  ]),
  dict(h2="Les six étapes de la mise en place", id="etapes", body=[
   ("p","Aucune étape ne demande d'accord collectif ni de consultation d'un CSE lorsqu'il n'y en a pas. Une décision unilatérale de l'employeur, écrite, suffit."),
   ("table",None),
   ("img",dict(src="in-petite-entreprise-1.jpg",alt="Dirigeant de petite entreprise qui remplit un formulaire sur ordinateur portable",cap="La commande initiale demande surtout un fichier propre des salariés bénéficiaires.")),
   ("p","L'étape la plus longue est presque toujours la collecte des données. Nom, prénom, date de naissance et adresse de livraison de la carte pour chaque salarié. Un fichier préparé à l'avance divise le délai par deux."),
  ]),
  dict(h2="Qui y a droit dans l'entreprise", id="beneficiaires", body=[
   ("p","Tous les salariés dont la pause déjeuner tombe dans l'horaire de travail, sans distinction de contrat. La règle est un titre par repas compris dans l'horaire journalier."),
   ("ul",[
    "Les salariés en CDI et en CDD, à temps plein comme à temps partiel, dès lors qu'un repas tombe dans leur journée",
    "Les alternants et les stagiaires, qui peuvent aussi en bénéficier",
    "Les salariés en télétravail, dans les mêmes conditions qu'au bureau",
    "Le dirigeant, seulement s'il a le statut de salarié, par exemple un président de SAS rémunéré",
   ]),
   ("quote","Les jours d'absence, de congés ou de formation avec repas fourni ne donnent pas droit à un titre. C'est la première cause de redressement dans les petites structures."),
  ]),
  dict(h2="Combien cela coûte pour 10 salariés", id="budget", body=[
   ("p","Prenons une entreprise de 10 salariés, 20 jours travaillés par mois, un titre de 12,20 euros financé à 60 %."),
   ("table2",dict(
     head=["Poste","Par salarié et par mois","Pour 10 salariés par an"],
     rows=[["Part patronale (7,32 € × 20 jours)","146,40 €","17 568 €"],["Part salariale (4,88 € × 20 jours)","97,60 €","11 712 €"],["Frais de l'émetteur","2 € à 5 €","240 € à 600 €"],["Cotisations sur la part patronale","0 €","0 €"]],
     note="Relevé de démonstration, frais d'émetteur sur devis types d'octobre 2026.")),
   ("img",dict(src="in-petite-entreprise-2.jpg",alt="Calculatrice et carnet de comptes sur un bureau",cap="La part patronale est entièrement déductible du résultat imposable.")),
   ("p","La même somme versée en prime coûterait environ 40 % de plus à l'entreprise une fois les cotisations ajoutées, et le salarié en toucherait moins en net. Le titre-restaurant est déductible du résultat et n'entre pas dans le revenu imposable du salarié."),
  ]),
  dict(h2="Les erreurs à éviter", id="erreurs", body=[
   ("h3","Dépasser 60 % de prise en charge"),
   ("p","Au-delà de 60 %, l'exonération tombe sur la totalité de la part patronale, pas seulement sur l'excédent."),
   ("h3","Oublier de déduire les absences"),
   ("p","Un titre distribué pour un jour de congé est un avantage en nature soumis à cotisations. Le chargement mensuel doit suivre les absences."),
   ("h3","Choisir sur le seul prix"),
   ("p","Des frais bas mais un réseau maigre autour de vos locaux, et le dispositif perd sa valeur aux yeux des salariés. Demandez la liste des commerces affiliés dans votre quartier avant de signer."),
   ("h3","Négliger la fin de la dérogation alimentaire"),
   ("p","L'utilisation des titres pour des produits alimentaires non directement consommables, comme les pâtes ou la farine, est autorisée jusqu'au 31 décembre 2026. Une prolongation est en discussion au Parlement."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Pour une entreprise de moins de 50 salariés, le titre-restaurant est l'avantage le plus simple à lancer et le plus rentable. Une décision écrite, un émetteur agréé, une prise en charge entre 50 et 60 % et une valeur faciale autour de 12,20 euros suffisent.",
  "Si votre priorité est la simplicité, choisissez un émetteur qui prend en charge la collecte des données et le premier chargement. Si vos salariés sont souvent en déplacement, privilégiez une carte avec paiement mobile.",
 ]),
 faq=[
  ("Une entreprise de moins de 50 salariés doit-elle donner des titres-restaurant ?","Non, aucune entreprise n'y est obligée. Elle doit seulement permettre aux salariés de se restaurer, et prévoir un emplacement pour déjeuner si au moins 25 salariés le demandent."),
  ("Peut-on donner des titres-restaurant avec un seul salarié ?","Oui, dès le premier salarié. Le dispositif repose sur une décision de l'employeur, sans seuil d'effectif ni accord collectif."),
  ("Quelle valeur choisir pour un titre-restaurant en 2026 ?","Pour profiter de l'exonération maximale de 7,32 euros, la valeur faciale doit se situer entre 12,20 euros (prise en charge à 60 %) et 14,64 euros (prise en charge à 50 %)."),
  ("Un stagiaire a-t-il droit aux titres-restaurant ?","Oui, l'employeur peut en attribuer aux stagiaires, dans les mêmes conditions que les salariés, dès lors que leur repas est compris dans leur horaire de travail."),
  ("Combien de temps faut-il pour mettre en place les titres-restaurant ?","Comptez 2 à 3 semaines entre la signature avec l'émetteur et le premier chargement, dont une bonne partie consacrée à la collecte des données salariés."),
  ("Le dirigeant d'une TPE peut-il recevoir des titres-restaurant ?","Seulement s'il a le statut de salarié, comme un président de SAS rémunéré ou un gérant minoritaire de SARL. Un gérant majoritaire ou un travailleur indépendant ne peut pas en bénéficier par ce biais."),
 ],
)
