# Projet ML – Prédiction du Churn Client

## Objectif
Le projet a pour objectif de prédire quels clients sont susceptibles de **quitter le service** (churn).  
Il inclut une **analyse exploratoire complète (EDA)**, la visualisation des facteurs influençant le churn, et la préparation d'un modèle de prédiction.

## Dataset
- Source : Telco Churn (fichier Excel `.xlsx`)
- Nombre de clients : 7043
- Variables (traduction en français) :

| Variable | Description |
|----------|------------|
| customerid | Identifiant unique du client |
| count | Nombre d'interactions (inutile pour le modèle) |
| country | Pays du client |
| state | État / région |
| city | Ville |
| zip_code | Code postal |
| lat_long | Coordonnées latitude/longitude |
| latitude | Latitude |
| longitude | Longitude |
| gender | Genre du client |
| senior_citizen | Senior (1 = oui, 0 = non) |
| partner | A un partenaire (oui/non) |
| dependents | A des personnes à charge (oui/non) |
| tenure_months | Ancienneté du client en mois |
| phone_service | Service téléphonique actif (oui/non) |
| multiple_lines | Plusieurs lignes téléphoniques (oui/non/aucun) |
| internet_service | Type d’internet (DSL, Fibre, Aucun) |
| online_security | Sécurité en ligne (oui/non) |
| online_backup | Sauvegarde en ligne (oui/non) |
| device_protection | Protection des appareils (oui/non) |
| tech_support | Support technique (oui/non) |
| streaming_tv | Streaming TV (oui/non) |
| streaming_movies | Streaming Films (oui/non) |
| contract | Type de contrat (Month-to-Month, One-Year, Two-Year) |
| paperless_billing | Facturation sans papier (oui/non) |
| payment_method | Méthode de paiement (Electronic Check, Bank Transfer, etc.) |
| monthly_charges | Montant facturé chaque mois |
| total_charges | Montant total payé par le client |
| churn_label | Churn : Oui/Non (objectif) |
| churn_value | Valeur numérique du churn (0/1) |
| churn_score | Score interne / prédiction initiale |
| cltv | Customer Lifetime Value (valeur client sur la durée) |
| churn_reason | Raison du churn (texte, descriptif uniquement) |

## Analyse exploratoire (EDA)
1. **Contract Type vs Churn Label**  
   Les clients en Month-to-Month présentent le taux de churn le plus élevé, tandis que ceux en contrat One-Year ou Two-Year sont plus fidèles.
2. **Tenure Group vs Churn Label**  
   Les clients avec 0 à 12 mois d’ancienneté churnent le plus, les clients plus anciens sont protégés.
3. **Tech Support vs Churn Label**  
   Les clients sans support technique churnent plus souvent. Le support technique est un facteur protecteur.
4. **Online Security vs Churn Label**  
   Les clients sans sécurité en ligne churnent plus que ceux qui ont ce service.
5. **Online Backup vs Churn Label**  
   Les clients sans sauvegarde en ligne ont un taux de churn plus élevé.
6. **Device Protection vs Churn Label**  
   Les clients sans protection des appareils churnent davantage.
7. **Streaming TV vs Churn Label**  
   L’effet sur le churn est faible, mais les clients sans streaming TV churnent légèrement plus.
8. **Streaming Movies vs Churn Label**  
   Même constat que pour le streaming TV.
9. **Monthly Charges vs Churn Label**  
   Les clients avec des charges mensuelles plus élevées churnent légèrement plus, avec quelques outliers.
10. **Total Charges vs Churn Label**  
    Les clients avec des charges totales faibles churnent le plus, les clients avec de grosses charges sont plus fidèles.
11. **Paperless Billing vs Churn Label**  
    Les clients en facturation sans papier churnent plus que ceux en facturation papier.
12. **Payment Method vs Churn Label**  
    Les clients utilisant Electronic Check churnent le plus, tandis que ceux utilisant Bank Transfer ou Credit Card automatique sont plus stables.

## Métriques prévues pour le modèle
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Courbe ROC / AUC

