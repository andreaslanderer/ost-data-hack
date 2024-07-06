# ost-data-hack

## Vorgehen

- Daten Visualisieren
    - Erkenntnisse:
        - Anzahl Datenpunkte 20758
        - Frauen scheinen tendenziell eher die höchsten Gewichte abzudecken, Männer in der Körperhöhe
        ![alt text](images/scatter_male_female.png)
        - Verteilung über die Obesity Klassen über alle Daten:
        ![alt text](images/histplot.png)
        - Es scheint falsch klassifizierte Daten zu geben:
        ![alt text](images/scatter_obesity.png)

- 1. Ansatz - erster Schnappschuss "wo stehen wir" / Funktioniert ein Modell
  - Split Train in Train und Validationset

  - Einfacher Decision tree ohne Hyperparameter
    <br>Accuracy ~83%
    ![alt text](images/1_approach_decision_tree.png)
  - Confusion Matrix
    ![alt text](images/1_approach_confusion_matrix.png)

  
- Aggregierte Spalte "BMI" einführen
  - histplot bmi/category
    ![alt text](images/bmi_category_histplot.png)




        