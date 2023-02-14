# Img Class de Papas

### ES
Un Modelo de Deep Learning para clasificar tipos de enfermedades de las papas

El código usa modelos de Deep Learning para poder clasificar enfermedades de las papas 

Los primeros pasos para cada modelo son la separación de data en train, test y validation. Se aplica un "resize" y reescala, al igual que el data augmentation (el data augmentation solo se aplica al train).

Primero se aplica un modelo de redes neuronales con maxpool, con activación relu y la última layer con Softmax, el fit se hace con optimizador Adam y una loss: SparseCategoricalCrossentropy. 

El segundo modelo es similar pero con un optimizador RMSprop y loss SparseCategoricalCrossentropy. 

El siguiente modelo aplica "Feature Extraction & Fine-Tuning" este modelo usa inceptionv3 creado por ingenieros de Google. Usa un optimizador Adam y loss SparseCategoricalCrossentropy. Primero se modela y entrena con solamente el Feature Extraction, y para mejorar, luego se aplica el Fine tuning.

### EN
A Deep Learning model to classify types of illnes on potatoes.

The code uses a Deep learning model to calssify some illnes on a potatoe leaf

The firsts steps for each model created are: 1 to separate the data in a train, test and val ds. Then we apply a "resize" and "rescale", then we augment the data (ONLY to the train ds)

First we apply a neural network model using amxpool and relu activation (which is the most common) and a last layer with SOFTMAX (to classify), the fit uses an Adam Optimizer and a Loss type: SparseCategoricalCrossentropy.

The second model is very similar but it uses an RMSprop optimizer and a loss SparseCategoricalCrossentropy.

The last model applies "Feature Extraction & Fine-Tuning" this model uses inceptionv3 (the google thing). This modl uses also adam and SparseCategoricalCrossentropy. First we modelate and train using Feature Extraction only, then to optimize it even more we apply Fine Tunning. Tho the results weren't the ones I was expecting.

### Despliegue en GCP

### ES
El otro codigo es una forma de desplegar el modelo en un bucket de Google Cloud. 
Mediante Postman puedes subir las imágenes de las hojas, para que el modelo te prediga que enfermedad tiene el tubérculo.

### EN
We deploy the model using GCP that's that tbh.


