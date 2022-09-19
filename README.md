# Img Class de Papas
Un Modelo de Deep Learning para clasificar tipos de enfermedades de las papas

El código usa modelos de Deep Learning para poder clasificar enfermedades de las papas 

Los primeros pasos para cada modelo son la separación de data en train, test y validation. Se aplica un "resize" y reescala, al igual que el data augmentation (el data augmentation solo se aplica al train).

Primero se aplica un modelo de redes neuronales con maxpool, con activación relu y la última layer con Softmax, el fit se hace con optimizador Adam y una loss: SparseCategoricalCrossentropy. 

El segundo modelo es similar pero con un optimizador RMSprop y loss SparseCategoricalCrossentropy. 

El siguiente modelo aplica "Feature Extraction & Fine-Tuning" este modelo usa inceptionv3 creado por ingenieros de Google. Usa un optimizador Adam y loss SparseCategoricalCrossentropy. Primero se modela y entrena con solamente el Feature Extraction, y para mejorar, luego se aplica el Fine tuning.
