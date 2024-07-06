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

## Daten bereinigen
- BMI in Dataset aggregiert (Gewicht / Höhe^2)
- id Column droppen
- Findings:
  - Falsch gelabelte Daten:
      | is | predicted | BMI|
      |:------------- |:---------------:| -------------:|
      | Obesity_Type_I    | Insufficient_Weight  | 17.10 |
      | Obesity_Type_II   | Normal_Weight        | 24.39 |
      | Obesity_Type_III  | Overweight_Level_I   | 25.91 |

## Feature Selection
- Standardisieren -> Modell Accuracy hat sich verschlechtert

## Model
  - Decision Tree: Gridsearch max_depth=10, main_samples_leave=1, split=2 Score 86.5
  - RandomForrest( Est. 200 ) Score 90.2

## Parameter Documentation
- Hyperparameter
- Seed
- Stats