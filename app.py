import streamlit as st
import time

# Configurazione della pagina
st.set_page_config(page_title="Scopri che tipo di collega sei", page_icon="🤝", layout="centered")

# Definizione delle domande e delle relative scelte
quiz_data = [
    {
        "question": "Un collega ti chiama disperato perché ha sbagliato strada e non trova lo studio del medico. Cosa fai?",
        "choices": [
            "🗺️ Lo aiuto subito con Google Maps, siamo una squadra!",
            "😏 Gli dico che è sfigato e che deve imparare a organizzarsi meglio",
            "🤷 Gli do indicazioni vaghe per vedere se riesce a uscirne da solo",
            "📵 Gli dico che sono occupatissimo e lo lascio nel panico"
        ]
    },
    {
        "question": "Durante il pranzo con i colleghi, uno si lamenta di un medico che non lo riceve mai. Come reagisci?",
        "choices": [
            "💡 Gli do qualche consiglio su come approcciarlo meglio",
            "😈 Gli dico che quel medico con me è sempre gentile, così lo faccio rosicare",
            "📱 Fingo di ascoltare mentre controllo il telefono",
            "🎭 Cambio discorso e parlo di me, perché i problemi degli altri non mi interessano"
        ]
    },
    {
        "question": "Un collega junior entra nel team e ti chiede consigli su come affrontare il lavoro. Cosa fai?",
        "choices": [
            "📖 Gli spiego tutto con calma, voglio che si integri bene nel gruppo",
            "🤐 Gli do informazioni vaghe, non sia mai che diventi più bravo di me",
            "🏢 Lo mando direttamente a parlare col capo, non ho tempo per queste cose",
            "🙄 Gli racconto aneddoti su come è impossibile avere successo in questo lavoro"
        ]
    },
    {
        "question": "Ti accorgi che un collega sta usando la tua stessa strategia con un medico che tu hai faticato a conquistare. Cosa fai?",
        "choices": [
            "🤝 Gli dico che apprezzo la sua iniziativa e magari collaboriamo",
            "👀 Lo guardo male e gli faccio capire che sta invadendo il mio territorio",
            "📝 Aspetto che faccia un errore e poi lo faccio notare al capo",
            "😈 Fingo di nulla, ma dentro covo vendetta"
        ]
    },
    {
        "question": "Un collega ti scrive nel gruppo WhatsApp di lavoro per chiedere chi ha già visitato un certo medico. Come rispondi?",
        "choices": [
            "✅ Gli dico la verità e gli do informazioni utili",
            "🤔 Gli dico che non so nulla, anche se ci sono stato il giorno prima",
            "😂 Rispondo con un meme e svicolo la domanda",
            "👻 Lascio il messaggio in lettura e non rispondo"
        ]
    }
]

# Inizializza lo stato della sessione
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

# Titolo dell'app
st.title("🤝 Scopri che tipo di collega sei!")

# Calcola e mostra la barra di avanzamento, garantendo che il valore non superi 1.0
progress = min((st.session_state.current_question + 1) / len(quiz_data), 1.0)
st.progress(progress)

# Controlla se il quiz è finito
if not st.session_state.completed:
    # Mostra la domanda attuale
    question_data = quiz_data[st.session_state.current_question]
    st.subheader(f"📝 Domanda {st.session_state.current_question + 1} di {len(quiz_data)}")
    st.write(question_data["question"])

    # Crea un pulsante per ogni scelta
    for choice in question_data["choices"]:
        if st.button(choice, use_container_width=True):
            # Passa alla domanda successiva
            st.session_state.current_question += 1

            # Se è l'ultima domanda, segnala il completamento
            if st.session_state.current_question >= len(quiz_data):
                st.session_state.completed = True

            st.rerun()  # Ricarica la pagina per aggiornare lo stato
else:
    # **Nasconde tutto il contenuto della pagina prima dell'analisi**
    st.empty()

    # Primo passaggio di suspense con animazione di caricamento (6 secondi)
    with st.spinner("🧐 Analizzando le tue risposte..."):
        time.sleep(7)

    # Secondo passaggio di suspense (6 secondi)
    st.empty()  # Cancella tutto di nuovo prima di mostrare il nuovo messaggio
    st.info("Nel tuo caso l'analisi sembra richiedere più del previsto...")
    time.sleep(9)

    st.success("✅ I risultati sono pronti!")
    st.header("💀 Sei un tumore!")
    st.markdown("### 😈 Il test ha confermato i miei peggiori sospetti...")
    st.image("https://media.giphy.com/media/cjWfHwdAD170ADNlqp/giphy.gif", use_container_width=True)

    # Pulsante per rifare il test
    if st.button("🔄 Rifai il test", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.completed = False
        st.rerun()
