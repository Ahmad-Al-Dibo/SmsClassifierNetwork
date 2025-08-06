# 📱 LSTM-netwerk voor SMS-classificatie (Ham vs. Spam)

## 🧾 Beschrijving van het Model

Dit LSTM-netwerk is ontworpen voor de classificatie van sms-berichten in twee categorieën: **ham** (normale berichten) en **spam** (ongewenste berichten). Het model maakt gebruik van een vooraf getrainde woordembedding om tekstuele informatie te representeren als vectoren, en verwerkt deze sequentiële gegevens met een LSTM-laag om contextuele relaties in de tekst vast te leggen.

### 🔧 Architectuur

1. **Embedding-laag**  
   - Initieel geladen met een vooraf getrainde embeddingmatrix (bijv. GloVe of Word2Vec).  
   - Niet-trainbaar, zodat de oorspronkelijke semantiek behouden blijft.  
   - Zet elk woord in een vaste vectorrepresentatie om.

2. **LSTM-laag**  
   - Verwerkt de volgorde van woorden in een sms-bericht en leert contextuele patronen.  
   - `recurrent_dropout` wordt toegepast voor regularisatie en overfittingpreventie.

3. **Dropout-laag**  
   - Random uitschakeling van 30% van de neuronen tijdens training om overfitting verder te reduceren.

4. **Dense-uitvoerlaag**  
   - Bestaat uit twee neuronen met een softmax-activatiefunctie, wat resulteert in waarschijnlijkheden voor de klassen **ham** en **spam**.

5. **Compilatie**  
   - **Optimizer**: RMSprop  
   - **Verliesfunctie**: `categorical_crossentropy`  
   - **Evaluatiemetriek**: `accuracy`

### 🎯 Doel van het Model

Het model leert kenmerken van spamberichten herkennen op basis van de tekstinhoud van sms’jes. Dankzij de LSTM-architectuur kan het niet alleen woorden herkennen, maar ook patronen in de volgorde waarin ze verschijnen — wat essentieel is bij natuurlijke taalverwerking.

<img width="576" height="455" alt="output2" src="https://github.com/user-attachments/assets/65b9fb59-f282-445c-8f1d-96a646c813ea" />


<img width="576" height="455" alt="output" src="https://github.com/user-attachments/assets/8199994b-a697-47f0-a9a2-167504395c38" />


<img width="710" height="460" alt="image" src="https://github.com/user-attachments/assets/2c830b1a-0f5d-4853-8aa5-d96b94e71ce2" />


# Auther: @Ahmad Mahmoud Al-Dibo
# Date: August 7 - 2025
