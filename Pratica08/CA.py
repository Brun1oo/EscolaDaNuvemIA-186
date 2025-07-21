from sklearn.datasets import load_breast_cancer #Dataset do CA de mama
from sklearn.ensemble import RandomForestClassifier #Algoritmo do Random Forest

#Metricas para avaliação do modelo
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

#Função para dividir o dataset
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X_train, X_test, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42)

#Iniciando o modelo com os parametros padrao
model = RandomForestClassifier()

#Treinar o modelo com os dados de treinamento
model.fit(X_train, y_test)

#Fazendo as previsoes com os dados de teste
y_prep = model.predict(X_test) #Previsoes de clase 0 ou 1
y_prep_proba = model.predict_proba(X_test)[:,1] #Probabilidade de ser de classe 1

precesion = precision_score(y_test, y_prep) #Precisao: TP / (TP + FP)
recall = recall_score(y_test, y_prep) #Sensibilidade: TP / (TP + FN)
f1 = f1_score(y_test, y_prep) #F1: (precision * recall)/(precision * recall)
auc = roc_auc_score(y_test, y_prep_proba) #Area sob curva ROC

print(f"""
Precisão: {precesion}
Recall: {recall}
F1-Score: {f1}
AUC-ROC: {auc}
""")

#Precisao alta = baixo numero de falsos positivos
#Recall alto = baixo numero de falsos negativos
#F1 alto = Equilibrio entre as metricas precision e recall
#AUC-ROC alto = Boa discriminacao entre as classes do modelo