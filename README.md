#Universidad de los Andes
#Maestria en Ingenieria de la Informacion
# Taller 3 Ciencia de Datos Aplicada


LINK VIDEO DESPLIEGUE API: https://youtu.be/Ony9JVhb8Ho

**SHAP VALUES** Favor referirse al cuaderno "ShapValues para ver el ejercicio"

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/e9c24079-31e9-4a82-a6c9-885fb6f4fa48)

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/47659a84-b557-417c-b84c-152237349688)

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/ee8cbcd2-7a2c-4d00-b08f-59bf3d265d54)

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/eabc9595-407e-424d-aa61-626f98344bde)

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/64cf42a8-db8c-44b2-8448-30258767dc3a)


## Primera Pregunta: Desarrollo del Modelo
¿Se evidencian problemas de overfitting o underfitting? ¿Cómo solucionarlos y a la vez continuar mejorando la capacidad predictiva del modelo?

R. En general, el modelo de clasificación tiene un rendimiento razonable. El modelo tiene una accuracy de 0,75, lo que significa que clasificó correctamente a 75 de cada 100 observaciones.

El modelo también tiene un f1-score de 0,64 para la clase "Sí", lo que significa que tuvo un rendimiento de 0,64 en términos de precisión y sensibilidad para los clientes que abandonaron la empresa.

Sin embargo, hay algunas áreas en las que el modelo podría mejorar. Por ejemplo, el modelo tiene una sensibilidad de solo 0,82 para la clase "Sí", lo que significa que no siempre detecta correctamente a los clientes que abandonaron la empresa.

El modelo también tiene una precisión de solo 0,52 para la clase "Sí", lo que significa que a veces clasifica incorrectamente a los clientes que no abandonaron la empresa como "Sí".

## Segunda Pregunta: A/B Testing

**Pregunta 1: Distribución de probabilidad y significancia estadística**

 Name: probabilidad, dtype: float64,
 ShapiroResult(statistic=0.719162106513977, pvalue=6.392974709340253e-28)

 La distribución de probabilidad se hizo a partir de la prueba Shapiro junto a un análisis descriptivo:
 
Análisis Descriptivo:

Modelo 'best':
Count: 492 observaciones.
Mean: La media de probabilidad es 0.274, lo que sugiere una probabilidad promedio relativamente baja.
Std: La desviación estándar es 0.204, indicando una variabilidad moderada en los datos.
Min-Max: Los valores varían entre 0.071 y 0.525, lo que muestra un rango amplio de probabilidades.

Modelo 'baseline':
Count: 507 observaciones.
Mean: La media es 0.432, notablemente más alta que en el modelo 'best'.
Std: Una desviación estándar de 0.279, indicando una variabilidad aún mayor.
Min-Max: El rango es más amplio (0.036 a 0.809), sugiriendo diferencias significativas entre las probabilidades más bajas y más altas.

Prueba de Normalidad (Shapiro-Wilk):
Modelo 'best': El estadístico de Shapiro-Wilk es 0.719 con un p-valor extremadamente bajo (prácticamente 0). Esto sugiere que las probabilidades del modelo 'best' no siguen una distribución normal.
Modelo 'baseline': El resultado es NaN. No se puede concluir nada sobre la normalidad de las probabilidades del modelo 'baseline'.

Prueba T para Comparar Medias:
Los resultados de la prueba T son NaN, lo que indica que no se pudo realizar la prueba. Hay diferencias notables en las medias y variabilidades de las probabilidades entre los modelos 'best' y 'baseline'. El modelo 'baseline' tiene en promedio probabilidades más altas y más variabilidad. Se sugiere que se deberían considerar pruebas no paramétricas para comparar las medias, como la prueba de Mann-Whitney U.

**Pregunta 2: Análisis de Porcentaje de Churn**
para Cada Modelo Se calculó el porcentaje medio y la desviación estándar de las predicciones de churn para cada modelo durante todo el período.

Modelo 'Baseline':

Porcentaje medio de churn: ≈ 49.37 % ≈49.37% Desviación estándar: ≈ 50.05 % ≈50.05% Modelo 'Best':

Porcentaje medio de churn: ≈ 31.49 % ≈31.49% Desviación estándar: ≈ 46.49 % ≈46.49% 
Estos resultados muestran que el modelo 'Baseline' tiene un porcentaje medio de churn más alto que el modelo 'Best', pero también una mayor variabilidad en sus predicciones.

**Pregunta 3: Porcentaje de Éxito del Modelo en la Predicción Diaria de Churn Efectivo**
Modelo 'Baseline': La precisión acumulada es aproximadamente 70.59 % 70.59%.
Modelo 'Best': La precisión acumulada es aproximadamente 76.53 % 76.53%.
Estos resultados indican que, después de ajustar la comparación de las predicciones con los valores reales de churn, el modelo 'Best' es más preciso que el modelo 'Baseline' en el conjunto de datos analizado.

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/f463c444-eea1-4696-8430-2471669a6023)

![image](https://github.com/asertas14/taller3_ciencia_aplicada/assets/141885465/80c7b387-1440-4c5b-97aa-ff04afd00f7e)


