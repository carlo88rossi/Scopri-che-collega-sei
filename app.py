import streamlit as st
import time

# Inizializzazione di eventuali variabili di sessione mancanti
if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "final" not in st.session_state:
    st.session_state.final = False

# Se il flag finale è True, mostra la pagina finale e interrompi l'esecuzione
if st.session_state.final:
    st.markdown("<h1 style='text-align: center;'>Lascia stare.</h1>", unsafe_allow_html=True)
    st.stop()

# Configurazione della pagina
st.set_page_config(page_title="Scopri che tipo di collega sei", page_icon="💼", layout="centered")

# Stile CSS personalizzato
st.markdown("""
    <style>
        /* Sfondo generale */
        body {
            background-color: #f5f7fa;
        }
        .main {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        /* Stile della barra di avanzamento */
        .stProgress > div > div > div > div {
            background-color: #4CAF50 !important;
        }
        /* Stile del box della domanda */
        .question-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        /* Stile pulsanti */
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Pagina introduttiva (mostrata solo la prima volta)
if not st.session_state.intro_seen:
    def start_test():
        st.session_state.intro_seen = True

    st.title("💼💊 Scopri che tipo di collega sei!")
    st.markdown("""
        **Benvenuto al test di valutazione professionale**

        In questa applicazione verrai sottoposto a un approfondito questionario volto a valutare le tue competenze relazionali e il tuo approccio nell'ambiente medico.
        
        **Come funziona?**
        - Risponderai a una serie di domande studiata per analizzare il tuo stile comunicativo e la tua attitudine collaborativa.
        - Al termine del questionario, riceverai una diagnosi personalizzata, elaborata in modo rigoroso sulla base delle tue risposte.

        Sei pronto ad affrontare una valutazione seria e accurata?
    """)
    st.button("Inizia il test", on_click=start_test)
    st.stop()

# Dati del quiz (con alcune domande aggiuntive)
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
    },
    # Domande aggiuntive
    {
        "question": "Stai preparando una presentazione importante per il team, ma un collega insiste per aggiungere dettagli superflui. Cosa fai?",
        "choices": [
            "🤝 Accolgo le sue idee e cerco di integrare le sue proposte.",
            "💬 Gli spiego che il focus deve rimanere sulla sintesi e sull’essenziale.",
            "😶 Ignoro il suo intervento e procedo come avevo pianificato.",
            "😡 Reagisco bruscamente, rifiutando qualsiasi modifica."
        ]
    },
    {
        "question": "Un collega ti chiede aiuto su un progetto urgente, ma sei già a corto di tempo. Come reagisci?",
        "choices": [
            "🤝 Mi offro di dare un rapido supporto per non lasciare il collega in difficoltà.",
            "💬 Gli spiego che al momento non posso aiutarlo e gli suggerisco altre soluzioni.",
            "😓 Accetto di aiutarlo, anche se so che rischio di sovraccaricarmi.",
            "🙄 Ignoro la richiesta per concentrarmi sulle mie scadenze."
        ]
    },
    {
        "question": "Durante una riunione, un collega propone una soluzione non convenzionale a un problema. Qual è la tua reazione?",
        "choices": [
            "🤔 Valuto la proposta e chiedo ulteriori dettagli per comprenderla meglio.",
            "🗣️ Critico immediatamente l’idea senza considerare alternative.",
            "💡 Propongo subito una soluzione basata sulla mia esperienza personale.",
            "🤫 Resto in silenzio, osservando come si sviluppa la discussione."
        ]
    }
]

# Callback per aggiornare il contatore della domanda
def handle_choice():
    st.session_state.current_question += 1
    if st.session_state.current_question >= len(quiz_data):
        st.session_state.completed = True

# Se il quiz non è completato, mostra la domanda corrente
if not st.session_state.completed:
    progress = min((st.session_state.current_question + 1) / len(quiz_data), 1.0)
    st.progress(progress)
    
    question_data = quiz_data[st.session_state.current_question]
    st.markdown(f"""
        <div class="question-box">
            <h3>📝 Domanda {st.session_state.current_question + 1} di {len(quiz_data)}</h3>
            <p>{question_data["question"]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    for idx, choice in enumerate(question_data["choices"]):
        st.button(choice, key=f"btn_{st.session_state.current_question}_{idx}", on_click=handle_choice)
        
# Se il quiz è completato, mostra i risultati
else:
    st.session_state.attempts += 1

    with st.spinner("🧐 Analizzando le tue risposte..."):
        time.sleep(5)
    
    # Messaggio informativo
    if st.session_state.attempts > 1:
        st.info("Magari questa volta va meglio...")
    else:
        st.info("Nel tuo caso l'analisi sembra richiedere più del previsto...")
    
    time.sleep(4)
    st.success("✅ I risultati sono pronti!")
    
    # Se siamo alla seconda esecuzione (attempts == 2)
    if st.session_state.attempts == 1:
        st.header("💀 Sei un tumore!")
        st.markdown("### 😈 Il test ha confermato i miei peggiori sospetti...")
        st.image("https://media.giphy.com/media/cjWfHwdAD170ADNlqp/giphy.gif", use_container_width=True)
        st.button("🔄 Rifai il test", on_click=lambda: (setattr(st.session_state, 'current_question', 0), setattr(st.session_state, 'completed', False)))
    elif st.session_state.attempts == 2:
        st.header("💀💀 Diagnosi confermata 💀💀")
        st.markdown("Guardati, hai ripetuto il test… spero che la seconda volta sia stata meno dolorosa della prima.")
        st.image("https://media.giphy.com/media/dPkQk7aiwL8DC/giphy.gif?cid=790b7611g9tnszfpqbn8ytjabzn1x31i7ijlc5a5p7m0lrj1&ep=v1_gifs_search&rid=giphy.gif&ct=g", use_container_width=True)
        # Il pulsante qui imposta il flag finale, così al click si mostra la pagina "Lascia stare." senza ripartire le domande.
        st.button("🔄 Rifai il test", on_click=lambda: setattr(st.session_state, 'final', True))
