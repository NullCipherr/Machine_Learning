# O Teorema de Bayes é um principio da teoria da probabilidade, possuindo diversas aplicações. 
# O funcionamento do teorema é o seguinte, ele nos permite calcular a probabilidade de um evento com base em informações anteriores, ou seja, ele apresenta uma atualização nas probabilidades á medida que novas evidências são apresentadas.
#
# Sua fórmula matemática é dada por: P(A|B) = P(B|A).P(A) / P(B)
#
# onde,
# P(A∣B) é a probabilidade de A dado que B ocorreu (probabilidade posterior).
# P(B∣A)P(B∣A) é a probabilidade de B dado que A ocorreu (probabilidade verossímil).
# P(A)P(A) é a probabilidade de A ocorrer (probabilidade a priori).
# P(B)P(B) é a probabilidade de B ocorrer (probabilidade marginal).
# 
# Aplicações Práticas
# - Aprendizado de máquina e Inteligência artificial.
# - Filtragem de Spam.
# - Detecção de Fraudes.
# - Diagnósticos Médicos Computacional.
# - Visão Computacional.

# Exemplo Prático
# Imagine que temos um sistema de detecção de e-mails spam. Queremos calcular a probabilidade de um e-mail ser spam se ele contém a palavra "promoção". As probabilidades conhecidas são:
#
# - P(spam)= 0.2P(spam) = 0.2 (20% dos e-mails são spam).
# - P(não spam)= 0.8P(não spam) = 0.8 (80% dos e-mails não são spam).
# - P(promoção∣spam) = 0.6P(promoção∣spam) = 0.6 (60% dos e-mails de spam contêm a palavra "promoção").
# - P(promoção∣não spam) = 0.1P(promoção∣não spam) = 0.1 (10% dos e-mails não spam contêm a palavra "promoção").

# Utilizando o Teorema de Bayes, podemos calcular a probabilidade de um email ser spam se ele contém a palavra "promoção".

# P(spam|promoção) = (P(promoção|spam) . P(spam)) / P(promoção)
#
# P(promoção) = P(promoção|spam) . P(spam) + P(promoção|não spam) . P(não spam)
#
# P(promoção) = 0.6 x 0.2 + 0.1 x 0.8 = 0.12 + 0.08 = 0.20
#
# Aplicando o teorema de Bayes : 
# 
# P(promoção|spam) = (0.6 x 0.2) / 0.2 = 0.12 / 0.2 = 0.6
# 
# Portanto, a chance de um email ser um spam contendo a palavra "promoção" é de 60%.

def bayes_theorem(prior_A, prob_B_given_A, prob_B):
    """
    Calcula a probabilidade posterior P(A|B) usando o Teorema de Bayes.

    Args:
    prior_A (float): A probabilidade a priori de A, P(A).
    prob_B_given_A (float): A probabilidade de B dado A, P(B|A).
    prob_B (float): A probabilidade marginal de B, P(B).

    Returns:
    float: A probabilidade posterior P(A|B).
    """
    posterior_A_given_B = (prob_B_given_A * prior_A) / prob_B
    return posterior_A_given_B

# Probabilidades conhecidas
prob_spam = 0.2  # P(spam)
prob_not_spam = 0.8  # P(not spam)
prob_promo_given_spam = 0.6  # P(promo|spam)
prob_promo_given_not_spam = 0.1  # P(promo|not spam)

# Calculando a probabilidade marginal de promoção P(promo)
prob_promo = prob_promo_given_spam * prob_spam + prob_promo_given_not_spam * prob_not_spam

# Usando o Teorema de Bayes para calcular P(spam|promo)
prob_spam_given_promo = bayes_theorem(prob_spam, prob_promo_given_spam, prob_promo)

print(f"A probabilidade de um e-mail ser spam, dado que contém a palavra 'promoção', é de {prob_spam_given_promo:.2f} ou {prob_spam_given_promo*100:.2f}%.")


# Exercicio Prático 2
#
# Probabilidades conhecidas
prob_disease = 0.01  # P(D), a probabilidade a priori de ter a doença
prob_no_disease = 0.99  # P(¬D), a probabilidade a priori de não ter a doença
prob_test_positive_given_disease = 0.9  # P(T^+|D), a probabilidade de testar positivo se tem a doença
prob_test_positive_given_no_disease = 0.05  # P(T^+|¬D), a probabilidade de testar positivo se não tem a doença

# Calculando a probabilidade marginal de testar positivo P(T^+)
prob_test_positive = (prob_test_positive_given_disease * prob_disease) + \
                     (prob_test_positive_given_no_disease * prob_no_disease)

# Usando o Teorema de Bayes para calcular P(D|T^+)
prob_disease_given_test_positive = bayes_theorem(prob_disease, prob_test_positive_given_disease, prob_test_positive)

print(f"A probabilidade de ter a doença, dado que testou positivo, é de {prob_disease_given_test_positive:.2f} ou {prob_disease_given_test_positive*100:.2f}%.")
