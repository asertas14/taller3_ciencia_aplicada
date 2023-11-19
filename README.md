#Universidad de los Andes
#Maestria en Ingenieria de la Informacion
# Taller 3 Ciencia de Datos Aplicada


## Primera Pregunta: Desarrollo del Modelo
¿Se evidencian problemas de overfitting o underfitting? ¿Cómo solucionarlos y a la vez continuar mejorando la capacidad predictiva del modelo?

R. En general, el modelo de clasificación tiene un rendimiento razonable. El modelo tiene una accuracy de 0,75, lo que significa que clasificó correctamente a 75 de cada 100 observaciones.

El modelo también tiene un f1-score de 0,64 para la clase "Sí", lo que significa que tuvo un rendimiento de 0,64 en términos de precisión y sensibilidad para los clientes que abandonaron la empresa.

Sin embargo, hay algunas áreas en las que el modelo podría mejorar. Por ejemplo, el modelo tiene una sensibilidad de solo 0,82 para la clase "Sí", lo que significa que no siempre detecta correctamente a los clientes que abandonaron la empresa.

El modelo también tiene una precisión de solo 0,52 para la clase "Sí", lo que significa que a veces clasifica incorrectamente a los clientes que no abandonaron la empresa como "Sí".

## Segunda Pregunta: A/B Testing

1) Para toda la ventana de tiempo, ¿cómo se distribuyen las probabilidades asignadas por el modelo entre los dos grupos? Asumiendo que las distribuciones tienen un comportamiento normal, ¿dichas diferencias entre las probabilidades de ambas variantes del modelo son significativas?


R.

2) ¿Cuál fue el incremento o decremento porcentual diario de predicción de casos de churn que tuvo el mejor modelo (punto 3) respecto al baseline (punto 2)?

3) En una base diaria, ¿cuál fue el porcentaje de éxito del modelo prediciendo casos de efectivos de churn?
